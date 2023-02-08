# Python Program to count all possible Unique paths from top left to bottom right using Recursion

def uniquePaths(m,n):
    if(m==1 or n==1):
        return 1
    return uniquePaths(m-1,n)+uniquePaths(m,n-1)

m=int(input("Enter the no. of Row:"))
n=int(input("Enter the no. of Column:"))
c=uniquePaths(m,n)
print("The total Unique Path to reach destination is equal to:",c)
# Time Complexity: O(2^n)
# Auxiliary Space: O(n+m)

# Python Program to count all possible Unique paths from top left to bottom right using combinatorics

def uniquePaths(m,n):
    uniquePaths=1
    for i in range(n,m+n-1):
        uniquePaths *= i
        uniquePaths /= (i - n + 1)
    return uniquePaths

m=int(input("Enter the no. of Row:"))
n=int(input("Enter the no. of Column:"))
c=uniquePaths(m,n)
print("The total Unique Path to reach destination is equal to:",c)
# Time Complexity: O(n)
# Auxiliary Space: O(1)