# Issue 5493: [with patch, needs review]

Issue created by migration from https://trac.sagemath.org/ticket/5493

Original creator: malb

Original creation time: 2009-03-11 23:03:38

Assignee: malb

Keywords: sphinx, crypto

The attached patch makes the Sphinx output for `mq.SR` look much nicer.


---

Attachment

yay, my first sphinx patch


---

Comment by mvngu created at 2009-03-16 07:50:50

REFEREE REPORT



The patch *sr_sphinx.patch* applied fine against Sage version 3.4. All tests passed, even with the `-long` option. The reference manual (which the patch touches) builds OK and looks rather prettier, which is what Martin wants :-)  Positive review.



Note that while reviewing this ticket, I also noticed some further enhancements that can be done to `sr.py`. But these are addressed in ticket #5527.


---

Comment by mabshoff created at 2009-03-20 20:50:41

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-20 20:50:41

Resolution: fixed
