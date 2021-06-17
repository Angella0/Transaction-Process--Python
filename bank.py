from datetime import datetime
class Account:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        self.balance = 0
        self.statement = []
        self.loan = 0
    def Show_balance(self):
        return f"Hello {self.name} you have deposited {self.balance}" 
    def deposit(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
        if amount <= 0:
            return f"you cannot deposit less than 0"
        else:
             self.balance += amount 
             now = datetime.now() 
             transaction ={
                 "amount": amount,
                 "time": now,
                 "Narration":"you deposited"

             }
             self.statement.append(transaction)
             return self.Show_balance () 
    def withdraw(self,money):
        try:
            4-money
        except TypeError:
            return f"you can not withdaw string"
        if money > self.balance:
            return f" your balance is {self.balance} you cannot withdraw {money}"
        else:
            self.balance -= money
            now = datetime.now() 
            transaction={
                "amount": money,
                "time": now,
                "Narration":"you have withdrawn"

            }
            self.statement.append(transaction)
            return self.Show_balance () 
             

    
    
    def show_statement(self):

        for transaction in self.statement:
            amount = transaction["amount"]
            narration = transaction["Narration"]
            time = transaction["time"]
            date = time.strftime("%d/%m/%y")
            print(f"{date}: {narration} {amount}")
            return

    def borrow(self,amount):
        try:
            7 + amount
        except TypeError:
            return f"You must input a figure not a word"
    
        if amount < 0:
            return f"You do not qaulify for this amount of{amount}"
        elif self.loan > 0:
          return f"You still have a loan of {amount}"
        elif amount >= 0.1 * self.balance:
            return f"You can't get ahead from here"
        else:
            loan = amount*1.05
            self.loan = loan
            self.balance += amount
            now = datetime.now() 
            transaction ={
                 "amount": amount,
                 "time": now,
                 "Narration":"you have borrowed"

             }
            self.statement.append(transaction)
            return f"You have successfully borrowed {self.loan}"

    def repay (self,amount):
        try:
            5*amount
        except TypeError:
            return f"The amount must be in figures"
        if amount < 0:
            return "You can not pay this loan"
        elif amount <= self.loan:
            loan=self.loan-amount
            self.loan = loan
            return f"You have paid {amount} and your loan is {self.loan}"
        elif amount>self.loan:
            diff = amount - self.loan
            self.loan = 0
            self.deposit(diff)
            now = datetime.now() 
            transaction ={
                 "amount": amount,
                 "time": now,
                 "Narration":"you have repaid"

             }
            self.statement.append(transaction)
            return f"You have successfully paid your loan and your current balance is{self.balance}"

    def transfer(self,account,amount):
        self.account=account
        self.amount=amount
        fee=amount*0.005
        total=fee+amount
        try:
            6 + amount
        except TypeError:
            return f"The amount should be in figures" 
      
        if total > self.balance:
            return f" your balance is {self.balance} and you need at least {total} for this transaction"
        else:
            self.balance-=total
            account.deposit(amount)
            now = datetime.now() 
            transaction ={
                 "amount": amount,
                 "time": now,
                 "Narration":"you have transferred:"

             }
            self.statement.append(transaction)
            return f"You have transferred {amount}. "
class MobileMoneyAccount(Account):
    def __init__(self,name,phoneNumber,services_provider):
        Account. __init__(self,name,phoneNumber)
        self.services_provider = services_provider

    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"the amount must be in figures"
        if amount < 0:
            return f"your amount is not enough to buy the airtime"
        elif self.balance<amount:
            return f"your balance is low to purchase this amount of credit"
        else:
            self.balance-=amount
            return f"you have purchased airtime worth {amount} from {self.services_provider}. Your account balance is {self.balance}"
                     
             



    

        


    

    
        
