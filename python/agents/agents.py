from display import Displayable

class Agent(Displayable):
    def initial_action(self, percept):
        return self.select_action(percept)

    def select_action(self, percept):
        raise NotImplementedError("select_action")

class Environment(Displayable):
    def initial_percept(self):
        raise NotImplementedError("initial_percept")

    def do(self, action):
        raise NotImplementedError("Environment.go")

class Simulate(Displayable):
    def __init__(self, agent, env):
        self.agent = agent
        self.env = env
        self.percept = self.env.initial_percept()
        self.percept_history = [self.percept]
        self.action_history = []

    def go(self, n):
        for i in range(n):
            action = self.agent.select_action(self.percept)
            self.display(2, f"i={i} action={action}")
            self.percept = self.env.do(action)
            self.display(2, f"    percept={self.percept}")
