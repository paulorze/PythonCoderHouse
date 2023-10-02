#Importamos json para poder manejar los datos de los archivos.
import json
#Importamos os para poder limpiar la consola antes de mostrar una tabla o un menu de opciones.
import os

#Creamos la variable que indicara al programa principal si el usuario ha iniciado sesion o es invitado.
#Creamos la variable que indica si el usuario es administrador o no, para modificar las opciones a las cuales tendra acceso.
#Creamos la variable que guardara el nombre de usuario una vez que inicia sesion de manera exitosa y la variable que guardara la lista en caso de que coloque productos en el carrito.
sesion_iniciada = False
sesion_administrador = False
sesion_username = ""
sesion_mail = ""
sesion_carrito = []

#Creamos la funcion que mostrara el menu de entrada y nos derivara a la opcion correspondiente dependiendo de la eleccion del usuario.
def menu_principal():
    print('''
                            Bienvenido a nuestro programa. Podras ver todos nuestros productos, filtrarlos por categoria o buscar por nombre y codigo.
                Puedes entrar como invitado, pero si inicias sesion, podras acceder tambien a la posibilidad de agregar productos a un carrito y solicitarnos un presupuesto.
                    
                                                                    [1] Iniciar Sesion.
                                                                    [2] Crear un nuevo usuario.
                                                                    [x] Cerrar el programa. 
        ''')
    decision = input('>>>>> La opcion elegida es >>>>> ')
    if decision == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        iniciar_sesion()
    elif decision == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        crear_usuario()
    elif decision == 'x':
        print('¡¡¡Gracias por haber utilizado nuestro programa!!!')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()

#Creamos la funcion que utilizaremos para iniciar sesion
def iniciar_sesion ():
# En primera instancia, accedemos al archivo que contiene los nombres de usuario.
# Luego, transformamos el archivo (para poder iterar sus diccionarios).
    users = open('./usuarios.json','r',encoding='utf-8')
    users_list = json.load(users)
#Pedimos al usuario que ingrese su nombre de usuario y contraseña, lo almacenamos en dos variables.
    print(f'''
                    ////////////////////////////////////
                    ////////// INICIAR SESION //////////
                    ////////////////////////////////////
        ''')
    username = input('>>>>> Por favor, ingrese su nombre de usuario >>>>> ')
    password = input('>>>>>    Por favor, ingrese su contraseña     >>>>> ')
#Llamamos a las variables iniciadas globalmente para que sean reconocidas dentro de la funcion.
    global sesion_iniciada
    global sesion_administrador
    global sesion_username
    global sesion_mail
#Iniciamos un bucle for en el cual revisamos cada user en users_list para ver si coinciden el usuario Y la contraseña, siempre que aun no se haya encontrado ninguna correspondencia.
#Si el usuario corresponde al de un administrador, tambien volvemos verdadera la variable sesion_administrador.
#Si no se encuentran correspondencias de usuario y contraseña, se le comunica al usuario y se vuelven a pedir los datos.
    for user in users_list:
        if sesion_iniciada == False:
            if user['username'] == username and user['password'] == password:
                sesion_iniciada = True
                sesion_username = user['username']
                sesion_mail = user['mail']
                if user['administrator'] == True:
                    sesion_administrador = True
        else:
            break
    if sesion_iniciada == False:
        print('''
    ❌❌❌ El nombre de usuario o contraseña ingresados son incorrectos. ¿Desea intentarlo nuevamente? ❌❌❌
                                
                                        [1] Iniciar Sesion nuevamente.
                                        [x] Salir del programa
                        ''')
        iniciar_sesion_nuevamente()
    else:
        if sesion_administrador == False:
                    print('''
            Usted ha iniciado sesion como usuario registrado.
                        ''')
        else:
            print('''
            Usted ha iniciado sesion como usuario administrador.
                        ''')

#Creamos una funcion que permitira al usuario decidir si desea intentar nuevamente iniciar sesion o simplemente acceder como invitado.
def iniciar_sesion_nuevamente ():
    decision = input('''>>>>> La opcion elegida es >>>>> ''')
    if decision == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        iniciar_sesion()
    elif decision == 'x':
        print('¡¡¡Gracias por haber utilizado nuestro programa!!!')
    else:
        print('❌❌❌ Por favor, ingrese una opcion valida ❌❌❌')
        iniciar_sesion_nuevamente()

