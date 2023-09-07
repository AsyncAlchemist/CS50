def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if starts_with_two_letters(s) and length_requirement(s) and only_alphanumeric(s) and first_not_zero(s) and numbers_at_end(s):
        return True
    else:
        return False

# “All vanity plates must start with at least two letters.”
def starts_with_two_letters(s:str):
    if len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
            return True
    return False

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def length_requirement(s):
    if len(s) > 1 and len(s) < 7:
        return True
    else:
        return False

# “Numbers cannot be used in the middle of a plate; they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
def numbers_at_end(s:str):
    i = 0
    n = len(s)
    start = 1000000
    has_digit = False
    while i < n:                            # search for starting number
        if s[i].isdigit() and i < start:
            start = i
        if s[i].isdigit():
            has_digit = True
        i = i + 1 
    if has_digit and s[start] == "0":       # Make sure starting number is not 0
        return False
    i = 0
    while i < n:                            # search for letters after starting number
        if s[i].isalpha() and i > start:
            return False                    # return false if a letter is found after starting number
        i = i + 1
    return True                             # return true if the loop finished without returning false

# The first number used cannot be a ‘0’.”
def first_not_zero(s:str):
    if s[0] == 0:
        return False
    else:
        return True

# “No periods, spaces, or punctuation marks are allowed.”
def only_alphanumeric(s:str):
    return s.isalnum()

main()
