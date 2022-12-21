# Issue 7321: numpy fails to build on cygwin due to not using the correct fortran compiler

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-27 05:17:15

Assignee: tbd

CC:  was

The solution is to add 'sage_fortran' to the beginning of the list of fortran compilers on the cygwin line in src/numpy/distutils/fcompiler/__init__.py


---

Comment by mhansen created at 2009-10-27 14:10:54

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-10-27 14:10:54

The spkg can be found a http://sage.math.washington.edu/home/mhansen/numpy-1.3.0.p3.spkg


---

Attachment


---

Attachment


---

Comment by pjeremy created at 2010-01-03 23:38:07

trac_7321-1.patch appears to already be part of numpy-1.3.0.p2 and I won't comment on it.

trac_7321-2.patch appears to be correct and I'll give it a positive review.

OTOH, comparing numpy-1.3.0p2.spkg in sage-4.3 with mhansen/numpy-1.3.0.p3.spkg shows a number of other differences which shouldn't be present:
   * Various emacs backup files (*~) exist
   * Various *.pyc files exist
   * patches/cygwin-core-setup.py has been copied to src/numpy/core/setup.py
   * patches/!__init!__.py has been copied to src/numpy/distutils/fcompiler/!__init!__.py
   * patches/gnu.py has been copied to src/numpy/distutils/fcompiler/gnu.py
   * patches/cygwin-lapack_lite-setup.py has been copied to src/numpy/linalg/setup.py
   * src/site.cfg exists
   * src/build exists
Overall, your numpy-1.3.0.p3.spkg needs rerolling to only include the changes in trac_7321-2.patch


---

Comment by pjeremy created at 2010-01-03 23:38:07

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2010-04-06 18:44:03

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-04-06 18:44:03

I've posted a new spkg based on p2 with only trac_7321-2.patch applied.  That should address the above concerns.


---

Comment by was created at 2010-04-27 00:10:55

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:05:53

Resolution: fixed
