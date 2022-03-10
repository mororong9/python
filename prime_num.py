def prime_checker(number):
    div=0
    for num in range(2, number - 1):
        if number % num == 0:
            print(f"devided by {num}")
            div+=1
    if div==0:
        print(f"prime{number}")


n = int(input("Check this number: "))
prime_checker(number=n)