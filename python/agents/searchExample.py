from searchProblem import Arc, Search_problem_from_explicit_graph, Search_problem

simp_delivery_graph = Search_problem_from_explicit_graph("Acyclic Delivery Graph",
    {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'},
    [    Arc('A', 'B', 2),
         Arc('A', 'C', 3),
         Arc('A', 'D', 4),
         Arc('B', 'E', 2),
         Arc('B', 'F', 3),
         Arc('C', 'J', 7),
         Arc('D', 'H', 4),
         Arc('F', 'D', 2),
         Arc('H', 'G', 3),
         Arc('J', 'G', 4)],
   start = 'A',
   goals = {'G'},
   hmap = {
        'A': 7,
        'B': 5,
        'C': 9,
        'D': 6,
        'E': 3,
        'F': 5,
        'G': 0,
        'H': 3,
        'J': 4,
    },
    positions = {
        'A': (0.4,0.1),
        'B': (0.4,0.4),
        'C': (0.1,0.1),
        'D': (0.7,0.1),
        'E': (0.6,0.7),
        'F': (0.7,0.4),
        'G': (0.7,0.9),
        'H': (0.9,0.6),
        'J': (0.3,0.9)
        }
    )
