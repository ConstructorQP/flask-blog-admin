# Blog con panel de administración

Blog web hecho con **Python, Flask y SQLite**. Tiene una parte pública para leer las entradas y un panel de administración para crearlas, editarlas y borrarlas.

Proyecto de la asignatura *Lenguajes de Marcas* de ASIR.

## Funcionalidades

- **Vista pública**: listado de entradas y página de detalle de cada una.
- **Panel `/admin`**: CRUD completo de entradas (título, fecha, autor y contenido).
- **Base de datos SQLite**: la tabla se crea sola al arrancar, con una entrada de ejemplo.
- **Plantillas Jinja2** con herencia (`base.html`) y una única hoja de estilos.

## Tecnologías

| Parte | Tecnología |
|---|---|
| Backend | Python 3 · Flask |
| Base de datos | SQLite (`sqlite3`) |
| Frontend | HTML5 · CSS3 · Jinja2 |

## Cómo ejecutarlo

```bash
git clone https://github.com/ConstructorQP/BLOG-ADMIN
cd BLOG-ADMIN/blog
pip install flask
python app.py
```

Abre `http://127.0.0.1:5000` para ver el blog y `http://127.0.0.1:5000/admin` para gestionarlo.

## Estructura

```
blog/
├── app.py               # Rutas y acceso a la base de datos
├── static/style.css     # Estilos
└── templates/
    ├── base.html        # Plantilla base
    ├── index.html       # Listado de entradas
    ├── entrada.html     # Detalle de una entrada
    ├── admin.html       # Panel de administración
    └── entrada_form.html# Formulario de alta y edición
docs/
└── memoria-proyecto.md  # Memoria de la práctica
```

## Próximas mejoras

- Login para proteger el panel de administración.
- Borrado mediante POST con confirmación en lugar de un enlace GET.
