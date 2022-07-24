time = input("What time is it? ")


def four_digits(time):
    if time[0] == "7":
        print("breakfast time")


def five_digits(time):
    if time[0] + time[1] == "12":
        print("lunch time")
    elif time [0] + time[1] == "13":
        print("lunch time")
    elif time[0] + time[1] == "18":
        print("dinner time")


if len(time) == 4:
    four_digits(time)
else:
    five_digits(time)
