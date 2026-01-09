
def add(num_01,num_02):
    num_add=num_01+num_02
    print(f"your number after sum is {num_add}")
def sub(num_01,num_02):
    num_sub=num_01-num_02
    print(f"your number after sub is {num_sub}")
def multiply(num_01,num_02):
    num_multiply=num_01*num_02
    print(f"your number after mutiply is {num_multiply}")
def divide(num_01,num_02):
    num_divide=num_01/num_02
    if num_02==0:
        print("num is not divisiable")
    else:
        print(f"your number after divide is {num_divide}")

if __name__=="__main__":
    while True:
        try:
            num_01=int(input("enter you num1:"))
            num_02=int(input("enter you num2:"))
            oper=input("enter the opertion you want to perform(+,*,-,/,exit):")
            
            if oper =="exit":
                break


            if oper == "+":
                print(add(num_01, num_02))
            elif oper == "-":
                print(sub(num_01, num_02))
            elif oper == "*":
                print(multiply(num_01, num_02))
            elif oper == "/":
                print(divide(num_01, num_02))
            else:
                print("Invalid operation")

        except ValueError:
         print("Please enter valid numbers")

