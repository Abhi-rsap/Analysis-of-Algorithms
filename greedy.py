import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def find_max(sorted_degree):
    max_degree = 0
    for degree in sorted_degree:
        if max_degree < degree:
            max_degree = degree
    return max_degree


def approximation_greedy_vc(g):

    v = nx.number_of_nodes(g)
    e = nx.number_of_edges(g)

    edge_set = set()
    vertex_set = set()
    degree_of_node = dict({})

    for node in nx.nodes(g):
        deg = nx.degree(g, node)
        if deg in degree_of_node:
            degree_of_node[deg].append(node)
        else:
            degree_of_node[deg] = [node]
            

    """
    for key in degree_of_node:
        print ("degree %d : " % key)
        for node in degree_of_node[key]:
            print ",", node
    """

    sorted_degree = [0]
    for i in range(1, v + 1):
        sorted_degree.append(nx.degree(g, i))
        # print 'node ', i
        # print 'degree', sorted_degree[i]

    while len(edge_set) != 2 * e:
        current_max = find_max(sorted_degree)
        if degree_of_node[current_max] is None or len(degree_of_node[current_max]) == 0:
            current_max -= 1
            continue
        nodes_with_current_degree = degree_of_node[current_max]
        random_choice = random.randint(0, len(nodes_with_current_degree) - 1)   # [0, len-1]
        chosen_node = nodes_with_current_degree[random_choice]

        vertex_set.add(chosen_node)
        for neighbor in nx.all_neighbors(g, chosen_node):
            if neighbor not in vertex_set:
                edge_set.update([(chosen_node, neighbor), (neighbor, chosen_node)])
                degree_of_node[sorted_degree[neighbor]].remove(neighbor)  # remove
                sorted_degree[neighbor] -= 1
                if sorted_degree[neighbor] not in degree_of_node:
                    degree_of_node[sorted_degree[neighbor]] = []
                degree_of_node[sorted_degree[neighbor]].append(neighbor)  # add

        degree_of_node[current_max].remove(chosen_node)
        sorted_degree[chosen_node] = 0

    return vertex_set


def text_and_run(g):
    start = time.time()
    vertex_cover = approximation_greedy_vc(g)
    end = time.time()
    print ("time is %f" % (end - start))
    return vertex_cover

# print("gg",g.nodes())
# text_and_run(g)






