# Issue 7010: sanity check key value of the shift cryptosystem

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-25 07:13:23

Assignee: somebody

CC:  rbeezer

This is a follow up to ticket #6841.


---

Comment by mvngu created at 2009-10-04 16:00:10

clean up sage/crypto/classical.py so it conforms to coding conventions


---

Attachment

The patch `trac_7010-code-clean-up.patch` mainly cleans up the file `sage/crypto/classical.py` so it conforms to coding conventions. The clean up also removes the deprecated way of raising exceptions, and instead uses the way that is more compatible with Python 3.x.


---

Attachment

apply on top of previous patch


---

Comment by rbeezer created at 2009-10-05 05:02:05

Applies, builds, functions, docs build, passes long tests.

No substantial code changes in the clean-up, sanity-check completes making the shift-cipher (#6841) complete with regard to poor input.

Positive review.


---

Comment by mhansen created at 2009-10-15 10:04:52

Resolution: fixed
