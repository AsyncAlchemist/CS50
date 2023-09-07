def main():
    user_input = input("camelCase: ").strip()
    i:int = 0
    output = []
    offset:int = 0

    # loop through the entire string and print each character
    while i < (len(user_input)):
        letter:str = user_input[i]
        if letter.isupper() == True:
            output.append("_")
            output.append(letter.lower())
        else:
            output.append(letter)
        i += 1

    output = "".join(output)
    print ("snake_case:", output)

main()