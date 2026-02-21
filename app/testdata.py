names = ["Bob", "Alice"]
marks = ["90", "80"]


res = [f"{n}: {m}" for n, m 
                in zip(names, marks)]
print(res)


x = 5
y = 0
while x > 0:
    y = y * 10 + x
    x = x - 1
print(" " + str(y))

speed = lambda x: x * 2
print(speed(5))