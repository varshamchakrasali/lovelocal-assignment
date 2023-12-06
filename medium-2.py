#Problem: Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def findElements(arr):
    result = []
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    limit  = len(arr)/3
    for key in freq:
        if freq[key] > limit:
            result.append(key)
    return result

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i+1} element: ")))     
print(findElements(arr))
       
