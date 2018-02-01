
def displayInDecimal(data):

    """
    Created on Wed Jan 31 23:37:16 2018
    does: converts latitude to decimals
    takes: list of int
    returns: float
    @author: andreyZ
    """
    SECONDINHOUR = 3600
    try:
        if len(data) == 3:
            totalSeconds = (data[1] * 60 + data[2]) / SECONDINHOUR
            return data[0] + totalSeconds
        else:
            raise Exception('READ!!!')
    except:
        print('\nWRONG INPUT PLEASE READ THE DIRECTIONS!!!')

# USER INPUT TO TEST THE FUNCTION
print('please enter latitude in degrees, minutes, and seconds')
userData = list(map(int, input('enter the data: ').split(',')))
try:
    print('{:d} degrees, {:d} minutes, {:d} seconds'.format(*userData), end='')
    print(' = {0:.4f} degrees'.format(displayInDecimal(userData)))
except:
    print('\nWRONG INPUT PLEASE READ THE DIRECTIONS!!!\n')