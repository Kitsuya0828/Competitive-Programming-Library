def prime_factorize(n):
    """Nの素因数分解の2次元リストを返す
    計算量　O(√N)
    """
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i,cnt])
    if temp != 1:
        arr.append([temp,1])
    if arr == []:
        arr.append([n,1])
    return arr

# 1を渡すと[[1,1]]
# 素数pを渡すと[[p,1]]
# 24を渡すと[[2,3], [3,1]]

def get_divisor_num(n):
    if n == 1:
        return 1
    arr = prime_factorize(n)
    num = 1
    for base, exponent in arr:
        num *= (exponent + 1)
    return num

# --------------------------------------------------

from math import sqrt
def sieve_of_eratosthenes(n):
    """エラトステネスの篩
    N以下の全ての素数を見つける
    計算量　O(NloglogN)"""
    p = [1]*(n+1)
    p[0] = p[1] = 0
    for x in range(2,int(sqrt(n))+1):
        if p[x]:
            for y in range(x*x, n+1,x):
                p[y] = 0
    return p

# インデックスが素数の時１、素数でない時０の１次元リストを返す
# [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

# --------------------------------------------------