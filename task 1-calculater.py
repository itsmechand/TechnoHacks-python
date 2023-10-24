def input_num():
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    return x,y
def add(x,y):
    print(f"Result: {x+y}")
def subtract(x,y):
    print(f"Result: {x-y}")
def mul(x,y):
    print(f"Result: {x*y}")
def division(x,y):
    if y!=0:
        print(f"Result: {x/y}")
    else:
        print("Denominator can't be Zero")

def welcome_msg():  
    print(f"""
        press 1--> ADD
        press 2--> SUBTRACT
        press 3--> MULTIPLY
        press 4--> DIVISION
        press 5--> exit""")
print("\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To ARITHMETIC OPERTIONAL CALCULATOR ☆*: .｡. o(≧▽≦)o .｡.:*☆ ")
while(True):
    welcome_msg()
    choice = int(input("Enter you choice: "))
    if choice == 1:
        x,y = input_num()
        add(x,y)
    elif choice==2:
        x,y = input_num()
        subtract(x,y)
    elif choice ==3:
        x,y = input_num()
        mul(x,y)
    elif choice ==4:
        x,y = input_num()
        division(x,y)
    elif choice ==5:
        exit()
    else :
        print("Enter Correct Choice") 