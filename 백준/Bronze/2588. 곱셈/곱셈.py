A = int(input())
B = int(input())

B001 = B % 10
B010 = ((B-B001) % 100) // 10
B100 = B // 100

print(A*B001, A*B010, A*B100, A*B, sep="\n")