n = int(input('Enter n: '))

''' i = 0
while i <= n:
    if not i % 2:
        print(i)
    i = i + 1 '''

# sequence of elements
# [0, n]
''' for v in range(0, n+1):
    if not v % 2:
        print(v)'''

for v in range(0, n + 1, 2):
    print(v)