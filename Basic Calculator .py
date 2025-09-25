# class calc:
print("\tBasic Calculator")

'''class Calc:
def get_valid_a(a):
    while True:
         a = float(int(input(str("Enter First Number:"))))        
    if all(part.isalpha() for part in a.split()):
            return a
    else:
            print(" Error: Please enter alphabetical characters only.")
            input("Press any key to try again...")
def get_valid_a(b):
    while True:
        b = float(int(input(str("Enter second number: "))))              
    if all(part.isalpha() for part in b.split()):
            return b
    else:
            print(" Error: Please enter alphabetical characters only.")
            input("Press any key to try again...")'''  


# float is used for inputing decimal value
a = float(int(input(str("Enter First Number:"))))
b = float(int(input(str("Enter second number: "))))

#this all are operation used 
def calculator(a,b):
    symbol = input("Enter operation (+, -, *, /,//,%): ")

    if symbol == "+":
        print(f"The Sum of {a} and {b} is "+str(a + b))
    elif symbol == "-":
        print(f"The Substraction of {a}  and {b} is "+str(a - b))
    elif symbol == "*":
        print(f"The Multiplication of {a} and {b} is "+str(a * b))
    elif symbol == "/":
        print(f"The Division of {a} and {b} is "+str(a / b))
    elif symbol == "//":
        print(f"The float of {a}  and {b} is "+str(a // b))
    elif symbol == "%":
        print(f"The Mode of {a}  and {b} is "+str(a % b))
    else:
        print("Invalid Approch, Plese Try Again")
        calculator(a,b)
#elif,if,else are used for

    # Thank You 
    #Be The Change 

# ob=Calc(a,b)
# ob.calc(a,b)
calculator(a,b)
#  ob=calc()

