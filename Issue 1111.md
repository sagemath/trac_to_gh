# Issue 1111: Symbolic equation expand left and right

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-11-06 05:25:35

Assignee: was


```
sage: eqn.expand() # does it to both sides
sage: eqn.expand('right') # does it to the right
sage: eqn.expand('left') # does it to the right
```


See the sage-devel thread Enhancing the SymbolicEquation class


---

Attachment


---

Comment by mhansen created at 2007-11-26 22:01:19

Changing status from new to assigned.


---

Comment by mhansen created at 2007-11-26 22:01:19

Changing assignee from was to mhansen.


---

Comment by robertwb created at 2007-12-01 00:08:40

Works great for me. Are there any other symbolic-expression functions that one would want to add to symbolic equations in a like manner? Could this be automated?


---

Comment by mabshoff created at 2007-12-01 11:31:59

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 11:31:59

Merged in 2.8.15.alpha0.
