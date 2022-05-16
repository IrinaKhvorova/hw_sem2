import unittest
import t4_list_stack_queue as t4


class LinkedListTest(unittest.TestCase):
    def test_empty_len(self):
        self.llist = t4.LinkedList()
        self.assertEqual(0, len(self.llist))

    def test_empty_repr(self):
        self.llist = t4.LinkedList()
        self.assertEqual("[]", str(self.llist))

    def test_add(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.assertEqual("[0]", str(self.llist))

    def test_nonempty_repr(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1)
        self.assertEqual("[0, 1]", str(self.llist))

    def test_len(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1)
        self.llist.add(2)
        self.assertEqual(3, len(self.llist))

    def test_add_by_index(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1, 0)
        self.llist.add(2, 2)
        self.assertEqual("[1, 0, 2]", str(self.llist))

    def test_add_by_incorrect_index(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)

        with self.assertRaises(IndexError):
            self.llist.add(1, 6)

    def test_add_to_empty_by_incorrect_index(self):
        self.llist = t4.LinkedList()
        with self.assertRaises(IndexError):
            self.llist.add(1, 6)

    def test_remove(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1)
        self.llist.add(2)
        self.llist.remove()
        self.assertEqual("[0, 1]", str(self.llist))

    def test_remove_by_index(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1)
        self.llist.add(2)
        self.llist.remove(1)
        self.assertEqual("[0, 2]", str(self.llist))

    def test_remove_without_index(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1)
        self.llist.add(2)
        self.llist.remove()
        self.assertEqual("[0, 1]", str(self.llist))

    def test_remove_one_element_list(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.remove()
        self.assertEqual("[]", str(self.llist))

    def test_remove_by_incorrect_index(self):
        self.llist = t4.LinkedList()
        self.llist.add(0)
        self.llist.add(1)
        self.llist.add(2)
        with self.assertRaises(IndexError):
            self.llist.remove(10)

    def test_remove_from_empty(self):
        self.llist = t4.LinkedList()
        with self.assertRaises(IndexError):
            self.llist.remove(1)


class StackTest(unittest.TestCase):
    def test_empty_len(self):
        self.stack = t4.Stack()
        self.assertEqual(0, len(self.stack))

    def test_empty_repr(self):
        self.stack = t4.Stack()
        self.assertEqual("[]", str(self.stack))

    def test_push(self):
        self.stack = t4.Stack()
        self.stack.push(0)
        self.stack.push(1)
        self.assertEqual(2, len(self.stack))

    def test_pull(self):
        self.stack = t4.Stack()
        self.stack.push(0)
        self.stack.push(1)
        self.assertEqual(1, self.stack.pull())

    def test_len(self):
        self.stack = t4.Stack()
        self.stack.push(0)
        self.stack.push(1)
        self.stack.pull()
        self.assertEqual(1, len(self.stack))


class QueueTest(unittest.TestCase):
    def test_empty_len(self):
        self.queue = t4.Queue()
        self.assertEqual(0, len(self.queue))

    def test_empty_repr(self):
        self.queue = t4.Queue()
        self.assertEqual("[]", str(self.queue))

    def test_push(self):
        self.queue = t4.Queue()
        self.queue.push(0)
        self.queue.push(1)
        self.assertEqual(2, len(self.queue))

    def test_pull(self):
        self.queue = t4.Queue()
        self.queue.push(0)
        self.queue.push(1)
        self.assertEqual(0, self.queue.pull())

    def test_len(self):
        self.queue = t4.Queue()
        self.queue.push(0)
        self.queue.push(1)
        self.queue.pull()
        self.assertEqual(1, len(self.queue))


if __name__ == '__main__':
    unittest.main()