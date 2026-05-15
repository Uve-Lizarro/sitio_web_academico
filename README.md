# Website_CRUD_gestion_academica
Sistema CRUD para la gestión académica, ya sea de un instituto o universidad, dicho sistema es muy básico y sirve unicamente para ver el funcionamiento del patrón MVC, construido con Flask usa PostgreSQL como base de datos.

# Estructura del proyecto
sitio_web_academico/
│
├── run.py                      # Archivo de ejecución principal (controller)
├── config.py                   # Conexión con la base de datos (PostgreSQL)
├── db_academico.sql            # Código completo para la creación de toda la base de datos (Tablas, funciones y triggers)
│
├── models/                     # Modelos por cada tabla (lógica que se comunica con la BD)
│   ├── docente_model.py
│   ├── estudiante_model.py
│   ├── inscrito_model.py
│   ├── materia_model.py
│   └── paralelo_model.py
│
├── static/
│   └── css
│        └── estilos.css        # Hoja de estilos (vacio)
│   └── js
│        └── scripts.js         # JvaScript: busqueda
│
├── js/
│   └── main.js                 # JavaScript: nav, cookies, animaciones, form
│
├── templates/                  # Carpeta para las vistas por tabla (views)
│   └── docente/
│        └── modificar.html    
│   └── estudiante/
│        └── modificar.html    
│   └── inscrito/
│        └── modificar.html    
│   └── materia/
│        └── modificar.html    
│   └── paralelo/
│        └── modificar.html    
│   └── index.html              # Página de inicio (Home)
│
└── README.md                   # Este archivo
