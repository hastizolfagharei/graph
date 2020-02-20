from link import Link
from graph import Graph
from node import Node

def main():
    # link = Link(1, 2)
    # print(link.out_node_id)
    g = Graph()
    g2 = Graph()
    n1 = Node((19, 4))
    n2 = Node((2, 44))

    l1 = Link(0, 1)

    g.add_node(n1)
    g.add_node(n2)
    g.add_link(l1)
    print(n1.degrees)
    print(n2.degrees)
    # print(g.node_counter)
    # print(g.n_dict)


if __name__ == '__main__':
    main()