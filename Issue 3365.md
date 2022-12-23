# Issue 3365: [with patch; needs review] add a %c mode to the notebook (like %fortran)

Issue created by migration from https://trac.sagemath.org/ticket/3365

Original creator: was

Original creation time: 2008-06-04 18:39:54

Assignee: cwitty

Michael Schmitz -- a student in Math 480 -- created this code.  It makes it so you can do %c in a notebook cell and write pure C functions.  Very fun.  E.g., 


```
%c
int foo(int a, int b) { return(a*b);}
```



```
foo(2r,3r)
///
6
```



---

Attachment


---

Comment by was created at 2008-06-04 18:44:06

this satandard python package must be installed with ' sage -python setup.py install'


---

Attachment


---

Comment by TimothyClemans created at 2008-06-09 03:48:16

Changing type from defect to enhancement.


---

Comment by TimothyClemans created at 2008-06-09 03:48:16

This works on sage.math and doctests for c.py pass.


---

Comment by mabshoff created at 2008-06-09 06:13:34

Do we really want to merge this as is since we are adding a new python package? Creating a new spkg for 10kb Python code also seems like a waste

Thoughts?


Cheers,

Michael


---

Attachment

this zip file contains both the patch and the new to-be-made spkg; it replaces the previous attached patches


---

Comment by craigcitro created at 2008-06-20 05:01:56

Changing keywords from "" to "editor_wstein".
