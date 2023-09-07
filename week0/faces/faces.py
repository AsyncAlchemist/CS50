def main():
    user_input = input()
    emoji_input = convert(user_input)
    print (emoji_input)


def convert(user_input:str):
    user_input = user_input.replace(":)", "🙂")
    user_input = user_input.replace(":(", "🙁")
    return user_input

main()