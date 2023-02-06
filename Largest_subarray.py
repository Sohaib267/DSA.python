# program to print the largest subarray with sum zero
def maxLen(arr):
 
 
    hash_map = {}
 
    max_len = 0
 
    curr_sum = 0
    for i in range(len(arr)):
 
        curr_sum += arr[i]
 
        if curr_sum == 0:
            max_len = i + 1
 
       
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
 
          
            hash_map[curr_sum] = i
 
    return max_len
 
if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 13]
 
    print("Length of the longest 0 sum subarray is %d" % maxLen(arr))
# Time complexity of this program 0(n)
# Splace complexity of this program is 0(n)
