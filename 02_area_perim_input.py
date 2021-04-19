# checks that users enter a number that is more than zero
valid = False
while not valid:
    
    error = "Please enter a number that is more than zero"
    
    try:
    
        # ask user to enter a number
        width = float(input("Enter the width: "))
        
        # checks number is more than zero
        if width > 0:
            valid = True
        
        # outputs error if input is invalid
        else:
            print(error)
            print()
            
    except ValueError:
        print(error)
        
# checks that users enter a number that is more than zero
valid = False
while not valid:
    
    error = "Please enter a number that is more than zero"
    
    try:
    
        # ask user to enter a number
        height = float(input("Enter a the height: "))
        
        # checks number is more than zero
        if height > 0:
            valid = True
        
        # outputs error if input is invalid
        else:
            print(error)
            print()
            
    except ValueError:
        print(error)
        
        
print()
print("The width is", width)
print("The height is", height)
        
    
    
        
    
    