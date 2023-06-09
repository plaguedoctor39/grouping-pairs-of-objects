from ortools.linear_solver import pywraplp
from func.Auxiliary_functions import *
from itertools import combinations
import time


# import multiprocessing
#
# print(multiprocessing.cpu_count())
def mainMIP_iter(n_rows, path):
    n_rows = n_rows
    df = ReadSource(n_rows, path)
    ships = [[[i[0], i[1]], calcRowOverlap(i[0], i[1], df)] for i in getAprovePairs(df.index)]

    start = time.time()

    # Initialize a list to store the groups
    all_groups = []
    all_weights = []

    # Start with original set of nodes
    nodes = list(df.index)
    iteration = 1
    # test = {(1, 2): 5, (1, 3): 5, (1, 4): 3, (1, 5): 3, (1, 6): 3, (2, 3): 5,(2, 4): 1, (2, 5): 4, (2, 6): 3,
    #         (3, 4): 3, (3, 5): 5, (3, 6): 1, (4, 5): 2, (4, 6): 2, (5, 6): 2}
    # nodes = [x for x in range(1, 7)]
    while len(nodes) > 0:
        print('--------------------')
        print(f'Iteration {iteration}')
        iteration += 1
        # Define the problem
        print('Define the problem')
        solver = pywraplp.Solver.CreateSolver('CP-SAT')
        solver.SetNumThreads(10)

        # Create variables and weights for current nodes
        x = {node: solver.IntVar(0, 1, f'x[{node}]') for node in nodes}
        weights = {(i, j): calcRowOverlap(i, j, df) for i, j in combinations(nodes, 2)}
        # print(weights)
        # weights = test
        # Create connections for current nodes
        connections = {(i, j): solver.IntVar(0, 1, f'c({i},{j})') for i, j in combinations(nodes, 2)}

        # Define the objective function
        print('Define the objective function')
        obj = solver.Objective()
        for (i, j), c in connections.items():
            obj.SetCoefficient(c, weights[(i, j)])
        obj.SetMaximization()

        # Add constraint to ensure we have a group of exactly 5 nodes (or fewer if less than 5 nodes are remaining)
        print('Add constraint to ensure we have a group of at most 5 nodes')
        # constraint = solver.Constraint(5, 5)
        group_size = min(len(nodes), 5)
        constraint = solver.Constraint(group_size, group_size)
        for i in nodes:
            constraint.SetCoefficient(x[i], 1)

        # Add constraints to ensure each connection is only active if both nodes are active
        print('Add constraints to ensure each connection is only active if both nodes are active')
        for (i, j), c in connections.items():
            solver.Add(c <= x[i])
            solver.Add(c <= x[j])
        # write model
        if len(nodes) == n_rows:
            with open("test.mps", "w") as out_f:
                mps_text = solver.ExportModelAsMpsFormat(fixed_format=False, obfuscated=False)
                out_f.write(mps_text)
        # Solve the problem
        print('Solve the problem')
        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            print('Solution: ')
            group = [i for i in nodes if x[i].solution_value() > 0.5]
            print('Group:', group)
            group_weight = sum(weights[(i, j)] for i, j in combinations(group, 2))
            print('Group weight:', group_weight)
            all_groups.append(group)
            all_weights.append(group_weight)
            print('Problem solved in %f milliseconds' % solver.wall_time())
            # Remove the nodes that were included in the group
            nodes = [node for node in nodes if node not in group]
        else:
            print('No solution exists')
            break

    end = time.time()
    # print('\nThe program took {:.2f} s to compute.'.format(end - start))
    # print(f'Maximum total weight: {sum(all_weights)} ')
    # for i in range(len(all_groups)):
    #     print(f'group {i + 1} - {all_groups[i]} | weight - {all_weights[i]}')
    return {'Objective': sum(all_weights), 'Groups': all_groups, 'Time': '{:.2f} s'.format(end - start)}

# print('All groups:', all_groups)
# print('All weights:', all_weights)

# # Define the problem
# print('Define the problem')
# solver = pywraplp.Solver.CreateSolver('CP-SAT')
# solver.SetNumThreads(10)
# x = [solver.IntVar(0, 1, f'x{i}') for i in range(n_rows)]
# weights = {(i[0], i[1]): calcRowOverlap(i[0], i[1], df) for i in getAprovePairs(df.index)}
# connections = {}
# for i in range(1, n_rows+1):
#     for j in range(i+1, n_rows+1):
#         connections[(i, j)] = solver.IntVar(0, 1, f'c({i},{j})')
#
# # Define the objective function
# print('Define the objective function')
# obj = solver.Objective()
# for (i, j), c in connections.items():
#     obj.SetCoefficient(c, weights[(i, j)])
# obj.SetMaximization()
#
# # Add constraint to ensure we have a group of exactly 5 nodes
# print('Add constraint to ensure we have a group of exactly 5 nodes')
# constraint = solver.Constraint(5, 5)
# for i in range(n_rows):
#     constraint.SetCoefficient(x[i], 1)
#
# # Add constraints to ensure each connection is only active if both nodes are active
# print('Add constraints to ensure each connection is only active if both nodes are active')
# for (i, j), c in connections.items():
#     solver.Add(c <= x[i-1])
#     solver.Add(c <= x[j-1])
#
#
#
# # Solve the problem
# print('Solve the problem')
# status = solver.Solve()
# print('solved')
# groups = [[i + 1 for i in range(n_rows) if x[i].solution_value() > 0.5]]
# print(groups)
# weight_sum = 0
# # Compute group weights
# print('Compute group weights')
# group_weights = {i: sum(weights[(i, j)] for i in group for j in group if i < j) for i, group in enumerate(groups)}
#
# print(group_weights)
# # Add constraints for all groups at once
# for i, weight in group_weights.items():
#     solver.Add(weight >= weight_sum)
#
# print('changes added')
# solver.Solve()
# print('solved')
# # Print the solution
# if status == pywraplp.Solver.OPTIMAL:
#     print('Solution: ')
#     groups = [[i + 1 for i in range(n_rows) if x[i].solution_value() > 0.5]]
#     print('Groups:', groups)
#     group_weight = sum(weights[(i, j)] for i in groups[0] for j in groups[0] if i < j)
#     print('Group weight:', group_weight)
# else:
#     print('No solution exists')
#
# end = time.time()
# print('\nThe program took {:.2f} s to compute.'.format(end - start))
