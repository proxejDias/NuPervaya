def evenOrOdd(a):
    if a % 2 == 0:
        return True
    else:
        return False


number = int(input("give me a number: "))

if evenOrOdd(number):
    print("your number is even")
else:
    print("your number is odd")