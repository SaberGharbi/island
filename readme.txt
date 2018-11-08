what is BFS:

Breadth-first search (BFS) is an algorithm used for traversing graph data structures. In other words,  BFS implements a specific strategy for visiting all the nodes
 (vertices) of a graph . What is this exploration strategy? It’s very simple and effective. BFS starts with a node, then it checks 
the neighbours of the initial node, then the neighbours of the neighbours, and so on. 

implementation of bfs algorithm on our example :

The approach is to visualize the given matrix as a graph with each cell representing a separate node of the graph and each node connected to four other nodes which are immediately up, down, left, and right of that cell.
At every cell (i, j), a BFS can be done. The possible moves from a cell will be either to east, west, north or south. we move to only those cells which are in range and have the same value.To avoid processing a cell more than once and reduce the number of BFS , we use a boolean visited array. 
If the same nodes have been visited previously, then the island found in the matrix is stored in island[][] array .





THANK YOU FOR READING !

 
