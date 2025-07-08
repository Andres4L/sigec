# 🏥 SIGEC - Sistema de Gestión de Pacientes

Este es un sistema básico de gestión de pacientes (SIGEC) que incluye:

- API RESTful con Flask (Python)
- Base de datos MySQL
- Frontend en HTML, CSS y JavaScript (vanilla)
- Comunicación vía Fetch API
- Separación de capas backend/frontend

---
---

## ⚙️ Requisitos

- Python 3.10+
- MySQL Server
- Navegador web (Chrome, Firefox, etc.)

---

## 🛠️ Instalación y Ejecución

### 1. Clonar o descargar el proyecto

git clone <url-del-repo> sigec
cd sigec

2. Configurar la base de datos MySQL
Abrir DataGrip o consola de MySQL.

Ejecutar:

CREATE DATABASE sigec_db;

CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    genero VARCHAR(10),
    numero_identificacion VARCHAR(50) UNIQUE
);


3. Backend (Flask API)
a. Crear entorno virtual (solo una vez)
cd backend
python -m venv venv
.\venv\Scripts\activate.bat
 En Windows CMD

b. Instalar dependencias

pip install Flask Flask-SQLAlchemy flask-cors pymysql

c. Archivo app.py (ya incluido) debe tener:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sigec_db' 
Ajustar usuario y contraseña según tu configuración de MySQL.

d. Ejecutar el servidor

python app.py
en CMD en la ruta donde se encuentra el backend en mi caso "C:\Users\andre\Desktop\Workspace\sigec\sigec-backend"

deberia mostrar algo como:
* Running on http://127.0.0.1:5000/


4. Frontend

a. Abrir con Live Server (VSCode) (en mi caso) el archivo index.html:


## 🌐 API Endpoints
GET	/pacientes	Lista todos los pacientes
GET	/pacientes/<id>	Obtiene paciente por ID
POST	/pacientes	Crea un nuevo paciente

## 🧪 Pruebas
Se uede usar Postman para probar los endpoints directamente:

GET http://127.0.0.1:5000/pacientes

POST http://127.0.0.1:5000/pacientes con body JSON

GET http://127.0.0.1:5000/pacientes/1


##❗ CORS
Se usa flask-cors para permitir conexión entre el frontend (localhost:5500) y backend (localhost:5000).


## 📸 Capturas 
![image](https://github.com/user-attachments/assets/0e26ba60-0933-49a9-bacb-0d517a284ebf)
![image](https://github.com/user-attachments/assets/c558f875-8333-426c-827c-d2884c890955)
![image](https://github.com/user-attachments/assets/17839725-319e-4147-bfa1-eaebcbc325d3)
![image](https://github.com/user-attachments/assets/80f08a0c-e6e5-4c71-8f4a-3550340c8246)
![image](https://github.com/user-attachments/assets/aeb55a34-1394-4e99-9944-a08cba7a07bb)


## 📌 Autor
Andrés Altamar
Prueba técnica - Gestión de Pacientes
Tecnologías: Flask · MySQL · HTML · CSS · JS



