

class seller():
    
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        self.prod_amount={}
        self.prod_quantity={}
    
    def login(self, mail, pas):
        if self.email!=mail or self.password!=pas:
            return -1
        else:
            return 1
    
    def add_products(self,name, price, quantity):
        self.prod_amount[name]=price
        self.prod_quantity[name]=quantity
    
    def product_amount(self):
        return self.prod_amount
    
    def product_quantity(self):
        return self.prod_quantity
    
    def __repr__(self):
        print('------Products lists------')
        for key,value in self.prod_amount.items():
            print(key,value,self.prod_quantity[key])



class customer():

    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        self.price_list={}
        self.quantity_list={}
        self.total_product_price=0
        self.total_customers_money=0
    
    def login(self, mail, pas):
        if self.email!=mail or self.password!=pas:
            return -1
        else:
            return 1
    
    def show(self,ar_n,ar_q):
        print('-----Available products-----')
        for key, value in ar_n.items():
            print(key,value,ar_q[key])
    
    def buy_products(self, name, amount, quantity, ar_n, ar_q):
        self.price_list[name]=ar_n[name]
        self.quantity_list[name]=ar_q[name]
        self.total_product_price=ar_n[name]*quantity
        self.total_customers_money=amount
        ar_q[name]-=1
    
    def __repr__(self):
        print('------Here is your product------')
        for key,value in self.price_list.items():
            print(key,value,self.quantity_list[key])
        print(f'Here is your extra money - {self.total_customers_money-self.total_product_price}')


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


tmp1={}
tmp2={}
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
            obj=seller(g,p)
            f=0
            while True:
                print('Please login with your gmail and password')
                print('gmail ',end="")
                x=input()
                print('pass ',end="")
                y=input()
                if obj.login(x,y) == 1:
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
                        obj.__repr__()
                    elif x==2:
                        break
            tmp1=obj.product_amount()
            tmp2=obj.product_quantity()

        case 2:
            print('Enter your gmail ',end="")
            g=input()
            print('Enter your password ',end="")
            p=input()
            obj=customer(g,p)
            f=0
            while True:
                print('Please login with your gmail and password')
                print('gmail ',end="")
                x=input()
                print('pass ',end="")
                y=input()
                if obj.login(x,y) == 1:
                    f=1
                    break
                else:
                    print('try again')
            
            if f==1:
                print('welcome')
                obj.show(tmp1,tmp2)
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
                        obj.buy_products(nm,pr,qn,tmp1,tmp2)
                        obj.__repr__()
                    elif x==2:
                        break













robi=seller('robi@gmail.com', 12345)

""""
p=robi.login('robi@gmail.com', 12345)
if(p == -1):
    print('Something wen wrong, plz try again!!')
else:
    print('Welcome Seller')
    robi.add_products('shirt', 600, 4)
    robi.add_products('pant',1000, 3)
robi.__repr__()
obj=robi.product_amount()



rimon=customer('rimon@gmail.com',5678)
q=rimon.login('rimon@gmail.com',5678)
if(q==-1):
    print('Something went wrong, plz try again!!')
else:
    print('Welcome Customer')
    rimon.buy_products('pant', 1002, 2, obj)
rimon.__repr__()
"""