# Issue 2776: [with patch, needs review] simplify BooleanPolynomialRing constructor for enduser

Issue created by migration from https://trac.sagemath.org/ticket/2776

Original creator: malb

Original creation time: 2008-04-02 16:16:47

Assignee: malb

CC:  burcin

Keywords: polybori

This now works:

```
sage: B.<x,y,z> = BooleanPolynomialRing()
```



---

Attachment


---

Comment by mabshoff created at 2008-04-02 19:24:25

Patch looks good to me. Doctests pass for me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-02 19:25:45

Resolution: fixed


---

Comment by mabshoff created at 2008-04-02 19:25:45

Merged in Sage 3.0.alpha1
