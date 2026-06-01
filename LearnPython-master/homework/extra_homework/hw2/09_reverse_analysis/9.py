results = [12, 5, 8, 13, 22, 9, 30]

for i in range(len(results) - 1, -1, -1):
    if results[i] % 2 == 0:
        print(results[i])