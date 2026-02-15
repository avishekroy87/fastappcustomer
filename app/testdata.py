names = ["Bob", "Alice"]
marks = ["90", "80"]


res = [f"{n}: {m}" for n, m 
                in zip(names, marks)]
print(res)