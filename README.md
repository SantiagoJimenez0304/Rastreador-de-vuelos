# Login con Registro y Almacenamiento en Base de Datos

Este proyecto es una aplicación web simple construida con **Flask**, que permite a los usuarios registrarse, iniciar sesión y visualizar un sistema de autenticación con datos almacenados en una base de datos SQLite.

## Características

- **Registro de usuario**: Los usuarios pueden crear una cuenta con un nombre de usuario único y contraseña.
- **Inicio de sesión**: Los usuarios registrados pueden acceder a la aplicación mediante su nombre de usuario y contraseña.
- **Base de datos**: Se utiliza SQLite para almacenar de manera persistente los datos de los usuarios.
- **Cifrado de contraseñas**: Las contraseñas se almacenan de manera segura utilizando el método de hashing `pbkdf2:sha256`.

## Requisitos

- Python 3.8 o superior

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/nombre-del-repositorio.git
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

4. Abre tu navegador y accede a:
   ```
   http://127.0.0.1:5000/
   ```

## Archivos principales

- **main.py**: Archivo principal que contiene el código de la aplicación.
- **templates/**: Carpeta con los archivos HTML (login, registro, etc.).
- **database.db**: Archivo de la base de datos SQLite para almacenar los usuarios.

## Dependencias

- Flask
- Flask-SQLAlchemy
- Werkzeug

## Mejoras futuras

- Validación avanzada de contraseñas.
- Integración con bases de datos externas como PostgreSQL o MySQL.
- Diseño responsivo mejorado para dispositivos móviles.

---

Creado por **Santiago Jiménez** y **Enzo González**.
