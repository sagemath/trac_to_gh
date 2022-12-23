# Issue 3407: [with patch, needs review] better error handling for GB calculations

Issue created by migration from https://trac.sagemath.org/ticket/3407

Original creator: malb

Original creation time: 2008-06-12 22:42:15

Assignee: malb

CC:  cremona wstein mhansen

** bail out of toy_buchberger if the term ordering is unknown
 * bail out of Singular conversion if number field is relative. Singular supports this, but our conversion not just yet.


---

Attachment


---

Comment by craigcitro created at 2008-06-15 21:54:18

Changing keywords from "" to "editor_malb".


---

Comment by malb created at 2008-06-16 03:28:38

IIRC mhansen wants to review it. mhansen can you confirm or deny.


---

Comment by mhansen created at 2008-06-16 03:33:02

Yep -- I'll do it in the next hour.


---

Comment by mabshoff created at 2008-06-23 08:47:48

I am seeing doctest failures:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 13 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 13 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed
```

#3406 shows issue in similar areas.

Cheers,

Michael


---

Comment by malb created at 2008-06-23 17:45:24

After fixing #3406.


```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
----------------------------------------------------------------------
All tests passed!
```


Since this patch depends on #3406 anyway, I'll add the positive review back.


---

Comment by mabshoff created at 2008-06-25 00:39:36

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-25 00:39:36

Resolution: fixed
