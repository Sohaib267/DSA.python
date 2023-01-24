class Solution(object):
   def setZeroes(self, matrix):
      n = len(matrix)
      m = len(matrix[0])
      flag = False
      if matrix[0][0] == 0:
         flag = True
         row = False
         column = False
      for i in range(1,n):
         if matrix[i][0] == 0:
            column = True
            break
      for i in range(1,m):
         if matrix[0][i] == 0:
            row = True
            break
      for i in range(1,n):
         for j in range(1,m):
            if matrix[i][j] == 0:
               matrix[0][j] = 0
               matrix[i][0]=0
      for i in range(1,n):
         for j in range(1,m):
            if not matrix[i][0] or not matrix[0][j]:
               matrix[i][j] = 0
      if flag:
         for i in range(n):
            matrix[i][0] = 0
         for i in range(m):
            matrix[0][i]=0
      else:
         if column:
            for i in range(n):
               matrix[i][0]=0
         if row:
            for i in range(m):
               matrix[0][i]=0
      return matrix
ob1 = Solution()
print(ob1.setZeroes([[1,0,1],[1,1,1],[1,1,1]]))