import unittest

from Node import Node, DoubleLinkedNode


class NodeTest(unittest.TestCase):
    def test_create_nodes(self):
        node = Node("some text", None)
        another_node = Node("more text", node)
        node.next = another_node
        self.assertEqual(node.next, another_node)  # todo assertIs
        self.assertEqual(another_node.next, node)  # todo assertIs

    def test_node_str(self):
        node1 = Node("one")
        node2 = Node("two")
        self.assertEqual("one", str(node1))
        self.assertEqual("two", str(node2))

    def test_node_repr(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertEqual("Node(1, Node(2))", repr(node1))
        self.assertEqual("Node(2, None)", repr(node2))

    def test_not_instance_node(self):
        node1 = Node(1)
        node2 = "not a node"
        with self.assertRaises(TypeError) as e:
            node1.next = node2
        self.assertEqual("passed node should be either None or Node", e.exception.args[0])  # todo str(e)


class DoubleLinkedNodeTest(unittest.TestCase):

    def test_create_nodes(self):
        first_node = DoubleLinkedNode("text")
        middle_node = DoubleLinkedNode("more text")
        last_node = DoubleLinkedNode("even more text")

        first_node.next = middle_node
        middle_node.next, middle_node.prev = last_node, first_node
        last_node.prev = middle_node

        self.assertIsNone(first_node.prev)
        self.assertEqual(first_node.next, middle_node)

        self.assertEqual(middle_node.prev, first_node)
        self.assertEqual(middle_node.next, last_node)

        self.assertEqual(last_node.prev, middle_node)
        self.assertIsNone(last_node.next)

    def test_dln_str(self):
        node = DoubleLinkedNode("text")
        self.assertEqual("text", str(node))

    def test_dln_repr(self):
        node1 = DoubleLinkedNode(1)
        node2 = DoubleLinkedNode(2)
        node3 = DoubleLinkedNode(3)

        # no next, no prev
        self.assertEqual("DoubleLinkedNode(1, None, None)", repr(node1))

        # next without prev
        node1.next = node2
        self.assertEqual("DoubleLinkedNode(1, DoubleLinkedNode(2, None, None), None)", repr(node1))

        # prev without next
        node2.prev = node1
        self.assertEqual("DoubleLinkedNode(2, None, DoubleLinkedNode(1, None, None))", repr(node2))

        #with next and prev
        node2.next = node3
        self.assertEqual("DoubleLinkedNode(2, DoubleLinkedNode(3, None, None), DoubleLinkedNode(1, None, None))", repr(node2))

    def test_not_instance_dl_node(self):
        node = DoubleLinkedNode("data")
        not_a_node = "not a node"
        not_a_dl_node = Node(0)

        with self.assertRaises(TypeError) as e1:
            node.next = not_a_node
        self.assertEqual("passed node should be either None or Node", e1.exception.args[0])

        with self.assertRaises(TypeError) as e2:
            node.next = not_a_dl_node
        self.assertEqual("passed node should be either None or Node", e2.exception.args[0])
