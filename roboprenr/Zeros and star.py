n = int(input("N0 of rows:" ))
i = 1
star = 1
while i<=n:
    j = 1
    while j <= 2*n + 1:
        if star == i and star == j:
            print('*', end = "")
            star = star + 1
         
        elif j == n + 1 or j == 2*n+2 - i:
            print('*', end = "")
        else:
            print(0, end = "")
        j = j + 1
    print()
    i = i + 1
