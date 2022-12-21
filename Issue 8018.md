# Issue 8018: Eigenvalues sorted, but not eigenvectors, in modular/modform/numerical.py

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-01-21 00:24:52

Assignee: craigcitro

CC:  was

In `sage/modular/modform/numerical.py`, the last half of `_eigenvectors` looks for eigenvectors with eigenvalues having multiplicty 1.  The eigenvalues get sorted for openers, but the eigenvectors in `B` don't follow along.

Print statements before and after the sort, and then running doctests on just this file, produces output like:


```
    Hecke: before sort [-283.0, 108.522012456, -92.2176402155, -90.3043722401, 142.0]
    Hecke: after sort [-283.0, -92.2176402155, -90.3043722401, 108.522012456, 142.0]
```


One fix would be to delete the sorting if the order of the eigenvectors is not important.

All the doctests in this module that call this code lack eigenvalues of multiplicity greater than 1, so maybe a new doctest could test this case.

Also, it appears the cached value returned differs from the return at the bottom of the function.


---

Comment by rbeezer created at 2010-01-24 05:25:05

This patch depends on #4756 due to intermediate changes in some of the CDF eigenvector code, so apply that patch first.  Since this patch computes the eigenvalues directly, it is not necessary to understand #4756.

Summary:

1.  Return value has changed to be the subset of eigenvectors with multiplicity one, rather than all the eigenvectors.  First few lines (immediate return without recalculation) indicate this was the intent.

2.  The eigenvalues do not get sorted now, fixing the observed bug.  An extra check of `uniq` will cause the loop to speed-up when the eigenvector has high multiplicity.

3.  Eigenvalues and eigenvectors are computed directly via `SciPy`.  This avoids various conversion overhead.

4.  Lots of blank lines marked as changed in the patch file.  An accident of a massive cut/paste job to recover from an error.


---

Comment by rbeezer created at 2010-01-24 05:25:05

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2010-04-03 07:53:56

Looks good.


---

Comment by AlexGhitza created at 2010-04-03 07:53:56

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:12:52

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 20:12:52

Merged "trac_8018-numerical-eigenforms.patch" in 4.4.alpha0
