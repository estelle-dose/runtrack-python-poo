def Calcule(num1, operator, num2):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    elif operator == "%":
        return num1%num2
    else :
        print("error")

print(Calcule(19, "+", 96))
print(Calcule(19, "*", 96))
print(Calcule(19, "-", 96))
print(Calcule(19, "%", 96))
print(Calcule(19, "/", 96))
