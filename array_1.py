''' Array can be classified into two types
1. fixed array
2.dynamic array
'''

#Fixed Array
fixed_arr = [0] * 5

#Dynamic_Array
dynamic_arr = []

'''-------------------------------------------------------------------------------------'''

''' Types of traversal 
1.Linear Traversal
2. Reverse Traversal
'''

#Linear Traversal
arr = [10,20,30,40,50]
print("\nLinear Traversal:",end = "")
for i in arr:
    print(i,end = " ")


#Resevrse Traversal
print("\nReverse Traversal:",end = "")
for j in range(len(arr)-1,-1,-1):
    print(arr[j],end=" ")
