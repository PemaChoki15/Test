for i in range(1, 10):
    if i == 3:
        print("skipping 3 in the inner loop")
        break
    if i <= 3:
        print(i)

for i in range(1, 10):
    if i == 7:
        print("reached 7, breaking outer loop")
        break
    if i >= 4:
        print(i)

