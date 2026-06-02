# Music Assistant IA

Mi primer proyecto backend desarrollado con Python y FastAPI.

## Descripción

Esta aplicación expone una API REST para gestionar una colección de canciones.

Actualmente permite:

* Crear canciones
* Listar canciones
* Actualizar canciones
* Eliminar canciones

Cada canción posee:

* ID
* Título
* Artista

## Tecnologías utilizadas

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git
* GitHub

## Endpoints

### Obtener canciones

```http
GET /songs
```

### Crear canción

```http
POST /songs
```

Ejemplo:

```json
{
  "title": "You shook me all night long",
  "artist": "AC/DC"
}
```

### Actualizar canción

```http
PUT /songs/{song_id}
```

Ejemplo:

```json
{
  "title": "You shook me all night long (Remastered)",
  "artist": "AC/DC"
}
```

### Eliminar canción

```http
DELETE /songs/{song_id}
```

## Ejecutar el proyecto

Instalar dependencias:

```bash
pip install fastapi uvicorn pydantic
```

Iniciar el servidor:

```bash
uvicorn main:app --reload
```

Documentación interactiva:

```text
http://127.0.0.1:8000/docs
```

## Próximas mejoras

* Persistencia con SQLite
* Búsqueda de canciones
* Filtros por artista
* Integración con IA
* Despliegue en la nube

## Autor

Franco Ortiz
