# SUM DIGITS OF AN INTEGAR
def sumDigits(n):
    sum  = 0
    while n != 0:
        sum = sum + n % 10
        n = n // 10
    return sum

def main():

    n= eval(input("Enter an integar"))
    print(sumDigits(n))
main()

# INTEGAR REVERSED
'''def reverse(number):
    reverse_number = 0
    while(number>0):
        remainder = number % 10
        reverse_number= (reverse_number*10)+ remainder
        number = number // 10
    print(reverse_number)
reverse(1234)'''
