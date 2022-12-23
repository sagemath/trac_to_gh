# Issue 6155: fix stein-watkins huge optional database

Issue created by migration from https://trac.sagemath.org/ticket/6155

Original creator: was

Original creation time: 2009-05-30 03:52:10

Assignee: tbd


```
The full Stein-Watkins package fails to install cleanly on x86_64-
redhat-linux

http://modular.math.washington.edu/Tables/ecdb/stein-watkins-ecdb.spkg

The relevant lines from install-log seem to be:

mv: invalid option -- r
Try `mv --help' for more information.

Since the install script only moves some .bz2 files into the data
directory, it's easy to figure out how to do this by hand and after a
2.7Gb download, one is remarkably motivated to do so. So I'm a very
happy user of the database now. But William might want to fix the
install script ...

Cheers,

Nils
```



---

Comment by jdemeyer created at 2013-08-13 16:09:32

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-08-13 16:09:32

`http://modular.math.washington.edu/Tables/ecdb/stein-watkins-ecdb.spkg` still contains a broken package, but at least the updated one at http://www.sagemath.org/spkg/huge/stein-watkins-ecdb.spkg works.


---

Comment by jdemeyer created at 2013-08-13 16:10:45

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 11:12:07

Resolution: worksforme
