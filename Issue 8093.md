# Issue 8093: Adding of prefixes and palindrome prefixes iterators to the Words library

Issue created by migration from Trac.

Original creator: abmasse

Original creation time: 2010-01-27 12:20:13

Assignee: abmasse

CC:  slabbe

Keywords: palindrome, prefix

Adds three functions to iterate over prefixes and palindrome prefixes of finite and infinite words.



---

Comment by abmasse created at 2010-01-29 09:30:22

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-01-31 22:52:32

Updated to synchronize with sage-combinat mercurial repository -- should be the same file


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-01-31 23:24:11

Changing status from needs_review to positive_review.


---

Attachment

All tests passed in sage/combinat/words. Doc builds fine. Code is good.

I added a small patch that edits the INPUT block and adds a TEST.

Positive review.


---

Comment by abmasse created at 2010-01-31 23:47:03

Alright with the modifs as far as I'm concerned.


---

Comment by mpatel created at 2010-02-11 14:47:23

Resolution: fixed


---

Comment by mpatel created at 2010-02-11 15:28:51

I'm updating the Author field per [the main wiki page](http://trac.sagemath.org/sage_trac/wiki).  Please let us know if they're wrong.


---

Comment by abmasse created at 2010-02-11 15:46:00

Thanks, this is indeed the right name (without dash).
