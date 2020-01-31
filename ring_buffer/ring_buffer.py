from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    # The `append` method adds elements to the buffer.
    """
    PLAN:
        if storage length is less than capacity
            set current to head
            add new element to head

        if storage length is equal to capacity
            if current is equal to head
                remove head, 
                add to head, 
                set current to current.next
            if current.next
                add to head
                reassign pointers of prev and next
                move current to head
                remove head
                move current to current.next
    """
    def append(self, item):
        # self.storage.add_to_head(item)
        # self.current = self.storage.head
        # print("\ncurrent: ", self.current.value)
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            return 

        if self.storage.length == self.capacity:
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.current.next
                return
            
            if self.current.next is not None:
                # print("\n****************START****************\n")
                # print("\nmycurrent value: ", self.current.value, "\n")
                # print("---------------------------Before---------------------")
                # print("DLL head: ", self.storage.head.value)
                # print("node 2: ", self.storage.head.next.value)
                # print("node 3: ", self.storage.head.next.next.value)
                # print("node 4: ", self.storage.head.next.next.next.value)
                # print("node 5: ", self.storage.head.next.next.next.next.value)                    
                # print("-------------------------End BEFORE-----------------------\n\n")
                # add new node to head of DLL
                self.storage.add_to_head(item)
                new_node = self.storage.head
                print('\bnew node value: ', new_node.value, '\n')
                # store current node location in DLL
                temp1 = self.current.next 
                # reassign pointers
                self.storage.head = self.storage.head.next
                self.current.next = new_node
                new_node.prev = self.current
                new_node.next = temp1
                temp1.prev = new_node


                # Change current
                if self.current.next.next:
                    self.current = self.current.next.next
                    # move current node to front
                    self.storage.move_to_front(self.current.prev.prev)
                    # remove from head, store remove node value for print.
                    el = self.storage.remove_from_head()
                    # print("---------------------------AFTER---------------------")
                    # print("\n\n\n\n************************\nmy el REMOVED:", el)
                    # print("mycurrent value: ", self.current.value)
                    # print("current after reassigning: ", self.current.value)
                    # # print("TEMPVAL", temp.value)
                    # print("new head: ", self.storage.head.value)
                    # print("node 2: ", self.storage.head.next.value)
                    # print("node 3: ", self.storage.head.next.next.value)
                    # print("node 4: ", self.storage.head.next.next.next.value)
                    # print("node 5: ", self.storage.head.next.next.next.next.value)                    
                    # # temp = self.current.prev
                    # print("TEMPVAL after reassigning PREV: ", temp1.value)
                    # # print("TEMPVAL.NEXT should equal current : ", temp1.next.value)
                    # print("-------------------------End AFTER-----------------------\n\n")
            else:
                self.current = self.storage.head
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)


    
    # The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

