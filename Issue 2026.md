# Issue 2026: matrix.eigenspaces doctest description is misleading

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-01 19:18:58

Assignee: was

In matrix2.pyx under eigenspaces():


```
        Next we compute the eigenspaces over the finite field
        of order 11:
        
            sage: # A = ModularSymbols(43, base_ring=GF(11), sign=1).T(2).matrix()
            sage: A = matrix(QQ, 4, [3, 9, 0, 0, 0, 9, 0, 1, 0, 10, 9, 2, 0, 9, 0, 2])
```


It seems like the description should be deleted or the doctest should be run and the output included.



---

Comment by was created at 2008-02-01 23:02:34

Changing status from new to assigned.


---

Attachment


---

Comment by jason created at 2008-02-01 23:38:05

apply on top of first patch.


---

Attachment

Apply instead of first patch (this includes the first patch)


---

Comment by jason created at 2008-02-01 23:40:32

okay, now I've messed all the attachments up.  What I mean is that the third patch "eigenspace-docs.2.patch" includes the first patch and the second patch, and so is the only patch that needs applying.  William deserves credit for the first patch, though.


---

Comment by was created at 2008-02-01 23:44:59

Jason positive reviewed my patch, and I positively review his patch on top of my patch.


---

Comment by mabshoff created at 2008-02-02 03:18:21

Merged eigenspace-docs.2.patch in Sage 2.10.1.rc5


---

Comment by mabshoff created at 2008-02-02 03:18:21

Resolution: fixed
