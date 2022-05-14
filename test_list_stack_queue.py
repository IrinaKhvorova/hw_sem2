import unittest
import t4_list_stack_queue as t4

class MyLinkedListCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 15

    def test_add(self):
        r = t4.LinkedList.add(1, 0)
        self.assertEqual(1, r)

    def test_remove(self):
        r = t4.LinkedList.remove()
        self.assertEqual()



if __name__ == '__main__':
    unittest.main()
