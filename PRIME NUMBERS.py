#PRIME NUMBERS

NUMBER_OF_PRIMES_PER_LINE = 8
count = 0
number = 2
print("    PRIME NUMBERS    ")
for i in range(2,1000):
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1
        print(format(number, "5d"), end = '')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print()

    number += 1


#PRINTING CHARACTERS

#def printChars(ch1,ch2,numberPerLine):
CHARACTERS_PER_LINE = 10
total = 1
char1 = chr(1)
char2 = chr(90)
print("Charachters from", char1, "to", char2)
for i in range(1,50):
    total += 1
    if total % CHARACTERS_PER_LINE ==0:
        print()
    print(char1, char2, end =' ')


#printChars('ch1', 'ch2', 'numberPerLine')





#PRINTING PATTERNS
print("PATTERN A")
for i in range(1,7):
    for j in range(1,7,+1):
        print(j if j <= i else " ", end = " ")
    print()

print("PATTERN B")
for i in range (1,7):
    for j in range (6,0,-1):
        print(j if j >= i else " ", end = " ")
    print()


print("PATTERN C")
for i in range(1, 7):
    for j in range(6, 0, -1):
      print(j if j <= i else " ", end = " ")
    print()

print("PATTERN D")
for i in range (1,7):
    for j in range (1,7,+1):
        print(j if j >= i else " ", end = " ")
    print()

