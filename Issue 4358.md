# Issue 4358: Sage spawn too many gp processes

Issue created by migration from https://trac.sagemath.org/ticket/4358

Original creator: anakha

Original creation time: 2008-10-24 05:17:34

Assignee: was

CC:  cremona jdemeyer

This:


```
sage: EllipticCurve('37a').sha().an_numerical()
```


spawn a new gp process every time it is computed.


---

Comment by cremona created at 2008-10-31 16:57:02

I think this might be in the Dokchitser call (line 94 of elliptic_curves/sha_tate.py)


---

Comment by AlexGhitza created at 2009-01-23 02:43:03

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2013-08-13 16:00:05

Why is this a bug? `gp` starts up very quickly, so it doesn't need to be "fixed".


---

Comment by jdemeyer created at 2013-08-13 16:00:05

Changing status from new to needs_review.


---

Comment by pbruin created at 2013-08-13 20:10:00

Tim Dokchitser's `gp` script `computel.gp`, which is used internally by `an_numerical`, uses global variables, which is a good reason to use a different `gp` instance for every call.

I first suspected an unnecessary line of code in `Lseries_ell.dokchitser()`, but this was not the cause:

```diff
--- a/sage/schemes/elliptic_curves/lseries_ell.py
+++ b/sage/schemes/elliptic_curves/lseries_ell.py
@@ -132,7 +132,6 @@
                        eps = self.__E.root_number(),
                        poles = [],
                        prec = prec)
-        gp = L.gp()
         s = 'e = ellinit(%s);'%list(self.__E.minimal_model().a_invariants())
         s += 'a(k) = ellak(e, k);'
         L.init_coeffs('a(k)', 1, pari_precode = s,
```

This line just starts the `gp` instance a bit sooner than necessary, so I don't think a patch is needed.


---

Comment by pbruin created at 2013-08-13 20:10:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 11:12:22

Resolution: wontfix
