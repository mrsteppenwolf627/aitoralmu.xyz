# Protocolo de optimización por URL

## Objetivo

Optimizar cada URL de aitoralmu.xyz para que responda mejor a una intención de búsqueda real, sea fácil de usar y entender, pueda rastrearse e indexarse sin ambigüedades, cargue rápido, sea accesible y ofrezca señales claras para buscadores y motores de respuesta.

No se considerará una página “terminada” por tener una puntuación alta en una herramienta. La validación combinará contenido, código, experiencia y datos reales cuando exista tráfico.

## Orden de trabajo por página

### 1. Intención y función

- Definir qué tarea quiere completar el visitante.
- Separar intención informativa, comparativa, transaccional o de herramienta.
- Elegir una keyword principal y un grupo pequeño de secundarias relacionadas.
- Revisar la SERP española actual: tipo de resultados, formatos, preguntas, entidades y nivel de competencia.
- Definir la acción principal de la página y el siguiente paso lógico.

### 2. Arquitectura y UX

- La propuesta de valor debe entenderse en los primeros segundos.
- El título, subtítulo y llamadas a la acción deben decir qué se obtiene.
- La navegación debe usar etiquetas previsibles y mantener el contexto.
- Cada enlace debe anticipar su destino; se evitarán textos genéricos como “más información”.
- La página debe ser escaneable con encabezados, resumen, tablas, listas y bloques visuales.
- En móvil, la acción principal y la información decisiva deben quedar visibles sin fricción.
- Las comparativas deben mostrar criterios, diferencias, límites, precio y recomendación.
- Las herramientas deben explicar entrada, proceso, resultado, privacidad y siguiente acción.

