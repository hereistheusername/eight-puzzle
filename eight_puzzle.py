from pprint import pprint
from PyInquirer import prompt, Separator
import numpy as np

import time
import sys
import threading
from multiprocessing import Process


from Astar import Problem,Operators,utils,Queue,Context,Node
from base.GeneralSearchAlgorithm import GeneralSearchAlgorithm


def input_custom_puzzle(answers):
    return answers['chosenPuzzle'] == questions[0]['choices'][1]

questions = [
    {
        'type': 'list',
        'name': 'chosenPuzzle',
        'message': 'choose puzzle',
        'choices': [
            'use a default puzzle',
            'enter your own puzzle'
        ]
    },
    {
        'type': 'input',
        'name': 'firstRow',
        'message': '''Enter your puzzle, use a zero to represent the blank
  Enter the first row, use space or tabs between numbers  ''',
        'when': input_custom_puzzle
    },
    {
        'type': 'input',
        'name': 'secondRow',
        'message': '''Enter the second row, use space or tabs between numbers ''',
        'when': input_custom_puzzle
    },
    {
        'type': 'input',
        'name': 'thirdRow',
        'message': '''Enter the third row, use space or tabs between numbers  ''',
        'when': input_custom_puzzle
    },
    {
        'type': 'list',
        'name': 'algorithm',
        'message': 'Enter your choice of algorithm',
        'choices': [
            'Uniform Cost Search',
            'A* with the Misplaced Tile heuristic',
            'A* with the Manhattan distance heuristic'
        ]
    }
]

operators = [
    Operators.Move_Blank_left('Move Blank left', 1),
    Operators.Move_Blank_right('Move Blank right', 1),
    Operators.Move_Blank_up('Move Blank up', 1),
    Operators.Move_Blank_down('Move Blank down', 1)
]

default_puzzle = np.array([[1,2,3],
                            [4,8,0],
                            [7,6,5]])

goal_state = np.roll(np.arange(9), -1).reshape(3,3)

def misplaced_distance(node):
    return utils.misplaced_distance(node.get_current_state(), goal_state)

def manhattan_distance(node):
    return utils.manhattan_distance(node.get_current_state(), goal_state)

def do_search(context):
        start_time = time.process_time()
        GeneralSearchAlgorithm(context)
        end_time = time.process_time()
        print(
            'the sum of the system and user CPU time of the current process in seconds: ',
            str(end_time - start_time)
        )
        sys.exit()

if __name__ == '__main__':
    answers = prompt(questions)

    problem = Problem.AStarProblem(default_puzzle, goal_state, operators)
    # if use custom puzzle
    if input_custom_puzzle(answers):
        firstRow = answers['firstRow'].split()
        secondRow = answers['secondRow'].split()
        thirdRow = answers['thirdRow'].split()
        custom_puzzle = np.array(firstRow+secondRow+thirdRow, dtype=int).reshape(3,3)
        problem.initial_state = custom_puzzle

    # choose h(n)
    if answers['algorithm'] == questions[4]['choices'][0]:
        # Uniform Cost Search is just A* with h(n) hardcoded to equal zero.
        h = lambda node: 0
    elif answers['algorithm'] == questions[4]['choices'][1]:
        h = misplaced_distance
    else:
        h = manhattan_distance

    # define g(n)
    def g(node):
        return node.cumulative_cost

    context = Context.AStarContext(problem, Queue.AStarQueue, Node.AStarNode, g, h)

    # do search
    search_process = threading.Thread(target=do_search, args=[context], daemon=True)
    search_process.start()
    time.sleep(15*60)
    if search_process.is_alive():
        print('run out of tim\n')
        sys.exit()
        