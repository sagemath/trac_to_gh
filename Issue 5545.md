# Issue 5545: bug in sage's Cython dependency tracker

Issue created by migration from https://trac.sagemath.org/ticket/5545

Original creator: cwitty

Original creation time: 2009-03-17 06:22:21

Assignee: mabshoff

To reproduce: Start with Sage 3.4.  Apply the attached patch (dependency-tracker-bug-testcase.patch).  Rebuild with "sage -b", then run Sage.  Type:

```
sage: import sage.rings.polynomial.real_roots
```

You will get an error:

```
TypeError: sage.rings.real_mpfi.RealIntervalField is not a type object
```

But if you touch real_roots.pyx and rebuild, the error goes away.

So somehow real_roots.pyx depends on real_mpfi.pyx in a way that the dependency tracker doesn't catch.  (It's not obvious how, because real_roots.pyx never even mentions `mpfi`.)


---

Attachment


---

Comment by jdemeyer created at 2014-09-02 09:19:21

worksforme:

```
jdemeyer@tamiyo:/usr/local/src/sage-git$ touch src/sage/rings/real_mpfi.pxd
jdemeyer@tamiyo:/usr/local/src/sage-git$ ./sage -b
scons: `install' is up to date.
Updating Cython code....
Enabling Cython debugging support
Compiling sage/rings/complex_interval.pyx because it depends on ./sage/rings/real_mpfi.pxd.
Compiling sage/rings/real_mpfi.pyx because it depends on sage/rings/real_mpfi.pxd.
Compiling sage/rings/polynomial/real_roots.pyx because it depends on ./sage/rings/real_mpfi.pxd.
[...]
```



---

Comment by jdemeyer created at 2014-09-02 09:19:21

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-09-02 09:19:26

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-09 14:52:58

Resolution: worksforme
