class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = new_node
            return
        new_node = Node(data, self.head, None)
        self.head.prev = new_node
        self.head = new_node

    # def print_forward(self):
    # This method prints list in forward direction. Use node.next

    def print_forward(self):
        iterator = self.head
        linked_list_string = ''
        while iterator:
            linked_list_string += str(iterator.data)
            linked_list_string += '---->'
            iterator = iterator.next
        print(linked_list_string)

    # def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.

    def print_backward(self):
        iterator = self.head
        linked_list_string = ''

        # Just printing

        while iterator:
            linked_list_string = '<---' + str(iterator.data) + linked_list_string
            iterator = iterator.next

        # while iterator.next:
        #     iterator = iterator.next
        # while iterator:
        #     linked_list_string += str(iterator.data)
        #     linked_list_string += '--->'
        #     iterator = iterator.prev
        print(linked_list_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        iterator = self.head
        while True:
            if iterator.next is None:
                new_node = Node(data, None, iterator)
                iterator.next = new_node
                return

            iterator = iterator.next

    def length_of_linked_list(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next

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
                new_node = Node(data, iterator.next, iterator)
                iterator.next.prev = new_node
                iterator.next = new_node
                return
            iterator = iterator.next
            count += 1

    def check_out_of_bounds(self, index):
        if index < 0 or index > self.length_of_linked_list():
            raise Exception("out of bounds")
        return

    def remove_from_start(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def remove_from_end(self):
        iterator = self.head
        count = 0
        while iterator:
            if count == self.length_of_linked_list() - 2:
                iterator.next.prev = None
                iterator.next = None
                return
            count += 1
            iterator = iterator.next

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
                # iterator.next.next.prev = iterator
                # Works if executed before next statement, (changing iterator.next) !!
                iterator.next = iterator.next.next
                iterator.next.prev = iterator
                return

            count += 1
            iterator = iterator.next

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
                new_node = Node(data, iterator.next, iterator)
                iterator.next.prev = new_node
                iterator.next = new_node
                return
            iterator = iterator.next

    # def remove_by_value(self, data):
    # Remove first node that contains data

    def remove_by_value(self, data):
        iterator = self.head

        if iterator.data == data:
            self.remove_from_start()
            return
        while iterator:
            if iterator.next and iterator.next.data == data:
                iterator.next = iterator.next.next
                if iterator.next:
                    iterator.next.prev = iterator
                return
            iterator = iterator.next


if __name__ == '__main__':
    doubly_linked = DoublyLinkedList()

    print('Doubly Linked List()')
    doubly_linked.print_forward()

    print('Doubly Linked List().insert_at_beginning(2)')
    doubly_linked.insert_at_beginning(2)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_at_beginning(10)')
    doubly_linked.insert_at_beginning(10)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_at_end(5)')
    doubly_linked.insert_at_end(5)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_at_end(100)')
    doubly_linked.insert_at_end(100)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_at_beginning(200)')
    doubly_linked.insert_at_beginning(200)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_at_index(5, 30)')
    doubly_linked.insert_at_index(2, 30)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    #
    # # linked.insert_at_index(100, 30) Exception!!

    print('Doubly Linked List().remove_from_start()')
    doubly_linked.remove_from_start()
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().remove_from_end()')
    doubly_linked.remove_from_end()
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().remove_at_index(2)')
    doubly_linked.remove_at_index(2)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_vales([1, 2, 3, 4, 5])')
    doubly_linked.insert_values([1, 2, 3, 4, 5])
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().insert_after_value(2,9)')
    doubly_linked.insert_after_value(2, 9)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Doubly Linked List().remove_by_value(9)')
    doubly_linked.remove_by_value(9)
    doubly_linked.print_forward()
    doubly_linked.print_backward()

    print('Length', doubly_linked.length_of_linked_list())
    doubly_linked.print_forward()

    #
    dll = DoublyLinkedList()
    dll.insert_values(["banana", "mango", "grapes", "orange"])
    dll.print_forward()
    dll.print_backward()
    dll.insert_after_value("mango", "apple")  # insert apple after mango
    dll.print_forward()
    dll.print_backward()
    dll.remove_by_value("orange")  # remove orange from linked list
    dll.print_forward()
    dll.print_backward()
    dll.remove_by_value("figs")
    dll.print_forward()
    dll.print_backward()
    dll.remove_by_value("banana")
    dll.remove_by_value("mango")
    dll.remove_by_value("apple")
    dll.remove_by_value("grapes")
    dll.print_forward()
    dll.print_backward()
