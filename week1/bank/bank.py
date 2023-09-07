def main():
    user_input = input("Greeting: ")
    cleaned_input = user_input.lower().strip()
    print(response(cleaned_input))

def response(cleaned_input):
    if "hello" in cleaned_input:
        return "$0"
    elif cleaned_input.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
