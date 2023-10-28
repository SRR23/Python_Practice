

class function():

    def __init__(self):
        self.sel_gml=''
        self.sel_pas=''
        self.cust_gml=''
        self.cust_pas=''
        self.prod_amount={}
        self.prod_quantity={}
        self.product={}
        self.x=0
        self.y=0
    
    def seller(self,email,password):
        self.sel_gml=email
        self.sel_pas=password
    
    def sel_login(self,email,password):
        if self.sel_gml!=email or self.sel_pas!=password:
            return -1
        else:
            return 1
    
    def add_products(self,name,price,quantity):
        self.prod_amount[name]=price
        self.prod_quantity[name]=quantity
    
    def show_sell_products(self):
        print('-----Available products-----')
        for key,value in self.prod_amount.items():
            print(key,value,self.prod_quantity[key])

    def customer(self,email,password):
        self.cust_gml=email
        self.cust_pas=password
    
    def cust_login(self,email,password):
        if self.cust_gml!=email or self.cust_pas!=password:
            return -1
        else:
            return 1
    
    def buy_products(self,name,money,quant):
        if name not in self.prod_amount:
            print('Products not available')
        elif self.prod_quantity[name] < quant:
            print(f'sorry, only {self.prod_quantity[name]} is available')
        else:
            self.product[name]=quant
            self.prod_quantity[name]-=quant
            self.x+=self.prod_amount[name]*quant
            self.y=money
    
    def show_buying_products(self):
        print('-----Your products-----')
        print(self.product)
        print(f'Here is your extra money {self.y-self.x}')

        

def fun():
    print('1. Sign up as a Seller')
    print('2. Sign up as a Customer')
    print('3. Login')

def sel():
    print('1. Add products')
    print('2. Logout')

def buy():
    print('1. Buy products')
    print('2. Logout')


obj=function()
s=0
c=0
while True:
    fun()
    print('Enter your choice ',end="")
    n=int(input())
    match n:
        case 1:
            print('Enter your gmail ',end="")
            g=input()
            print('Enter your password ',end="")
            p=input()
            obj.seller(g,p)
            s=4

        case 2:
            print('Enter your gmail ',end="")
            g=input()
            print('Enter your password ',end="")
            p=input()
            obj.customer(g,p)
            c=5
        
        case 3:
            print('1. Seller')
            print('2. Customer')
            print('Enter your choice ',end="")
            t=int(input())
            if t==1:
                f=0
                while True:
                    print('Please login with your gmail and password')
                    print('gmail ',end="")
                    x=input()
                    print('pass ',end="")
                    y=input()
                    if obj.sel_login(x,y) == 1:
                        f=1
                        break
                    else:
                        print('try again')
            
                if f==1:
                    print('welcome')
                    while True:
                        sel()
                        print('Enter your choice ',end="")
                        x=int(input())
                        if x==1:
                            print('Name ',end="")
                            nm=input()
                            print('Price ',end="")
                            pr=int(input())
                            print('Quantity ',end="")
                            qn=int(input())
                            obj.add_products(nm, pr, qn)
                            obj.show_sell_products()
                        elif x==2:
                            break
            
            elif t==2:
                f=0
                while True:
                    print('Please login with your gmail and password')
                    print('gmail ',end="")
                    x=input()
                    print('pass ',end="")
                    y=input()
                    if obj.cust_login(x,y) == 1:
                        f=1
                        break
                    else:
                        print('try again')
            
                if f==1:
                    print('welcome')
                    obj.show_sell_products()
                    while True:
                        buy()
                        print('Enter your choice ',end="")
                        x=int(input())
                        if x==1:
                            print('Name ',end="")
                            nm=input()
                            print('Price ',end="")
                            pr=int(input())
                            print('Quantity ',end="")
                            qn=int(input())
                            obj.buy_products(nm,pr,qn)
                            obj.show_buying_products()
                        elif x==2:
                            break



""""
obj=fun()
obj.seller('abc',23)
obj.sel_login('abc',23)
obj.add_products('shirt',500,5)
obj.add_products('pant',700,5)
obj.add_products('shoes',1000,5)
obj.show_sell_products()

obj.customer('df',45)
obj.cust_login('df',45)
obj.buy_products('shirt',700,1)
"""