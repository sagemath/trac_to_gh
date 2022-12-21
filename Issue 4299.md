# Issue 4299: sha bound totally busted for rank 0 curves

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-15 15:09:34

Assignee: was


```
sage: E = EllipticCurve('11a1')
sage: Sha = E.sha()
sage: Sha.bound()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/wstein/sage/devel/sage-main/sage/schemes/elliptic_curves/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in bound(self)
    698         B of primes such that any divisor of Sha is in this list.
    699         """
--> 700         if self.L1_vanishes():
    701             B = self.bound_kolyvagin()
    702         else:

AttributeError: 'Sha' object has no attribute 'L1_vanishes'
sage:
                                        
```


This is likely easy to fix and was caused by refactoring without enough doctests.


---

Comment by was created at 2008-10-15 15:18:52

note -- this is against 3.1.2 and sha.py, but sha.py was renamed for 3.1.3, so this patch will need a manual REBASE!  but it's better than nothing.


---

Comment by was created at 2008-10-15 15:22:01

Resolution: fixed


---

Attachment

this is fixed in 3.1.3  yeah!
