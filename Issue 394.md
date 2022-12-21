# Issue 394: flatten command for nested lists

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2007-06-28 16:04:21

Assignee: mhampton

Keywords: lists, flatten

The attached file has a candidate function for a flatten command. The default types to flatten are lists and tuples, but more can be added.  Here are the examples from my EXAMPLES section:


```
EXAMPLES:
        sage: flatten([[1,1],[1],2])
        [1, 1, 1, 2]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
        ['Hi', 2, (1, 2, 3), 4, 5, 6]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)),ltypes=(list, tuple, sage.modules.vector_rational_dense.Vector_rational_dense))
        ['Hi', 2, 1, 2, 3, 4, 5, 6]
```




---

Comment by mhampton created at 2007-06-28 16:07:33

Resolution: duplicate
