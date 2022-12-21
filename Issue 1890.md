# Issue 1890: Sage 2.10.1.alpha2: interfaces/libecm.pyx doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-23 10:55:01

Assignee: rlm

I get the following doctest failure on sage.math with 2.10.1.alpha1 plus the libecm patch applied:

```
sage -t  devel/sage-main/sage/interfaces/libecm.pyx
**********************************************************************
File "libecm.pyx", line 18:
    sage: ecmfactor(999, 0.00, verbose=True)
Expected:
    Performing one curve with B1=0
    Found factor in step 1: 999
    (True, 999)
Got:
    Performing one curve with B1=0
    Found factor in step 1: 27
    (True, 27)
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-24 00:06:54

The patch looks good? I looked at the url provided in the code for ecm and there wasn't really much there. I am also wondering why the output of ecmfactor varies on different platforms. I assume the algorithm depends on some kind of input from an entropy pool?

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-24 00:33:42

With positive review since Robert says:

```
Michael,

It is not platform dependent: it is not deterministic ;)
```



---

Comment by mabshoff created at 2008-01-24 00:34:30

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-24 00:34:30

Resolution: fixed
