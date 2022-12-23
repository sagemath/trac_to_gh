# Issue 2088: Optional spkgs should be integrated into the automated cython building

Issue created by migration from https://trac.sagemath.org/ticket/2088

Original creator: jason

Original creation time: 2008-02-07 19:52:08

Assignee: mabshoff

There should be a way of building optional cython interfaces for optional spkgs in a way that is very easy for the user.  For example, it would be nice to have optional spkg cython things automatically built in the sage -b process.



---

Comment by jdemeyer created at 2013-08-13 15:44:58

I guess this works now, using

```
if is_package_installed('some_package'):
```

in `module_list.py`.


---

Comment by jdemeyer created at 2013-08-13 15:44:58

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-08-13 15:59:17

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 11:11:39

Resolution: worksforme
