def findTargetSum(arr, target): 
    
    result = set() 

   
    for i in range(len(arr)): 

       
        curr_sum = arr[i]  
        rem_sum = target - curr_sum  

        if rem_sum in result:  
            print("The two elements whose sum is equal to the given target are", rem_sum, "and", curr_sum)  

        else:    
            result.add(curr_sum)     

    return False;      									 
if __name__ == "__main__":    

    arr = [2,4,5,6,3]    

    target = 7;    

    findTargetSum(arr,target);   