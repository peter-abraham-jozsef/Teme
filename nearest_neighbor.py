def nearest_neighbor(graph:dict, start:int):
    unvisited = set(graph.keys())
    unvisited.remove(start)         

    path = [start]                   
    current = start                  
    total = 0                        
    while unvisited:
        best_node = None             
        best_dist = float('inf')     
        
        for neighbor, dist in graph[current].items():
            
            if neighbor in unvisited and dist < best_dist:
                best_node = neighbor     
                best_dist = dist

        
        if best_node is None:
            break

   
        path.append(best_node)
        unvisited.remove(best_node)
        total += best_dist
        current = best_node         

    return path, total

if __name__ == "__main__":
    graf = {
        1: {2: 4, 3: 2},
        2: {4: 5, 5: 3},
        3: {4: 1, 6: 7},
        4: {5: 2, 7: 6},
        5: {2: 1, 7: 3},
        6: {7: 4},
        7: {},
        }
    restult=nearest_neighbor(graf,1)
    print(restult)
                
        
        
        

        
    
