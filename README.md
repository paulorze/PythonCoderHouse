
# AkaliAlimentos

Sitio web diseñado para AkaliAlimentos, emprendimiento productor de alimento balanceado para felinos.




## Tech Stack

**Client:** Django, JS, Bootstrap

**Server:** Django, MySQL


## Autor

- [@paulorze](https://www.github.com/paulorze)


## Documentación

  El sitio web dispone de diversas implementaciones para asegurar una buena Experiencia de Usuario:
- Tienda con carga de productos dinámica y búsqueda de productos por su nombre;
- Formulario de contacto con persistencia en Base de Datos;
- Registro de nuevos usuarios;
- Login;
- Vistas restringidas para usuarios no identificados.
- Vista diferenciada para usuarios comunes y de tipo administrador. Ambos podrán acceder al Dashboard, pero el usuario sin privilegios solo podrá modificar sus datos, ver historial de compras y cerrar su sesión. Los administradores podrán desde su Dashboard agregar nuevos productos además de acceder al historial de compras de todos los usuarios y cerrar su sesión. También podrán modificar o eliminar los productos directamente desde la tienda.
- Persistencia de los carritos en la Base de Datos. Paso de carrito a compra una vez confirmada la misma.

## Pruebas y video de funcionamiento
Para ver las pruebas realizadas, hace click [aquí](https://docs.google.com/spreadsheets/d/1LK0ikRHCsQOmwIX5LgX-PJw0ickKvjfIBcOJuXcyy6o/edit?usp=sharing).
El video explicativo del funcionamiento del sitio esta [aquí](https://youtu.be/xF3mOaRSh9A).

## Lecciones Aprendidas

### Iniciar nuevo proyecto
  Para iniciar un nuevo proyecto en Django, debemos pararnos sobre la ruta base y correr los siguientes comandos:
  ```
    django-admin startproject projectname
    cd projectname
    python manage.py startapp appname
```

### Correr el server
  Dentro de la terminal, ejecutamos el siguiente comando:
```
    python manage.py runserver
```

### Configura la App en settings.py
```
INSTALLED_APPS = [
    'appname',
]
```
### Migrar los cambios en modelos
```
    python manage.py makemigrations
    python manage.py migrate
```

### Seteado de modelos, views, urls:
  Revisar los archivos correspondientes en las carpetas de la app y el proyecto para ver ejemplos.
