class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.link:
                cur_node = cur_node.link
            cur_node.link = new_node

    def show(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.link

    def __getitem__(self, index):
        cur_node = self.head
        for i in range(index):
            if cur_node is None:
                raise IndexError("List index out of range")
            cur_node = cur_node.link
        if cur_node is None:
            raise IndexError("List index out of range")
        return cur_node.data

    def __add__(self, other):
        new_list = LinkedList()
        new_list.head = Node(self.head.data)
        new_list_node = new_list.head

        cur_node = self.head.link
        while cur_node is not None:
            new_node = Node(cur_node.data)
            new_list_node.link = new_node
            new_list_node = new_node
            cur_node = cur_node.link

        cur_node = other.head
        while cur_node is not None:
            new_node = Node(cur_node.data)
            new_list_node.link = new_node
            new_list_node = new_node
            cur_node = cur_node.link

        return new_list


def main():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(4)
    list1.show()
    print(f'\n{list1[1]}')

    list2 = LinkedList()
    list2.append(3)
    list2.append(5)
    list2.append(6)
    list2.show()
    print(f'\n{list2[2]}')

    list3 = list1 + list2
    list3.show()
    print(f'\n{list3[3]}')


if __name__ == '__main__':
    main()
