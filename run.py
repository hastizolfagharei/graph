from link import Link
from graph import Graph
from node import Node


def main():
    # link = Link(1, 2)
    # print(link.out_node_id)
    g = Graph()
    g2 = Graph()
    n0 = Node((19, 4))
    n1 = Node((2, 44))
    n2 = Node((54, 8))
    n3 = Node((54, 99))
    n4 = Node((65, 13))

    l1 = Link(0, 1)
    l2 = Link(3, 4)
    l3 = Link(1, 3)
    l4 = Link(3, 2)
    l5 = Link(3, 0)
    l6 = Link(4, 2)
    l7 = Link(4, 0)
    l8 = Link(0, 2)
    l9 = Link(1, 4)

    g.add_node(n0)
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)

    g.add_link(l1)
    g.add_link(l2)
    g.add_link(l3)
    g.add_link(l4)
    g.add_link(l5)
    g.add_link(l6)
    g.add_link(l7)
    g.add_link(l8)
    g.add_link(l9)

    print(n0.degrees)
    print(n1.location)
    print(n2.id)
    print(n3.id)
    print(n4.degrees)

    g.delete_link(l8)

    # print(g.node_counter)
    # print(g.n_dict)


if __name__ == '__main__':
    main()
