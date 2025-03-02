# 1931
import sys

input = sys.stdin.readline
n= int(input())
data =[]
for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key = lambda x : (x[1],x[0]))

end_t = data[0][1]
cnt = 1

for i in range(1,n):
    if data[i][0]>=end_t:
        cnt += 1
        end_t = data[i][1]

print(cnt)