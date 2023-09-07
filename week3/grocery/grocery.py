list = {}

print ("New version")

while True:
    try:
        user_input = input("Item: ").upper()
        x = list.setdefault(user_input, 1)
        print (list, x, user_input)
    except KeyError:
        pass
    except EOFError:
        break