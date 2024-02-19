def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
num1 = 16
num2 = 28
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))