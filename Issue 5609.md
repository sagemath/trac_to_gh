# Issue 5609: [with patch, needs review] some functions for BooleanPolynomialIdeal

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-03-25 16:00:22

Assignee: malb

CC:  polybori burcin rpw

Keywords: polybori

Added `interreduced_basis()` and `__cmp__()` functions to `BooleanPolynomialIdeal`. 


---

Comment by malb created at 2009-03-25 16:01:30

the attached patch depends on #5586 and #5576


---

Comment by burcin created at 2009-03-25 18:10:20

Just a question after reading the patch: 

Why do you implement both `__cmp__()` and `__richcmp__()` in `BooleanPolynomialIdeal`? The doctests for these two functions also seem to be the same.


---

Comment by malb created at 2009-03-25 18:41:06

It is just because I am confused which one I have to implement (it seem Cython changed in that regard?)


---

Comment by malb created at 2009-04-27 13:08:52

I removed the `__richcmp__`, Burcin can you review this new patch?


---

Comment by malb created at 2009-05-12 01:16:09

rebased to 3.4.2


---

Attachment

rebased the attached patch to 3.4.2


---

Comment by burcin created at 2009-05-12 15:20:09

Looks good to me.


---

Comment by mabshoff created at 2009-05-12 21:47:10

This patch completely moves the docstring of two `__init__` methods to the class. Is that the desired effect, i.e. why not add back minimal doctests? I understand that underscore and double underscore methods aren't in the manual, but this makes a difference for -coverage and ought to be fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 21:50:10

Resolution: fixed


---

Comment by mabshoff created at 2009-05-12 21:50:10

Merged in Sage 4.0.alpha0.

Cheers,

Michael