#Creamos una funcion que permita al usuario crear un nuevo usuario.
def crear_usuario():
    users = open('./usuarios.json','r',encoding='utf-8')
    users_list = json.load(users)
    print('''
                ////////////////////////////////////////////////////
                //// Bienvenido al menu de creacion de usuario. ////
                ////////////////////////////////////////////////////
        ''')
    print('''
    En primer lugar, ingrese su Nombre de Usuario. El mismo no debera existir en nuestra base de datos. No distingue entre mayusculas y minusculas.
    ''')
    username = verify_user(users_list)
    print('''
    En segundo lugar, ingrese su mail. El mismo no debera existir en nuestra base de datos y debe tener un formato valido (incluir '@' y '.com'). No distingue entre mayusculas y minusculas.
    ''')
    mail = verify_mail(users_list)
    print('''
    En tercer lugar, ingrese su contrasena. La misma debe contar con al menos 8 caracteres, una mayuscula, una minuscula y un numero.
    ''')
    primera_contrasena = verify_password()
    print('''
    Por favor, confirme su contrasena ingresandola nuevamente.
    ''')
    segunda_contrasena = verify_second_password(primera_contrasena)
    nuevo_usuario = {
        "username" : username,
        "password" : primera_contrasena,
        "mail" : mail,
        "administrator" : False
    }
    users_list.append(nuevo_usuario)
    with open ('./usuarios.json','w',encoding='UTF-8') as users_nuevo:
        users_nuevo.write(json.dumps(users_list,indent=2))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
El usuario ha sido creado exitosamente. Por favor, inicie sesion para confirmar el usuario.''')
    iniciar_sesion()

def verify_user(users_list):
    username_invalido = False
    username = input('>>>>> Nombre de Usuario deseado >>>>> ').lower().strip()
    if len(username) == 0:
        username_invalido = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print('❌❌❌ Por favor, ingrese un nombre de usuario ❌❌❌')
        return verify_user(users_list)
    else:
        for user in users_list:
            if user["username"] == username:
                username_invalido = True
                os.system('cls' if os.name == 'nt' else 'clear')
                print('❌❌❌ El Nombre de Usuario solicitado ya existe en nuestra base de datos. ❌❌❌')
                return verify_user(users_list)
                break
    if username_invalido == False:
        return username

def verify_mail(users_list):
    mail_invalido = False
    mail = input('>>>>> Su direccion de mail es >>>>> ').lower().strip()
    if len(mail) < 8 or not '@' in mail or not '.com' in mail:
        mail_invalido = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print('❌❌❌ Por favor, ingrese un mail de formato valido. ❌❌❌')
        verify_mail(users_list)
    else:
        for user in users_list:
            if user["mail"] == mail:
                mail_invalido = True
                os.system('cls' if os.name == 'nt' else 'clear')
                print('❌❌❌ El mail ingresado ya existe en nuestra base de datos. ❌❌❌')
                verify_mail(users_list)
                break
    if mail_invalido == False:
        return mail

def verify_password():
    primera_contrasena = input('>>>>> Nueva contrasena >>>>> ')
    length = False
    uppercase = False
    lowercase = False
    number = False
    if len(primera_contrasena) >= 8:
        length = True
    for caracter in primera_contrasena:
        if caracter.isupper():
            uppercase = True
            break
    for caracter in primera_contrasena:
        if caracter.islower():
            lowercase = True
            break
    for caracter in primera_contrasena:
        if caracter.isdigit():
            number = True
            break
    if length and uppercase and lowercase and number:
        return primera_contrasena
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('❌❌❌ Por favor, ingrese una contrasena valida.❌❌❌')
        verify_password()

def verify_second_password(primera_contrasena):
    segunda_contrasena = input('>>>>> Ingrese nuevamente su contrasena >>>>> ')
    if segunda_contrasena != primera_contrasena:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('❌❌❌ Las contrasenas no coinciden. ❌❌❌')
        verify_second_password(primera_contrasena)
    else:
        return segunda_contrasena


menu_principal()