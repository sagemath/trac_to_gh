# Issue 5168: [with patch, needs review] matrix0.pyx: fix doctest for commutator

Issue created by migration from https://trac.sagemath.org/ticket/5168

Original creator: jhpalmieri

Original creation time: 2009-02-03 21:17:52

Assignee: was

Keywords: matrix0, commutator

Here is the extent of the docstring for the commutator method in matrix0.pyx:

```
        Return the commutator self*other - other*self.

        EXAMPLES:
            sage: A = Matrix(QQ[['t']], 2, 2, range(4))
```

Fix the doctest so that it actually computes a commutator.



---

Attachment


---

Comment by cwitty created at 2009-02-05 06:57:01

New doctests look good, and they pass.

(Good catch on noticing the original bug, too.)

Positive review.


---

Comment by mabshoff created at 2009-02-05 11:10:01

Resolution: fixed


---

Comment by mabshoff created at 2009-02-05 11:10:01

Merged in Sage 3.3.alpha6.

Cheers,

Michael
