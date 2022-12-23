# Issue 8295: Documentation for Kazhdan-Lusztig polynomials and Iwahori Hecke algebras

Issue created by migration from https://trac.sagemath.org/ticket/8295

Original creator: bump

Original creation time: 2010-02-17 18:24:49

Assignee: AlexGhitza

CC:  sage-combinat

Adds documention for new files `kazhdan_lusztig.py` and `iwahori_hecke_algebras.py` to reference manual.


---

Attachment

Add documentation for new files to reference manual


---

Comment by bump created at 2010-02-17 18:29:33

Changing status from new to needs_review.


---

Comment by bump created at 2010-02-17 18:29:33

Changing priority from major to minor.


---

Comment by bump created at 2010-02-18 00:10:04

Changing component from algebra to documentation.


---

Comment by bump created at 2010-02-18 00:10:04

Changing assignee from AlexGhitza to bump.


---

Comment by mvngu created at 2010-02-20 12:07:10

Looks good. The documentation for these two modules now appear in the reference manual:

 * `sage/algebras/iwahori_hecke_algebra.py`
 * `sage/combinat/kazhdan_lusztig.py`

The module `sage/combinat/kazhdan_lusztig.py` has some bad ReST formatting, which results in a warning when building the reference manual. See #8310 for a patch to fix this.


---

Comment by mvngu created at 2010-02-20 12:07:10

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 22:15:35

Daniel: The patch doesn't contain your username. I have merged [trac_8295_doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8295/trac_8295_doc.patch) in your name.


---

Comment by mvngu created at 2010-03-02 22:15:35

Resolution: fixed
