class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next

        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Test setup
def test_reverse():
    # Create linked list: 1 -> 2 -> 3 -> 4
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("Original:", print_list(head))  # Should print [1, 2, 3, 4]

    # Reverse it
    reversed_head = reverse_linked_list(head)

    print("Reversed:", print_list(reversed_head))  # Should print [4, 3, 2, 1]

test_reverse()
