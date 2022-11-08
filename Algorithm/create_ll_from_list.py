class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


def create_linked_list_from_list(list_objects):
    if list_objects:
        list_linked = Node(list_objects[0])
        list_linked_tmp = list_linked

        for obj in list_objects:
            node = Node(obj)
            while not list_linked_tmp.next:
                list_linked_tmp.next = node

        list_linked_tmp = list_linked
        while list_linked_tmp:
            print(node.val)
            list_linked_tmp = list_linked_tmp.next
        return list_linked


create_linked_list_from_list([1,2,3])