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
        node_info = self.n_dict.pop(rem_node.id)

        # check if connected nodes are single or not
        key_list = []
        for degree in node_info.degrees:
            len_deg = len(self.n_dict[degree].degrees)
            if len_deg == 0 :
                key_list.append(self.n_dict[degree])

        self.delete_isolated_nodes(key_list)

        # delete links which are connected to this node
        for key in self.l_dict:
            if key[0] == rem_node or key[1] == rem_node:
                del self.l_dict[key]

        # sorting ids respectively
        ex_dict = {}
        for key in self.n_dict.copy():
            if key > rem_node.id:
                ex_dict[key] = self.n_dict.pop(key)
        for key in ex_dict:
            self.n_dict[key - 1] = ex_dict[key]

    def delete_isolated_nodes(self, key_list):
        for key in key_list:
            self.n_dict[key].pop()

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
        if len(self.n_dict[link.in_node_id].degrees) == 0:
            self.n_dict.pop(link.in_node_id)
        if len(self.n_dict[link.out_node_id].degrees) == 0:
            self.n_dict.pop(link.out_node_id)

        # delete link from link_dictionary
        l = None
        for key in self.l_dict:
            if (key[0] == link.in_node_id and key[1] == link.out_node_id) or (key[0] == link.out_node_id and key[1] == link.in_node_id) :
                l = key
        del self.l_dict[l]


