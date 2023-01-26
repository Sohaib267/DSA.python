
# Program to print 

N = 3

def rotate(arr):
    global N
 
  
    for i in range(N):
        for j in range(i):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
 

    for i in range(N):
        for j in range(int(N/2)):
            temp = arr[i][j]
            arr[i][j] = arr[i][N-j-1]
            arr[i][N-j-1] = temp
 
 
# Driver code
arr = [[1, 2, 3],
       [5, 6, 7],
       [9, 10, 11]]
 
rotate(arr)
 
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
 