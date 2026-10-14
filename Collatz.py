def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    num = int(input("Enter a number: "))
    while num != 1:
        num = collatz(num)
        print(num)
except ValueError:
    print("Please enter a valid integer.")