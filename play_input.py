print('Program starts')

i = input('Enter n: ')

# exception handling
try:
    n = int(i)
except ValueError:
    print('Please pass in integer')
else:
    # will execute if there is no exception in the corresponding try block
    # will execute if the corresponding try block is a success
    print('Odd') if n % 2 else print('Even')

print('Program ends')