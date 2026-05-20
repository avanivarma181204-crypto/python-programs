for j in range(1, 101):
    if j % 3 == 0 and j % 5 == 0:
        print("fizzbus")
    elif j % 3 == 0:
        print("fizz")
    elif j % 5 == 0:
        print("bus")
    else:
        print(j)