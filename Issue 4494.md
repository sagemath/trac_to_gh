# Issue 4494: conjugate method returns error on ZZ matrix

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-11 18:47:01

Assignee: tbd

This should be easy to fix:


```


sage:  a=random_matrix(ZZ,2)
sage: a.conjugate()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/grout/jason/byu/papers/minrank-f2r3-laa/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.conjugate (sage/matrix/matrix2.c:24447)()

AttributeError: 'sage.rings.integer.Integer' object has no attribute 'conjugate'
```




---

Comment by jason created at 2008-11-11 18:47:13

Changing component from algebra to linear algebra.


---

Comment by jason created at 2008-11-11 18:47:13

Changing assignee from tbd to was.


---

Comment by jason created at 2008-11-14 05:31:42

This is a problem with the Integer class, not with the matrix class.  The matrix code is:

return self.new_matrix(self.nrows(), self.ncols(), [z.conjugate() for z in self.list()])

The problem is that the Integer class doesn't have a conjugate method.  Should it, or should the integer matrices override this definition?


---

Comment by jason created at 2008-11-14 05:32:33

Changing component from linear algebra to algebra.


---

Comment by jason created at 2008-11-14 05:32:33

Gee, apparently *I* was the one to change it to linear algebra.  Oops!


---

Comment by jason created at 2008-11-14 05:32:33

Changing assignee from was to tbd.


---

Comment by AlexGhitza created at 2008-12-20 15:51:18

I'm attaching a patch that implements trivial conjugate() methods for ZZ, QQ, and RR, and adds some doctests to the matrix conjugate method in matrix2.pyx.


---

Attachment


---

Comment by jason created at 2008-12-20 21:26:22

Great; I updated http://wiki.sagemath.org/LinearAlgebraSEP to reference this ticket.


---

Comment by cremona created at 2008-12-21 17:36:57

Positive review.  The patch simply supplies the correct solution.  It applies cleanly to 3.2.2.  Tests in sage/matrix and sage/rings all pass.


---

Comment by mabshoff created at 2008-12-21 22:26:35

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 22:26:35

Merged in Sage 3.2.3.alpha0
