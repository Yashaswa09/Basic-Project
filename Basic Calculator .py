
print("Basic Calculator")

# float is used for inputing decimal value 
a = float(int(input(str("Enter First Number:"))))
b = float(int(input(str("Enter second number: "))))      


#this all are operation used 
def calculator(a,b):
    symbol = input("Enter operation (+, -, *, /,//,%,**): ")

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
    elif symbol == "**":
        print(f"The Exponational  of {a}  and {b} is "+str(a**b))
    else:
        print("Invalid Approch, Plese Try Again")
        calculator(a,b)
 

    
calculator(a,b)
#elif,if,else are used for

    # Thank You 
    #Be The Change
