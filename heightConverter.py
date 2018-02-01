def convertHeight(height):
    """
    converts height from just inches to
    feets and inches
    takes: int height
    returns: tuple of int with height in
    feets and inches
    """
    height = int(height)
    inchesHeight = height % 12
    feetHeight = height // 12
    return(feetHeight, inchesHeight)

userHeight = input('Please enter height in inches: ')
print('you entered height is: {}'.format(userHeight))
print('you height is {} feet and {} inch'.format(*(convertHeight(userHeight))))
