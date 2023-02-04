from collections import defaultdict
 
def reverse(num):
 
    rev_num = 0

    while (num > 0):
 
        rev_num = rev_num * 10 + num % 10
        num = num // 10
  
    return rev_num

def countReverse(arr, n):
 
    freq = defaultdict (int)

    for i in range (n):
        freq[arr[i]] += 1
 
    res = 0
    
    for i in range (n):
        freq[arr[i]] -= 1
        res += freq[reverse(arr[i])]
    
    return res
if __name__ == "__main__":
   
    a = [1,3,2,3,1]
    n = len(a)
    print (countReverse(a, n))