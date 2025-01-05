#Topic 4: Create AVL Tree for Fixed Number of Orders
# AVL Tree Implementation
def create_node(data):
    return {"data": data, "left": None, "right": None, "height": 1}

def height(node):
    return node["height"] if node else 0

def balance_factor(node):
    return height(node["left"]) - height(node["right"])

def rotate_right(y):
    x = y["left"]
    T2 = x["right"]
    x["right"] = y
    y["left"] = T2
    y["height"] = 1 + max(height(y["left"]), height(y["right"]))
    x["height"] = 1 + max(height(x["left"]), height(x["right"]))
    return x

def rotate_left(x):
    y = x["right"]
    T2 = y["left"]
    y["left"] = x
    x["right"] = T2
    x["height"] = 1 + max(height(x["left"]), height(x["right"]))
    y["height"] = 1 + max(height(y["left"]), height(y["right"]))
    return y

def insert(root, data):
    if not root:
        return create_node(data)
    elif data < root["data"]:
        root["left"] = insert(root["left"], data)
    else:
        root["right"] = insert(root["right"], data)
    
    root["height"] = 1 + max(height(root["left"]), height(root["right"]))
    bf = balance_factor(root)

    # Rotations
    if bf > 1 and data < root["left"]["data"]:
        return rotate_right(root)
    if bf < -1 and data > root["right"]["data"]:
        return rotate_left(root)
    if bf > 1 and data > root["left"]["data"]:
        root["left"] = rotate_left(root["left"])
        return rotate_right(root)
    if bf < -1 and data < root["right"]["data"]:
        root["right"] = rotate_right(root["right"])
        return rotate_left(root)

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root["left"])
        print(root["data"], end=" ")
        inorder_traversal(root["right"])


root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 5)
inorder_traversal(root)  
