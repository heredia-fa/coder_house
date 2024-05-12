import  json
from cliente import *

#Cambie el archivo por un json para poder guardar clientes, cuando estaba haciendo la parte de guardar modificaciones en la bd
#me di cuenta que cuando paso un cliente es por memoria en un primer momento recorria la lista de clientes lo borraba
#y hacia append del mismo modificado.
#Cuando me di cuenta que lo manejaba por memoria saque eso y hice un save en cada modificacion. 
#Me podrias decir si eso esta bien en la devolucion? Gracias
#Tambien entiendo que con archivos grandes esa no esta no es la forma correcta o si?


#Menu  principal
def main():
    #Al iniciar el programa se cargan todos los usuarios. 
    bd_users, dic_users=load_db()
    welcome_flag=0
    #cliente_sesion=None Esta iniciada una sesion para pruebas mas rapidas
    cliente_sesion=bd_users[1]
    
    while True:
        if cliente_sesion==None:
            if welcome_flag ==0:
                print("Bienvenido que desea hacer?")
                welcome_flag =1
            print("""   Menu:
                1)Ver lista usuarios
                2)Nuevo Cliente
                3)Logearse
                4)Salir""")
            opcion = input("Seleciones una opcion ingresando un numero: ")

            try:
                if int(opcion)==1:
                   print( show_db(dic_users))
                elif int(opcion)==2:
                    add_user(bd_users,dic_users)
                elif int(opcion)==3:
                    cliente_sesion=login(bd_users,dic_users)
                elif int(opcion)==4:
                    print("Programa  cerrado")
                    break
                else:
                    print("\n--Opcion no valida--\n")
            except ValueError:
                print("\n--Valor  ingresado  no valido--\n")
            except Exception as e:
                print(type(e).__name__)
        else :
            print(f"Hola {cliente_sesion.get_name()}")

            print("""   Menu:
                1)Comprar
                2)Agreagar a lista de deseados
                3)Mostrar lista de deseados
                4)Borrar lista de deseados
                5)Guardar cambios lista de deseados
                6)Cerrar sesion
                7)Salir""")
            opcion = input("Seleciones una opcion ingresando un numero: ")
            #Menu nuevo de compra cliente
            try:
                if int(opcion)==1:
                    product=input("Ingrese el producto que desea comprar: ")
                    amount=input("Ingrese la cantidad que desea comprar: ")
                    store=input("Ingrese la tienda donde desea comprarlo: ")
                    cliente_sesion.buy(product,amount,store)
                elif int(opcion)==2:
                    product=input("Ingrese el producto que desea agregar a la lista: ")
                    amount=input("Ingrese la cantidad que desea agregar a la lista: ")
                    store=input("Ingrese la tienda donde desea agregar a la lista: ")
                    cliente_sesion.add_wishlist(product,amount,store)
                    save_db(bd_users)
                elif int(opcion)==3:
                    cliente_sesion.show_wishlist()
                    save_db(bd_users)
                elif int(opcion)==4:
                    cliente_sesion.delete_wishlist()
                    save_db(bd_users)
                    

                elif int(opcion)==6:
                    cliente_sesion=None
                    welcome_flag=0
                elif int(opcion)==7:
                    print("Programa  cerrado")
                    break
                else:
                    print("\n--Opcion no valida--\n")
            except ValueError:
                print("\n--Valor  ingresado  no valido--\n")
            except Exception as e:
                print(type(e).__name__)

#Abre archivo json y arma una lista de clientes, ademas arma un dic usuario>clave para manejar login mas facil           
def load_db():
    with open("Preentraga\\Preentrega2\\clientes.json", "r") as json_file:
        json_load_customers = json.load(json_file)
        load_customers = [cliente(**customer) for customer in json_load_customers]
        dic={}
        for customer in load_customers:
            dic[customer.get_user()]= customer.get_password()
        return load_customers,dic
    
#Funcion para transformar y guardar json
def save_db(bd_users):
    #transforma los clientes a dic
    customer_dict = [customer.to_dict() for customer in bd_users]
    #reescrive json
    with open("F:Preentraga\\Preentrega2\\clientes.json", "w") as json_file:
        json.dump(customer_dict, json_file,indent=4)
         
