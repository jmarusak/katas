from variable import Variable

class Constraint(object):
    """
    A constraint is a relation between variables.

    :param scope: a tuple or list of variables
    :param condition: a Boolean function
    :param string: a string for printing the constraint
    """
    def __init__(self, scope, condition, string=None, position=None):
        self.scope = scope
        self.condition = condition
        self.string = string
        self.position = position
