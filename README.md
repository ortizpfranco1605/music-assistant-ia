# 🎵 Music Assistant

Uno de mis primeros proyectos **full-stack**, desarrollado con **Python**, **FastAPI**, **SQLite** y un frontend en **HTML, CSS y JavaScript**.

El objetivo de este proyecto fue comenzar a desarrollar aplicaciones completas, conectando un frontend con una API REST y una base de datos.

# 🚀 Funcionalidades

## Backend

* CRUD completo de canciones.
* Búsqueda de canciones por ID.
* Búsqueda de canciones por artista.
* Persistencia de datos utilizando SQLite.
* Validación de datos mediante Pydantic.
* Documentación automática de la API con Swagger.

## Frontend

* Listado dinámico de canciones.
* Crear canciones.
* Editar canciones.
* Eliminar canciones.
* Interfaz con tema oscuro.
* Formulario reutilizable para crear y editar.
* Actualización dinámica de la interfaz utilizando Fetch API.

---

# 🛠 Tecnologías utilizadas

## Backend

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn

## Frontend

* HTML
* CSS
* JavaScript
* Fetch API

## Herramientas

* Git
* GitHub

---

# 📌 API REST

| Método | Endpoint           | Descripción                  |
| ------ | ------------------ | ---------------------------- |
| GET    | `/songs`           | Obtener todas las canciones  |
| GET    | `/songs/{song_id}` | Buscar una canción por ID    |
| GET    | `/songs/search`    | Buscar canciones por artista |
| POST   | `/songs`           | Crear una nueva canción      |
| PUT    | `/songs/{song_id}` | Actualizar una canción       |
| DELETE | `/songs/{song_id}` | Eliminar una canción         |

---

# ⚙️ Cómo ejecutar el proyecto

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Ingresar al proyecto:

```bash
cd Music-Assistant
```

Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

Activar el entorno virtual:

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install fastapi uvicorn pydantic
```

Iniciar el servidor:

```bash
uvicorn main:app --reload
```

Abrir la documentación interactiva:

```text
http://127.0.0.1:8000/docs
```

---

# 📚 Lo que aprendí

Durante el desarrollo de este proyecto puse en práctica conceptos como:

* Desarrollo de APIs REST con FastAPI.
* Operaciones CRUD (Create, Read, Update y Delete).
* Persistencia de datos utilizando SQLite.
* Validación de datos mediante Pydantic.
* Consumo de APIs desde JavaScript utilizando Fetch API.
* Manipulación del DOM.
* Integración entre frontend y backend.
* Organización de un proyecto full-stack.
* Uso de Git y GitHub para el control de versiones.

---

# 🚀 Próximas mejoras

* Conectar la búsqueda por ID al frontend.
* Conectar la búsqueda por artista al frontend.
* Mejorar la interfaz para dispositivos móviles.
* Publicar la aplicación en la nube.
* Incorporar nuevas funcionalidades relacionadas con música.

---

# 💡 Sobre este proyecto

Este proyecto representa un paso importante en mi aprendizaje como desarrollador.

Después de realizar la carrera de Licenciatura en Informática en UDE, cursos, resolver ejercicios y proyectos académicos durante un tiempo, decidí comenzar a desarrollar aplicaciones completas para integrar backend, frontend y base de datos en un mismo proyecto.

Mi objetivo es seguir construyendo nuevos proyectos para continuar aprendiendo y ampliar mi portfolio.

---

# 👨‍💻 Autor

**Franco Ortiz**
