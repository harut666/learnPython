def check_even(num):
    if not isinstance(num, int):
        print("input not number")
        return None

    evenNum = num % 2

    if evenNum == 0:
        print(f"'{num} is even")
    else:
        print(f"'{num} is odd")
check_even(27)