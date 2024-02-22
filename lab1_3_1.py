

from tree import *

def postorder(tree):
    if is_empty_tree(tree):
        return []
    return postorder(left_subtree(tree)) + postorder(right_subtree(tree)) + [root(tree)]

# Example usage
tree_ex = makeTree ('/',
                    makeTree ('+',
                              makeTree(40,
                                       make_empty_tree(),
                                       make_empty_tree()),
                              makeTree(5,
                                       make_empty_tree(),
                                       make_empty_tree())),
                    makeTree('*',
                              makeTree(3,
                                       make_empty_tree(),
                                       make_empty_tree()),
                              makeTree('-',
                                       makeTree(7,
                                                make_empty_tree(),
                                                make_empty_tree()),
                                       makeTree(2,
                                                make_empty_tree(),
                                                make_empty_tree()))))

print(postorder(tree_ex))
