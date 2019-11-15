'''
1. Fibo series
2. Even series
3. Even odd
4. Exit
Enter choice: 1
Enter n: 8
0 1 1 2 3 5 8 13
1. Fibo series
2. Even series
3. Even odd
4. Exit
Enter choice: 2
Enter n: 8
0 2 4 6 8
1. Fibo series
2. Even series
3. Even odd
4. Exit
Enter choice: 3
Enter n : 10
Even
1. Fibo series
2. Even series
3. Even odd
4. Exit
Enter choice: 4
'''
# import com.abc.lib.series # imports the module and not the functions inside it

# import the functions directly from the module
from com.abc.lib.series import get_even_series as evenseries, get_fibo_series

import com.abc.lib.math as maths

while True:
    # print('1. Fibo Series\n2. Even Series\n3. Even or odd\n4. Exit')
    print('1. Fibo Series', '2. Even Series', '3. Even or odd', '4. Exit', sep='\n')
    choice = int(input('Enter choice: '))

    if choice == 4:
        break
    
    if choice == 1 or choice == 2 or choice == 3:
        # scope of variables in python is either the 
        # global (entire file)
        # function
        n = int(input('Enter n: '))
    
    if choice == 1:
        # print(com.abc.lib.series.get_fibo_series(n))
        print(get_fibo_series(n))
    elif choice == 2:
        # print(com.abc.lib.series.get_even_series(n))
        # print(get_even_series(n))
        print(evenseries(n))
    elif choice == 3:
        print(maths.evenodd(n))
    else:
        print('wrong choice')
