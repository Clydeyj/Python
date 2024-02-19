

def gcd(num1, num2):
     if num2 == 0:
          return num1
     else:
          return gcd(num2, num1%num2)
     
num1= 3
num2 =5

print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))