# Issue 3720: stupid bug in elliptic curves caused by refactoring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-24 11:31:34

Assignee: was


```
sage: EllipticCurve([0,0,0,-193^2,0]).sha().an()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in an(self, use_database)
    157         eps = E.root_number()
    158         if eps == 1:
--> 159             L1_over_omega = E.lseries().L_ratio()
    160             if L1_over_omega == 0:
    161                 return self.an_numerical(use_database=use_database)

/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell.py in L_ratio(self)
    695                 quo = Q(n) / Q(C)
    696                 self.__lratio = quo / self.__E.real_components()
    697                 return self.__lratio
    698             k += sqrtN
--> 699             misc.verbose("Increasing precision to %s terms."%k)

NameError: global name 'misc' is not defined
```


this was reported by Nils Bruin and John Cremona.


---

Attachment


---

Comment by cremona created at 2008-07-25 16:44:56

Resolution: duplicate


---

Comment by cremona created at 2008-07-25 16:44:56

This is a duplicate of #3651 which has already been fixed in 3.0.6.rc0, hence this one can be closed as a duplicate.
