user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
cleaned_input = user_input.replace(" ","").replace("-","").lower()

if cleaned_input == "42" or cleaned_input == "fortytwo":
    print("Yes")
else:
    print("No")