# Issue 2743: make symbolic equalities and inequalities callable

Issue created by migration from https://trac.sagemath.org/ticket/2743

Original creator: jason

Original creation time: 2008-03-31 20:36:25

Assignee: mabshoff

It would be nice if the following worked:


```
sage: f = x>3
sage: f(2)
False
sage: f(4)
True
```




---

Comment by jason created at 2008-03-31 20:36:39

Changing assignee from mabshoff to was.


---

Comment by jason created at 2008-03-31 20:36:39

Changing component from Cygwin to calculus.


---

Comment by jason created at 2008-04-02 06:30:31

original

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: %timeit eq(x=2, y=3)
10 loops, best of 3: 54.6 µs per loop
```



After

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: %timeit eq(x=2, y=3)
10 loops, best of 3: 78.9 ms per loop
```



---

Attachment


---

Comment by jason created at 2008-04-02 07:11:02

While there currently is callable functionality, it is broken.  See the doctests in the patch for several breakages of the current functionality.

This patch hands all the work off to symbolic matrices.  That makes it really slow, but it works.  The next thing to do would be to write the functionality directly into this class.


---

Comment by robertwb created at 2008-04-06 06:25:57

Yep, this works well for me. It looks like the matrix is used to ensure that substitutions are to the correct variables, and that works well.


---

Comment by mabshoff created at 2008-04-06 06:37:33

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 06:37:33

Merged in Sage 3.0.alpha2
