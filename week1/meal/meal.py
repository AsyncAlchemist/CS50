def main():
    user_input = input("What time is it? ")
    time = convert(user_input)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time:str):
    hour = float(time.partition(":")[0])
    minutes = float(time.partition(":")[2])
    return (hour + (minutes / 60))


if __name__ == "__main__":
    main()