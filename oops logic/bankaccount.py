"""
Docstring for oops logic.bankaccount
backaccount has : bank acccount no , account holder name , balance
bankaccount does : deposit , withdrawal , show balance
"""
class bankaccount:
    def __init__(self,accountnumber,holdername,balance):
        self.accountnumber=accountnumber
        self.holdername=holdername
        self._balance=balance # --> protected

    def deposit(self,amount):
            if amount<=0:
                  return "Deposit amount must be greater than 0"
            
            self._balance+=amount
            return self._balance
                
    def withdraw(self,amount):
        if amount<=0:
             return "Withdrawal amount must be greater than 0"
        
        if amount > self._balance:
            return "Insufficient balance"
        
        self._balance -= amount
        return self._balance
                 
    def get_balance(self):
        return self._balance

if __name__=="__main__":
    accountnumber=int(input("enter your bank account number:"))
    holdername=str("enter your bank acount holder name:")   
    balance=int(input("enter your inital balance:"))
    acc=bankaccount(accountnumber,holdername,balance)
    while True:
          print("1.deposit")
          print("2.withdrawal")
          print("3.show balance")
          print("4.exit")
          choose=input("Enter your choice from 1-4:")
          if choose=="1":
               amount=int(input("enter your amount:"))
               print("balance:",acc.deposit(amount))
          elif choose=="2":
                amount=int(input("enter your amount:"))
                print("balance:",acc.deposit(amount))
          elif choose=="3":
                print("balance:",acc.get_balance())
          elif choose=="4":
                break
          else:
                print("invaild choose! try again")
                break    

          