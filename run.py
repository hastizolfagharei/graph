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
    n3 = Node((54, 8))
    n4 = Node((54, 99))
    n5 = Node((65,13))

    l1 = Link(0, 1)
    l2 = Link(3, 4)
    l3 = Link(1, 3)
    l4 = Link(3, 2)

    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)

    g.add_link(l1)
    g.add_link(l2)
    g.add_link(l3)
    g.add_link(l4)

    print(n1.degrees)
    print(n2.location)
    print(n3.id)
    print(n4.id)
    print(n5.degrees)

    # print(g.node_counter)
    # print(g.n_dict)


if __name__ == '__main__':
    main()