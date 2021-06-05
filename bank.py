from datetime import datetime
class Account:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        self.balance = 0
        self.statement = []
    def Show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}" 
    def deposit(self,amount):
        if amount <= 0:
            return f"you cannot deposit less than 0"
        else:
             self.balance += amount 
             now = datetime.now() 
             transaction ={
                 "amount": 50,
                 "time": now,
                 "Narration":"you deposited"

             }
             self.statement.append(transaction)
        return self.Show_balance () 
    def withdraw(self,money):
         if money > self.balance:
             return f" your balance is {self.balance} you cannot withdraw {money}"
         else:
             self.balance -= money
              
             now = datetime.now() 
             withdraw ={
                 "amount": 50,
                 "time": now,
                 "Narration":"you deposited"

             }
             self.statement.append(withdraw)
             return self.Show_balance () 
             

    def borrow(self,amount):
        return f" Hey {self.name} you have successfully borrowed {amount}"

    def pay_loan(self,amount):
        return f"Hello, {self.name} you have deposited {amount}"

    def show_statement(self):

        for transaction in self.statement:
            amount = transaction["amount"]
            narration = transaction["Narration"]
            time = transaction["time"]
            date = time.strftime("%d/%m/%y")
            print(f"{date}: {narration} {amount}")
            return 
    

    
        
     # Attributes = name,id number, pin, phonenumber,email, address,account, balance
    # Methods = deposit,withdraw, borrow, show balance, transfer,uodate,freeze,close  
    
