# LIST
# IT IT MUTABLE
'''l1 = [1,4,2,7]
l2 = list([1,"hello", 2, "true"])
l3 = list("cde")
print(type(l1))
print(l1[0])
print(l1[1])
print(l1[len(l1)-1])
print(l2[1])
# adding special charakter or space("") between every element, l3 should be STRING, ONLY WORKS FOR STRING

s7 = "***".join(l3)
print(s7)

s8  = "".join([str(x) for x in l2])
print(s8)'''

#PRACTICE CHAPTER 8
'''s1 = "Welcome to Python"
s2 = s1
s3 = "Welcome to Python"
s4 = "to"

print(s1==s2)
print(s2.count('o'))
print(id(s1) == id(s2))
print(id(s1) == id(s3))
print(s1<= s4)
print(s2>= s4)
print(s1 != s4)
print(s1.find(s4))
print(s1[4])
print(s1[4:8])
print(4*s4)
print(len(s1))
print(max(s1))
print(min(s1))
print(s1[-4])
print(s1.lower())
print(s1.rfind('o'))
print(s1.startswith("o"))
print(s1.endswith("o"))
print(s1.isalpha())
print(s1.isdigit())
print(s1+s1)'''

# CHAPTER 10
# ARRAY
'''l1 = ["red", "green", "blue","black", "yellow"]
l2 = [1,2,3,4,2]'''
'''print(l1)
s1 = " ".join(l1)
print(l1)
l1.append(1000)
print(l1)
l1.extend([1000,2000])
print(l1)
l1.insert(2,3000)
print(l1)
l1.remove(2)
print(l1)
l2.remove(2,3)
print(l2)
print(l1[1])'''
'''print(l1.count("green"))
print(l1.sort())
print(l1.reverse())
l1.reverse()
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
#print(l1.pop(2))
print(id(l1))
print(l1.append("pink"))'''

'''print(l1[-1])
for item in l1:
    print(item)'''

'''i = 0
while i< len(l1):
    print(l1[i])
    i += 1


a= 10
b = 20
c = a+b
#d = sum(c,10)
#print(d)'''

'''l1=[1,2,3,4,5,6,7,8,9,10]
#L2 = []
for item in l1:
    l2.append(item + 1)
print(l2)

l2 = [x for x in l1 if x % 2 ==0]
print(l2)

l2 = [2* x for x in l1 if x<5]
print(l2)

l2 = [x for x in range(0,5)]
print(l2)'''

#COMPARING LIST
'''l1 = ["red","blue", "black"]
l2 = [" green", "yellow", "pink"]
print(l1<=l2)
s1 = "Hello python and you are cool"
l1 = s1.split(" ")
print(l1)'''

# COPIYING LIST
'''l1 = [1,2,3,4]
l2 = list(l1)
l1[0] = 10000
print(l2)'''

# PASSING LIST TO FUNCTIONS
'''def printList(list1):
    for item in list1:
        print(item)
list2 = [1,2,3,4]
printList(list2)'''

'''def changeList(list1):
    list1[0] = 1000
list2 = [1,2,3,4]
print(changeList(list2))'''

'''def add(x,list=[]):
    if not x in list:
        list.append(x)
    return list
list1 = add(1)
print(list1)
list2 = add(2)
print(list2)
list3 = add(3,[11,12,13,14])
print(list3)
list4 = add(4)
print(list4)'''

# FUNCTION THAT GETS A LIST AND REVERSE IT
'''def reverse(l1):
    l2 = []
    for i in range (len(l1) -1, -1, -1):
        l2.append(l1[i])
    return l2

l1 = [1,2,3,4,5]
print(reverse(l1))'''

# chapter 11
#TWO DIMENSIONAL LIST
l1 = [[1,2],[2,3],[6,7]]
'''print(len(l1))
print(l1[0])
print(l1[1])'''

'''print(l1[2][1])
print(len(l1[0]))'''
'''import random
n = eval(input("How many rows:"))
m = eval(input("How many column"))
matrix = []
for i in range (0,n):
    matrix.append([]) #[ [1,2,3],[5,6,7] ]
    for j in range(0,m):
        #num = eval(input("Enter a number"))
        matrix[i].append(random.randint(0,100))
print(matrix)'''

# PRINTING THE LIST
matrix = [[1,2,3],[4,5,6]]
for i in range(0,len(matrix[1])):
    for j in range(0,len(matrix[i])):
      print(matrix[i][j], end = " ")

       print(matrix)





















