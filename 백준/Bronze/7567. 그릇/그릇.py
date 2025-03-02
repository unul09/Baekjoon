plates = input()
height = 10

for i in range(1, len(plates)):
    if plates[i] != plates[i-1]:
        height += 10
    else:
        height += 5

print(height)