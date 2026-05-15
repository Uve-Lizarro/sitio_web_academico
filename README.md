# Website_CRUD_gestion_academica
Sistema CRUD para la gestión académica, ya sea de un instituto o universidad, dicho sistema es muy básico y sirve unicamente para ver el funcionamiento del patrón MVC, construido con Flask usa PostgreSQL como base de datos.

# Para ejecutar
El proyecto fue concebido en su totalidad usando Python 3.11.0 y PostgreSQL 17.7, en el archivo `db_academico.sql` esta todo el código para copiarlo directo en el pgAdmin 4, de cambiar el nombre de la base de datos, asegurese de que en el archivo `config.py` coincida con los nombres que coloque.
Asimismo, es necesario contar con las librerias necesarias para ejecutarlo (en local o en un host, esto mediante VS Code).
```text
py -3.11 -m pip install Flask
py -3.11 -m pip install psycopg2
```

# Estructura del Proyecto

```text
sitio_web_academico/
│
├── run.py                      # Archivo de ejecución principal (Controller)
├── config.py                   # Conexión con la base de datos (PostgreSQL)
├── db_academico.sql            # Código SQL para la creación de la base de datos (Tablas, funciones y triggers)
│
├── models/                     # Modelos por cada tabla (Lógica de comunicación con la BD)
│   ├── docente_model.py
│   ├── estudiante_model.py
│   ├── inscrito_model.py
│   ├── materia_model.py
│   └── paralelo_model.py
│
├── static/                     # Archivos estáticos del proyecto
│   ├── css/
│   │   └── estilos.css         # Hoja de estilos personalizados (Vacía)
│   └── js/
│       ├── scripts.js          # JavaScript: Configuración de búsquedas avanzadas (Select2)
│       └── main.js             # JavaScript: Navegación, cookies, animaciones y formularios
│
├── templates/                  # Vistas HTML organizadas por módulos (Views)
│   ├── docente/
│   │   └── modificar.html    
│   ├── estudiante/
│   │   └── modificar.html    
│   ├── inscrito/
│   │   └── modificar.html    
│   ├── materia/
│   │   └── modificar.html    
│   ├── paralelo/
│   │   └── modificar.html    
│   └── index.html              # Página de inicio principal (Home)
│
└── README.md                   # Documentación general del proyecto
```
