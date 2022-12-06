# Exercise from Elements of Programming Interviews in Python

x = 0b10001000
result = 0
while x:
    result ^= 1
    x &= x - 1

print(result)
