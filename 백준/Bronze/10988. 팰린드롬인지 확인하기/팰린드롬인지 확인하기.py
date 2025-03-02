word = input()

isP = 1

for i in range(len(word)//2):
    if word[i] != word[-1*(i+1)]:
        isP = 0
        break

print(isP)