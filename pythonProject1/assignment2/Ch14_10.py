# GUESS THE CAPITALS
import random
correct_count = 0
states = {"Alabama ": "Montgomery", "Alaska": "Juneau", "Arizona": " Phoenix", "Arkansas": "Little Rock",
          "California": " Sacramento", "Colorado": "Denver", " Connecticut": "Hartford", "Delaware": "Dover",
          "Florida": "Tallahassee", " Georgia": "Atlanta", "hawaii": "Honolulu", "Idaho": "Boise",
          "Illinois": "Springfield",
          "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": " Frankfort",
          "Louisiana": "Baton Rouge",
          "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston", "Michigan": "lansing",
          "Minnesota": "Saint Paul",
          "Mississippi": "Jackson", "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln",
          "Nevada": "Carson City",
          "New Hampshire": " Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany",
          "North Carolina": "Raleigh",
          "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem",
          "Pennsylvania": "Harrisburg",
          "Rhode island": " Providence", "South Carolina": "Columbia", "South Dakota": "Pierre",
          "Tennessee": "Nashville",
          "Texas": "Austin", "Utah": "salt lake City", "Vermont": "Montpelier", "Virginia": "Richmond",
          "Washington": "Olympia",
          "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"}
for state in states:
    i = random.randint(0, 49)
    capitals = input("What is the capital of " + tuple(states.keys())[i] + "?").strip()
    if capitals.lower == states[state].lower:
        print("Correct Answer")
        correct_count += 1
    else:
        print("Wrong Answer")
        print("Correct Answer is " + states[state])
print("CorrectCount is " + correct_count)


# DISPLAY NONDUPLICATE WORDS IN ASCENDING ORDER
f = open('14.8_textFile', 'r')
words = f.read()
print(words)
s = set()
items = words.split()
s = set(str(x) for x in items)
print(sorted(s))
f.close()

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

print("Number of constants", constants)…..print("Number of vowels", Vowels)

  


