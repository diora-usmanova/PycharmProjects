x,y,z = eval(input("Enter three integar numbers: "))
if x<= y & y<= z:
     print(x,y,z)
elif x >= y & y >= z :
    print(z,y,x)
elif z <= x & x <=y:
    print(z,x,y)
else:
    print(y,x,z)