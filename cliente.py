import persona

class cliente(persona.persona):
    
    def __init__(self, name,last,dni,age,email,user,password,wishlist=None) :
        super().__init__(name,last,dni,age)
        self.email=email
        self.user=user
        self.password=password
        if wishlist is None:
            wishlist =[]
        self.wishlist=wishlist

    def to_dict(self):
        return vars(self)
    
    def get_user(self):
        return self.user
    
    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.password
    
    def buy(self, product, amount,store):
        print(f"\n {self.name} compraste  {amount} {product} en  {store}.\n")
        print(f"Se envio un correo con el detalle a {self.email}.\n")

    def add_wishlist(self,product,amount,store):
        compra=[product,amount,store]
        self.wishlist.append(compra)
        print(f"\nLa compra de {amount} {product} en {store} fue agreagado a tu lista de deseados")

    def show_wishlist(self):
        if self.wishlist:
            print("\nUsted tiene los siguientes productos en lista de deseados\n")
            for buy in self.wishlist:
                print(f"- {buy[1]} {buy[0]} en {buy[2]} ")
            op=input("Desea comprarlos 1si 2no: ")
            while True:
                
                if op =="1":
                    print("\nCompra realizada")
                    print(f"Se envio un correo con el detalle a {self.email}\n")
                    self.delete_wishlist()
                    break
                elif op=="2":
                    print("\nCompra no realizada\n")
                    break
                else:
                    op=input("Opcion no valida, 1 si 2 no: ")
        else:
            print("Su lista de deseados esta vacia")

        

    
    def delete_wishlist(self):
        self.wishlist=[]
        print("\nLista de deseados vaciada\n")
        

    def __str__(self):
        return f"{super().__str__()} Mail: {self.email} "
