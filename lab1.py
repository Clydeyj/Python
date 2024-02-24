from tree import *

def postorder(tree):
    if is_empty_tree(tree):
        return []
    return postorder(left_subtree(tree)) + postorder(right_subtree(tree)) + [root(tree)]



print(postorder(tree))
