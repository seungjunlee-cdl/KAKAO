def convert(n,k):
    base = ''

    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)

    return base[::-1]

def is_prime_number(x):
    if x==1:
        return False

    for i in range(2, int(x*0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    nk_str = convert(n,k)
    cnt = 0

    for i in nk_str.split('0'):
        if i.isdigit():
            if is_prime_number(int(i)):
                cnt += 1
    return cnt
