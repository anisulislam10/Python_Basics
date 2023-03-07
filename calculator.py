num1 = float(input("Enter Value 1: "))
print(num1)
num2 = float(input("Enter Value 2"))
optr = input("Enter operator (+, -, *, /)")
if optr == '+':
    print(num1+num2)
elif optr == '*':
    print(num1*num2)
elif optr == '-':
    print(num1-num2)
elif optr == '/':
    print(num1/num2)

else:
    print("Invalid Selection!...")
