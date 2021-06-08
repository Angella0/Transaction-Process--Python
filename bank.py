from datetime import datetime
class Account:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        self.balance = 0
        self.statement = []
        self.loan = 0
    def Show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}" 
    def deposit(self,amount):
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
             

    # def borrow(self,amount):
    #     return f" Hey {self.name} you have successfully borrowed {amount}"

    # def pay_loan(self,amount):
    #     return f"Hello, {self.name} you have deposited {amount}"

    def show_statement(self):

        for transaction in self.statement:
            amount = transaction["amount"]
            narration = transaction["Narration"]
            time = transaction["time"]
            date = time.strftime("%d/%m/%y")
            print(f"{date}: {narration} {amount}")
            return

    def borrow(self,amount):
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
        if amount < 0:
            return "You can not pay this loan"
        elif amount <= self.loan:
             self.loan -= amount
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
            return f"You have successfully paid your loan and your current balance is{self.deposit}"
        


    

    
        
