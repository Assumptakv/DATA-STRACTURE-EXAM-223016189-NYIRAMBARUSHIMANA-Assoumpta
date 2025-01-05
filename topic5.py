#Topic 5: Use Singly Linked List
# Singly Linked List
def create_node(data):
    return {"data": data, "next": None}

def insert_end(head, data):
    new_node = create_node(data)
    if not head:
        return new_node
    temp = head
    while temp["next"]:
        temp = temp["next"]
    temp["next"] = new_node
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp["data"], end=" -> ")
        temp = temp["next"]
    print("None")


head = None
head = insert_end(head, "File1")
head = insert_end(head, "File2")
head = insert_end(head, "file3" )
print_list(head)  
