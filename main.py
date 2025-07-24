
from app.meta.test import Test

"""
Consideraciones importantes:
Versión de la API: La API de Marketing de Meta se actualiza regularmente. Asegúrate de que la versión de la API que estás usando en tu código (v18.0 en los ejemplos) coincida con la versión por defecto de tu aplicación en el panel de desarrollador de Meta. Si no especificas una versión, el SDK usará la última por defecto o la configurada en tu aplicación.

Permisos: El token de acceso del usuario de sistema debe tener los permisos adecuados para acceder a los datos que solicitas (ads_read es el mínimo para leer métricas).

Manejo de errores: Es crucial implementar un manejo de errores robusto (try-except FacebookRequestError) para capturar problemas como tokens caducados, permisos insuficientes o límites de tasa de la API.

Paginación: Las llamadas a la API pueden devolver un número limitado de resultados por defecto. Para conjuntos de datos grandes, deberás manejar la paginación para obtener todos los resultados. El SDK de facebook_business maneja la paginación automáticamente cuando iteras sobre el objeto de respuesta.

Campos y Parámetros: La documentación de la API de Marketing de Meta es tu mejor amiga para saber qué campos y parámetros están disponibles para cada tipo de objeto y para los insights.

actions y action_values: El campo actions devuelve una lista de diccionarios, donde cada diccionario representa un tipo de acción (ej. link_click, offsite_conversions, lead). action_values devuelve el valor monetario de esas acciones. Necesitarás parsear estos campos para obtener métricas específicas como el número de leads o el valor de las compras.

Con estos ejemplos, tienes una base sólida para empezar a extraer datos de la API de Marketing de Meta para tus reportes.
"""