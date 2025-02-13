import random
from agents import Agent, Environment, Simulate
from utilities import select_from_dist

class TP_env(Environment):
    sd = 5
    price_delta = [0, 0, 0, 21, 0, 20, 0, -64, 0, 0, 23, 0, 0, 0, -35,
       0, 76, 0, -41, 0, 0, 0, 21, 0, 5, 0, 5, 0, 0, 0, 5, 0, -15, 0, 5,
       0, 5, 0, -115, 0, 115, 0, 5, 0, -15, 0, 5, 0, 5, 0, 0, 0, 5, 0,
       -59, 0, 44, 0, 5, 0, 5, 0, 0, 0, 5, 0, -65, 50, 0, 5, 0, 5, 0, 0,
       0, 5, 0] 

    def __init__(self):
        """paper buying agent"""
        self.time = 0
        self.stock = 20
        self.stock_history = []
        self.price_history = []

    def initial_percept(self):
        self.price = round(234 + self.sd * random.gauss(0, 1))
        self.price_history.append(self.price)
        self.stock_history.append(self.stock)
        return {'price': self.price, 'stock': self.stock}

    def do(self, action):
        self.time += 1
        
        used = select_from_dist({6:0.1, 5:0.1, 4:0.1, 3:0.3, 2:0.2, 1:0.2})
        self.stock = self.stock - used
        self.stock_history.append(self.stock)

        self.price = round(self.price
                        + self.price_delta[self.time%len(self.price_delta)]
                        + self.sd*random.gauss(0,1))
        self.price_history.append(self.price)
        return {'price': self.price, 'stock': self.stock}
    

class TP_agent(Agent):
    def select_action(self, percept):
        self.price = percept['price']
        self.stock = percept['stock']
        
        tobuy = 0
        return {'buy': tobuy}

if __name__ == "__main__":
    env = TP_env()
    ag = TP_agent()
    sim = Simulate(ag, env)
    sim.go(20)
