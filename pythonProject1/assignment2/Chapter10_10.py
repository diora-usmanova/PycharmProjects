# REVERSE A LIST
List = eval(input("Enter a list : "))
print(List)


def Reverse( List):
    return [x for x in reversed(List)]


print("Updated list", Reverse(List))
