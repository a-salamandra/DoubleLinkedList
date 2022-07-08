from collections.abc import MutableSequence
from typing import Iterable, Optional, Any

from Node import Node, DoubleLinkedNode

class LinkedList(MutableSequence):
    node_type = Node

    def __init__(self, data: Iterable = None):
        self._length = 0
        self._head = None
        self._tail = None

        if data is not None:
            for item in data:
                self.append(item)

    def append(self, value: Any) -> None:
        append_node = self.node_type(value)

        if self._length == 0:
            self._head = append_node
        else:
            self.link_nodes(self._tail, append_node)

        self._length += 1
        self._tail = append_node

    @staticmethod
    def link_nodes(left_node: Node, right_node: Node) -> None:
        left_node.next = right_node

    def get_node_by_index(self, index: int) -> Node:

        self.validate_index(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        node = self.get_node_by_index(index)
        return node._value

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.get_node_by_index(index)
        node._value = value

    def __delitem__(self, key: int) -> None:

        self.validate_index(key)

        if key == 0:
            self._head = self._head.next
        elif key == self._length - 1:
            new_tail = self.get_node_by_index(key - 1)
            new_tail.next = None
            self._tail = new_tail
        else:
            previous_node = self.get_node_by_index(key - 1)
            deleted_node = self.get_node_by_index(key)
            self.link_nodes(previous_node, deleted_node.next)

        self._length -= 1

    def insert(self, index: int, data: Any) -> None:

        self.validate_index(index, out_of_range_allowed=True)

        if self._length == 0:
            self.append(data)
            return

        inserted_node = self.node_type(data)

        if index == 0:
            head_node = self._head
            self.link_nodes(inserted_node, head_node)
            self._head = inserted_node
        elif index >= self._length:
            self.append(data)
            return
        else:
            prev_node = self.get_node_by_index(index - 1)
            next_node = self.get_node_by_index(index)

            self.link_nodes(prev_node, inserted_node)
            self.link_nodes(inserted_node, next_node)

        self._length += 1

    def __str__(self) -> str:
        return f"{[i for i in self]}"

    def __repr__(self) -> str:
         return f"{self.__class__.__name__}({[i for i in self]})"

    def __len__(self) -> int:
        return self._length

    def validate_index(self, index: int, out_of_range_allowed = False) -> None:

        if not isinstance(index, int):
            raise TypeError("index must be an integer")

        if index < 0:
            raise IndexError("index must be greater than zero")

        if index >= self._length and out_of_range_allowed == False:
            raise IndexError("index out of range")


class DoubleLinkedList(LinkedList):

    node_type = DoubleLinkedNode

    def __init__(self, data: Iterable = None):
        super().__init__(data)

    @staticmethod
    def link_nodes(left_node: DoubleLinkedNode, right_node: DoubleLinkedNode) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def __delitem__(self, key: int) -> None:

        self.validate_index(key)

        if key == 0:
            self._head = self._head.next
            self._head.prev = None
        elif key == self._length - 1:
            new_tail = self.get_node_by_index(key - 1)
            new_tail.next = None
            self._tail.prev = None
            self._tail = new_tail
        else:
            previous_node = self.get_node_by_index(key - 1)
            deleted_node = self.get_node_by_index(key)
            self.link_nodes(previous_node, deleted_node.next)

        self._length -= 1