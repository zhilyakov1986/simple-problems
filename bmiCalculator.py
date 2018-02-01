
def calculateBMI(data):
    """
    Created on Wed Jan 31 22:37:23 2018
    does: calculates BMI
    takes: tree int numbers
    returns: float
    @author: andreyZ
    """
    METERININCH = 0.0254
    LBSINKILO = 2.2
    try:
        if len(data) == 3:
            height = (data[0]) * 12 + data[1]
            heightInMeter = height * METERININCH
            weightInKilo = data[2] / LBSINKILO
            # BMI formula
            BMI = weightInKilo / (heightInMeter ** 2)
            return BMI
        else:
            raise Exception('Plese input correct data')
    except:
        print('incorrect data! READ THE DIRECTIONS')

# get user parameters
print('\n\n\n\n')
print("""***Please enter height in feet & inch and weight
in lbs use comma after each item.""")
userData = list(map(int,input('Please enter your data ').split(',')))
#shows how to round using format
print('Your BMI is: {number:.{digits}f}'.format(number = calculateBMI(userData),digits = 4))
