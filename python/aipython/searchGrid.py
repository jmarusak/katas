# searchGrid.py - A grid problem to demonstrate A*

from searchProblem import Search_problem, Arc

class GridProblem(Search_problem):
    """a node is a pair (x,y)"""
    def __init__(self, size=10):
        self.size = size
        
    def start_node(self):
        """returns the start node"""
        return (0,0)
    
    def is_goal(self,node):
        """returns True when node is a goal node"""
        return node == (self.size,self.size)
    
    def neighbors(self,node):
        """returns a list of the neighbors of node"""
        (x,y) = node
        return [Arc(node,(x+1,y)), Arc(node,(x,y+1))]
   
    def heuristic(self,node):
        (x,y) = node
        return abs(x-self.size)+abs(y-self.size)

class GridProblemNH(GridProblem):
    """Grid problem with a heuristic of 0"""
    def heuristic(self,node):
        return 0

from searchGeneric import Searcher, AStarSearcher
from searchMPP import SearcherMPP
from searchBranchAndBound import DF_branch_and_bound

def testGrid(size = 10):
    print("\nWith MPP")
    gridsearchermpp = SearcherMPP(GridProblem(size))
    print(gridsearchermpp.search())
    print("\nWithout MPP")
    gridsearchera = AStarSearcher(GridProblem(size))
    print(gridsearchera.search())
    print("\nWith MPP and a heuristic = 0 (Dijkstra's algorithm)")
    gridsearchermppnh = SearcherMPP(GridProblemNH(size))
    print(gridsearchermppnh.search())
    
