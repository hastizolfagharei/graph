from link import Link
from node import Node

class Graph:

    def __init__(self):
        self.node_counter = 0
        self.n_dict = {}
        self.l_dict = {}

    def add_node(self, input_node):
        self.n_dict[self.node_counter] = input_node
        self.node_counter += 1

    def delete_node(self, rem_node):
        pass



    def add_link(self, input_link):
        # add link to dict
        self.l_dict[(input_link.in_node_id, input_link.out_node_id)] = input_link

        # add nodes to degrees, which are connected to each other by this link
        self.n_dict[input_link.in_node_id].degrees.append(input_link.out_node_id)
        self.n_dict[input_link.out_node_id].degrees.append(input_link.in_node_id)

    def delete_link(self):
        pass
