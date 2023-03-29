
def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n2 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    
operations = {"+":add,"-":subtract,"*":multiply,"/":divide}


def calculator():
    num1 = float(input("Enter a number? "))
    loop = True
    while loop:
        for operation in operations:
            print(operation)  
        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("Enter a number? "))
        first_calc = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {first_calc}")
        condition = input(f"Type 'y' to continue with {first_calc}, type 'n' to start fresh or type 'exit' to exit.: ")
        if condition == 'y':
            num1 = first_calc
        elif condition == 'n':
            loop = False
            calculator()
        else:
            exit()
            
calculator()







#calculation = operations.get(operation_symbol)(num1,num2))
#print(calculation)