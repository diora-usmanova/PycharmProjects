# fIND THE NUMBERS DIVISIBLE BY 5 AND 6
numbers_per_line = 10
count = 0
'''for i in range(100, 1000):
    if i % 5 == 0 and i % 6 == 0:
        count += 1
        print(format(i, "5d"), end=" ")
        if count % numbers_per_line == 0:
            print()'''

# find the num divisible by 5 or 6, but not both
for num in range(100, 200):
    if num % 5 == 0 or num % 6 == 0 and not 
(num % 5 == 0 and num % 6 == 0):
        count += 1
        print(format(num, "5d"), end=' ')
        if count % numbers_per_line == 0:
            print()
