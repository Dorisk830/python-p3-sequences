def print_fibonacci(length):
    if length < 0:
        return []

    fib_series = []

    if length == 0:
        print("[]")
        return fib_series

    if length == 1:
        fib_series = [0]
    elif length == 2:
        fib_series = [0, 1]
    else:
        fib_series = [0, 1]
        for _ in range(2, length):
            next_number = fib_series[-1] + fib_series[-2]
            fib_series.append(next_number)

    print(fib_series)
    return fib_series


print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)   
print_fibonacci(10)  
