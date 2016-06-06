# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0



def returnAasNumber(filename):
    try:
        f = open(filename)
        text = f.read()
        f.close()
        numberOfA = 0
        for i in text:
            if i == 'a':
                numberOfA = numberOfA + 1
        return numberOfA
    except FileNotFoundError:
        return 0

print(returnAasNumber('holiday.txt'))
