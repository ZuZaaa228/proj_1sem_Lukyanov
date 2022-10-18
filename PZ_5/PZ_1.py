def f(lst: list) -> int:
    return sum(lst)


lst = input().split()

for index in range(len(lst)):
    lst[index] = int(lst[index])

print(f(lst))
