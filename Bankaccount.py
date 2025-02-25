class BankAccount:

    def __init__(self,owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self,amount):
        if amount >0:
            self.__balance +=amount
            print(f"deposit successfully now , your balance is {self.__balance}")

        else:
            print("your amount is  not valid")

    def width_drow(self,amount):

        if amount > 0 and amount < self.__balance:
            self.__balance -=amount
            print(f"widthed successfully , now your balance is {self.__balance}")
        elif self.__balance < amount:
            print("incuficent balance ")
        else:
            print("Enter valid amount")

    def print_balance(self):
        print(f"now your balance is {self.__balance}")

if __name__ =="__main__":

    account = BankAccount("afzal",600000)
    account.deposit(4000)
    account.width_drow(1000)
    account.print_balance()


