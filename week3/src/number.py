def main():
    var = "f"
    x = get_int("f")
    print (f"{var} is {x}")

def get_int(x):
    while True:
        try:
            x = int(input (f"What's {x}? "))
        except ValueError:
            pass
            print("Invalid input. Use a valid integer.")
        else:
            return x
    
main()