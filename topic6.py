#Topic 6: Implement Tree for Hierarchical Data
# Tree to Represent Hierarchical Data
def create_node(data):
    return {"data": data, "children": []}

def add_child(parent, child_data):
    child = create_node(child_data)
    parent["children"].append(child)
    return child

def print_tree(root, level=0):
    print("  " * level + root["data"])
    for child in root["children"]:
        print_tree(child, level + 1)

# Example Usage
root = create_node("Root Folder")
child1 = add_child(root, "Folder1")
add_child(child1, "File1.1")
add_child(root, "File2")
print_tree(root)
