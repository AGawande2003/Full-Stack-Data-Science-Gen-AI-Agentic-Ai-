
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i)

print("Even numbers:")
for i in range(2, 21, 2):
    print(i)

print("Table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

total = 0
i = 1

while i <= 10:
    total += i
    i += 1

print("Sum of 1 to 10:", total)
