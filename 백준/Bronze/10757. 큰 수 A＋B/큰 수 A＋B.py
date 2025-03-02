a, b = input().split()

# 길이 맞추기
if len(a) < len(b): a, b = b, a
b = (len(a)-len(b)) * "0" + b

# 올림 고려해서 길이 1개 더 길게 설정
result = [0 for _ in range(len(a)+1)]

# 덧셈
for i in range(1, len(a)+1):
    sum = int(a[-i]) + int(b[-i]) + result[-i]

    # 올림 발생시
    if sum >= 10:
        result[-i-1] = 1
        sum -= 10

    result[-i] = sum

# 최종 올림 없을시 앞의 0은 삭제
if result[0] == 0:
    del result[0]

# 문자열로 조인해서 출력
print("".join(map(str, result)))
