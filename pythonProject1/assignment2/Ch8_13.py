
# LONGEST COMMON PREFIX
def prefix(s1, s2):
    s3 = ""
    for a in range(len(s1)):
        if s1[a] == s2[a]:
            s3 = s3 + s1[a]
        else:
            return s3
    return s3


def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter a second string")
    print(prefix(s1, s2))


if __name__ == "__main__":
    main()
