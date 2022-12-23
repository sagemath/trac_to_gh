# Issue 1724: Creating ModularForms from q-expansions

Issue created by migration from https://trac.sagemath.org/ticket/1724

Original creator: ljpk

Original creation time: 2008-01-08 21:20:05

Assignee: was

There is a way of creating modular forms from their Fourier expansions; for instance


```
S12=CuspForms(1,12)
PSR.<q>=PowerSeriesRing(QQ)
S12(q- 24*q^2 + 252*q^3 - 1472*q^4)
```

gives

```
q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
```


However, one needs strictly more than the Sturm bound's worth of Fourier coefficients to make this work:

```
S12(q+O(q^2))
```

gives

```
Exception (click to the left for traceback):
...
TypeError: q-expansion needed to at least precision 4
```


... as here the Sturm bound is 1.


---

Comment by craigcitro created at 2008-01-21 08:46:00

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-01-21 08:46:00

Changing assignee from was to craigcitro.


---

Attachment

This fixes the above bug. It also smooths out a few issues to do with the following: at  various places in the modular forms code, it seems that self.prec() is used where self.sturm_bound() is what we really want. There may be more of these that are hard to track down -- for instance, one might use self.basis()[0].prec(), etc.


---

Comment by craigcitro created at 2008-01-21 08:46:42

Oops -- I forgot to mention, this patch will only apply to a branch that already has the patches for #1844 applied.


---

Comment by AlexGhitza created at 2008-01-25 23:06:47

Looks good to me.


---

Comment by mabshoff created at 2008-01-25 23:21:23

Resolution: fixed


---

Comment by mabshoff created at 2008-01-25 23:21:23

Merged in Sage 2.10.1.alpha2
