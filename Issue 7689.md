# Issue 7689: cd spkg/; ./install scripts --- this results in an annoying (but harmless error message); get rid of it

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-15 19:39:08

Assignee: GeorgSWeber

An "official" way to setup the basic bootstrap for building Sage is to execute the following in an extracted Sage source tarball from SAGE_ROOT:

```
cd spkg/; ./install scripts
```


Doing so works, but unfortunately also results in:

```
...
python: can't open file '/scratch/wstein/build/x/sage-4.3.rc0/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
```


Fix this.  Get rid of this error message. 


---

Comment by jdemeyer created at 2013-12-29 23:21:40

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-29 23:21:40

Currently, `cd build; ./install scripts` doesn't work and it certainly isn't an "official" way to bootstrap anything.


---

Comment by jdemeyer created at 2014-01-04 00:04:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-04 02:38:21

Resolution: invalid
