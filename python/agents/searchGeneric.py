from display import Displayable
from searchProblem import Path
from searchExample import simp_delivery_graph

class Searcher(Displayable):
    def __init__(self, problem):
        self.problem = problem
        self.num_expanded = 0
        self.initialize_frontier()
        self.add_to_frontier(Path(problem.start_node()))

    def initialize_frontier(self):
        self.frontier = []
    def empty_frontier(self):
        return self.frontier == []
    def add_to_frontier(self,path):
        self.frontier.append(path)

    def search(self):
        """returns (next) path from the problem's start node to a goal node. 
        Returns None if no path exists.
        """
        while not self.empty_frontier():
            path = self.frontier.pop()
            self.num_expanded += 1
            print(path)
            if self.problem.is_goal(path.end()):
                return path
            else:
                neighs = self.problem.neighbors(path.end())
                for arc in reversed(list(neighs)):
                    self.add_to_frontier(Path(path, arc))
        return None

#simp_delivery_graph.show(show_costs=True)

searcher = Searcher(simp_delivery_graph)
searcher.search()
