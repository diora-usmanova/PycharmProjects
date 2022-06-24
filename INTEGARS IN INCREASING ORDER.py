
x,y,z = eval(input("Enter three integar numbers with comma separated : "))
if x<= y & y<= z:
     print(x,y,z)
elif x >= y & y >= z:
    print(z,y,x)
elif z <= x & x <=y:
    print(z,x,y)
elif x>= z & z >= y:
    print(y,z,x)
else:
    print(y,x,z)

