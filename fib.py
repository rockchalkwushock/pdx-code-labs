def memoize(fn):
    cache = {}

    def helper(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    return helper


# @memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(40))
