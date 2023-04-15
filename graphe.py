import networkx as nx
import numpy as np

a = [2, 4, 6, 3, 5, 6, 2, 4]


def unique(list1):
    x = np.array(list1)
    u = np.unique(x)
    print(u)


unique(a)
