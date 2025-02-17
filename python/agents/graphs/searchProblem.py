import matplotlib.pyplot as plt
import random

class Search_problem(object):
    def start_node(self):
        raise NotImplementedError("start_node must be implemented")
    def is_goal(self, node):
        raise NotImplementedError("is_goal must be implemented")
    def neighbors(self, node):
        raise NotImplementedError("neighbors must be implemented")
    def heuristic(self, node):
        return 0

class Arc(object):
    def __init__(self, from_node, to_node, cost=1, action=None):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost
        self.action = action

    def __repr__(self):
        if self.action:
            return f"{self.from_node} --{self.action}--> {self.to_node}"
        else:
            return f"{self.from_node} --> {self.to_node}"

class Search_problem_from_explicit_graph(Search_problem):
    def __init__(self, title, nodes, arcs, start=None, goals=set(), hmap={}, positions=None):
        """Initializes a search problem from an explicit graph.
        - nodes is a set of nodes
        - arcs is a sequence of pairs of nodes
        - start is a node
        - goals is a set of nodes
        - hmap is a heuristic map
        - positions is a dictionary of node positions
        """

        self.title = title
        self.neighs = {}
        self.nodes = nodes
        for node in nodes:
            self.neighs[node]=[]
        self.arcs = arcs
        for arc in arcs:
            self.neighs[arc.from_node].append(arc)
        self.start = start
        self.goals = goals
        self.hmap = hmap
        if positions is None:
            self.positions = {node:(random.random(),random.random()) for node in nodes}
        else:
            self.positions = positions

    def start_node(self):
        """returns start node"""
        return self.start
    
    def is_goal(self,node):
        """is True if node is a goal"""
        return node in self.goals

    def neighbors(self,node):
        """returns the neighbors of node (a list of arcs)"""
        return self.neighs[node]

    def heuristic(self,node):
        """Gives the heuristic value of node n.
        Returns 0 if not overridden in the hmap."""
        if node in self.hmap:
            return self.hmap[node]
        else:
            return 0
        
    def __repr__(self):
        """returns a string representation of the search problem"""
        res=""
        for arc in self.arcs:
            res += f"{arc}.  "
        return res

    def show(self, fontsize=10, node_color='orange', show_costs = True):
        """Show the graph as a figure
        """
        self.fontsize = fontsize
        self.show_costs = show_costs
        plt.ion()   # interactive
        ax = plt.figure().gca()
        ax.set_axis_off()
        plt.title(self.title, fontsize=fontsize)
        self.show_graph(ax, node_color)
        plt.savefig('search_problem.png')

    def show_graph(self, ax, node_color='orange'): 
        bbox = dict(boxstyle="round4,pad=1.0,rounding_size=0.5",facecolor=node_color)
        for arc in self.arcs:
            self.show_arc(ax, arc)
        for node in self.nodes:
            self.show_node(ax, node, node_color = node_color)

    def show_node(self, ax, node, node_color):
            x,y = self.positions[node]
            ax.text(x,y,node,bbox=dict(boxstyle="round4,pad=1.0,rounding_size=0.5",
                                    facecolor=node_color),
                        ha='center',va='center', fontsize=self.fontsize)
        
    def show_arc(self, ax, arc, arc_color='black', node_color='white'):
            from_pos = self.positions[arc.from_node]
            to_pos = self.positions[arc.to_node]
            ax.annotate(arc.to_node, from_pos, xytext=to_pos,
                        arrowprops={'arrowstyle':'<|-', 'linewidth': 2,
                                            'color':arc_color},
                        bbox=dict(boxstyle="round4,pad=1.0,rounding_size=0.5",
                                                 facecolor=node_color),
                                ha='center',va='center',
                                fontsize=self.fontsize)
            # Add costs to middle of arcs:
            if self.show_costs:
                ax.text((from_pos[0]+to_pos[0])/2, (from_pos[1]+to_pos[1])/2,
                         arc.cost, bbox=dict(pad=1,fc='w',ec='w'),
                         ha='center',va='center',fontsize=self.fontsize)

class Path(object):
    """A path is either a node or a path followed by an arc"""
    
    def __init__(self,initial,arc=None):
        """initial is either a node (in which case arc is None) or
        a path (in which case arc is an object of type Arc)"""
        self.initial = initial
        self.arc=arc
        if arc is None:
            self.cost=0
        else:
            self.cost = initial.cost+arc.cost

    def end(self):
        """returns the node at the end of the path"""
        if self.arc is None:
            return self.initial
        else:
            return self.arc.to_node

    def nodes(self):
        """enumerates the nodes of the path from the last element backwards
        """
        current = self
        while current.arc is not None:
            yield current.arc.to_node
            current = current.initial
        yield current.initial

    def initial_nodes(self):
        """enumerates the nodes for the path before the end node.
        This calls nodes() for the initial part of the path.
        """
        if self.arc is not None:
            yield from self.initial.nodes()
        
    def __repr__(self):
        """returns a string representation of a path"""
        if self.arc is None:
            return str(self.initial)
        elif self.arc.action:
            return f"{self.initial}\n   --{self.arc.action}--> {self.arc.to_node}"
        else:
            return f"{self.initial} --> {self.arc.to_node}"
