# Issue 3263: [with patch, needs review] typo in lseries_ell.py

Issue created by migration from https://trac.sagemath.org/ticket/3263

Original creator: craigcitro

Original creation time: 2008-05-21 08:23:57

Assignee: craigcitro

There was a silly typo in `sage/schemes/elliptic_curves/lseries_ell.py` that caused the following:


```
sage: EllipticCurve('37a').lseries().deriv_at1()
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell
.py in deriv_at1(self, k)
    463         k = int(k)
    464         sqrtN = float(self.__E.conductor().sqrt())
--> 465         if k == 0: k = int(math.ceil(sqrtN))
    466         an = self.__E.anlist(k)           # list of C ints
    467         # Compute z = e^(-2pi/sqrt(N))

<type 'exceptions.NameError'>: global name 'math' is not defined
```


This was just a simple issue where ceil wasn't getting imported. Patch is the obvious fix, and adds a doctest that would have caught this. 


---

Attachment

Positive review.


---

Comment by mabshoff created at 2008-05-21 13:25:29

Merge in Sage 3.0.2.rc0


---

Comment by mabshoff created at 2008-05-21 13:25:29

Resolution: fixed
