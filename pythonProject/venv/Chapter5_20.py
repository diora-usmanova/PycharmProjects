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