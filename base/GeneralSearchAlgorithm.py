def GeneralSearchAlgorithm(problem, queue):
    nodes = queue(problem.get_initial_state())

    while True:
        if nodes.isEmpty():
            return ("failure")
        node = nodes.remove_front()
        if problem.goal_test(node.get_current_state()):
            return ("success", node)
        nodes.queueing(node.expand(problem.operators))
