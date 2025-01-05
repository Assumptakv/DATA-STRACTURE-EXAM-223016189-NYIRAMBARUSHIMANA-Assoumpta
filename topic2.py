#Topic2:  Implement Circular Queue and Array to manage data in the cloud-based file sharing system for small teams.



# Circular Queue Implementation
def create_circular_queue(size):
    return {"queue": [None] * size, "front": -1, "rear": -1, "size": size}

def is_full(cq):
    return (cq["rear"] + 1) % cq["size"] == cq["front"]

def is_empty(cq):
    return cq["front"] == -1

def enqueue(cq, value):
    if is_full(cq):
        print("Queue is Full")
        return
    if is_empty(cq):
        cq["front"] = 0
    cq["rear"] = (cq["rear"] + 1) % cq["size"]
    cq["queue"][cq["rear"]] = value

def dequeue(cq):
    if is_empty(cq):
        print("Queue is Empty")
        return None
    data = cq["queue"][cq["front"]]
    if cq["front"] == cq["rear"]:
        cq["front"] = cq["rear"] = -1  # Reset queue
    else:
        cq["front"] = (cq["front"] + 1) % cq["size"]
    return data

# Example Usage
cq = create_circular_queue(5)
enqueue(cq, "File1")
enqueue(cq, "File2")
print(dequeue(cq))  


# Array to Manage Files:

# Array Implementation
file_array = ["File1", "File2", "File3"]
file_array.append("File4")  
file_array.append("File5")
file_array.append("file6")

file_array.remove("file6")
   
print(file_array)  
