# Issue 6308: [with spkg, needs review] Fix scipy spkg to play nicely with gfortran and g95

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-06-16 06:32:32

Assignee: mabshoff

CC:  jason jkantor wstein

Keywords: scipy

The new `scipy-0.7.spkg` from #3391 is great -- except that it accidentally forgets to include a fix to `scipy.optimize.optimize` if `gfortran` is used instead of `g95`. There's a new spkg up that fixes that here: 

  http://sage.math.washington.edu/scratch/craigcitro/patches/scipy-0.7.p1.spkg 

Indeed, I spoke with Jason Grout, and he confirmed that the new `optimize.py` should be patched in regardless of what fortran compiler we use.

I'm adding a few potential reviewers to the cc.


---

Comment by craigcitro created at 2009-06-16 06:34:52

Oh, I should say: I've tested this on both `sage.math` and `cleo` on skynet, which uses `gfortran` -- it worked fine in both cases.


---

Comment by craigcitro created at 2009-06-18 02:06:57

Resolution: fixed