#Impreme de la lista pares usuario>contraseña usando el diccionario
def show_db(dic):
    
    str_lista="---------------------------------\n"
    str_lista+="Lista de usuarios/contraseñas: \n"
    for  i, x in enumerate(dic):
        str_lista+= f"{i+1}. {x} --> {dic[x]} \n" 
    str_lista+="---------------------------------\n"
    return str_lista
    
#Agrega usuario  al diccionario en memoria y al archivo para siguientes usos del programa
def add_user(bd_users,dic_users):

    new_user=input("Ingrese el nombre del nuevo usuario (4-12 caracteres,SIN caracteres especiales): ")

    while True:
        if new_user in dic_users:
            new_user=input("El nombre de usuario ya existe, ingrese otro usuario: ")
            continue
        elif not 3<len(new_user)<13:
            new_user=input("Cantidad de caracteres erroneo ingrese otro usuario: ")
            continue
        elif  not new_user.isalnum():
            new_user=input("El usuario  no debe tener caracteres especiales, ingrese otro usuario: ")
            continue

        break

    new_password=input("Ingrese la clave del nuevo usuario (4-12 caracteres): ")
    new_password_confirmation=input("Reingrese la clave: ")

    while True:
        if not 3<len(new_password)<13:
            print("Cantidad de caracteres erroneo")
            new_password=input("Ingrese la clave del nuevo usuario (4-12 caracteres): ")
            new_password_confirmation=input("Reingrese la clave: ")
            continue
        elif new_password!=new_password_confirmation:
            print("Las claves no coinciden, pruebe de nuevo")
            new_password=input("Ingrese la clave del nuevo usuario (4-12 caracteres): ")
            new_password_confirmation=input("Reingrese la clave: ")
            continue

        break
        
    

    print("Usuario y clave aceptados, por favor ingrese el resto de la informacion del cliente")

    # Luego de validar usuario y contraseña pide name last dni age email
    # Por ahota valida entero y un dato mal ingresado obliga a ingresar todo de vuelta, si tengo tiempo lo cambio.
    while True:
        try:
            new_name=input("Ingrese el nombre del cliente: ").capitalize().strip()
            new_last=input("Ingrese apellido del cliente: ").capitalize().strip()
            new_dni=input("Ingrese dni. Solo los 7-8 numeros sin puntos: ")
            if 6<len(new_dni)<9:
                new_dni=int(new_dni)
            else:
                print ("Cantidad de numeros incorrecta, pruebe de vuelta")
                continue

            new_age=int(input("Ingrese edad, solo numeros: "))
            new_email=input("Ingrese email: ")
            if "@" not in new_email or "." not  in new_email:
                print("Email no valido pruebe de vuelta")
                continue
            break
            
        except Exception as e:
            print(type(e).__name__)
            print("Algun dato no es valido pruebe de vuelta")
            continue

    
    #agrega a dic
    dic_users[new_user]=new_password

    #agreaga a lista clientes
    new_customer= cliente(new_name,new_last,new_dni,new_age,new_email,new_user,new_password)
    bd_users.append(new_customer)

    #reescrive json
    save_db(bd_users)
    

    print("-------------------------------")
    print("Usuario agregado correctamente")
    print("-------------------------------")
    
#Trata de logear y avisa si  hay algun error con los parametros.
def login(bd_users,dic_users):
    print("Iniciando secion...")
    for x in range(3):
        user=input("Ingrese usuario: ")
        password=input("Ingrese clave: ")

        if dic_users.get(user)==None:
            print("---------------------------------------------")
            print("Usuario o clave incorrecta, pruebe de nuevo")
            print("---------------------------------------------")
        elif dic_users.get(user)!=password:
            print("---------------------------------------------")
            print("Usuario o clave incorrecta, pruebe de nuevo")
            print("---------------------------------------------")
        else:
            print("------------------------------")
            print("Usted ingreso correctamente.")
            print("------------------------------")
            for customer in bd_users:
                if customer.get_user()==user:
                    print (customer)
                    return customer
            
    else:
        print("-------------------------------------------------")
        print("Demasiados intentos, volviendo al menu principal")
        print("-------------------------------------------------")


    
        
        

if __name__== "__main__":
    main()