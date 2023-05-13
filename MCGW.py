def genStates():
    g = []
    for i in ["E", "W"]:
        for j in ["E", "W"]:
            for h in ["E", "W"]:
                g.append(i + j + h)
    return g
    
def genLegalStates(graph, S, next_pos, cur_state):
    # determine the current position of the man
    if next_pos == 'E':         
        cur_pos = 'W'
    else:
        cur_pos = 'E'
    
    # initialize the list of legal next states    
    graph[cur_state] = []             
    next_states = []
        
    # iterate though the whole states, if the state is legal then append it into queue
    for state in S:
        # C, G; G, W
        # If the wolf and goat or goat and cabbage are on the same side of the river, the man cannot leave them alone so it will skip it
        if state[0] == state[1] and next_pos != state[1]:
            continue
        if state[1] == state[2] and next_pos != state[1]:
            continue
        
                                    # the times of movement should be <= 1, if times == 1, the direction should be the same with man's position
        else:
                                    # check if the times of movement <= 1
            count = 0
            count_m = 0
            for i in range(0, 3):
                if cur_state[i] != state[i]:
                    count += 1
                    if state[i] == next_pos:
                        count_m += 1
                                    # If the times of movement is 1 and the direction of movement is the same as the man's position, add the state to the list of legal next states 
            if count == 1 and count_m == 1:
                graph[cur_state].append(state)
                next_states.append(state)
                
            elif count == 0:        # If the times of movement is 0, add the state to the list of legal next states
                graph[cur_state].append(state)
                next_states.append(state)
    return graph, next_states
    
                                    # E      W      E      W      E      W      E      W
                                    # EEE -> EWE -> EWE -> WWE -> WEE -> WEW -> WEW -> WWW     '''our thinking path'''
                                    #                   -> EWW -> EEW ->
def genLegalGraph(S, start, end):
    next_pos = 'W'                  # man should change his position in every iteration
    cur_state = start
    graph = {}
    next_states = [start]
    past_states = []
    
    while cur_state != end:                                                                                  # until state == 'WWWW'
        for cur_state in next_states:
            if next_pos == 'E':
                cur_pos = 'W'
            else:
                cur_pos = 'E'
            '''print('cur_pos: ', cur_pos)             #we include this for checking our code
            print('cur_state: ', cur_state)'''
            
            if cur_pos + cur_state in past_states:
                continue
            graph, next_states = genLegalStates(graph, S, next_pos, cur_state)
            past_states.append(cur_pos + cur_state) 
            '''print('graph: ', graph)
            print('next_states: ', next_states)         #we include this for checking our code
            print('past_states: ', past_states)
            print('----------')
        print('-----------------------------------------------')'''
        
                                                                                                            # change man's position
        cur_pos, next_pos = next_pos, cur_pos


    return graph
    



def findShortestPath(graph, start, end, path=[]):
    """
    A function to find a shortest path from start to end on a graph
    This function is obtained from https://www.python.org/doc/essays/graphs/
    with one change due to the deprecation of the method has_key().
    
    Input: A graph, a starting node, an end node and an empty path
    Output: Return the shortest path in the form of a list.
    """
    
    path = path + [start]
    if start == end:
        return path

    if not (start in graph):
        return None
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
    return shortestPath
def ifnopath(path):
    final_path=[]
    for i in range(len(path)):
        final_path.append(path[i])
        if path[i][0]!=path[i][1] and path[i][1]!=path[i][2]:
            a=path[i]
            final_path.append(a)
    return final_path
def printPath(path):
    east='east'
    west='west'
    #print(path)
    East=["man", "cabbage", "goat", "wolf"]
    West=[]
    print('East:{:40}West:{}'.format(', '.join(East), ', '.join(West)))
    for i in range(len(path)):   
        j=i+1
        if j<len(path):
            if path[i][2]!=path[j][2]:                                                                      #unnecessary to consider the man position     #in order to fit the required output path
                if east=='east':
                    East.remove('man')                                                                          #remove the man from the current side
                    East.remove('cabbage')                                                                      #remove the cabbage from the current side
                    West.insert(1, 'cabbage')                                                                   #insert it to the destination side
                    West.insert(0, 'man')                                                                       #insert it to the destination side
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "cabbage", east, west))     #first time will always go from east to west
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
                else:
                    West.remove('man')                                                                          #remove the man from the current side
                    West.remove('cabbage')                                                                      #remove the cabbage from the current side
                    East.insert(1, 'cabbage')                                                                   #insert it to the destination side
                    East.insert(0, 'man')                                                                       #insert it to the destination side
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "cabbage", east, west))     #first time will always go from east to west
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
            elif path[i][1]!=path[j][1]:                                                                    #unnecessary to consider the man position
                if east=='east':
                    East.remove('man')
                    East.remove('goat')
                    West.insert(2, 'goat')
                    West.insert(0, 'man')
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "goat", east, west))        #first time will always go from east to west
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
                                                                                                                #first time will always go from east to west(we change the goat from 1 to 2 and change the wolf from 2 to 1 in order to fit the required
                else:
                    West.remove('man')
                    West.remove('goat')
                    East.insert(2, 'goat')
                    East.insert(0, 'man')
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "goat", east, west))        #first time will always go from east to west
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
                                                                                                                #first time will always go from east to west(we change the goat from 1 to 2 and change the wolf from 2 to 1 in order to fit the required
            elif path[i][0]!=path[j][0]:                                                                    #unnecessary to consider the man position 
                if east=='east':
                    East.remove('man')
                    East.remove('wolf')
                    West.insert(3, 'wolf')
                    West.insert(0, 'man')
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "wolf", east, west))       
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
                else:
                    West.remove('man')
                    West.remove('wolf')
                    East.insert(3, 'wolf')
                    East.insert(0, 'man')
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "wolf", east, west))       
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
            else:
                if east == 'east':
                    East.remove('man')
                    West.insert(0, 'man')
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "only himself", east, west))       #first time will always go from east to west
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
                else:
                    West.remove('man')
                    East.insert(0, 'man')
                    print("{}. The man takes {} from the {} to the {}.".format(i+1, "only himself", east, west))       #first time will always go from east to west
                    print("-->")
                    print('East: {:40}West: {}'.format(', '.join(East), ', '.join(West)))
            
        east, west=west, east   #change side
def main():
    if __name__ == '__main__':
        print("A solution to the MCGW problem is:")
        states = genStates()
        graph = genLegalGraph(states, 'EEE', 'WWW') #start from EEE to WWW
        '''print(graph)'''   #our testing code
        path = findShortestPath(graph,'EEE','WWW')
        '''print(path)'''    #our testing code
        #print(path)
        final_path = ifnopath(path)
        #print(final_path)
        printPath(final_path)
        print("Congratulate yourself for solving the MCGW problem")
        
main()