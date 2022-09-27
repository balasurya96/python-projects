from balasuriyatest5 import *
print("-----------WELCOME--TO--THE--LOGITISICES-------------")
print("Today List of Salary")
print("---------------------")
def start():
    l = list(Db)
    print(l)

def content():
    name = input("Enter Name: ")
    d = input("Enter a Role: ")
    print(d)
    a = int(input("Enter the total order:"))
    print(a)
    Total = (a * (Db[d]["Order"]) + Db[d]["pertol"] + Db[d]["allowance"])
    print(f" Total of  :{Total}")

    if a >= 0 and a <= 5:
        extrabounce = 25
        Amount = Total + extrabounce
        print(f"One Day salary of {name.title()} :{Amount} *includes Taxes")
    elif a >= 6 and a <= 10:
        extrabounce = 50
        Amount = Total + extrabounce
        print(f"One Day salary of {name.title()} :{Amount} *includes Taxes")
    elif a >= 11 and a <= 15:
        extrabounce = 100
        Amount = Total + extrabounce
        print(f"One Day salary of {name.title()} :{Amount} *includes Taxes")
    else:
        extrabounce = 150
        Amount = Total + extrabounce
        print(f"One Day salary of {name.title()} :{Amount} *includes Taxes")

def choose():
    while True:
        choice=int(input("Enter a Choose:"))
        if choice==1:
            start()
        elif choice==2:
            content()
        else:
            print("--------Exit------------")
            quit()
choose()
