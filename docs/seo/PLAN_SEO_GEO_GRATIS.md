# Plan SEO + GEO gratuito — aitoralmu.xyz

Adaptación del dosier "Sistema Integral de SEO y GEO 2026" al proyecto aitoralmu.xyz.
Restricción: solo herramientas gratuitas (o con versión gratuita suficiente). Más trabajo manual, mismo método.

## 0. Principios y alcance

- Repo editorial: `aitoralmu.xyz` (Astro + Tailwind, rama `main`). El proyecto Next.js de la carpeta de servicios queda fuera de alcance.
- Mercado: España, idioma español, `google.es` (`hl=es`, `gl=es`).
- Oferta: webs estáticas en 24 h desde plantilla; paquetes 50 €, 100 € y 150 €; landing nacional como prioridad; `/servicios` como hub.
- Cada fase tiene entregable, criterio de cierre y control humano. Ningún texto se publica sin revisión.
- Las cifras de volumen son rangos del Planificador, no cifras exactas. Las métricas GEO son manuales y muestrales.

## 1. Herramientas: equivalencias gratuitas del dosier

| Dosier (de pago o no gratuito) | Sustituto gratuito | Límite a documentar |
|---|---|---|
| ChatGPT / Claude con proyecto | ChatGPT o Claude en plan gratuito, proyecto dedicado | Límite de mensajes; archivo `business_brief.txt` como fuente |
| Data for SEO (volumen, CPC, PAA, fan-out) | Google Ads Keyword Planner (rangos), Google Trends, autocompletado, PAA manual en google.es, pipeline propio `scripts/seo-entropy/analyze.py` | Rangos de volumen; sin dificultad SEO real |
| Ahrefs / Semrush (competencia, backlinks) | Google Search Console y Bing Webmaster Tools (datos propios); Ubersuggest y Moz en plan gratuito (competidores) | Datos de competidores limitados y aproximados |
| Análisis de sitemap de competidor | `curl` del sitemap.xml + limpieza con script propio | Ninguno relevante |
| Napkin.ai (diagramas) | Excalidraw, draw.io o Mermaid; export a SVG | Sin generación automática |
| PNG a WebP | Squoosh (web) o `cwebp` en local | Ninguno |
| SEO Wallet (on-page) | DevTools del navegador y una extensión gratuita de inspección SEO | Revisión manual por URL |
| Google Lighthouse | Lighthouse en DevTools (gratis) | Ninguno |
| Link Whisperer / Data Wise Writer (enlazado) | Mapa de enlaces en hoja de cálculo; enlaces escritos a mano en Astro | Trabajo manual |
| Data Wise AI Visibility / Brand Tracker | Registro manual semanal de prompts en ChatGPT, Claude y Google AI Overviews, con capturas y fecha | Muestra pequeña; ruido alto |
| Bing AI Performance (citas) | Bing Webmaster Tools (gratis) | Disponibilidad del informe según cuenta |
| Bright Local (citaciones NAP) | Alta manual en Google Business Profile, Bing Places, Páginas Amarillas e Infoempresas | Tiempo manual |
| Connectivity (PR digital) | Connectivity en plan gratuito (3 respuestas/pitches al mes) | Cuota fija |
| Get Me Links / Rhino Rank (compra de enlaces) | Descartado. Outreach manual a directorios de nicho y colaboraciones sin pago | Volumen bajo |

## 2. Decisiones previas (gate de entrada)

Estas decisiones bloquean la Fase 4. Están pendientes desde `KEYWORD-RESEARCH-PRIORITY-01`.

- D1. Keyword de la home.
- D2. Slug de la landing nacional.
- D3. Si se mantiene `/diseno-web-badalona` como landing local provisional, o se elimina hasta que haya volumen local demostrado.
- D4. Confirmar la fuente de verdad de los precios (50/100/150 €) y del plazo de 24 h antes de escribir ninguna página.

Criterio de cierre: D1–D4 registradas en `docs/seo/DECISIONES.md` con fecha.

## 3. Fases

### Fase 0 — Entorno IA y brief de negocio (1–2 días)

1. Crear un proyecto dedicado en ChatGPT o Claude (plan gratuito), con nombre `aitoralmu_SEO_2026`.
2. Ejecutar el prompt "Tab 0 Business Brief" con datos reales: servicios, precios, plazos, plantilla, ubicación, competidores conocidos y diferenciadores técnicos.
3. Guardar la respuesta como `docs/seo/business_brief.txt` y cargarla como fuente del proyecto.
4. Revisión humana: el brief solo se da por válido si lo aprueba el propietario del negocio. Ningún dato inventado.

Entregable: `docs/seo/business_brief.txt` aprobado.

### Fase 1 — Arquitectura objetivo (gate, 1–2 días)

1. Resolver D1–D4.
2. Definir la taxonomía de URLs fija: `aitoralmu.xyz/servicios/{servicio}` y, solo si se valida demanda, `aitoralmu.xyz/servicios/{servicio}/{ubicacion}`.
3. Listar money pages (una por servicio) y content pages (una por cluster informacional).
4. Crear `docs/seo/SEO_MAP_V1.md` con la arquitectura. Si ya existe en otra copia del proyecto, reconciliarla con el repo.

