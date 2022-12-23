# Issue 2142: product of two subdivided matrices should yield a subdivided matrix if it makes sense

Issue created by migration from https://trac.sagemath.org/ticket/2142

Original creator: jason

Original creation time: 2008-02-12 04:16:22

Assignee: was

If you multiply two subdivided matrices so that the product can be thought of as a product of partitioned matrices, it would be nice if the resulting matrix had the natural subdivision introduced by thinking of the product as a block matrix multiplication.


---

Comment by jason created at 2008-02-12 21:02:32

Additionally, copying a matrix probably ought to copy the subdivisions.


---

Comment by ncalexan created at 2008-03-06 08:37:30

#2255 has been marked a duplicate of this: transpose should maintain subdivision info.


---

Attachment


---

Comment by ncalexan created at 2008-03-06 20:18:13

Great docstrings, great patch.  Apply!


---

Comment by mabshoff created at 2008-03-07 03:15:39

Resolution: fixed


---

Comment by mabshoff created at 2008-03-07 03:15:39

Merged in Sage 2.10.3.rc3


---

Comment by jason created at 2008-03-07 03:48:02

Wow, this looks like great work!  Thanks Robert!
