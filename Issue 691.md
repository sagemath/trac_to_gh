# Issue 691: .coefficients() for EisensteinSeries does not return requested coefficients

Issue created by migration from https://trac.sagemath.org/ticket/691

Original creator: mhansen

Original creation time: 2007-09-18 22:11:56

Assignee: was


```
sage: e = G.gen()
sage: E = EisensteinForms(e, 3)
sage: v = E.eisenstein_series()
sage: f = v[0]
sage: f
15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11 + q + (4*zeta10 + 1)*q^2 + (-9*zeta10^3 + 1)*q^3 + (16*zeta10^2 + 4*zeta10 + 1)*q^4 + (25*zeta10^3 - 25*zeta10^2 + 25*zeta10 - 24)*q^5 + O(q^6)
sage: f.coefficients([0,1,2,3,4])

[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,
 1,
 4*zeta10 + 1,
 -9*zeta10^3 + 1,
 16*zeta10^2 + 4*zeta10 + 1]
sage: f.coefficients([0,1,2,3,4])
[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11]
```



---

Comment by mhansen created at 2007-09-18 22:12:06

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-09-18 22:21:01

Patch attached.


---

Comment by mhansen created at 2007-09-19 00:57:48

Actually, there is a problem with f._compute.  Ignore the above patch for now.


---

Attachment


---

Attachment

Patch attached which fixes the issues.


---

Comment by was created at 2007-09-21 00:28:16

Resolution: fixed
