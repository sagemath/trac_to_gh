# Issue 401: list * integer works but integer * list doesn't work

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-07-10 00:16:34

Assignee: somebody

In SAGE 2.6, you can do list * integer but not integer * list. Either they should both work (more like python) or neither of them should work (for internal consistency).


```
sage: [3, 4, 5] * 2
 [3, 4, 5, 3, 4, 5]

sage: 2 * [3, 4, 5]
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/sage-2.6/<ipython console> in <module>()

/home/dmharvey/sage-2.6/element.pyx in element.RingElement.__mul__()

/home/dmharvey/sage-2.6/element.pyx in element.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'list'>'
```




---

Comment by mabshoff created at 2007-08-24 13:05:57

Resolution: worksforme


---

Comment by mabshoff created at 2007-08-24 13:05:57

Work's for me with Sage 2.8.2:

```
sage: [3,4,5]*3
[3, 4, 5, 3, 4, 5, 3, 4, 5]
sage: 3*[4,5,6]
[4, 5, 6, 4, 5, 6, 4, 5, 6]
```


Cheers,

Michael
