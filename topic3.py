
#Topic 3: Implement Doubly Linked List
# Doubly Linked List Implementation
def create_node(data):
    return {"data": data, "next": None, "prev": None}

def insert_end(head, data):
    new_node = create_node(data)
    if not head:
        return new_node
    temp = head
    while temp["next"]:
        temp = temp["next"]
    temp["next"] = new_node
    new_node["prev"] = temp
    return head

def delete_node(head, key):
    temp = head
    while temp:
        if temp["data"] == key:
            if temp["prev"]:
                temp["prev"]["next"] = temp["next"]
            if temp["next"]:
                temp["next"]["prev"] = temp["prev"]
            if temp == head:
                head = temp["next"]
            break
        temp = temp["next"]
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp["data"], end=" <-> ")
        temp = temp["next"]
    print("None")
head = None
head = insert_end(head, "File1")
head = insert_end(head, "File2")
head = insert_end(head,"file3")
head = delete_node(head, "File1")
print_list(head)  
