
#COUNT CONSTATANT AND VOWELS
import os.path
import sys

filename = input("Enter a file name: ").strip()
infile = open(filename, 'r')
letters = infile.read().split()
print(letters)
vowels = set("AEIOU")
print("Vowels are", vowels)
Vowels = 0
constants = 0
for i in letters:
    if i in vowels:
        Vowels += 1
    else:
        constants += 1

print("Number of constants", constants)
print("Number of vowels", Vowels)
