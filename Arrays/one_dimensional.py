from array import *

#create an array and traverse.
my_array = array('i', [1,2,3,4,5])

for i in my_array:
    print(i)

#access individual elements through indexes
print("\nStep 2")
print(my_array[0])
print(my_array[3])

#append any value to the array using append() method
print("\nStep 3")
my_array.append(6)
print(my_array)

#insert value in an array using insert() method
print("\nStep 4")
my_array.insert(3,11)
print(my_array)

#extend python array using extend() method
print("\nStep 5")
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)

#add items from lst into array using fromlist() method
print("\nStep 6")
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

#remove any array element using remove() method
print("\nStep 7")
my_array.remove(22)
print(my_array)

#remove last array element using pop() method
print("\nStep 8")
my_array.pop()
print(my_array)

#fetch any element through its index ysing index() method
print("\nStep 9")
print(my_array.index(20))

#reverse a python array using reverse() method
print("\nStep 10")
my_array.reverse()
print(my_array)

#get array buffer information through buffer_info() method
print("\nStep 11")
print(my_array.buffer_info())

#check for number of occurences of an element using count() method
print("\nStep 12")
print(my_array.count(11))
print(my_array)

#convert array to string using tostring() method
#print("\nStep 13")
#strTemp = my_array.tostring()
#print(strTemp)

#convert array to a python list with same elements using tolist() method
print("\nStep 14")
print(my_array.tolist())

#append a string to char array using fromstring() method
print("\nStep 15")


#slice elements from an array
print("\nStep 16")
print(my_array[3:])