Entregable: `docs/seo/SEO_MAP_V1.md` y `docs/seo/DECISIONES.md`.

### Fase 2 — Investigación de keywords (5–7 días)

Transaccionales:
1. Ampliar las 21 keywords de `research_notes/keywords/KEYWORD_RESEARCH_LANDING.xlsx` con variantes por servicio.
2. Registrar volumen (rango), CPC bajo/alto y competencia publicitaria en el Planificador.
3. Tendencias con Google Trends (máximo 5 términos por grupo).
4. Agrupar por intención en una hoja de clusters.

Informacionales:
1. Autocompletado de Google (`suggestqueries`) para cada semilla.
2. PAA a profundidad 3, extraído manualmente de google.es en modo sin personalizar (`gbv=1`).
3. Fan-out manual: para cada semilla, consultas de seguimiento en ChatGPT, Claude y Google AI Mode. Anotar las subconsultas que aparecen en las respuestas. Documentar que es una muestra manual.

Análisis de texto:
1. Ejecutar `scripts/seo-entropy/analyze.py` sobre las páginas de resultados de cada cluster.
2. Mínimo 10 páginas válidas por keyword. Si no se alcanza, marcar la keyword como "muestra insuficiente" y no tomar decisiones de contenido con ella.

Entregables: `keywords_transaccionales.csv`, `keywords_informacionales.csv`, `clusters.csv`, y los JSON en `research_notes/keywords/terminos/`.
Criterio de cierre: cada cluster tiene una URL propuesta en `SEO_MAP_V1` y una muestra de al menos 10 páginas, o una nota de muestra insuficiente.

### Fase 3 — Ingeniería inversa de competidores (4–5 días)

1. Identificar de 1 a 3 competidores orgánicos reales en España para los servicios de web en 24 h y landings de diseño web. Excluir comparativas y directorios (Capterra, Appvizer, blogs genéricos).
2. Descargar `sitemap.xml` de cada competidor con `curl`.
3. Limpiar con un script: eliminar `/wp-content/uploads/`, etiquetas, categorías y páginas de utilidad.
4. Clasificar el resto en tres columnas: servicios, ubicaciones y blog.
5. Para cada competidor, anotar sus keywords posicionadas en Ubersuggest o Moz (plan gratuito) y registrar el límite de datos.
6. Auditar el perfil de enlaces con los límites del plan gratuito. Documentar que es aproximado.

Entregable: `docs/seo/competidores.csv` y `docs/seo/competidores_sitemap_limpio.csv`.
Criterio de cierre: cada money page tiene al menos un competidor de referencia.

### Fase 4 — Producción de contenidos (7–10 días)

Money pages (una por servicio):
1. Regla de 1 página por servicio. Ninguna página agrupa servicios heterogéneos.
2. Regla de los 2 segundos: en el primer pliegue deben aparecer qué se hace, dónde (si aplica) y un botón de acción visible.
3. Precio o rango de precio visible (50/100/150 €), plazo de 24 h y alcance del paquete.
4. FAQ de 3 a 5 preguntas de carácter transaccional.
5. Schema JSON-LD `Service` y, en la página de hub, `Organization`.
6. Testimonios solo si son reales y el propietario los aporta.

Content pages (blog):
1. Técnica "Content Capsule": respuesta de 20–25 palabras justo debajo de cada H2 o H3 formulado como pregunta.
2. Dentro de la cápsula no puede haber hipervínculos.
3. Cualquier cifra o norma se enlaza en el párrafo de apoyo posterior a la cápsula, priorizando fuentes oficiales (.gov, .gob.es, BOE).
4. Experiencia propia (E-E-A-T): solo hechos aportados por el propietario. No se inventan casos.

Imágenes:
1. Diagramas en Excalidraw o draw.io, export a SVG o PNG.
2. Convertir a WebP con Squoosh antes de publicar.

Control humano: un editor revisa cada pieza antes de publicarla. Checklist en `docs/seo/CHECKLIST_CONTENIDO.md`.

Criterio de cierre: cada money page cumple la checklist, y cada content page tiene cápsula sin enlaces y al menos una fuente oficial enlazada.

### Fase 5 — Implementación en Astro (3–5 días)

1. Crear las rutas según `SEO_MAP_V1`.
2. Añadir `@astrojs/sitemap` (gratuito) y generar `sitemap.xml`.
3. Crear `robots.txt` con referencia al sitemap.
4. Canonical en cada página. Un solo H1 por página.
5. Title menor de 60 caracteres y metadescripción menor de 150.
6. JSON-LD por tipo de página.
7. Verificar con `npm run build` sin errores.

Entregable: build limpio y commit en `main`.

### Fase 6 — Auditoría on-page (2–3 días)

1. Checklist por URL: title, metadescripción, H1 único, jerarquía H2–H3, schema válido.
2. Validar schema con Rich Results Test (gratuito).
3. Lighthouse en ventana de incógnito. Umbral de publicación: 90 en Performance y SEO. Objetivo: 100 en las cuatro categorías.
4. Si una URL no llega a 90, se corrigen imágenes (WebP, dimensiones) y plantilla antes de publicar.

