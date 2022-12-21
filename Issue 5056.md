# Issue 5056: rename Ideal.reduced_basis to Ideal.interreduced_basis

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-01-22 18:34:52

Assignee: malb

CC:  john_perry

It seems like people get confused by the name and assume the function returns the reduced *Gröbner* basis. Thus `reduced_basis()` should be deprecated and `interreduced_basis()` should take its place.


---

Comment by john_perry created at 2009-01-22 23:09:38

"patch", not "path"


---

Attachment


---

Comment by SimonKing created at 2009-01-24 16:46:41

The patch applies cleanly (in spite of its strange name :) ), there is a deprecation warning, and the doc tests of `multi_polynomial_ideal.py` pass. In other words, the patch does what it is supposed to.
Positive review!


---

Comment by mabshoff created at 2009-01-25 02:21:05

Resolution: fixed


---

Comment by mabshoff created at 2009-01-25 02:21:05

Merged in Sage 3.3.alpha2.

Cheers,

Michael
