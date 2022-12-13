
from collections import deque
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import count
from typing import Any


# Refactoring the Code Using a Mixin Class
class IterableMixin():
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

# Building a Queue Data Type
class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# Building a Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# Representing Priority Queues with a Heap
# Building a Priority Queue Data Type
# Handling Corner Cases in Your Priority Queue
class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]
    
@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value
