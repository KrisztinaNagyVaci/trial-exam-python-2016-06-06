# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

exampleList = [1, 2, 3, 4]
examplestring = 'hollywood'


def listElementDoubler(listInput):
    if isinstance(listInput, list):
        outputList = []
        for i in listInput:
            outputList.append(i * 2)
        return outputList
    else:
        return 'The parameter is not a list'
print(listElementDoubler(examplestring))
