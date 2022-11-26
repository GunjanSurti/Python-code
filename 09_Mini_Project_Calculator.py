first = input("Enter your First no.") # it is string not integer
operator = input("Enter Operator (+,-,*,/,%)")
second = input("Enter Second no.")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

elif operator == "%":
    print(first % second)


else:
    print("Invalid Operator")