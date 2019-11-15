# variable number of arguments (parameters) 0 to n
def myadd(*args):
    # print(args) # tuple object
    sum = 0
    for arg in args:
        sum += arg
    return sum

# positional arguments packing
print(myadd()) # 0
print(myadd(5)) # 5
print(myadd(4, 5, 5)) # 14
print(myadd(5, 6, 7, 2, 4, 7, 8, 9))


def area(length, breadth):
    return length * breadth

stats = (6, 4) # cud even be a list
# print(area(stats[0], stats[1]))

# the order of the positiona arguments matches with the order in the tuple
print(area(*stats)) # positional argument unpacking

def perimeter(**kwargs):
    # print(kwargs) # dict object
    return 2 * (kwargs['length'] + kwargs['breadth'])

# print(perimeter(5.2, 4.9)) # will not work
# keyword arguments packing
print(perimeter(length=5.2, breadth=4.9))
# print(perimeter(len=5.2, bre=4.9)) # will not work


# keyword argument unpacking
smap = {'breadth': 4, 'length': 5}
# print(area(smap['length'], smap['breadth']))
print(area(**smap))