try:
    x = int(input('Enter a number: '))
    print(0/0)
    
except ValueError:
    print('Value error occuered')
except:
    print('Something Else Went Wrong!')
else:
    print('Running else')
    result = x * 9
    print(result)