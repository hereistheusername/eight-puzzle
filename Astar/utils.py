import numpy as np

# both of two are not including the blank

def misplaced_distance(current_state, goal_state):
    misplaced_numbers = goal_state[goal_state!=current_state]
    return misplaced_numbers.size if misplaced_numbers.all() else (misplaced_numbers.size - 1)

def manhattan_distance(current_state, goal_state):
    misplaced_numbers = goal_state[goal_state!=current_state]
    distance = 0
    for n in np.delete(misplaced_numbers, np.where(misplaced_numbers == 0)):
        in_goal = np.array(np.where(goal_state == n))
        in_current = np.array(np.where(current_state == n))
        distance += np.abs(in_goal-in_current).sum()
    
    return distance
