size = int(input("Enter the size of the pattern: "))
i = 0

while size > i:
    j = 0
    for j in range(size):
        print("*", end="")
        j += 1

    print()    
    i += 1 

