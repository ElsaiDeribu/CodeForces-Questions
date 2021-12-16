E = input()
i = E.index(" ")
x = int(E[0:i])
y = int(E[i+1:])


def elsai(m, n):
    boxes = int((m * n) / 2)
    if n == 1:
        boxes = 0
    return boxes


print(elsai(x, y))
