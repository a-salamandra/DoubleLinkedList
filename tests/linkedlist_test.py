from LinkedList import LinkedList, DoubleLinkedList
import unittest


class LinkedListTest(unittest.TestCase):
    def test_creating_ll(self):
        list1 = LinkedList("test")
        list2 = LinkedList([1, 2, 3, 4, 5])
        list3 = LinkedList((1, 2, 3, 4, '5'))

        self.assertEqual("LinkedList(['t', 'e', 's', 't'])", repr(list1))
        self.assertEqual("LinkedList([1, 2, 3, 4, 5])", repr(list2))
        self.assertEqual("LinkedList([1, 2, 3, 4, '5'])", repr(list3))

        self.assertEqual("['t', 'e', 's', 't']", str(list1))
        self.assertEqual("[1, 2, 3, 4, 5]", str(list2))
        self.assertEqual("[1, 2, 3, 4, '5']", str(list3))

        somelist = LinkedList("d")
        self.assertEqual("['d']", str(somelist))

    def test_nodes(self):
        llist = LinkedList([1, 2, 3])
        first_node = llist.get_node_by_index(0)
        second_node = llist.get_node_by_index(1)
        third_node = llist.get_node_by_index(2)
        self.assertTrue(first_node.next is second_node)  # todo self.assertIs
        self.assertTrue(second_node.next is third_node)  # todo self.assertIs
        self.assertIsNone(third_node.next)

    def test_length(self):
        list_ll = [
            (LinkedList("qwerty"), 6),
            (LinkedList(), 0)
        ]
        for ll, len_ in list_ll:
            with self.subTest(list=ll, len=len_):
                self.assertEqual(len_, len(ll))

    def test_append(self):
        ll = LinkedList()
        ll.append(0)  # todo for
        ll.append(1)
        ll.append(0)
        self.assertEqual("[0, 1, 0]", str(ll))
        self.assertEqual(3, len(ll))

    def test_getitem(self):
        ll = LinkedList([0,1,2,3,4])
        self.assertEqual(0, ll[0])
        self.assertEqual(4, ll[4])

    def test_not_iterable(self):
        with self.assertRaises(TypeError) as e:
            ll = LinkedList(100)
        self.assertEqual("'int' object is not iterable", e.exception.args[0])

    def test_out_of_range_getitem(self):
        l = LinkedList("test")
        with self.assertRaises(IndexError) as e:
            a = l[100]
        self.assertEqual("index out of range", e.exception.args[0])

    def test_index_wrong_type_getitem(self):
        l = LinkedList("test")
        with self.assertRaises(TypeError) as e:
            a = l["100"]
        self.assertEqual("index must be an integer", e.exception.args[0])

    def test_set_value(self):
        ll = LinkedList([1, 2, 3])
        ll[0] = 9
        self.assertEqual("[9, 2, 3]", str(ll))
        ll[1] = 8
        self.assertEqual("[9, 8, 3]", str(ll))
        ll[2] = 7
        self.assertEqual("[9, 8, 7]", str(ll))

    def test_delete_node(self):
        ll1 = LinkedList(["X", 2, 3, 4, 5])
        ll2 = LinkedList([1, 2, "X", 4, 5])
        ll3 = LinkedList([1, 2, 3, 4, "X"])

        del ll1[0]
        self.assertEqual("[2, 3, 4, 5]", str(ll1))
        del (ll2[2])
        self.assertEqual("[1, 2, 4, 5]", str(ll2))
        del (ll3[4])
        self.assertEqual("[1, 2, 3, 4]", str(ll3))

        self.assertEqual(4, len(ll1))
        self.assertEqual(4, len(ll2))
        self.assertEqual(4, len(ll3))

        with self.assertRaises(IndexError) as e:
            del (ll3[10])
        self.assertEqual("index out of range", e.exception.args[0])

    def test_insert_node(self):
        llist = LinkedList([1, 2, 4, 5, 6])
        llist.insert(0,0)
        self.assertEqual("[0, 1, 2, 4, 5, 6]", str(llist))
        llist.insert(6, 7)
        self.assertEqual("[0, 1, 2, 4, 5, 6, 7]", str(llist))
        llist.insert(3, 3)
        self.assertEqual("[0, 1, 2, 3, 4, 5, 6, 7]", str(llist))
        self.assertEqual(8, len(llist))
        llist.insert(1000, 1000)
        self.assertEqual("[0, 1, 2, 3, 4, 5, 6, 7, 1000]", str(llist))
        with self.assertRaises(IndexError) as e:
            llist.insert(-10, 1000)
        self.assertEqual("index must be greater than zero", e.exception.args[0])

