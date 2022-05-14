class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):  # чтобы можно было красиво вывести
        node = self.head
        nodes = []  # для значений связанного списка
        if self.head is None:
            return 'None'
        while node is not None:
            nodes.append(str(node.data))  # добавляем значения связанного списка
            node = node.next
        #nodes.append('None')  # для конца списка или при нулевом связанном списке
        return "->".join(nodes)

    def __iter__(self):  # итерация по связанному списку
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def add(self, item, index=None):  # вставка
        node = Node(item)
        if self.head is None:   # если список пустой
            if index == 0 or index is None:
                self.head = node
            else:
                raise ValueError("Wrong index")
        elif index == 0:        # вставка в начало списка
            node.next = self.head
            self.head = node
        else:                   # вставка по индексу
            current_node = self.head
            i = 1
            while (index is None or i < index) and current_node.next is not None:
                current_node = current_node.next
                i += 1
            if index is not None and i < index and current_node.next is None:
                raise ValueError("Wrong index")
            node.next = current_node.next
            current_node.next = node

    def remove(self, index=None):
        if self.head is None:   # если список пустой
            raise ValueError("Linked list is empty")
        elif index == 0:        # удаление первого элемента
            self.head = self.head.next
        elif index is None and self.head.next is None:
            self.head = None
        else:                   # вставка по индексу
            previous_node = self.head
            i = 0
            for node in self:
                if i == index:
                    previous_node.next = node.next
                if index is None and node.next is None:
                    previous_node.next = None
                i += 1
                previous_node = node


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def __len__(self):
        return self.items.__len__()

    def __repr__(self):
        return self.items.__repr__()

    def push(self, item):
        self.items.add(item, 0)

    def pull(self):
        self.items.remove(0)


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def __repr__(self):
        return self.items.__repr__()

    def __len__(self):
        return self.items.__len__()

    def push(self, item):
        self.items.add(item, 0)

    def pull(self):
        return self.items.remove()



# llist = LinkedList()
# print(len(llist))
# print(llist)
# llist.add(1)
# print(llist)
# # llist.add(2)
# # print(llist)
# llist.remove()
# print(llist)


q = Queue()
print(q)
print(len(q))
q.push(4)
q.push(3)
print(q)
print(len(q))
q.pull()
print(q)


# st = Stack([1, 2, 3])
# print(st)
# print(len(st))
# st.push(4)
# print(st)
# print(len(st))
# st.pull()
# print(st)


# llist = LinkedList([1, 2, 3, 4, 5, 6])
# print(len(llist))
# llist.remove(0)
# print(llist)
# llist.remove()
# print(llist)
# llist.remove(2)
# print(llist)

# for node in llist:
#     print(node)
# print(llist)
# llist.add(0)
# print(llist)
# try:
#     llist.add(4, 8)
#     print(llist)
# except Exception as e:
#     print(e)
# llist.add(5, 2)
# print(llist)
# llist.add(6, 0)
# print(llist)
# llist.add(7)
# print(llist)
# llist.add_first(Node("0"))
# print(llist)
# llist.add_last(Node("f"))
# llist.add_after("c", Node("ccc"))
# llist.add_before("c", Node("cc"))
# print(llist)
# llist.remove("cc")
# print(llist)
# llist.add_after("c", Node("cc"))
# print(llist)

# st = Stack([1, 3, 4, 2])
# st.push(6)
# print(st)
# st.pull()
# print(st)
# st.pull()
# st.pull()
# print(len(st))
# print(st.is_empty())
# print(st.peek())

# q = Queue([1, 2, 3])
# print(q)
# q.push(7)
# print(q)
# q.pull()
# print(q)
# print(q.peek())
# print(len(q))
