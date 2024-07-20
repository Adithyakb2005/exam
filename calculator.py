
from cal import *

def main():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        ch=input("enter your choice:")
        if ch== '5':
             print("exiting the program")
             break
        num1=int(input("enter a number:"))
        num2=int(input("enter a number:"))
        if ch == '1':
            print( add(num1, num2))
        elif ch== '2':
            print( subtract(num1, num2))
        elif ch== '3':
            print( multiply(num1, num2))
        elif ch== '4':
            print(divide(num1, num2))
main()
