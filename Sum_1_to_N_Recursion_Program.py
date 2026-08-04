# Sum of 1 to N using Recursion

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

n = int(input("Enter the value of N: "))
result = sum_n(n)

print("Sum of numbers from 1 to", n, "is", result)
