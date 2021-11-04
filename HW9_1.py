def Fibonacci(n):
    if n < 0:
        return -1
    elif n <= 1:
        return n

    return Fibonacci(n-1) + Fibonacci(n-2)

if __name__ == "__main__":
    print("input Fibonacci number: ")
    start_num = int(input())
    print("Fibonacci({}) is {}".format(start_num, Fibonacci(start_num)))
