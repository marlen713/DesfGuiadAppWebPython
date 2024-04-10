# DesfGuiadAppWebPython
Desafío guiado - Aplicación de web en Python

Tips: Las urls quedarían de la siguiente forma:
from holaMundo.views import home,about, contact
urlpatterns = [
path('admin/', admin.site.urls),
path('', home),
path('about/', about),
path('contact/', contact)
]

Requerimientos
1. Crea la vista para el Home de la aplicación.
(3 Puntos)
2. Crea la vista para el About de la aplicación.
(3 Puntos)
3. Crea la vista para el Contact de la aplicación y posee un mini formulario de contacto
para ejemplificarle al cliente el resultado.
(4 Puntos)


http://127.0.0.1:8000/