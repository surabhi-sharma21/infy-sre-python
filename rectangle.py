def area(length, breadth):
    return length * breadth

def perimeter(length, breadth):
    return 2 * (length + breadth)

l = float(input('Enter length: '))
b = float(input('Enter breadth: '))

a = area(l, b)
p = perimeter(l, b)

print(p)
print(a)