La base UX se apoya en el concepto de “information scent” de Nielsen Norman Group: el texto y el contexto de un enlace deben dar señales suficientes para que el usuario anticipe el valor de seguirlo. [NN/G: Information Scent](https://www.nngroup.com/articles/information-scent/)

### 3. SEO on-page

- Un solo `h1` claro y alineado con la intención.
- `title` único, descriptivo y orientado al clic.
- `meta description` útil, sin promesas que el contenido no cumpla.
- URL corta, estable, legible y sin parámetros innecesarios.
- Canonical absoluta y coherente con la URL pública.
- Enlaces internos hacia la página desde su categoría y páginas relacionadas.
- Texto alternativo descriptivo en imágenes informativas.
- Fechas visibles solo cuando exista una fecha editorial real y mantenida.
- Autoría, metodología y fuentes cuando el contenido dependa de experiencia o datos externos.
- No crear páginas vacías solo para introducir JSON-LD.

Google recomienda URLs lógicas, enlaces rastreables, metadatos válidos, canonicals y sitemap; el sitemap es una señal de las URLs canónicas que se desean mostrar, no una garantía de indexación. [Google: Crawling and indexing](https://developers.google.com/search/docs/crawling-indexing) [Google: Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

### 4. Contenido y confianza

- Responder pronto a la pregunta principal.
- Añadir experiencia propia: prueba, captura, resultado, procedimiento o comparación reproducible.
- Declarar limitaciones, fecha de revisión y cambios de precio.
- Diferenciar hechos, interpretación y recomendación.
- Añadir fuentes primarias para afirmaciones técnicas, legales o de producto.
- Evitar contenidos generados en serie sin valor añadido.
- Mantener una página de metodología y una política de afiliación visible.

Para el proyecto, una ficha de herramienta tendrá como mínimo: caso de uso, usuario recomendado, alternativa, precio, límites, privacidad, prueba, fecha de revisión y enlace de acción.

### 5. Datos estructurados y GEO

Se usará JSON-LD solo cuando describa contenido visible y real de la URL. La base será:

- `WebSite` y `Organization` en el nivel global.
- `BreadcrumbList` en páginas profundas.
- `Article` para guías y análisis.
- `SoftwareApplication` o `Product` solo cuando la página describa un producto concreto con datos comprobables.
- `ItemList` para listados cuando represente realmente el contenido visible.

El marcado estructurado puede hacer una página apta para resultados enriquecidos, pero Google no garantiza que los muestre. JSON-LD es el formato recomendado por Google para facilitar el mantenimiento. [Google: Structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) [Google: General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

Para GEO se priorizará la claridad semántica: respuesta directa, definiciones, tablas, listas, entidades consistentes, fuentes, fechas y relaciones internas. `llms.txt` se mantendrá como recurso editorial experimental, sin atribuirle capacidad garantizada de posicionamiento.

### 6. Rendimiento y estabilidad

Objetivos de campo en el percentil 75, separados por móvil y escritorio:

- LCP igual o menor que 2,5 s.
- INP igual o menor que 200 ms.
- CLS igual o menor que 0,1.

Se medirán con PageSpeed Insights, Lighthouse, Chrome DevTools y, cuando haya datos, CrUX/Search Console. Lighthouse sirve para pruebas de laboratorio; INP real necesita interacción de usuarios y datos de campo. [web.dev: Web Vitals](https://web.dev/articles/vitals)

Controles por URL:

- HTML estático siempre que sea posible.
- CSS y JavaScript mínimos.
- Imágenes dimensionadas, comprimidas y en formatos modernos.
- Fuentes locales o con carga controlada.
- Sin elementos que cambien de tamaño al cargar.
- Reservar espacio para imágenes, embeds y avisos.
- No añadir scripts de analítica, anuncios o widgets antes de justificar su coste.

### 7. Accesibilidad

- HTML semántico y landmarks.
- Navegación completa con teclado.
- Foco visible.
- Contraste suficiente.
- Formularios con label, estado y mensaje de error.
- No depender solo del color.
- Botones y enlaces con nombre accesible.
- Jerarquía de encabezados coherente.
- Respeto por `prefers-reduced-motion`.

Se tomará WCAG 2.2 AA como referencia operativa. WCAG organiza los criterios bajo los principios perceptible, operable, comprensible y robusto. [W3C: WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)

### 8. Conversión y medición

Cada URL tendrá un objetivo principal medible:

- Clic a una comparativa.
- Uso de una herramienta.
- Descarga de una plantilla.
- Suscripción a la newsletter.
- Clic de afiliación.

Se medirá primero con eventos simples y privacidad mínima. Search Console será la fuente principal para impresiones, consultas, clics y CTR orgánico; Analytics servirá para comportamiento y conversiones dentro del sitio. [Google: Search Console y Analytics](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)

## Ficha de auditoría que se aplicará a cada URL

1. URL y estado.
2. Intención primaria.
3. Keyword principal y secundarias.
4. SERP y competidores directos.
5. Propuesta de valor.
6. Arquitectura de encabezados.
7. Título, descripción y canonical.
8. Enlazado interno y breadcrumbs.
9. JSON-LD aplicable.
10. Accesibilidad.
11. Rendimiento y Core Web Vitals.
12. CTA y evento de conversión.
13. Riesgos, datos que faltan y fecha de revisión.
14. Verificación final de build, HTML, sitemap y enlaces.

## Orden propuesto para aitoralmu.xyz

1. Home `/`: entidad, propuesta de valor, rutas de navegación y captación.
2. `/articulos/`: hub editorial y distribución de autoridad interna.
3. `/herramientas/`: hub de utilidades y conversión.
4. Primer artículo sobre IA aplicada: prueba de arquitectura editorial.
5. Primer comparador de herramientas IA: activo diferenciador.
6. Plantilla de ficha individual de herramienta.
7. Categorías de automatización y SEO/GEO.

## Fuentes de referencia

- [Google Search Central: documentación SEO](https://developers.google.com/search/docs)
- [Google Search Central: SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Central: AI features](https://developers.google.com/search/docs/appearance/ai-features)
- [web.dev: Web Vitals](https://web.dev/articles/vitals)
- [W3C WAI: WCAG 2](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [Nielsen Norman Group: Information Scent](https://www.nngroup.com/articles/information-scent/)
