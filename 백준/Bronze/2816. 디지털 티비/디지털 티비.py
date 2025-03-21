n = int(input())
ch = list(input() for _ in range(n))
res = ""

k1 = ch.index("KBS1")
k2 = ch.index("KBS2")

# 1 찾아서 아래로 내리기 (버튼1)
res += k1 * "1"

# 1 찾아서 위로 옮기기 (버튼4)
res += k1 * "4"

# k2가 밀렸을 경우
if k1 > k2:
    k2 += 1

# 2 찾아서 아래로 내리기 (버튼1)
res += k2 * "1"

# 2 찾아서 위로 옮기기 (버튼4) (2번째로 옮기므로 1 빼주기)
res += (k2-1) * "4"

print(res)