height = 5

for i in range(6):
    j = 0
    for j in range(6):
        if j == 0 and i  <5:
            print('*',end = " ")
        if j >= 0 and i == 5:
            print('*',end = " ")
    print("\n")