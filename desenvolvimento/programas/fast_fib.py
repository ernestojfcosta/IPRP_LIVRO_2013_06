def fibonacci(n, res={}):
    if n == 1 or n == 2:
        return 1
    else:
        if n in res:
            return res[n]
        else:
            fib_n = fibonacci(n-1, res) + fibonacci(n-2, res)
            res[n] = fib_n
            return fib_n
        
if __name__ == '__main__':
    
    for i in range(1,10):
        print(fibonacci(i))