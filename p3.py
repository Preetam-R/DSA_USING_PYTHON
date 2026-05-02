'''Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].'''

nums = list(map(int,input("enter the elements in the array:").split()))
n = int(input("enter the target:"))
result = []

if n <= 0:
    print("enter the target above 0.")
else:
    for i in range(n):
        result.append(nums[i])      
        result.append(nums[i + n])  
    print(result)

