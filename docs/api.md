# API Documentation

## Autenticación
### POST /api/auth/login
Login de usuario

**Request Body:**
```json
{
  "email": "string",
  "password": "string"
}
```

### POST /api/auth/register
Registro de nuevo usuario

**Request Body:**
```json
{
  "name": "string",
  "email": "string",
  "password": "string",
  "role": "string"
}
```

## Tareas
### GET /api/tasks
Obtener lista de tareas

### POST /api/tasks
Crear nueva tarea

**Request Body:**
```json
{
  "title": "string",
  "description": "string",
  "dueDate": "string",
  "status": "string",
  "type": "string",
  "assignedTo": "string"
}
```

[Resto de endpoints pendientes]
