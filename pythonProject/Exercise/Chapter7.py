
s= "Hello Python "
print(s[0])
print(s[1])
print(s[len(s) - 1])

print(s[2:7])
print(s[2:3])
print(s[8:2:-2])
print(s[0:7])
print(s[2:]) # goes from third element to the end
print(s[-2:-6:-1])# goes to right to left
print(s[: : -1]) # REVERSE THE S
print(int(str(6789)[::-1])) # REVERSE THE NUMBER
# CONCATINATING STRING
s1 = "welcome"
s2 = "python"
s3 = s1+ " to "+s2
print(s3)

s1 = " Hello Python  and java"
"come " in s1

for i in range (0,len(s)):
    print(s[i])

for ch in s1:
    print(ch)
# GOES IN ALPHABATICAL ORDER, first letters are bigger
s1 = "green"
s2 = "glow"
#print(s1==s2)

#LOWER CASES ARE ALWAYS BIGGER THAN UPPER CASES
#print("abcde" > "abcdE" )

# METHODS
print(s.isalnum())
print(s.isalpha())
print(s.lower())
print(s.isdigit())
print(s.isspace())
print(s.isidentifier())
print(s.startswith("Hello"))
print(s.endswith("Python"))
print(s.find('o'))
print(s.find("Py"))
print(s.rfind('o'))
print(s.rfind('o',8))
print(s.rfind('o',4))
s4 = "Hello Python "
print(s4.count("o"))
print(s4.capitalize())
print(s.lstrip())
s5 = "Hello"
print(s5.ljust(20))
print(s5.rjust(20))
print(s5.ljust(20))

s6 = "aaabbbaaa"
def isPalindrom(s):
    for i in range (0, len(s6) // 2):
        if s6[i] != s[len(s6) - i -1]:
            return False
    return True
print(s6)


def isPalindrom(s6):
    return s[:: -1] == s6











