# Issue 4313: Add some functionality to matrices in eclib

Issue created by migration from https://trac.sagemath.org/ticket/4313

Original creator: cremona

Original creation time: 2008-10-17 17:11:47

Assignee: was

CC:  jason

Keywords: eclib CremonaModularSymbols

The attached patch (based on 3.1.4) makes two changes in libs/cremona/mat*:
    1. Adds getitem methods to the matric class so i,j entries may be extracted;
    2. Changes the conversion to sage of matrices so that matrices over ZZ are constructed instead of ZZ.

These were done as part of a hands-on tutorial William gave to John in Bordeaux.


---

Attachment


---

Comment by craigcitro created at 2008-11-27 08:40:10

Code looks good. Only thing needed are some doctests on `__getitem__` in `mat.pyx` -- it would be nice to see a few doctests there, especially ones written to test weird corner cases.

(Also edited a typo in the description for this ticket.)


---

Attachment

Replace previous one with this


---

Comment by cremona created at 2009-05-30 15:43:34

I added a docstring for the getitem function with doctest, and also fixed one other doctest.  Now the coverage is 100% (though there is no loads(dumps) test).

Should work on 4.0.


---

Comment by rlm created at 2009-06-24 10:05:34

Resolution: fixed
