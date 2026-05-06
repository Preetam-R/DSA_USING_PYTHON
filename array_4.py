#inserting the element at beginning 
#custom method 

arr = [10,20,30,40,0]

element = 50
n = 4

print("\narray before the insertion:",end = "")
for i in arr:
    print(i,end = " ")

for i in range(n-1,-1,-1):
    arr[i+1] = arr[i]

arr[0] = element

print("\nafter insertion:")
for i in range(n+1):
    print(arr[i],end = " ")
