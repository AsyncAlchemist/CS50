omitted_letters = ["a","e","i","o","u","A","E","I","O","U"]
text_output = []
i = 0

user_input = input("Input: ")
length = len(user_input)

while i < length:
    if user_input[i] in omitted_letters:
        i = i+1
    else:
        text_output.append(user_input[i])
        i = i+1
    

text_output = "".join(text_output)
print ("Output:", text_output)