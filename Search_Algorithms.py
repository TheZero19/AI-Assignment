from State import State
from queue import PriorityQueue
from queue import LifoQueue

#Depth-first Search with limited depth
def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth == 30:
            continue #go to the next branch

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))


def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n)
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return
