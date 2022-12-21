# Issue 5686: mpi4py is very outdated

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2009-04-04 22:55:34

Assignee: mabshoff

mpi4py in the optional package is version 0.3.1, while the newest version is 1.0.0.


---

Comment by mabshoff created at 2009-04-04 23:08:22

Changing component from optional packages to experimental package.


---

Comment by mabshoff created at 2009-04-04 23:08:22

mpi4py is experimental, not optional.

Cheers,

Michael


---

Comment by syazdani created at 2009-04-05 19:29:00

I have an .spkg for this package now. Here is the link:
http://sage.math.washington.edu/home/syazdani/mpi4py-1.0.0.spkg

Soroosh


---

Comment by was created at 2009-12-16 02:03:17

I've created a new version here:

  http://sage.math.washington.edu/home/wstein/patches/mpi4py-1.1.0.spkg


To build it and test do:


```
sage -i openmpi-1.1.4 mpi4py-1.1.0.spkg
```


Then


```
sage: import mpi4py
sage: help(mpi4py)
```


Note: I will also update openmpi spkg at #7701


---

Comment by was created at 2009-12-16 02:04:56

Changing status from new to needs_review.


---

Comment by syazdani created at 2009-12-17 21:20:23

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-19 05:22:40

Resolution: fixed


---

Comment by was created at 2009-12-19 05:22:40

I posted the spkg.
