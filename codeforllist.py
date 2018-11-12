class Date:
    def __init__(self, data):
        self.data = data
        self.next = None


class Wholedata:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Date(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, k):

        cur_node = self.head

        if cur_node and cur_node.data == k:
            self.head = cur_node.next
            return

        prev = None
        while cur_node and cur_node.data != k:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next

    def len(self, node):
        if node is None:
            return 0
        return self.len(node.next) + 1

    def reverse(self):

        def reverse1(cur, prev):
            if not cur:
                return prev

            next1 = cur.next
            cur.next = prev
            prev = cur
            cur = next1
            return reverse1(cur, prev)

        self.head = reverse1(cur=self.head, prev=None)

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Date(data)

        new_node.next = prev_node.next
        prev_node.next = new_node




def main():
    llist = Wholedata()
    llist.append("09.04.2018")
    llist.append("17.11.2018")
    llist.append("21.08.2018")
    llist.append("10.05.2018")
    print("Your list is")
    llist.print_list()

    llist.reverse()
    print ("*" * 17)
    print("The reverse of your list is")
    llist.print_list()

    llist.remove("10.05.2018")
    print ("*" * 17)
    print("item is deleted")
    llist.print_list()
    print ("*" * 17)
    print("item is added")

    llist.insert_after_node(llist.head.next, "04.12.2018")

    llist.print_list()
    print ("end of the process")
    
    raw_input("please add date in this form dd.mm.yy ")
    llist.append(raw_input())
    llist.print_list()
    
main()
