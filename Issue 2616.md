# Issue 2616: Replace all matrix.submatrix() instances

Issue created by migration from https://trac.sagemath.org/ticket/2616

Original creator: dfdeshom

Original creation time: 2008-03-20 17:51:24

Assignee: dfdeshom

Pending review and inclusion of #2355, we can replace all instances of M.submatrix() with `M[indexa, indexb]`

Note: I only found one function is using the submatrix method (subdivisions in matrix2.pyx). 


---

Attachment


---

Comment by AlexGhitza created at 2008-04-13 22:22:15

Actually, there are a couple of other places where submatrix() is used.  See the attached patch, where I have replaced all of them.


---

Comment by dfdeshom created at 2008-04-14 20:17:38

Replying to [comment:1 AlexGhitza]:
> Actually, there are a couple of other places where submatrix() is used.  See the attached patch, where I have replaced all of them.

Thanks! Patch looks good. I say apply!


---

Comment by mabshoff created at 2008-04-14 20:39:19

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 20:39:19

Merged in Sage 3.0.alpha5
