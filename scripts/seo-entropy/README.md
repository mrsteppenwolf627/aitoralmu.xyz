# Análisis gratuito de términos de competidores

Versión gratuita del método de keyword research automatizado (artículo de referencia), sin DataForSEO ni APIs de pago.

## Pasos
1. **Expansión de semilla:** Google autocomplete (`suggestqueries.google.com`), gratuito.
2. **SERP:** top orgánico de Google.es con búsqueda web; se guardan las URLs en `urls_*.txt`.
3. **Extracción:** `curl` + `bs4` (texto de `article`/`main`, mínimo 300 palabras por página).
4. **Términos:** unigramas y bigramas sin stopwords; cobertura por página y frecuencia.
5. **Entropía:** `H_norm = H / log2(N)` sobre la distribución de frecuencias entre páginas.

## Clasificación (adaptación)
- El artículo no define la fórmula de H ni el tratamiento entre 0,3 y 0,7.
- Aquí la clase se decide por cobertura: `consenso` si cobertura ≥ 0,7; `especialista` si cobertura ≤ 0,2 y frecuencia total ≥ 5; `resto` en otro caso.
- H_norm se guarda como dato, sin usarlo para clasificar.

## Límites observados
- Muestras pequeñas (3–8 páginas válidas por semilla); el artículo usa top 10.
- Sin lista de stopwords de marca ni de navegación: aparecen términos como `google`, `youtube`, `amazon` (ruido).
- Con N pequeño, la clase `especialista` no se alcanza.

## Uso
```
python3 analyze.py --seed "software crm" --urls urls.txt --out resultados.json
```
