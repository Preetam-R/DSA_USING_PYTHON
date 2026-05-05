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

Ht =  [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

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
    my_list[index].append(name)

# hash_function("Preetam")
add("Bob")

add('Pete')
add('Jones')
add('Lisa')
add('Siri')

print(Ht)
'''
-------------------------------------------------------------------------------------------
'''

# 4.Looking up an element using a hash function.

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))

'''
-------------------------------------------------------------------------------------------
'''

# 5. Colision Handling
add('Stuart')
print(Ht)

''' Searching for "Stuart" now takes a little bit longer time, because we also find "Lisa"
 in the same bucket, but still much faster than searching the entire Hash Table.'''

 

