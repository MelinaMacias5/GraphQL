# Mi Proyecto Zarpado 🚀

Este proyecto hace magia con la terminal. Acá te dejo cómo usarlo:

## Clonado de proyecto
```bash
git clone https://github.com/Thepropollo/GraphQL-Flask.git
cd GraphQL-Flask
```
## Creación/Activacion de Entorno Virtual
```bash
python -m venv env
```
activar si es en windows
```bash
./venv/Scripts/activate
```
activar si es en linux
```bash
source env/bin/activate
```

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Creacion de base de datos
![imagen](https://github.com/user-attachments/assets/562c9bd4-48a3-4b66-9282-4ca38130e3e6)

## Editamos la Conexion de la base de Datos
Esto dentro de algun editor como vscode<br>
///////
DENTO DEL ARCHIVO __init__.py ubicado dentro de la carpeta api<br>
///////
Ubicamos la Contraseña de nuestro postgres en PASSWORD y en DATABASE_NAME  el nombre de la base de datos que creamos previemente<br>

![imagen](https://github.com/user-attachments/assets/2b46ed79-b78f-4fdd-9931-031934691f79)

## Importar modelos
```bash

>>> from app import app, db
... 
... with app.app_context():
...     db.create_all()
...     
>>> exit
```

## Ejecutamos el Proyecto 
```bash
flask run
```
