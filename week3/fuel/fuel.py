def main():
    z = get_fraction()
    if z >= .99:
        print ("F")
    elif z <= .01:
        print ("E")
    else:
        print(f"{z * 100:.0f}%")
    
def get_fraction():
    while True:
        try:
            user_input = input("Fraction: ")
            x = int(user_input.partition("/")[0])
            y = int(user_input.partition("/")[2])
            z = x / y            
            if x > y:
                raise ArithmeticError()
            else:
                return z
        except:
            pass

main()