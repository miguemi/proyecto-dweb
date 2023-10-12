# Proyecto - Desarrollo Web

Proyecto final del curso Desarrollo Web basado en la siguiente:
[serie de videos](https://youtube.com/playlist?list=PLxm9hnvxnn-j5ZDOgQS63UIBxQytPdCG7).

## 1. Dependencias

### PostgreSQL 
Esta [dependencia](https://www.postgresql.org/download/) es opcional ya que podemos configurar 
el proyecto para utilizar SQLite, pero en caso de usar la configuración por defecto debemos de instalar 
PostgreSQL. 

### GTK3
Esta [dependencia](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer) 
NO es opcional, la necesitaremos para crear los PDF's dentro del apartado de ventas.

## 2. Como inicializar el proyecto 

Lo primero que tenemos que realizar es clonar el proyecto de este repositorio, 
posteriormente debemos de situarnos en la carpeta raiz del proyecto.

### Configuración del entorno virtual de Python
- Estando situados en el directorio raiz del proyecto debemos de crear nuestro entorno
virtual con el siguiente comando `python -m venv env`

- Una vez creado el entorno virtual debemos de activarlo con el siguiente comando
```.\env\Scripts\activate``` si activamos correctamente el entorno debe aparecer
la terminal con el prefijo (env)

- Por ultimo tenemos que instalar las dependencias, dentro del directorio raiz
hay un archivo llamado `requirements.txt`, este archivo contiene todas las dependencias
necesarias para el proyecto; para instalarlas debemos de ejecutar 
el siguiente comando `pip install -r requirements.txt` 

### Configuración del proyecto de Django
- Primero debemos de situarnos en la carpeta "src" que es donde se encuentran los archivos
del proyecto de Django (`cd ./src/`)

- Luego debemos de crear las migraciones de los modelos de django 
con el siguiente comando `python .\manage.py makemigrations`

- Una vez creadas las migraciones debemos de ejecutar el comando `python .\manage.py migrate`
para crear los modelos en nuestra base de datos respectiva.

- Por ultimo debemos de crear los archivos estaticos con el comando `python .\manage.py collectstatic`

### Iniciar el proyecto

Si realizamos los pasos anteriores con exito deberiamos de ser capaces de poner
en ejecucion nuestro servidor con el siguiente comando `python .\manage.py runserver`

## 3. Anexos

- [Setup de Django](https://realpython.com/django-setup/)
