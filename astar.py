maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_node = (0, 0)
end_node = (9, 4) 

def get_neighbors(node):

    r, c = node 

    valid_neighbors = [] 

    if (r - 1 >= 0) and (maze[r - 1][c] == 0):
        valid_neighbors.append((r - 1, c))

    if (r+1 < len(maze)) and maze[r+1][c]==0:
        valid_neighbors.append((r + 1, c))

    if (c-1 >=0) and maze[r][c-1]==0:
        valid_neighbors.append((r, c-1))

    if (c+1 <len(maze[0])) and maze[r][c+1]==0:
        valid_neighbors.append((r, c+1))

    return valid_neighbors

print("Safe steps from start:")
print(get_neighbors(start_node))

def get_heuristic(node, target):
    r1,c1=node
    r2,c2=target
    distance = abs(r1 - r2) + abs(c1 - c2)
    return distance

to_do_list = [start_node]  
done_list = []          

steps_taken = {}              
total_score = {}              
breadcrumbs = {}           

steps_taken[start_node] = 0
total_score[start_node] = get_heuristic(start_node, end_node)



while len(to_do_list) > 0:
    
    current_node = to_do_list[0]
    for node in to_do_list:
        if total_score[node] < total_score[current_node]:
            current_node = node
            
    print("Exploring:", current_node)

    if current_node==end_node:
        print('Found the exit!')
        break



    to_do_list.remove(current_node)
    done_list.append(current_node)
    

    neighbors = get_neighbors(current_node)
    
    for neighbor in neighbors:
        if neighbor in done_list:
            continue  
            
        trial_g_cost = steps_taken[current_node] + 1
        
        if neighbor not in to_do_list or trial_g_cost < steps_taken.get(neighbor, 999999):
            
            breadcrumbs[neighbor] = current_node
            
            steps_taken[neighbor] = trial_g_cost
            h_cost = get_heuristic(neighbor, end_node)
            total_score[neighbor] = trial_g_cost + h_cost
            
            if neighbor not in to_do_list:
                to_do_list.append(neighbor)


path = []
current = end_node

while current in breadcrumbs:
    path.append(current)
    current = breadcrumbs[current]

path.append(start_node)
path.reverse()          

print("The Optimal Path is:")
print(path)               