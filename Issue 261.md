# Issue 261: a new matrix constructor

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-14 06:49:52

Assignee: was

CC:  jason

Kyle Schalm suggests:

```
 
 
here is a matrix constructor i would like to see:
 
Matrix(M, N, f):
   for i in range(1,M+1):
     for j in range(1,N+1):
       self[i][j] = f(i,j)   # or whatever the syntax is
 
 
i might use it like this:
 
A = Matrix(3, 3, lambda i,j: i+j)
 
i'd do it myself, but i don't have a development environment set up,
and don't wanna do that right now.
 
cheers,
kyle
 
```



---

Comment by mabshoff created at 2008-08-31 06:07:28

Changing assignee from was to mhansen.


---

Comment by jason created at 2008-11-14 06:45:28

Changing assignee from mhansen to jason.


---

Comment by jason created at 2008-11-14 06:45:28

Changing status from new to assigned.


---

Comment by jason created at 2009-11-19 22:40:01

Remove assignee jason.


---

Comment by mhansen created at 2010-03-16 06:32:56

Changing status from new to needs_review.


---

Attachment

On my system seems to be working fine. A light cosmetic suggestion for the patch - I would use 'import numpy' only once, at the very beginning. 

A desirable thing is to adjust 'vector' correspondingly - both vorking as 'vector(3,f)' and 'vector(v)' for a 1-dimensional numpy array v with dtype=int, dtype=object or any other dtype, which possible currently to do as 'vector(list(v))'. I'll try to add this as a ticket later (when I'll have more time) if it won't be created earlier.

Alec Mihailovs


---

Comment by AlecMihailovs created at 2010-03-20 21:29:28

This patch includes not only this enhancement, but also fixes a bug for matrix(v) with v being a 1x1 numpy array, which currently produces a n x n zero matrix for v being a 1x1 numpy array with one element n. So it should be, perhaps, marked not only as an enhancement, but also as a defect. 

Alec Mihailovs


---

Comment by AlecMihailovs created at 2010-03-20 22:01:04

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-14 20:40:26

I get a doctest failure with this.  I'm attaching a trivial patch to fix it.


---

Comment by jhpalmieri created at 2010-04-14 20:40:46

apply on top of other patch


---

Comment by jhpalmieri created at 2010-04-15 05:18:48

Resolution: fixed


---

Attachment

Merged both patches in 4.4.alpha0.
