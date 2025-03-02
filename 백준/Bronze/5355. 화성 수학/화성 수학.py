t = int(input())

for _ in range(t):
    eq = input().split()

    number = float(eq.pop(0))

    for op in eq:
        if op == '@':
            number *= 3
        elif op == '%':
            number += 5
        elif op == '#':
            number -= 7

    # print(f"{number: .2f}")
    print("{:.2f}".format(number))