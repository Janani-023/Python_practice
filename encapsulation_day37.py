class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount#balance=balance+amount
        self.balance=900
        
    def show_balance(self):
        print("balance is:",self.balance)
b=BankAccount(5000)
b.show_balance()
b.deposit(2000)
b.show_balance()
print(b.balance)


class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance+=amount#balance=balance+amount
        self.__balance=900
        
    def show_balance(self):
        print("balance is:",self.__balance)
c=BankAccount(5000)
c.show_balance()
c.deposit(2000)
c.show_balance()
print(c.__balance)
