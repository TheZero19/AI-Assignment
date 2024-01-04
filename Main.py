from Search_Algorithms import DFS, AStar_search
from State import State, print_space_tree

root = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal = [2, 0, 8, 1, 6, 3, 7, 5, 4]

print("The initial state is:", root)
print("The goal state is:", goal)

#State Space Tree Generation:
initial_node = State(root, None, None, 0, 0)
print_space_tree(initial_node)
print('\n')

#DFS solver:
DFS_solution = DFS(root, 3)
print('DFS Solution is ', DFS_solution[0])
print('Number of explored nodes is ', DFS_solution[1])
print('\n')

#AStar with Manhattan Distance:
AStar_solution = AStar_search(root, 3)
print('A* Solution using Manhattan Distance is ', AStar_solution[0])
print('Number of explored nodes is ', AStar_solution[1])
