taking_input = True
while taking_input:
    try:
        x = int(input('Enter a number: '))
        
    except ValueError:
        print('Please Input only numbers')
    except:
        print('Something Else Went Wrong!')
    else:
        taking_input = False
        result = x * 9
        print(result)
    
    finally:
        print('Running Finally...')
        # close connection with api
        # close files
        # close connection with data
    

# slicing
# scope


