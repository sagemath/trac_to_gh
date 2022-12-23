# Issue 5529: bring documentation of classical.py to 100%

Issue created by migration from https://trac.sagemath.org/ticket/5529

Original creator: mvngu

Original creation time: 2009-03-16 10:44:03

Assignee: tba

Keywords: classical.py, doctest

As the subject says.


---

Attachment


---

Comment by mvngu created at 2009-03-16 10:47:13

The patch *trac_5529_doc.patch* should bring the documentation coverage of `sage.crypto.classical.py` to 100%... woo hoo...


---

Comment by jhpalmieri created at 2009-03-23 02:46:04

Looks good, mostly.  I've made a few small changes and a few bigger ones.  The small changes: I changed "EXAMPLE::" to "EXAMPLES::" several times.  I changed "\mathbb{Z}" to "\mathbf{Z}" since this is the Sage style: try `latex(ZZ)`.  One line wasn't indented quite far enough, and I did a little minor rewording.

The more major changes: in the reference manual, methods which begin with an underscore don't appear.  For the most part, this doesn't bother me, but `__init__` methods often have important documentation, so for this file, I moved the docs for the `__init__` methods up a level to documentation for the class. This way it appears in the reference manual (as the first thing for the class) and also when you run sage and type `HillCryptosystem?`, for example.

I give mvngu's part of this a positive review, so only my patch needs reviewing.


---

Attachment

apply this on top of the other patch


---

Comment by mvngu created at 2009-03-23 05:27:05

The patch *5529-new.patch* applies fine against Sage 3.4, all doctests passed even with `-long` option. Rebuilding the HTML version of the reference manual, I see that documentation of many `_init__` methods are now visible. So positive review for jhpalmieri's part.


---

Comment by mabshoff created at 2009-03-23 21:02:06

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 21:02:06

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
