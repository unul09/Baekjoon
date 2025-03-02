while(True):
    n = int(input())
    if n == -1: break

    div_sum = 1
    div_list = [1]

    for i in range(2, round(n/2)+1):
        if n%i == 0:
            div_sum += i
            div_list.append(i)

        if div_sum > n:
            break

    if div_sum == n:
        print(n, "=", end=" ")
        for num in div_list:
            if(num != div_list[-1]):
                print(num, "+", end=" ")
            else:
                print(num)
    else:
        print(n, "is NOT perfect.")