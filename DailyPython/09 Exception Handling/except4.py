try:
    x = int(input('Enter a number: '))
    
except ValueError:
    print('Please Enter only numbers.')
except:
    print('Something Else Went!')


result = x * 9
print(result)
