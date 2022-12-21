# Issue 607: Coleman integration bug

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-07 00:29:15

Assignee: was

**sage: p = 71; m = 4
        sage: K = pAdicField(p, m)
        sage: x = polygen(K)
        sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
        sage: P = C(-1, 1); P1 = C(-1, -1)
        sage: Q = C(0, 1/4); Q1 = C(0, -1/4)
        sage: x, y = C.monsky_washnitzer_gens()
        sage: w = C.invariant_differential()
        sage: w.integrate(P, Q), (x*w).integrate(P, Q)
        (O(71^4), O(71^4))
        sage: R, R1 = C.lift_x(4, all=True)
        sage: w.integrate(P, R)
        42*71 + 63*71^2 + 55*71^3 + O(71^4)
        sage: w.integrate(P, R) + w.integrate(P1, R1)



---

Comment by robertwb created at 2007-09-07 00:29:38


```
+        sage: p = 71; m = 4
+        sage: K = pAdicField(p, m)
+        sage: x = polygen(K)
+        sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
+        sage: P = C(-1, 1); P1 = C(-1, -1)
+        sage: Q = C(0, 1/4); Q1 = C(0, -1/4)
+        sage: x, y = C.monsky_washnitzer_gens()
+        sage: w = C.invariant_differential()
+        sage: w.integrate(P, Q), (x*w).integrate(P, Q)
+        (O(71^4), O(71^4))
+        sage: R, R1 = C.lift_x(4, all=True)
+        sage: w.integrate(P, R)
+        42*71 + 63*71^2 + 55*71^3 + O(71^4)
+        sage: w.integrate(P, R) + w.integrate(P1, R1)

```



---

Attachment


---

Attachment


---

Comment by robertwb created at 2007-09-07 00:31:44

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-07 00:31:44

Changing assignee from was to robertwb.


---

Comment by was created at 2007-09-07 04:27:20

Resolution: fixed
