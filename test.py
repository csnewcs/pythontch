a = 5
b = 8
i = 0
while i < 50:
    a += i
    i += 1
arr = [a, b, a+b, a*b]
sum = 0
for one in arr:
    sum += one
print(sum)