# Issue 9488: [easy] parse make -j N as well as make -jN for parallel builds

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-07-13 05:17:47

Assignee: GeorgSWeber

The code in setup.py to pull the parallelization parameter out of the MAKE environment variable can't handle the extra space, but could easily be re-written. 


---

Comment by drkirkby created at 2010-07-13 07:11:57

To work in accordance with the man page for GNU make, the following should also be acceptable


```
make -j
```


in which case the number of threads is infinite - i.e. limited only by what the build system allows.


---

Comment by jdemeyer created at 2013-05-19 13:10:43

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:10:43

This already works.


---

Comment by jdemeyer created at 2013-05-19 13:10:52

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:22:48

Resolution: worksforme
