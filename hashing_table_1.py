''' Hashing is the method to store and retrive the data in O(1) time'''

''' Hash table is the data structure to store the data in correct methodology'''

#LET'S BUILD THE HASH TABLE FROM SCRATCH
'''
1.Create an empty list (it can also be a dictionary or a set).
2.Create a hash function.
3.Inserting an element using a hash function.
4.Looking up an element using a hash function.
5.Handling collisions.
'''

#1. Creating an empty list

Ht = [None,None,None,None,None,None,None,None,None,None]

'''
-------------------------------------------------------------------------------------------
'''

#2. Create a Hash function

#in this function we are using unicode to calculate the char to int (for calculating the index)

def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)  #calculates and sums the unicodes

    return sum_of_char % 10  #this gives the index value (and this returned value is called hash code)

print("Preetam has the hash code of:",hash_function("Preetam"))

'''
-------------------------------------------------------------------------------------------
'''

# 3.Inserting an element using a hash function.

def add(name):
    index = hash_function(name)
    Ht[index] = name

# hash_function("Preetam")
add("Preetam")
print(Ht)

'''
-------------------------------------------------------------------------------------------
'''

# 4.Looking up an element using a hash function.


