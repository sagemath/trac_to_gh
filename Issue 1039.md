# Issue 1039: [with patch] Dokchitser L-series of number field

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2007-10-31 17:37:07

Assignee: was

wrapper for Dokchitser L-series of a number field, so that one can do the following:


```
sage: K.<a> =NumberField(x^2+x-1)
sage: L = K.Lseries_dokchitser()
sage: L(-1)
0.0333333333333333
```



---

Attachment

I will take a look at this soon.


---

Comment by was created at 2007-11-01 08:11:25

Apply this patch instead.


---

Attachment

applied to 2.8.11.alpha0


---

Comment by mabshoff created at 2007-11-01 09:27:01

Resolution: fixed