Nota: el dosier usa 100/100 en el módulo 6 y 90/100 en el SOP. Aquí se toman ambos: 90 es el umbral y 100 el objetivo.

Entregable: `docs/seo/AUDITORIA_ONPAGE.csv` con una fila por URL.

### Fase 7 — Enlazado interno (2 días)

1. Mapa de enlaces en `docs/seo/enlazado.csv`: origen (blog), destino (money page), anchor text.
2. Anchor text contextual. Prohibido "haz clic aquí" y textos genéricos.
3. Implementar los enlaces en Astro.
4. Revisar que cada money page recibe al menos 3 enlaces internos desde contenido informacional relevante.

Entregable: `docs/seo/enlazado.csv` aplicado.

### Fase 8 — Despliegue y Search Console (1–2 días)

1. Verificar la propiedad en Google Search Console (DNS o HTML).
2. Enviar `sitemap.xml`.
3. Importar la configuración en Bing Webmaster Tools desde GSC.
4. Confirmar el estado "Correcto" o "Success" en ambos.

Entregable: propiedades verificadas y sitemap en estado correcto.

### Fase 9 — Seguimiento GEO manual (continuo, semanal)

Cada semana:
1. Registrar en `docs/seo/tracking_geo.csv` 30 prompts (marca, servicio, comparativas) en ChatGPT, Claude y Google AI Overviews.
2. Por prompt: ¿se cita una URL propia? ¿se menciona la marca? Guardar captura y fecha.
3. GSC: impresiones, clics y posición media por URL.
4. Bing Webmaster Tools: citas y páginas citadas.

Métricas que se revisan: impresiones, clics, posición media, citas, menciones.
Regla de interpretación: con muestras de 30 prompts, un cambio de 1 o 2 citas no es significativo.

### Fase 10 — Autoridad off-page (continuo, con disparador)

Disparador (dosier): si las money pages mantienen impresiones altas sin menciones directas tras 60 días, se activa esta fase.

1. Ficha NAP idéntica en Google Business Profile, Bing Places, Páginas Amarillas e Infoempresas.
2. Connectivity en plan gratuito: responder solo a consultas con afinidad real (máximo 3 al mes).
3. Outreach manual a directorios de nicho y colaboraciones sin pago.
4. Prohibido: paquetes masivos de citas, granjas de enlaces y compra de enlaces.

Entregable: `docs/seo/offpage_log.csv` con cada acción, fecha y resultado.

### Fase 11 — Operación mensual (SOP simplificado)

Como el proyecto lo lleva una sola persona, los cuatro roles del dosier se concentran en el propietario. Cada bloque mantiene su control de calidad.

- Semana 1: revisión de GSC (impresiones y clics).
- Semana 2: revisión de Bing Webmaster y de `tracking_geo.csv`.
- Semana 3: evaluación del disparador de la Fase 10.
- Semana 4: respuestas periodísticas (Connectivity) y revisión del enlazado interno.

Escalado: si una content page no es citada ni recibe impresiones tras 45 días, se reescribe con datos de experiencia propia antes de tocar nada más.

## 4. Calendario orientativo

| Fase | Duración estimada | Dependencia |
|---|---|---|
| 0. Entorno y brief | 1–2 días | Ninguna |
| 1. Arquitectura y decisiones | 1–2 días | Fase 0 |
| 2. Keywords | 5–7 días | Fase 1 |
| 3. Competidores | 4–5 días | Fase 2 |
| 4. Contenidos | 7–10 días | Fases 1, 2 y 3 |
| 5. Implementación Astro | 3–5 días | Fase 4 |
| 6. Auditoría on-page | 2–3 días | Fase 5 |
| 7. Enlazado interno | 2 días | Fases 4 y 6 |
| 8. Despliegue y GSC | 1–2 días | Fase 6 |
| 9. Seguimiento GEO | Continuo | Fase 8 |
| 10. Off-page | Continuo, con disparador | Fase 9 |
| 11. Operación mensual | Continuo | Fase 9 |

Duración total hasta la Fase 8: aproximadamente 6 a 8 semanas de trabajo.

## 5. Riesgos y límites

- Muestra pequeña en las fases de keywords: algunas keywords tendrán menos de 10 páginas válidas. Se marcan como muestra insuficiente.
- Métricas GEO manuales: poco volumen y alto ruido. No se toman decisiones con variaciones pequeñas.
- Datos de competidores aproximados con los planes gratuitos.
- Afirmaciones del dosier sin fuente verificable: "el SEO clásico es el 80 % de la base de GEO", "GEO es el único acrónimo respaldado por literatura científica" y "no hay penalización por contenido de IA". Se tratan como hipótesis hasta comprobarlas.
- Discrepancia de stack: el proyecto editorial es Astro. Cualquier referencia a Next.js de la carpeta de servicios no aplica a este plan.

## 6. Registro de versiones

- v1 (2026-10-19): primera versión adaptada del dosier a herramientas gratuitas.
