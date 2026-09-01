from functions.addition import sum
from functions.substraction import sub
from functions.multiplication import mul
from functions.division import div

def main():   # Function Definition

    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))

    choice = input("Enter the choice ")

    if choice == 'sum':
        # Addition
        ans = sum(num1,num2) # Arguments
    elif choice =='sub':
        # Subtraction
        ans = sub(num1,num2) # function calling : sum
    elif choice == 'mul':
        # Multiplication
        ans = mul(num1,num2)
    elif choice == 'div':
        # Division
        ans= div(num1,num2)
    else:
        print("Invalid Choice")
    print(ans)


main()        # Function calling : Orcehstrator