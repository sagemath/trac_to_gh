# Issue 836: L-series dokchitser -- infinite recursion

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-06 22:59:20

Assignee: was


```
sage: e = EllipticCurve([1,1,0,-63900,-1964465932632])
sage: L = e.Lseries_dokchitser(15)
```


This leads to

```
<type 'exceptions.RuntimeError'>: maximum recursion depth exceeded in cmp
```



---

Comment by was created at 2007-10-06 22:59:55

Changing status from new to assigned.


---

Comment by was created at 2007-11-03 20:08:42

Hmm, things go wrong at a different point now:

```
sage: e = EllipticCurve([1,1,0,-63900,-1964465932632])
sage: L = e.Lseries().dokchitser(15)
sage: L(1)
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py in __call__(self, s, c)
    314             raise ArithmeticError, z
    315         elif '***' in z:
--> 316             raise RuntimeError, z
    317         elif 'Warning' in z:
    318             i = z.rfind('\n')

<type 'exceptions.RuntimeError'>:   ***   I was expecting an integer here: lfundigits
                                         ^----------
```



---

Attachment


---

Comment by was created at 2007-11-03 20:26:55

Resolution: fixed
