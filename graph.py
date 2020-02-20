from link import Link
from node import Node


class Graph:
    # attributes of Graph class
    def __init__(self):
        self.node_counter = 0
        self.n_dict = {}
        self.l_dict = {}

    # methods:
    def add_node(self, input_node):
        self.n_dict[self.node_counter] = input_node
        self.n_dict[self.node_counter].id = self.node_counter
        self.node_counter += 1

    def delete_node(self, rem_node):
        # delete node from node dictionary
        node_info = self.n_dict.pop(rem_node)

        # sorting ids respectively
        for key in self.n_dict:
            if key > rem_node:
                self.n_dict[key - 1] = self.n_dict.pop(key)
                self.n_dict[key - 1].id = key - 1

        # delete links which are connected to this node
        degree = len(node_info.degree)
        for key in self.l_dict:
            if key[0] == rem_node or key[1] == rem_node:
                del self.l_dict[key]

        # check if connected nodes are single or not
        for degree in node_info.degrees:
            self.check_node(degree)

    # this method will check if a node is single or not
    def check_node(self, node):
        if len(self.n_dict[node].degrees) == 0:
            self.delete_node(node)

    def add_link(self, input_link):
        # add link to dict
        self.l_dict[(input_link.in_node_id, input_link.out_node_id)] = input_link

        # add nodes to degrees, which are connected to each other by this link
        self.n_dict[input_link.in_node_id].degrees.append(input_link.out_node_id)
        self.n_dict[input_link.out_node_id].degrees.append(input_link.in_node_id)

    def delete_link(self, link):
        # deleting degrees
        self.n_dict[link.in_node_id].degrees.remove(link.out_node_id)
        self.n_dict[link.out_node_id].degrees.remove(link.in_node_id)

        # check if in_node_id, out_node_id become single or not
        self.check_node(link.in_node_id)
        self.check_node(link.out_node_id)

        # delete link from link_dictionary
        for key in self.l_dict:
            if (key[0] == link.in_node_id and key[1] == link.out_node_id) or \
                    (key[0] == link.out_node_id and key[1] == link.in_node_id):
                del self.l_dict[key]

