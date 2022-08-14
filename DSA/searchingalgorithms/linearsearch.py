#create function with two parameters wich are an array and a value
#loop through the array and check if the current array element is equal to the value
#if it is return the index at which the element id found
#if the value s never found return -1


def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1







print(linearSearch([20,40,30,50,90], 100))