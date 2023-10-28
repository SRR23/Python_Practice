

class Product:
    
    def __init__(self, P_name, P_price):
        self.P_name=P_name
        self.P_price=P_price


class Shopping(Product):

    def __init__(self):
        self.cart={}
    
    def add_Product(self, P_name, P_price):
        super().__init__(P_name, P_price)
        self.cart[P_name]=P_price
    
    def buy_Product(self, name, price):
        self.name=name
        self.price=price
        if self.name not in self.cart:
            print('Sorry!, Product is not available')
        else:
            f=0
            for key,value in self.cart.items():
                if key==self.name:
                    if self.price >= value:
                        f=1
                    else:
                        f=value
            
            if f==1:
                print('Yes! you can buy it')
            else:
                print(f'Sorry! you need extra {f-self.price} money')
            


tani=Shopping()
tani.add_Product('Shirt', 600)
tani.add_Product('pant', 1000)
tani.add_Product('t-shirt', 700)
tani.add_Product('shoes', 1500)

tani.buy_Product('belt',600)
