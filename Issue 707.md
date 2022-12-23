# Issue 707: Database for Knuth's Power Tree

archive/issues_000707.json:
```json
{
    "body": "Assignee: boothby\n\nCreate a database which contains representations of addition chains for Knuth's Power Tree.  Write a generic_power_knuth(x,n) which utilizes the database in a highly optimal manner.\n\nIssue created by migration from https://trac.sagemath.org/ticket/707\n\n",
    "created_at": "2007-09-20T17:22:41Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "Database for Knuth's Power Tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/707",
    "user": "boothby"
}
```
Assignee: boothby

Create a database which contains representations of addition chains for Knuth's Power Tree.  Write a generic_power_knuth(x,n) which utilizes the database in a highly optimal manner.

Issue created by migration from https://trac.sagemath.org/ticket/707





---

archive/issue_comments_003717.json:
```json
{
    "body": "To be able to see the tree, here is the code from codegolf, slightly adapted to sage:\n\n```\ndef chain(tree, x):\n    c = [x]\n    while x != 1:\n        x = tree[x]\n        c.append(x)\n    return c[::-1]\n\ndef knuth_tree(levels):\n    \"\"\"\n    EXAMPLES::\n\n        sage: knuth_tree(5).show(layout='tree',tree_root=1)\n        sage: G = knuth_tree(6)\n        sage: Poset(G).show(layout='tree')\n    \"\"\"\n    tree = {1: None}\n    leaves = [1]\n    for _ in range(levels):\n        newleaves = []\n        for m in leaves:\n            for i in chain(tree, m):\n                if i + m not in tree:\n                    tree[i + m] = m\n                    newleaves.append(i + m)\n        leaves = newleaves\n    return DiGraph([[i, tree[i]] for i in tree if not i == 1])\n```\n",
    "created_at": "2014-10-22T20:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/707#issuecomment-3717",
    "user": "chapoton"
}
```

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
    return DiGraph([[i, tree[i]] for i in tree if not i == 1])
```

