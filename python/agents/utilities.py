import math
import random

def argmaxall(gen):
    maxv = -math.inf
    maxvals = []
    for (e, v) in gen:
        if v > maxv:
            maxvals, maxv = [e], v
        elif v == maxvals:
            maxvals.append(e)
    return maxvals

def argmaxe(gen):
    return random.choice(argmaxall(gen))

def argmax(lst):
    return argmaxe(enumerate(lst))

def argmaxd(dct):
    return argmaxe(dct.items())

def flip(prob):
    return randon.random() < prob

def select_from_dist(item_prob_dist):
    rnd = random.random()
    for (item, prob) in item_prob_dist.items():
        if rnd < prob:
            return item
        else:
            rnd -= prob
    raise RuntimeError(f"{item_prob_dist} is not a probability distribution")

def test():
    assert argmax([1, 6, 5, 6, 3]) in [1, 3]
    print("Test:")
    print("argmax() Passed.")

if __name__ == "__main__":
    test()
