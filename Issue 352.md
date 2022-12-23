# Issue 352: error in matrix creation options

Issue created by migration from https://trac.sagemath.org/ticket/352

Original creator: was

Original creation time: 2007-04-19 21:15:46

Assignee: was


```
> After trying some things, I've noticed that it is possible to coerce a
> flat list into a sparse matrix but not a list of lists.
> 
> E.G.
> sage: B = MatrixSpace(ZZ,5,5)
> sage: v = [0 for i in range(25)]
> sage: u = [[0 for i in range(5)] for j in range(5)]
> sage: B(v)
> [0 0 0 0 0]
> [0 0 0 0 0]
> [0 0 0 0 0]
> [0 0 0 0 0]
> [0 0 0 0 0]
> 
> sage: B(u) ---> results in the same error as before.
> Is there a conceptual reason that a flat list works, but a list of

That looks like just a mistake on our paper.  We should make
it so both cases work. 
```




---

Comment by mabshoff created at 2007-08-18 23:53:56

Resolution: fixed


---

Comment by mabshoff created at 2007-08-18 23:53:56

This work since at least Sage 2.8.1


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.1, Release Date: 2007-08-18                       |
| Type notebook() for the GUI, and license() for information.        |
sage: B = MatrixSpace(ZZ,5,5)
sage: v = [0 for i in range(25)]
sage: u = [[0 for i in range(5)] for j in range(5)]
sage: B(u)

[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
sage: B(v)

[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
```

