import csv
#IMPORTANTE: aclaraciones use un csv solo para practicar porque es lo que estoy viendo de forma autodidacta si es necesario lo cambio.

#Menu  principal
def main():
    #Al iniciar el programa se cargan todos los usuarios. 
    bd_users=load_db()
    welcome_flag=0
    sesion=[0]
    
    while True:
        if sesion[0]==0:
            if welcome_flag ==0:
                print("Bienvenido que desea hacer?")
                welcome_flag +=1
            print("""   Menu:
                1)Ver base de datos
                2)Agregar usuario
                3)Logearse
                4)Salir""")
            opcion = input("Seleciones una opcion ingresando un numero: ")

            try:
                if int(opcion)==1:
                    show_db(bd_users)
                elif int(opcion)==2:
                    add_user(bd_users)
                elif int(opcion)==3:
                    login(bd_users,sesion)
                elif int(opcion)==4:
                    print("Programa  cerrado")
                    break
                else:
                    print("\n--Opcion no valida--\n")
            except ValueError:
                print("\n--Valor  ingresado  no valido--\n")
            except Exception as e:
                print(type(e).__name__)
        elif sesion[0]==1:
            print(f"Hola {sesion[1]}")

            print("""   Menu:
                1)(Agregar opciones a futuro)
                2)Cerrar sesion
                3)Salir""")
            opcion = input("Seleciones una opcion ingresando un numero: ")

            try:
                if int(opcion)==1:
                    print("----------------")
                    print("No implementado")
                    print("----------------")
                elif int(opcion)==2:
                    sesion=[0]
                    welcome_flag=0
                elif int(opcion)==3:
                    print("Programa  cerrado")
                    break
                else:
                    print("\n--Opcion no valida--\n")
            except ValueError:
                print("\n--Valor  ingresado  no valido--\n")
            except Exception as e:
                print(type(e).__name__)

#Abre archivo csv y arma diccionario con par usuario>contraseña           
def load_db():
    users={}
    with open("usuarios.csv") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            users[row["user"]]=row["password"]
    return  users
         
#Impreme la lista de usuarios>contraseña
def show_db(dic):
    print("---------------------------------")
    print("Lista de usuarios/contraseñas: ")
    for  i, x in enumerate(dic):
        print(f"{i+1}. {x} --> {dic[x]}" )
    print("---------------------------------")
    
#Agrega usuario  al diccionario en memoria y al archivo para siguientes usos del programa
def add_user(bd_users):

    new_user=input("Ingrese el nombre del nuevo usuario (4-12 caracteres,SIN caracteres especiales): ")

    while True:
        if new_user in bd_users:
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
        
    bd_users[new_user]=new_password

    with open("usuarios.csv", "a", newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["user","password"])
        writer.writerow({"user": new_user, "password":new_password})
    print("-------------------------------")
    print("Usuario agregado correctamente")
    print("-------------------------------")
    
#Trata de logear y avisa si  hay algun error con los parametros.
def login(dic,lista):
    print("Iniciando secion...")
    for x in range(3):
        user=input("Ingrese usuario: ")
        password=input("Ingrese clave: ")

        if dic.get(user)==None:
            print("---------------------------------------------")
            print("Usuario o clave incorrecta, pruebe de nuevo")
            print("---------------------------------------------")
        elif dic.get(user)!=password:
            print("---------------------------------------------")
            print("Usuario o clave incorrecta, pruebe de nuevo")
            print("---------------------------------------------")
        else:
            print("------------------------------")
            print("Usted ingreso correctamente.")
            print("------------------------------")
            lista[0]=1
            lista.append(user)
            break
    else:
        print("-------------------------------------------------")
        print("Demasiados intentos, volviendo al menu principal")
        print("-------------------------------------------------")
        
        

if __name__== "__main__":
    main()