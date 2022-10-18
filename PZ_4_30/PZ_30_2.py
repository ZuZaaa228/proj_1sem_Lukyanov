N = input()

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Введите число еще раз!: ")

if N % 10 == 2:
    print(True)
else:
    print(False)