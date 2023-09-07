name = input("What's your name? ")

match name:
    case "Harry" |"Hermone" | "Ron":
        house = "Gryffindor"
    case "Draco":
        house = "Slytherin"
    case _:
        house = "Who?"

print(house)