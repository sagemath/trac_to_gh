# Issue 2475: doctest -- get coverage of modular/dims.py up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/2475

Original creator: was

Original creation time: 2008-03-11 23:06:58

Assignee: was

When I started this (sage-2.10.3):

```
dims.py
SCORE dims.py: 11% (6 of 54)
```



---

Comment by was created at 2008-03-12 01:08:47

SCORE dims.py: 31% (17 of 54); and I fixed a serious bug in p-new subspace!


---

Attachment

this brings coverage to 100% and fixes a serious bug.


---

Attachment

To referee these patches:
  1. verify that they fix the coverage to 100%
  2. look for typos in the docstrings
  3. The p-new subspace "serious bugfixes" make it so one doesn't get negative dimensions.  This was because the old new subspace code subtracted off the images of old subspaces from the tiny little new subspace instead of subtracting off from the ful l cuspidal subspace. 
  4. This is almost all docstring addition and fixing return types to be Integer.

After applying these two patches:

```
teragon:modular was$ sage -coverage dims.py
----------------------------------------------------------------------
dims.py
SCORE dims.py: 100% (46 of 46)
----------------------------------------------------------------------
```



---

Attachment


---

Comment by craigcitro created at 2008-03-15 08:01:08

Looks good. Changed a few comments in doctests, touched up a few things.


---

Comment by craigcitro created at 2008-03-15 08:18:23

I forgot an `r` on the docstring for `mu30`. mabshoff is correcting this when he merges.


---

Attachment


---

Comment by mabshoff created at 2008-03-15 08:32:39

Resolution: fixed


---

Attachment

Merged all six patches in Sage 2.10.4.alpha0
