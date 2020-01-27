import json

from anytree import Node, RenderTree

"""
  Write a function to generate the json (tree) from xpath list.

  *Input*

    [
        '/this/is/a',
        '/this/a/great',
        '/you/can/code',
        '/you/have/done/it'
    ]

  *Output*
  
    {
        "this" : {
            "is" : "a",
            "a"  : "great",
        },
        "you"  : {
            "can"  : "code",
            "have" : {
                "done" : "it"
            }
        }
    }
"""

xpath_input = ['/this/is/a', '/this/a/great', '/you/can/code', '/you/have/done/it']
root_node = Node(name="root")

print(f"Given list:\n{xpath_input}\n")


def generate_tree(root_node, xpath_input):
    for index, xpath in enumerate(xpath_input):
        xpath = xpath_input[index].split("/")[1:]
        parent = root_node
        for ind, val in enumerate(xpath):
            repeated_values = [node for node in root_node.descendants if (node.name == val and node.parent == parent)]
            if not repeated_values:
                current_node = Node(name=val, parent=parent)
                parent = current_node
            else:
                parent = repeated_values[0]
    return root_node


# First, generate tree from the above xpath
tree_root = generate_tree(root_node=root_node, xpath_input=xpath_input)

print(f"#### THE LIST IN TREE FORMAT IS:\n{RenderTree(root_node)}\n\n")
print(f"Creating JSON from the above tree:\n")

result_json = {}


# then populate the dictionary from the above tree
def populate_JSON(Node, result_json):
    if len(Node.children) == 1 and len(Node.descendants) == 1:
        result_json[Node.name] = Node.children[0].name
    elif len(Node.children) >= 1:
        result_json[Node.name] = {}
        for child in Node.children:
            populate_JSON(child, result_json[Node.name])


populate_JSON(tree_root, result_json=result_json)

result_json = json.dumps(result_json["root"], indent=4)
print(f"The resulting JSON is:\n{result_json}))")
