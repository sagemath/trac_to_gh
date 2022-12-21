# Issue 707: Database for Knuth's Power Tree

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2007-09-20 17:22:41

Assignee: boothby

Create a database which contains representations of addition chains for Knuth's Power Tree.  Write a generic_power_knuth(x,n) which utilizes the database in a highly optimal manner.


---

Comment by chapoton created at 2014-10-22 20:29:57

To be able to see the tree, here is the code from codegolf, slightly adapted to sage:

```
def chain(tree, x):
    c = [x]
    while x != 1:
        x = tree[x]
        c.append(x)
    return c[::-1]

def knuth_tree(levels):
    """
    EXAMPLES::

        sage: knuth_tree(5).show(layout='tree',tree_root=1)
        sage: G = knuth_tree(6)
        sage: Poset(G).show(layout='tree')
    """
    tree = {1: None}
    leaves = [1]
    for _ in range(levels):
        newleaves = []
        for m in leaves:
            for i in chain(tree, m):
                if i + m not in tree:
                    tree[i + m] = m
                    newleaves.append(i + m)
        leaves = newleaves
    return DiGraph([This is the Trac macro *i, tree[i* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#i, tree[i-macro) for i in tree if not i == 1])
```

