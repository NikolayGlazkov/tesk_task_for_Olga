def cercle_aray(n,m):
    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()


n = int(input("Введите n = "))
m = int(input("Введите m = "))
cercle_aray(n,m)