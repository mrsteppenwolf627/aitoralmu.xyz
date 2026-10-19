"""Análisis gratuito de términos de competidores (sin APIs de pago).

Uso:
  python3 analyze.py --seed "software crm" --urls urls.txt --out resultados.json

- urls.txt: una URL por línea (top orgánico de Google.es para la semilla).
- Descarga cada página con curl, extrae el texto principal con bs4 y calcula,
  para unigramas y bigramas sin stopwords:
    * cobertura: nº de páginas que usan el término / nº de páginas válidas
    * frecuencia total y distribución de frecuencias entre páginas
    * entropía de Shannon normalizada H_norm = H / log2(N)  (N = páginas válidas)
Clasificación (adaptación documentada, ver README):
    consenso    -> cobertura >= 0.7
    especialista -> cobertura <= 0.2 y frecuencia total >= 5
    resto       -> intermedio
El artículo de referencia no define la fórmula exacta de la entropía ni el tratamiento
de valores entre 0.3 y 0.7; por eso la clasificación usa la cobertura como criterio principal.
"""
import argparse, collections, json, math, re, subprocess, sys
from bs4 import BeautifulSoup

STOP = set("""a al algo como con de del desde el ella ellas ellos en entre era es esa ese eso esta este esto estas estos
la las le les lo los más mas me mi mis muy no o para pero por que qué quien se sin sobre su sus te tu tus un una uno unos
y ya the and of to in is for with on are as be by an it this that from at or your you we our"""
.split())

def fetch(url):
    try:
        out = subprocess.run(["curl", "-sL", "-m", "40", "-A", "Mozilla/5.0", url],
                             capture_output=True, timeout=60).stdout
        return out.decode("utf-8", errors="ignore")
    except Exception:
        return ""

def main_text(html):
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "nav", "footer", "header", "aside", "form", "noscript"]):
        t.decompose()
    node = soup.find("article") or soup.find("main") or soup.body or soup
    text = node.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", text).lower()

def tokens(text):
    words = re.findall(r"[a-záéíóúñü0-9]+", text)
    return [w for w in words if len(w) > 2 and w not in STOP]

def ngrams(toks):
    uni = set(toks)
    bi = {f"{a} {b}" for a, b in zip(toks, toks[1:]) if a not in STOP and b not in STOP}
    return uni | bi, collections.Counter(toks)

def entropy_norm(freqs):
    total = sum(freqs)
    n = len(freqs)
    if total == 0 or n < 2:
        return 0.0
    h = -sum((f / total) * math.log2(f / total) for f in freqs if f > 0)
    return h / math.log2(n)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--urls", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    urls = [u.strip() for u in open(a.urls, encoding="utf-8") if u.strip()]
    docs, skipped = [], []
    for u in urls:
        text = main_text(fetch(u))
        if len(text.split()) < 300:
            skipped.append(u); continue
        docs.append((u, text))
    N = len(docs)
    if N < 3:
        sys.exit(f"Muy pocas páginas válidas ({N}). Revisa las URLs.")
    per_doc_terms, per_doc_counts = [], []
    for _, t in docs:
        terms, counts = ngrams(tokens(t))
        per_doc_terms.append(terms); per_doc_counts.append(counts)
    cover = collections.Counter()
    for s in per_doc_terms:
        cover.update(s)
    rows = []
    for term, c in cover.items():
        if c < 2:
            continue
        freqs = []
        for counts in per_doc_counts:
            if " " in term:
                a1, b1 = term.split(" ", 1)
                freqs.append(min(counts.get(a1, 0), counts.get(b1, 0)))
            else:
                freqs.append(counts.get(term, 0))
        total = sum(freqs)
        cov = c / N
        if cov >= 0.7:
            cls = "consenso"
        elif cov <= 0.2 and total >= 5:
            cls = "especialista"
        else:
            cls = "resto"
        rows.append({"term": term, "cobertura": round(cov, 2), "paginas": c,
                     "frecuencia_total": total, "H_norm": round(entropy_norm(freqs), 3), "clase": cls})
    rows.sort(key=lambda r: (-r["cobertura"], -r["frecuencia_total"]))
    result = {"seed": a.seed, "paginas_validas": N, "paginas_descartadas": skipped,
              "urls_validas": [u for u, _ in docs], "terminos": rows[:300]}
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"seed={a.seed} validas={N} descartadas={len(skipped)} terminos={len(rows)} -> {a.out}")

if __name__ == "__main__":
    main()
