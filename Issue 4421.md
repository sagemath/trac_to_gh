# Issue 4421: create an optional singular_surf.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4421

Original creator: mabshoff

Original creation time: 2008-11-02 02:31:43

Assignee: mabshoff

We have removed the Java binaries required for surf (which is part of Singular). Since there are optional doctests in sage/rings/polynomial/multi_polynomial_ideal.py that depend on it and since people have complained about it not being available we should add it back via an optional spkg.

Cheers,

Michael


---

Comment by mderickx created at 2017-09-13 12:49:17

There is already a surf package so I think this can be closed. The surf package however doesn't build but we have #6316 for this. Putting up for review so someone else can look wether this can be closed.


---

Comment by mderickx created at 2017-09-13 12:49:17

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2017-09-13 18:05:25

Resolution: duplicate
