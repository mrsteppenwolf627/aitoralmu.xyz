# Documento de continuidad — aitoralmu.xyz (SEO + GEO gratuito)

Fecha de corte: 2026-10-19. Pegar este documento al inicio de cualquier chat nuevo (ChatGPT Work o Claude) para retomar el trabajo sin perder contexto.

## 1. Objetivo

Construir la estrategia SEO y GEO (Generative Engine Optimization) de aitoralmu.xyz, una web de servicios de diseño y creación de webs en España, con un método completamente gratuito.

Restricciones vigentes:
- Solo herramientas gratuitas o con versión gratuita suficiente. Sin pagos ni suscripciones.
- No contratar APIs de pago (se descartó DataForSEO).
- Mercado: España, idioma español, `google.es` (`hl=es`, `gl=es`).
- No comprar enlaces ni usar granjas de enlaces ni paquetes masivos de citas.
- Google Ads: solo usar la cuenta existente en modo lectura del Planificador. No crear cuentas sin permiso explícito.
- Ninguna publicación de texto sin revisión humana.

## 2. Repositorio y entorno

- Repo editorial: `https://github.com/mrsteppenwolf627/aitoralmu.xyz.git`, rama `main`.
- Clone local: `/home/claude/aitoralmu.xyz/`. Stack: Astro + Tailwind (verificado por `package.json`).
- Permiso para commit y push en `main` cuando sea necesario.
- Identidad de commits ya configurada. Trailers de commit: `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` y `Claude-Session: https://claude.ai/code/session_01JBD2ubJqcRcA9NTshfMy45`.
- Discrepancia a tener en cuenta: en la carpeta conectada de Windows (`C:\Users\a.alarcon\Desktop\Cursor projects\aitoralmu.xyz\`) hay un proyecto Next.js 14.2.5 de servicios, distinto del repo editorial Astro. Ese proyecto no está en alcance y no se ha modificado salvo añadidos en `docs/seo/` de los CSV de servicios.
- Documentos previos del proyecto (`PROJECT_STATUS.md`, `package.json` de Next) referencian `docs/seo/SEO_MAP_V1.md` y `docs/business/BUSINESS_OFFER_MAP.md`; estos no están en el repo Astro y deben reconciliarse en la Fase 1.

## 3. Oferta comercial (base para el brief)

- Webs estáticas en 24 h desde plantilla.
- Paquetes de 50 €, 100 € y 150 €.
- Objetivo comercial declarado: unas 20 ventas en 12 meses.
- Prioridad SEO: landing nacional. `/servicios` es el hub. `/diseno-web-badalona` es landing local provisional.

Los datos anteriores proceden de la conversación y del estado del proyecto. Deben validarse en la Fase 0 antes de usarlos en cualquier página.

## 4. Estado actual

| Área | Estado |
|---|---|
| Método gratuito de keywords | Implementado y probado (`scripts/seo-entropy/analyze.py`) |
| Keyword research (21 keywords) | Volumen, Trends y SERP registrados en la hoja Excel |
| Términos por keyword | Ejecutado en 20 de 21 keywords. "chatgpt gratis" no ejecutado |
| Decisiones D1–D4 | Pendientes |
| Fase 0 (brief de negocio) | Pendiente |
| Fase 1 (arquitectura) | Pendiente, bloqueada por D1–D4 |
| Plan SEO + GEO gratuito | Redactado y en repo (`docs/seo/PLAN_SEO_GEO_GRATIS.md`) |

Decisiones pendientes:
- D1. Keyword de la home. No cambiar la home hasta decidirla.
- D2. Slug de la landing nacional.
- D3. Mantener o eliminar `/diseno-web-badalona` hasta validar demanda local.
- D4. Confirmar precios (50/100/150 €) y plazo (24 h) con el propietario.

## 5. Resultados del keyword research

Archivos clave:
- `research_notes/keywords/KEYWORD_RESEARCH_LANDING.xlsx`. Hojas: "Keywords", "Leyenda y pendientes" y "Términos (método gratis)".
- `research_notes/keywords/terminos/*.json`. Un JSON por keyword con páginas válidas, descartadas, URLs y términos clasificados.
- `docs/seo/KEYWORD_RESEARCH_01.csv` y `docs/seo/KEYWORD_RESEARCH_01_TRENDS_SERP.csv` en la carpeta conectada de servicios.

Método:
- Volumen: rangos del Google Ads Keyword Planner (España, es, oct 2025 a sept 2026). Son rangos, no cifras exactas.
- Tendencias: Google Trends, índice relativo por grupo de comparación de hasta 5 términos.
- SERP: google.es, `gbv=1`, `hl=es`, `gl=es`, revisada el 19/10/2026.
- Términos: autocompletado de Google, búsquedas reales en WebSearch y descarga con curl de páginas válidas (mínimo 300 palabras). Cobertura y entropía de Shannon normalizada (H_norm = H / log2 N).
- Clasificación adaptada: consenso si cobertura ≥ 0,7; especialista si cobertura ≤ 0,2 y frecuencia ≥ 5; resto, otro.

Resultados relevantes:
- Keywords transaccionales con encaje alto: "crear página web" (1 mil a 10 mil búsquedas/mes, CPC 1,79–7,03 €), "crear web", "diseño de páginas web", "creador de páginas web".
- Keywords descartadas para landing: "hosting", "comprar un dominio", "ovh vps", "banahosting", "prompts", "n8n", "pagina web gratis" (intención de gratuidad).
- Google SERP de "diseño de páginas web": bloque local de agencias de Barcelona; el encaje nacional requiere diferenciación.
- Google SERP de "crear página web": constructores SaaS (Canva, Wix, IONOS, GoDaddy, Squarespace) y anuncios de agencias con precios de referencia (189 €, 590 €, 899 €).
- Tendencias: "hosting" en caída desde julio 2026; "n8n" y "prompts" en descenso.

Hallazgos del método gratuito:
- Páginas válidas por keyword (de 20 ejecutadas):
  - Cumplen mínimo 10: chatgpt (11), crear página web (11), software crm (13), crm (12), hosting (10), posicionamiento SEO (10), wordpress (10).
  - No cumplen mínimo 10: keyword research (9), verifactu (9), gemini (8), generador de imágenes IA (8), prompts (8), ahrefs (7), zapier (7), claude IA (6), email marketing (6), n8n (6), notion (6), semrush (6), framer (5).
- Clase "especialista": vacía en las 20 keywords con este tamaño de muestra.
- Consenso: contiene ruido (marcas, números, genéricos). Tratar como orientativo.
- Scripts de apoyo: `scripts/seo-entropy/analyze.py` y `scripts/seo-entropy/README.md`.

## 6. Plan de trabajo (resumen)

Plan completo en `docs/seo/PLAN_SEO_GEO_GRATIS.md`. Fases:

0. Entorno IA y brief de negocio (1–2 días). Proyecto dedicado en ChatGPT o Claude gratuito; prompt "Tab 0 Business Brief"; guardar `docs/seo/business_brief.txt`, aprobado por el propietario.
1. Arquitectura objetivo (gate, 1–2 días). Resolver D1–D4; crear `docs/seo/SEO_MAP_V1.md` y `docs/seo/DECISIONES.md`.
2. Investigación de keywords (5–7 días). Transaccionales (Planner, Trends, clusters), informacionales (autocompletado, PAA manual depth 3, fan-out manual), análisis con el pipeline. Mínimo 10 páginas o nota de muestra insuficiente.
3. Ingeniería inversa de competidores (4–5 días). 1 a 3 competidores reales en España; sitemap limpio; keywords y enlaces con límites gratuitos.
4. Producción de contenidos (7–10 días). Money pages (una por servicio, regla de 2 segundos, schema) y content pages (cápsulas de 20–25 palabras sin enlaces, fuentes oficiales, experiencia propia real).
5. Implementación en Astro (3–5 días). Rutas, `@astrojs/sitemap`, robots, metadatos, JSON-LD, build limpio.
6. Auditoría on-page (2–3 días). Umbral Lighthouse 90, objetivo 100.
7. Enlazado interno (2 días).
8. Despliegue y Search Console / Bing Webmaster (1–2 días).
9. Seguimiento GEO manual (continuo, semanal). 30 prompts por semana en ChatGPT, Claude y Google AI Overviews; GSC y Bing.
10. Autoridad off-page (continuo, con disparador de 60 días sin menciones). NAP manual, Connectivity gratuito, outreach sin pago.
11. Operación mensual (SOP simplificado para una persona).

## 7. Próximo paso

Fase 0: crear el proyecto de IA gratuito, ejecutar el brief de negocio con datos reales y obtener la aprobación del propietario antes de pasar a la Fase 1.

## 8. Reglas de trabajo y estilo de respuesta

- Respuestas serias y directas. Sin sugerencias, preguntas ni planes que no se hayan pedido.
- Al final de cada respuesta: número de mensajes del usuario en el chat y contexto usado en esa respuesta.
- Cada entregable en el repo: commit y push a `main` con los trailers indicados en la sección 2.
- Ante datos inciertos: documentar el límite, no inventar cifras. Los rangos de volumen y las muestras pequeñas se marcan como tales.
- Todo texto de web que se publique pasa por revisión humana.

## 9. Cómo retomar en un chat nuevo

1. Pegar este documento completo como primer mensaje.
2. Indicar la fase en la que se trabaja (ahora: Fase 0).
3. Adjuntar o pegar los archivos que se necesiten (`business_brief.txt` cuando exista, hoja Excel, plan).
4. Las decisiones D1–D4 se registran en `docs/seo/DECISIONES.md` antes de avanzar a la Fase 4.

## 10. Historial

- 2026-10-19: keyword research con Trends y SERP; método gratuito implementado; términos ejecutados en 20 de 21 keywords; plan SEO + GEO gratuito redactado; documento de continuidad creado.
