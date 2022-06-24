# GCD
numbers = []
num = input("Enter 5 numbers : ")
items = num.split()
numbers = [eval(x) for x in items]
print(numbers)


def gcd(numbers):
    gcd = 1
    k = 2
    while k <= numbers[0] and k <= numbers[-1]:
        if numbers[0] % k == 0 and numbers[-1] % k == 0:
            gcd = k
        k += 1
    return gcd


print(gcd(numbers))
