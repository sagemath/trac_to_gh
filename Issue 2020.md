# Issue 2020: change an error message when running a certain command and the elliptic curve database is too small

Issue created by migration from https://trac.sagemath.org/ticket/2020

Original creator: was

Original creation time: 2008-01-31 23:56:42

Assignee: was

In the session below the command fails because the optional LARGE Cremona elliptic curves database is not installed (it works fine if it is).  The error message should clearly say why the failure occurs, instead of Sage mysteriously bombing out. 


```
sage@modular:~$ build/sage-2.10.1.rc3/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1.rc3, Release Date: 2008-01-30                  |
| Type notebook() for the GUI, and license() for information.        |
sage: EllipticCurve('14a4').sha().an(use_database=True)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home2/sage/<ipython console> in <module>()

/home2/sage/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in an(self, use_database)
    148         if use_database:
    149             try:
--> 150                 self.__an = int(round(float(self.E.database_curve().db_extra[4])))
    151                 return self.__an
    152             except RuntimeError, AttributeError:

<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'db_extra'
```



---

Attachment

Looks good. (Actual review comments were in person, all taken care of.)


---

Comment by mabshoff created at 2009-01-24 14:47:41

This patch exposes a numerical noise issue in sha_tate:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 157:
    sage: E.sha().an()
Expected:
    0.999999999999998
Got:
    1.00000000000000
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 14:57:54

I was wrong, the above is not caused by this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 15:30:48

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 15:30:48

Merged in Sage 3.3.alpha2
