# COUNTING A CHARACTER IN A STRING

str = input("Enter a string : ")
ch = input("Enter a character: ")


def count(str, ch):
    num = 0
    for i in range(0, len(str)):
        if str[i] == ch:
            num += 1
    return num


print(count(str, ch))
