#insert the element at the beginning 
#using built in method

arr = [10,20,30,40]
print("array before insertion.")
for i in arr:
    print(i,end = " ")

element = int(input("\nenter the element you need to insert:"))

arr.insert(0,element)

print("\narray after inssertion of the element")
for i in range(len(arr)):
    print(arr[i],end = " ")
