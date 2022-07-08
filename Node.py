from typing import Any, Optional

class Node:

    def __init__(self, value_: Any, next_: Optional["Node"] = None) -> None:
        self._value = value_
        self.next = next_

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError("passed node should be either None or Node")

    def __str__(self) -> str:
        return f"{self._value}"

    def __repr__(self) -> str:
        return f"Node({self._value}, None)" if self.next is None else f"Node({self._value}, Node({self.next}))"


class DoubleLinkedNode(Node):

    def __init__(self, value_: Any, next_: Optional["Node"] = None, prev_: Optional["Node"] = None) -> None:
        super().__init__(value_, next_)
        self.prev = prev_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.is_valid(prev_)
        self._prev = prev_

    def __repr__(self) -> str:
        next_node_repr = f"DoubleLinkedNode({self.next._value}, None, None)" if self.next else "None"
        prev_node_repr = f"DoubleLinkedNode({self.prev._value}, None, None)" if self.prev else "None"
        return f"DoubleLinkedNode({self._value}, {next_node_repr}, {prev_node_repr})"
