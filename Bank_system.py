
class function:
    def __init__(self) -> None:
        self.__reg_list={}
        self.__admin_gml=''
        self.__admin_pas=''
        self.__user_list={}
        self.__transaction_diposit={}
        self.__transaction_withdraw={}
        self.__transaction_transfer={}
        self.__transaction_loan={}
        self.__bank_total=0
        self.__total_loan=0
        self.__off_loan=0
    
    def user_reg(self,gml,pas):
        self.__reg_list[gml]=pas
        self.__user_list[gml]=0
        self.__transaction_diposit[gml]=0
        self.__transaction_withdraw[gml]=0
        self.__transaction_transfer[gml]=0
        self.__transaction_loan[gml]=0
    
    def user_login(self,gml,pas):
        if gml not in self.__reg_list or self.__reg_list[gml] != pas:
            return -1
        else:
            return 1
    
    def deposit(self,gml,money):
        if gml not in self.__user_list:
            print('Sorry, this person doesn\'t exist, try again')
        else:
            self.__user_list[gml]+=money
            self.__bank_total+=money
            self.__transaction_diposit[gml]+=money

    
    def user_balance(self,gml):
        return self.__user_list[gml]
    
    def withdraw(self,gml,money):
        if self.__user_list[gml] < money:
            print('You haven\'t sufficient money for withdraw')
        else:
            print(f'Here is your money = {money} taka')
            print(f'Your account has = {self.__user_list[gml]-money} taka')
            self.__user_list[gml]-=money
            self.__bank_total-=money
            self.__transaction_withdraw[gml]+=money
    
    
    def transer_money(self,gml1,gml,money):
        self.__user_list[gml]+=money
        self.__transaction_diposit[gml]+=money
        self.__user_list[gml1]-=money
        self.__transaction_transfer[gml1]+=money
    
    def transcation_history(self,gml):
        print('-----Transaction History-----')
        print(f'Deposit = {self.__transaction_diposit[gml]}')
        print(f'Withdraw = {self.__transaction_withdraw[gml]}')
        print(f'Transfer = {self.__transaction_transfer[gml]}')
        print(f'Loan = {self.__transaction_loan[gml]}')

    
    def admin_reg(self,gml,pas):
        self.__admin_gml=gml
        self.__admin_pas=pas
    
    def admin_login(self,gml,pas):
        if self.__admin_gml != gml or self.__admin_pas != pas:
            return -1
        else:
            return 1
    
    def bank_balance(self):
        return self.__bank_total
    
    
    def loan_on_off(self,money):
        self.__off_loan=money
    
    def user_loan(self,gml,money):
        if self.__bank_total<=self.__off_loan:
            print('Sorry, this service is off')
        elif money>self.__bank_total:
            print('Sorry, bank has insufficient money')
        elif money>self.__user_list[gml]*2:
            print('Sorry, you are not eligible for this amount of loan')     
        else:
            self.__total_loan+=money
            self.__bank_total-=money
            self.__user_list[gml]+=money
            self.__transaction_loan[gml]+=money
            print(f'Here is your loan = {money} taka')
    
    def loan_amount(self):
        return self.__total_loan
    



obj=function()
while True:
    print()
    print('1. Signup as a Admin')
    print('2. Signup as a User')
    print('3. Login')
    print('Enter your choice = ',end="")
    n=int(input())
    gm=''
    match n:
        case 1:
            print('Enter your gmail = ',end="")
            g=input()
            print('Enter your password = ',end="")
            p=input()
            obj.admin_reg(g,p)
            print()
        case 2:
            print('Enter your gmail = ',end="")
            g=input()
            print('Enter your password = ',end="")
            p=input()
            obj.user_reg(g,p)
            print()
        case 3:
            print('1. Login as a Admin')
            print('2. Login as a User')
            print('Enter your choice = ',end="")
            t=int(input())
            match t:
                case 1:
                    f=0
                    while True:
                        print('Please login with your gmail and password')
                        print('gmail = ',end="")
                        g=input()
                        print('pass = ',end="")
                        p=input()
                        if obj.admin_login(g,p) == 1:
                            f=1
                            break
                        else:
                            f=0
                            break
                        
                    if f==1:
                        print()
                        print('Welcome Admin, here is your choice:')
                        while True:
                            print('1. Check total bank balance')
                            print('2. Check total loan amount')
                            print('3. Off loan system')
                            print('4. Logout')
                            print('Enter your choice = ',end="")
                            m=int(input())
                            match m:
                                case 1:
                                    print(f'Total bank balance = {obj.bank_balance()}')
                                    print()
                                case 2:
                                    print(f'Total loan amount = {obj.loan_amount()}')
                                    print()
                                case 3:
                                    print('Enter minimum balance to off loan system = ',end="")
                                    m=int(input())
                                    obj.loan_on_off(m)
                                    print()
                                case 4:
                                    break
                    else:
                        print('Something went wrong, please try again')       

                case 2:
                    f=0
                    while True:
                        print('Please login with your gmail and password')
                        print('gmail = ',end="")
                        g=input()
                        print('pass = ',end="")
                        p=input()
                        if obj.user_login(g,p) == 1:
                            f=1
                            gm=g
                            break
                        else:
                            break

                    if f==1:
                        print()
                        print('Welcome User, here is your choice:')
                        while True:
                            print('1. Deposite money')
                            print('2. Withdraw money')
                            print('3. Check balance')
                            print('4. Transfer money')
                            print('5, Show transaction')
                            print('6. Apply for loan')
                            print('7. Logout')
                            print('Enter your choice = ',end="")
                            m=int(input())
                            match m:
                                case 1:
                                    print('Enter money = ',end="")
                                    p=int(input())
                                    obj.deposit(gm,p)
                                    print()
                                case 2:
                                    print('Enter money = ',end="")
                                    p=int(input())
                                    obj.withdraw(gm,p)
                                    print()
                                case 3:
                                    print(f'Total balance of, {gm} = {obj.user_balance(gm)} taka')
                                    print()
                                case 4:
                                    print('Receiver gmail = ',end="")
                                    g2=input()
                                    print('Transfer money = ',end="")
                                    p=int(input())
                                    if obj.user_balance(gm)<p:
                                        print('Sorry, you haven\'t sufficient money for transfer')
                                    else:
                                        obj.transer_money(gm,g2,p)
                                    print()
                                case 5:
                                    obj.transcation_history(gm)
                                    print()
                                case 6:
                                    print('Loan amount = ',end="")
                                    loan=int(input())
                                    obj.user_loan(gm,loan)
                                    print()
                                    
                                case 7:
                                    break
                    
                    else:
                        print('Something went wrong, please try again')
