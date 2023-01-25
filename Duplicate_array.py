# Program that prints the duplicate element in array.

arr = [2,3,4,1,2]

for i in range(0, len(arr)):
    
    for j in range(i+1,len(arr)):
        
        if (arr[i]==arr[j]):
            
            print(arr[j])
     