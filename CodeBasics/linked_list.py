class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # Accepted
        # new_node = Node(data, self.head)
        # self.head = new_node
        if self.head is None:
            new_node = Node(data, None)
            self.head = new_node
            return
        new_node = Node(data, self.head)
        self.head = new_node

    def print(self):
        iterator = self.head
        linked_list_string = ''
        while iterator:
            linked_list_string += str(iterator.data)
            linked_list_string += ' ---> '

            iterator = iterator.pointer
        print(linked_list_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        iterator = self.head
        # Accepted
        # while itr.pointer:
        #     itr = itr.pointer
        #
        # itr.pointer = Node(data, None)

        while True:
            if iterator.pointer is None:
                new_node = Node(data, None)
                iterator.pointer = new_node
                return

            iterator = iterator.pointer

    def length_of_linked_list(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.pointer

        return count

    def insert_at_index(self, index, data):
        self.check_out_of_bounds(index)

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.length_of_linked_list():
            self.insert_at_end(data)
            return
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                new_node = Node(data, iterator.pointer)
                iterator.pointer = new_node
                return
            iterator = iterator.pointer
            count += 1

    def check_out_of_bounds(self, index):
        if index < 0 or index > self.length_of_linked_list():
            raise Exception("out of bounds")
        return

    def remove_from_start(self):
        self.head = self.head.pointer

    def remove_from_end(self):
        iterator = self.head
        count = 0
        while iterator:
            if count == self.length_of_linked_list() - 2:
                iterator.pointer = None
                return
            count += 1
            iterator = iterator.pointer

    def remove_at_index(self, index):
        self.check_out_of_bounds(index)

        if index == 0:
            self.remove_from_start()
            return
        if index == self.length_of_linked_list() - 1:
            self.remove_from_end()

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.pointer = iterator.pointer.pointer
                return

            count += 1
            iterator = iterator.pointer

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    # def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node\

    def insert_after_value(self, value, data):
        iterator = self.head
        while iterator:
            if iterator.data == value:
                new_node = Node(data, iterator.pointer)
                iterator.pointer = new_node
                return
            iterator = iterator.pointer

    # def remove_by_value(self, data):
    # Remove first node that contains data
    def remove_by_value(self, data):
        iterator = self.head

        if iterator.data == data:
            self.head = iterator.pointer
            return
        while iterator:
            if iterator.pointer.data == data:
                iterator.pointer = iterator.pointer.pointer
                return
            iterator = iterator.pointer


if __name__ == '__main__':
    linked = LinkedList()

    print('Linked List()')
    linked.print()

    print('Linked List().insert_at_beginning(2)')
    linked.insert_at_beginning(2)
    linked.print()

    print('Linked List().insert_at_beginning(10)')
    linked.insert_at_beginning(10)
    linked.print()

    print('Linked List().insert_at_end(5)')
    linked.insert_at_end(5)
    linked.print()

    print('Linked List().insert_at_end(100)')
    linked.insert_at_end(100)
    linked.print()

    print('Linked List().insert_at_beginning(200)')
    linked.insert_at_beginning(200)
    linked.print()

    print('Linked List().insert_at_index(5, 30)')
    linked.insert_at_index(5, 30)
    linked.print()

    # linked.insert_at_index(100, 30) Exception!!
    print('Linked List().remove_from_start()')
    linked.remove_from_start()
    linked.print()

    print('Linked List().remove_from_end()')
    linked.remove_from_end()
    linked.print()

    print('Linked List().remove_at_index(2)')
    linked.remove_at_index(2)

    print('Linked List().insert_vales([1, 2, 3, 4, 5])')
    linked.insert_values([1, 2, 3, 4, 5])
    linked.print()

    print('Linked List().insert_after_value(2,9)')
    linked.insert_after_value(100, 9)
    linked.print()

    print('Linked List().remove_by_value(9)')
    linked.remove_by_value(10)
    linked.print()

    print('Length', linked.length_of_linked_list())
    linked.print()

    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
