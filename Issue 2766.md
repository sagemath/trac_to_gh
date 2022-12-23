# Issue 2766: graph adjacency matrix defaults to sparse

Issue created by migration from https://trac.sagemath.org/ticket/2766

Original creator: jason

Original creation time: 2008-04-02 02:24:18

Assignee: rlm

When a graph is small or dense, the adjacency matrix should be a dense matrix.


---

Comment by jason created at 2008-04-02 03:14:06

This is the ONLY patch---ignore all others.


---

Attachment

Ignore the .2.patch file---it contains unrelated changes by accident.


---

Comment by rlm created at 2008-04-02 07:08:21

Looks good to me.


---

Comment by mabshoff created at 2008-04-02 19:27:38

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-02 19:27:38

Resolution: fixed


---

Comment by mabshoff created at 2008-04-02 20:20:14

Please mention the fact that you didn't doctest:

```
sage -t -long devel/sage-main/sage/graphs/graph.py
*********************************************************************
File "graph.py", line 505:
    sage: m = matrix(G); m.parent()
Expected:
    Full MatrixSpace of 5 by 5 sparse matrices over Integer Ring
Got:
    Full MatrixSpace of 5 by 5 dense matrices over Integer Ring
```

and 

```
sage -t -long devel/sage-main/sage/matrix/constructor.py 
**********************************************************************
File "constructor.py", line 136:
    sage: m = matrix(g); m; m.parent()
Expected:
    [0 1 0 0 1 1 0 0 0 0]
    [1 0 1 0 0 0 1 0 0 0]
    [0 1 0 1 0 0 0 1 0 0]
    [0 0 1 0 1 0 0 0 1 0]
    [1 0 0 1 0 0 0 0 0 1]
    [1 0 0 0 0 0 0 1 1 0]
    [0 1 0 0 0 0 0 0 1 1]
    [0 0 1 0 0 1 0 0 0 1]
    [0 0 0 1 0 1 1 0 0 0]
    [0 0 0 0 1 0 1 1 0 0]
    Full MatrixSpace of 10 by 10 sparse matrices over Integer Ring
Got:
    [0 1 0 0 1 1 0 0 0 0]
    [1 0 1 0 0 0 1 0 0 0]
    [0 1 0 1 0 0 0 1 0 0]
    [0 0 1 0 1 0 0 0 1 0]
    [1 0 0 1 0 0 0 0 0 1]
    [1 0 0 0 0 0 0 1 1 0]
    [0 1 0 0 0 0 0 0 1 1]
    [0 0 1 0 0 1 0 0 0 1]
    [0 0 0 1 0 1 1 0 0 0]
    [0 0 0 0 1 0 1 1 0 0]
    Full MatrixSpace of 10 by 10 dense matrices over Integer Ring
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-02 20:52:07

Reviewer asleep? :)


---

Attachment

Merged trac_2766-fix-doctests.patch in Sage 3.0.alpha1
