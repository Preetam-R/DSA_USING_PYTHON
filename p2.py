#concatination of array/list
'''Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]'''

lst = list(map(int,input("Enter the elements of the array:").split()))

print("the array is:\n",lst)

copy_lst = lst.copy()
ans = copy_lst + lst

print(ans)


