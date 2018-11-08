#python program to print the largest island found
#in a random matrix

import numpy as np

#number of columns and rows
n = 10

#random matrix with elements
#from 0 to 4
matrix = np.random.choice([x for x in range(0, 5)], n*n)
matrix.resize(n, n)
 

#stores information about which cells 
#are already visited in a particular search
visited = [[False for i in range(n)] for j in range(n)]

#stores the final result matrix 
island = [['.' for i in range(n)] for j in range(n)]

#A function to check if a given cell
#can be included in our search ie it is inside 
#the matrix and value equal to key and not yet visited 
def isSafe(i,j,key,matrix,visited): 

        return (i >= 0 and i < n and 
                j >= 0 and j < n and 
                not visited[i][j] and matrix[i][j]==key) 

#a recurssive function to find all cells in 
# connection with key = matrix[i][j]forming
#an island based on BFS algorithm
#for more details check readme.txt
def BFS(x,y,i,j,matrix,visited):
    
    #stores the number of cells
    #in an island
    global count
    
    #terminating case for our search
    if(x!=y):
        return visited
    
    #mark the cell as visited
    visited[i][j] = True
    count+=1
    
    #These arrays are used to get row and  
    #column numbers of the 4 neighbours in 
    #north,south,east and west of a given cell
    row_move=[1, -1, 0, 0] 
    col_move=[0, 0, 1, -1]
    
    #checks all 4 neighbours of matrix[i][j]
    for k in range(4): 
            if isSafe(i + row_move[k], j + col_move[k],x,matrix,visited): 
                BFS(x,y,i + row_move[k], j + col_move[k],matrix,visited)

#If a larger island is found this 
#function is called to store
#information about that island               
def result(key,matrix,visited):
      
    for i in range(n):
        for j in range(n):
             if ( visited[i][j] and matrix[i][j]==key ):
                island[i][j]='x'
             else:
                island[i][j]='.'
    
          

#function to find the largest island 
def find_largest_island(matrix):
    
 global count
 current_max=0
 
 for i in range(n):
     for j in range(n):
         
      #Initially all cells are unvisited   
      visited = [[False for i in range(n)] for j in range(n)]
      count=0
      
      #checking cell to the right
      if (j+1<n):
         BFS(matrix[i][j],matrix[i][j+1],i,j,matrix,visited)
         
         #updating the result if we found a larger island
         if (count >= current_max):  
            current_max=count
            result(matrix[i][j],matrix,visited)
            
      #we reset visited before the next BFS so every cell
      #is unvisited       
      visited = [[False for i in range(n)] for j in range(n)]
      count=0
      
      #checking cell downwards  
      if (i+1<n): 
         BFS(matrix[i+1][j],matrix[i][j],i,j,matrix,visited)
         
         #updating the result if we found a larger island
         if (count>= current_max):  
           current_max=count
           result(matrix[i][j],matrix,visited)
         
      
    

 

# our main code to display the random matrix
# and then show the largest island.

find_largest_island(matrix)
print(matrix)
island=np.matrix(island)
island.resize(n,n)
print ("largest island is : ")
print(island)



