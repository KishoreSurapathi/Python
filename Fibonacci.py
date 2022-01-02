import time

memo = {}
def fibnacci(n):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    temp = fibnacci(n-1) + fibnacci(n-2)
    memo[n] = temp
    return temp

start = time.time()

for i in range(1,100):
    print(fibnacci(i))

end = time.time()

print("The time of execution:", end-start)
