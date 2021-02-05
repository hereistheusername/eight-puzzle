from base import Problem

class AStarProblem(Problem.AbstractProblem):
    def __init__(self,
                initial_state,
                goal_state,
                operators):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = operators

    # state is not node
    # for eight-puzzle problem I will use numpy.array to 
    # represent the state
    def goal_test(self, state):
        return (self.goal_state == state).all()
    
    def get_initial_state(self):
        return self.initial_state
        
    def get_goal_state(self):
        return self.goal_state

    def get_operators(self):
        return self.operators