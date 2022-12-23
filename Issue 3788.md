# Issue 3788: [with patch, needs review] many matrix_dense_modn operations are unreasonably slow

Issue created by migration from https://trac.sagemath.org/ticket/3788

Original creator: robertwb

Original creation time: 2008-08-07 10:04:21

Assignee: was

This is because they use the generic algorithms (extracting each element as a Python object). 

See discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/dae70440d7fd41




---

Comment by mhansen created at 2008-08-07 16:35:38

Hi Robert,

Everything looks good except I got one little doctest failure:


```
File "/opt/sage/tmp/matrix_modn_dense.py", line 204:
    sage: matrix(GF(7), 2, 2, [-1, int(-2), GF(7)(-3), 1/4])
Expected:
    [6 2]
    [4 2]
Got:
    [6 0]
    [4 2]
```


Shouldn't int(-2) go to 5 instead of either 2 or 0?


---

Attachment


---

Comment by robertwb created at 2008-08-07 17:04:10

That change to `mod_int` being unsigned bites again, and when I changed the doctest to test a negative int, coincidentally the output was the same (should have caught that nonetheless)--glad it was different for you. 

The patch has been updated.


---

Comment by mhansen created at 2008-08-07 17:10:36

With the new patch, I get these failures:


```
sage -t  devel/sage-work/sage/matrix/matrix_modn_dense.pyx  **********************************************************************
File "/opt/sage/tmp/matrix_modn_dense.py", line 26:
    sage: a^2
Expected:
    [ 3 23 31]
    [20 17 29]
    [25 16  0]
Got:
    [ 0 23 31]
    [ 0 17 29]
    [ 0 16  0]
**********************************************************************
File "/opt/sage/tmp/matrix_modn_dense.py", line 42:
    sage: b*a
Expected:
    [15 18 21]
    [20 17 29]
Got:
    [ 0 18 21]
    [ 0 17 29]
**********************************************************************
```



---

Comment by robertwb created at 2008-08-07 17:27:49

???

Me too--no idea why that just changed, it used to work and I thought I only touched a couple of lines. Now I wish I had made a new patch instead of qrefresh. I'll look at this.


---

Attachment

There was certainly a bug, but not in the code I touched so I don't know why it suddenly showed up now. I've fixed it, it should be working find again.


---

Attachment


---

Comment by mhansen created at 2008-08-08 06:24:25

Apply only 3788.patch


---

Comment by mabshoff created at 2008-08-08 23:37:55

Resolution: fixed


---

Comment by mabshoff created at 2008-08-08 23:37:55

Merged 3788.patch in Sage 3.1.alpha1
