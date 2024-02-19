def ifactorial(n):
    def helper(x, result):
        if x == 1:
            return result
        else:
            return helper(x - 1, result * x)
    return helper(n, 1)

# Example usage:
print("Factorial of 4 is:", ifactorial(4))
