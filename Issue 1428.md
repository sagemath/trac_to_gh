# Issue 1428: add SVD method to matrix_complex_double_dense

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-08 14:53:32

Assignee: was

CC:  dfdeshom@gmail.com


```
Hallo!

I tried to compute the SVD of a complex matrix (module
matrix.matrix_complex_double_dense), but I didn't found a function to
do so. However, real matrices (module matrix.matrix_real_double_dense)
support it. Is there really no way to compute a complex SVD? If I
remember correctly, at least the underlying library GSL supports
complex SVDs... What would I have to do to integrate those functions
into Sage?

Sander
```


Basically all that needs to be done is to translate the real code over to the complex case.


---

Comment by mhansen created at 2007-12-22 13:15:23

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2007-12-22 13:15:23

Changing assignee from was to mhansen.


---

Comment by dfdeshom created at 2008-01-15 01:57:24

The patch looks great. I would suggest making an option that would just return S, instead of the tuple (U,S,V') since people that use this method tend to care more about S than anything else.


---

Comment by mabshoff created at 2008-01-15 03:01:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 03:01:03

Merged in Sage 2.10.alpha3
