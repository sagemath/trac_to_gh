# Issue 1143: [with patch] improve nintegrate documentation in response to Paul Zimmerman's talk

Issue created by migration from https://trac.sagemath.org/ticket/1143

Original creator: was

Original creation time: 2007-11-11 11:32:47

Assignee: tba

CC:  jason




---

Attachment

Do not apply -- Paul points out that

```
Of course. It seems to me that **nintegral** calls Maxima and not GSL
(it is numerical_integral which calls GSL).

You might want to provide only one interface to numerical quadrature
(which might call GSL or Maxima or Pari with some options), and also
allow for arbitrary precision quadrature (it seems only Pari/GP allows this).
```

and he's right -- it's just calling maxima.  So the above patch would
actually break the docs!


---

Comment by mabshoff created at 2007-11-18 14:15:00

So, should be invalidate this or what is the solution to this ticket?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-12-02 20:23:23

Resolution: fixed


---

Attachment
