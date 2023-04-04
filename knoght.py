
def knight_shortest_path(N, source, destination): 
  

    if (source[0] > N - 1 or source[1] > N - 1 or
        destination[0] > N - 1 or destination[1] > N - 1): 
        return -1

    moves = [[-2, -1], [-2, 1], [-1, 2], [1, 2],  
             [2, 1], [2, -1], [1, -2], [-1, -2]] 
  

    queue = [] 

    queue.append([source, 0]) 
  

    visited = [[False for i in range(N)] for j in range(N)] 

    visited[source[0]][source[1]] = True
 
    while len(queue) > 0: 

        current = queue.pop(0) 
        i, j = current[0][0], current[0][1] 
        dist = current[1] 

        if i == destination[0] and j == destination[1]: 
            return dist 
  

        for k in range(8): 
  
            x = i + moves[k][0] 
            y = j + moves[k][1] 
  

            if (x >= 0 and x < N and y >= 0 and
                y < N and not visited[x][y]): 
                visited[x][y] = True
                queue.append([[x, y], dist + 1]) 

    return -1
  

N = 8
source = [7, 0] 
destination = [0, 7] 
print("Shortest path to reach destination is:",knight_shortest_path(N, source, destination))