for _ in range(3):
    status = list(map(int, input().split()))

    bae_count = status.count(0)

    if bae_count == 0:
        print("E")
    elif bae_count == 1:
        print("A")
    elif bae_count == 2:
        print("B")
    elif bae_count == 3:
        print("C")
    elif bae_count == 4:
        print("D")