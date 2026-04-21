# LTRC Registry

**La Tribu Running Club** — Sistema de registro en línea para eventos de carrera.

## Descripción

LTRC Registry es una aplicación web desarrollada en Django para gestionar el registro de corredores al evento anual **THE END** organizado por La Tribu Running Club. Permite a los participantes registrarse en línea, confirmar su asistencia y consultar la lista de corredores inscritos.

## Características

- 📝 Formulario de registro de corredores
- ✅ Confirmación de registro por correo electrónico
- 📋 Listado de corredores con búsqueda por nombre
- 🎽 Selección de talla de playera (CH / M / G)
- 🏃 Gestión de clubes de running
- 📅 Soporte para múltiples ediciones del evento (por año)
- 🔐 Panel de administración (Django Admin)
- 📄 Página de aviso de privacidad y ruta del evento

## Tecnologías

| Herramienta | Versión |
|---|---|
| Python | 3.6.7 |
| Django | 2.1.3 |
| PostgreSQL | — |
| Gunicorn | 19.9.0 |
| Whitenoise | 4.1.1 |
| django-import-export | 1.2.0 |
| django-phonenumber-field | 3.0.1 |

## Requisitos previos

- Python 3.6+
- PostgreSQL
- pip

## Instalación local

```bash
# 1. Clonar el repositorio
git clone https://github.com/iscenigmax/ltrc-registry.git
cd ltrc-registry/ltrc

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno / settings.py
#    Edita ltrc/settings.py y agrega:
#      - SECRET_KEY
#      - Credenciales de la base de datos (DATABASES)
#      - Credenciales de correo (EMAIL_*)

# 5. Aplicar migraciones
python manage.py migrate

# 6. Crear superusuario
python manage.py createsuperuser

# 7. Levantar el servidor de desarrollo
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Estructura del proyecto

```
ltrc/
├── ltrc/           # Configuración principal del proyecto (settings, urls, wsgi)
├── registro/       # App principal: registro y gestión de corredores
├── inicio/         # App de la página de inicio
├── w2r/            # App auxiliar (Walk to Run)
├── templates/      # Plantillas HTML globales
├── requirements.txt
├── manage.py
├── Procfile        # Configuración para despliegue en Heroku
└── runtime.txt     # Versión de Python para Heroku
```

## URLs principales

| Ruta | Descripción |
|---|---|
| `/` | Página de inicio |
| `/registro/corredor/create/` | Formulario de registro |
| `/registro/corredor/` | Listado de corredores |
| `/confirmacion/<id>/` | Confirmación de registro |
| `/terminos/` | Aviso de privacidad |
| `/ruta/` | Ruta del evento |
| `/admin/` | Panel de administración |

## Despliegue en Heroku

El proyecto incluye `Procfile` y `runtime.txt` para despliegue directo en Heroku:

```bash
heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Licencia

Consulta el archivo [LICENSE](LICENSE) para más detalles.
