# Issue 4559: Merge commits from Jon Hanke's devel/sage/sage/quadratic_forms/genera/genus.py tree

Issue created by migration from https://trac.sagemath.org/ticket/4559

Original creator: mabshoff

Original creation time: 2008-11-20 00:30:15

Assignee: justin

There are a number of commits to devel/sage/sage/quadratic_forms/genera/genus.py

```
changeset:   10632:8403d5ca95be
tag:         tip
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Sun Nov 09 23:00:32 2008 -0800
summary:     Some changes to fix the segfault and add two interface routines.

changeset:   10628:05a3db2f6057
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Tue Apr 01 05:51:40 2008 +0200
summary:     Fixed signature name overloading bug in quadratic form genus routines, and also moved them to .pyx files.

changeset:   10626:dcad7b2c0a42
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Wed Mar 26 12:01:33 2008 +0100
summary:     Added a Hessian_matrix() routine for Quadratic forms, and added Nebe's correction of a typo in genus.py, and min
or interface changes.

changeset:   10597:f220b913963e
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Mon Nov 12 23:17:00 2007 +0100
summary:     Added updated genus code from David Kohel and Gabrielle Nebe (received Sept 6th, 2007).

changeset:   10569:8fa815df5c0c
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Tue Sep 04 00:09:12 2007 +0200
summary:     Added simple interface to QuadraticForm for the genus routines in quadratic_form/genera.
```



---

Comment by davidloeffler created at 2009-06-07 16:05:28

This is fixed via #5954, isn't it?


---

Comment by ncalexan created at 2009-06-15 15:52:45

Verified as fixed in 4.0.2.rc0.


---

Comment by ncalexan created at 2009-06-15 15:52:45

Resolution: fixed
