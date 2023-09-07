def main():
    print_square(10,30)

def print_column(height:int):
    for _ in range (height):
        print("#")

def print_row(width:int):
    print ("?" * width)

def print_square(height:int, width:int):
    for _ in range (height):
        print ("🟥" * width)

main()