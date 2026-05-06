''' Applications of traversal 
1.searching elements
2.modifying elements
'''

#1.searching elements 

arr = [20,45,29,48,34]

found = False
target = 29
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("element not found")


#2.Modifying array
#if i want to add array elements by 5

print("\nOriginal array",end = "")
for j in arr:
    print(j,end = " ")

print("\nadding 5 to the every element of the array.........")
for k in range(len(arr)):
    arr[k] += 5

print("\nmodified array is:",end = "")
for num in arr:
    print(num,end = " ")




