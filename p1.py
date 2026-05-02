#find the maximum element array
# import numpy as np

# arr = list(map(int,input("enter the array elements:").split()))
# arr = np.array(arr)

# print(arr)

# max_ele = np.max(arr)
# print(max_ele)

#without using in built methods and libraries\

arr = list(map(int,input("enter the array elements:").split()))
print(arr)

max_val = arr[0]
for i in arr:
    if i > max_val:
        max_val = i

print("the maximum number in the array is:",max_val)
