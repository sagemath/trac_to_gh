# Issue 1733: notebook bug -- %foo (or anything else) in a cell by itself (with nothing else in the cell) does not give an error but it *should*

Issue created by migration from https://trac.sagemath.org/ticket/1733

Original creator: was

Original creation time: 2008-01-09 08:51:02

Assignee: boothby

This is probably easy to fix in server/notebook/worksheet.py


---

Attachment


---

Comment by was created at 2008-05-10 22:56:24

The attached patch:

     1. Fixed the problem where %foobar with no input in the cell didn't give an error -- now it does, about
foobar not being defined.

     2. While I was at it I improved how %foo modes in the notebook work, so that they can have everything on one line, e.g., 

```
   %magma Factorization(9038049823)
```

on a single line works in the notebook.

     3. NOTE that the actual patch replaces a bunch of crappy hard to understand code with like 3 simple
    lines that fix all of the above.


---

Comment by boothby created at 2008-05-12 05:15:15

Great stuff!  Works well, and makes the code cleaner!


---

Comment by mabshoff created at 2008-05-12 11:03:18

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-12 11:03:18

Resolution: fixed