class DoubleLinkedListTest(unittest.TestCase):

    def test_creating_dll(self):

        list1 = DoubleLinkedList("test")
        list2 = DoubleLinkedList([1, 2, 3, 4, 5])
        list3 = DoubleLinkedList((1, 2, 3, 4, '5'))

        self.assertEqual("DoubleLinkedList(['t', 'e', 's', 't'])", repr(list1))
        self.assertEqual("DoubleLinkedList([1, 2, 3, 4, 5])", repr(list2))
        self.assertEqual("DoubleLinkedList([1, 2, 3, 4, '5'])", repr(list3))

        self.assertEqual("['t', 'e', 's', 't']", str(list1))
        self.assertEqual("[1, 2, 3, 4, 5]", str(list2))
        self.assertEqual("[1, 2, 3, 4, '5']", str(list3))

    def test_nodes(self):
        dllist = DoubleLinkedList(["a", "b", "c"])
        first_node = dllist.get_node_by_index(0)
        second_node = dllist.get_node_by_index(1)
        third_node = dllist.get_node_by_index(2)

        self.assertTrue(first_node.next is second_node)
        self.assertTrue(second_node.next is third_node)
        self.assertIsNone(third_node.next)

        self.assertIsNone(first_node.prev)
        self.assertTrue(second_node.prev is first_node)
        self.assertTrue(third_node.prev is second_node)

    def test_append(self):
        ll = DoubleLinkedList()
        ll.append(0)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        self.assertEqual("[0, 1, 0, 1]", str(ll))
        self.assertEqual(4, len(ll))

    def test_getitem(self):
        ll = DoubleLinkedList([0,1,2,3,4])
        self.assertEqual(0, ll[0])
        self.assertEqual(4, ll[4])

    def test_delete_node(self):
        ll1 = DoubleLinkedList(["X", 2, 3, 4, 5])
        ll2 = DoubleLinkedList([1, 2, "X", 4, 5])
        ll3 = DoubleLinkedList([1, 2, 3, 4, "X"])

        del (ll1[0])
        self.assertEqual("[2, 3, 4, 5]", str(ll1))
        del (ll2[2])
        self.assertEqual("[1, 2, 4, 5]", str(ll2))
        del (ll3[4])
        self.assertEqual("[1, 2, 3, 4]", str(ll3))

        self.assertEqual(4, len(ll1))
        self.assertEqual(4, len(ll2))
        self.assertEqual(4, len(ll3))

        with self.assertRaises(IndexError) as e:
            del (ll3[10])
        self.assertEqual("index out of range", e.exception.args[0])

    def test_insert_node(self):
        llist = DoubleLinkedList([1, 2, 4, 5, 6])
        llist.insert(0, 0)
        self.assertEqual("[0, 1, 2, 4, 5, 6]", str(llist))
        llist.insert(6, 7)
        self.assertEqual("[0, 1, 2, 4, 5, 6, 7]", str(llist))
        llist.insert(3, 3)
        self.assertEqual("[0, 1, 2, 3, 4, 5, 6, 7]", str(llist))
        self.assertEqual(8, len(llist))
        llist.insert(1000, 1000)
        self.assertEqual("[0, 1, 2, 3, 4, 5, 6, 7, 1000]", str(llist))
        self.assertEqual(9, len(llist))

        somelist = DoubleLinkedList()
        somelist.insert(0, "text")
        self.assertEqual("['text']", str(somelist))
        with self.assertRaises(IndexError) as e:
            somelist.insert(-10, 0)
        self.assertEqual("index must be greater than zero", e.exception.args[0])