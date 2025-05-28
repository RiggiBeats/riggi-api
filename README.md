
# API de Análisis de Datos Musicales (Riggi Beats)

Esta API recibe un archivo Excel con datos de rendimiento de beats (YouTube, BeatStars, etc.) y devuelve un resumen automático.
Puede ser desplegada en Render como Web Service y conectarse con un GPT personalizado.

## Endpoint principal

POST /analisis_rendimiento

### Parámetros:
- excel_file (archivo .xlsx)
- descripcion_textual (texto opcional)
- objetivo (texto opcional)

### Respuesta:
Resumen del Excel + texto enviado + objetivo + mensaje de éxito.
