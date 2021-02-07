# ctx is context, which is used to control output message when expanding node or finding the goal
def GeneralSearchAlgorithm(ctx):
    problem = ctx.get_problem()
    queue = ctx.get_queue_function()

    nodes = queue(problem.get_initial_state())
    ctx.onInit()

    while True:
        if nodes.isEmpty():
            return ("failure")
        node = nodes.remove_front()
        # expanding node
        ctx.onExpand(node)
        if problem.goal_test(node.get_current_state()):
            # found the goal
            ctx.onSuccess(node)
            return ("success", node)
        nodes.queueing(node.expand(problem.operators))
