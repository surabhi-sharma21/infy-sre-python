pointers = [5, 10, 5, 6, 3, 8, 9, 1, 10, 5, 4]

# get a new list of odd pointers from pointers list (filtering)
''' odds = []
for pointer in pointers:
    if pointer % 2:
        odds.append(pointer) '''

# for comprehensions
# pre requisite - needing a new list
odds = [pointer for pointer in pointers if pointer % 2]
print(odds)

# get a new list of even pointers greater than 5 from pointers list (filtering)
evens = [pointer for pointer in pointers if not pointer % 2 and pointer > 5]
print(evens)

# get a new list of pointers deducted by 1 from pointers list (mapping)
deducted_marks = [pointer - 1 for pointer in pointers]
print(deducted_marks)

# get a new list of squares of odd pointers greater than or equal 5 from pointers list
# (filtering + mapping)
ans = [pointer ** 2 for pointer in pointers if pointer % 2 and pointer >= 5]
print(ans)


m1 = [1, 3, 5, 10]
m2 = [3, 4, 5, 9]

common = []
for a in m1:
    if a in m2:
        common.append(a)