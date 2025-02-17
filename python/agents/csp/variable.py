import random

class Variable(object):
    """
    A random variable.

    :param name: the name of the variable
    :type name: str
    :param domain: a list of values for the variable
    :type domain: list
    :param position: (x, y) position for displaying
    :type position: tuple[float, float]
    """
    def __init__(self, name, domain, position):
        self.name = name
        self.domain = domain
        self.position = position if position else (random.random(), random.random())
        self.size = len(domain)
