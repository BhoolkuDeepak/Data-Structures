class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
# Print the linked list

    def print_data(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
            
# ADD AT THE BEGINNING

    def at_beginning(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        
# ADD AT THE END

    def at_the_end(self, data):
        LastNode = Node(data)
        prevNode = self.head
        while prevNode.next:
            prevNode = prevNode.next
        prevNode.next = LastNode
        
# ADD IN-BETWEEN

    def in_between(self,middle_node,data):
        if middle_node == None:
            print("Middle Node absent")
        NewNode=Node(data)
        NewNode.next=middle_node.next
        middle_node.next=NewNode
        
#REMOVE WHEN DATA IS KNOWN

    def remove_node(self,remove_data):
        head=self.head
        if head!=None:
            if head.data==remove_data:
                self.head=head.next
                print("{{1}}")
                head=None
                return
            
        while head != None:
            if head.data==remove_data:
                break
            prev=head
            head=head.next
        
        if head==None:
            print("{{3}}")
            return
        
        prev.next=head.next
        head=None

list1 = LinkedList()
list1.head = Node("MONDAY")
day2 = Node("TUEDAY")
day3 = Node("WEDNESDAY")
day4 = Node("FRIDAY")
day5 = Node("NODAY")

list1.head.next = day2
day2.next = day3
day3.next = day4
day4.next = day5

list1.at_beginning("SUNDAY")
list1.at_the_end("SATURDAY")
list1.in_between(day3,"THURSDAY")
list1.remove_node("NODAY")
list1.print_data()
