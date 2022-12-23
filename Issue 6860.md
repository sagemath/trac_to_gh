# Issue 6860: dimensions of modular forms spaces for Gamma(N) is busted / not implemented

Issue created by migration from https://trac.sagemath.org/ticket/6860

Original creator: was

Original creation time: 2009-09-02 02:22:05

Assignee: was


```
sage: dimension_cusp_forms(Gamma(11))
[hangs forever]
```



---

Comment by was created at 2009-09-02 13:05:35

Changing type from defect to enhancement.


---

Comment by was created at 2009-09-02 13:05:35

Wait, I'm just impatient, since:

```
sage: dimension_cusp_forms(Gamma(11))
26
```


So I'm changing this to an enhancement, since I think this should be fast.


---

Comment by davidloeffler created at 2013-07-22 15:22:54

Changing component from number theory to modular forms.


---

Comment by davidloeffler created at 2013-07-22 15:22:54

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2013-07-22 15:22:54

This has now been fastified:

```python
sage: %time dimension_cusp_forms(Gamma(10^28+731))                             
CPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s
Wall time: 1.54 s
36274370885528165103530592700784546931709800073501194539717685491542679896172544001
```

(and most of that is the time taken to factor the level). I propose closing this as fixed.


---

Comment by AlexGhitza created at 2013-07-22 16:41:40

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2013-07-22 16:41:40

Agreed.


---

Comment by AlexGhitza created at 2013-07-22 16:41:40

Changing type from enhancement to defect.


---

Comment by AlexGhitza created at 2013-07-22 16:46:51

Changing keywords from "" to "sd51".


---

Comment by jdemeyer created at 2013-08-13 08:46:45

Resolution: duplicate
