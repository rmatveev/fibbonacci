import worker

numbers = [10, 100, 56]

for number in numbers:
    print(f"Fibonacci for {number} is ", worker.Fibonacci(number))