t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    # 문자열 포맷팅. ex) f"제 이름은 {name}이고, 나이는 {age}살입니다."
    print(f"Case #{i+1}: {a+b}")