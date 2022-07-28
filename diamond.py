ch = '*'
space = ' '
max = 50
i = 0
# while i < max:
#     j = i + 1
#     print(space * ((max - j) // 2) + ch * j)
#     i += 2
# while i < max * 2:
#     j = i + 1
#     print(space * ((j - max) // 2) + ch * (max*2 - j))
#     i += 2
while i < max * 2:
    j = i + 1
    s = abs(j-max) // 2
    print(space * s + ch * (max - (2 * s)))
    i += 2