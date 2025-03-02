a = input()
op = input()
b = input()

if op == '*':
    result = a + b[1:]

elif op == '+':
    if len(b) == len(a):
        result = "2"+a[1:]
    else:
        if len(b) > len(a): a, b = b, a
        result = a[:len(a)-len(b)] + b

print(result)