user_input = input("Expression: ").strip()
x = float(user_input.partition(" ")[0])
operation = user_input.partition(" ")[2].partition(" ")[0]
y = float(user_input.partition(" ")[2].partition(" ")[2])

def math(sign):
    match sign:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y

output = "{:.1f}".format(math(operation))

print (output)