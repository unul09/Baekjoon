n = int(input())

yes = 0
no = 0

for _ in range(n):
    vote = int(input())
    if vote == 1:
        yes += 1
    else:
        no += 1

if yes > no:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")