# Issue 6952: follow-up to #6774: fix warnings and stylistic niceties

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-17 23:02:29

Assignee: tba

CC:  ncohen jason

This is a follow-up to ticket #6774.


---

Comment by mvngu created at 2009-09-17 23:04:25

There's a warning when building the tutorial with the two patches at #6774:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/doc/en/tutorial/tour_graphtheory.rst:91: (WARNING/2) Title underline too short.

Compute maximum matchings
^^^^^^^^^^^^^^^^^^^
```

There are also some stylistic errors that I'll take care of.


---

Attachment

depends on #6774


---

Comment by mvngu created at 2009-09-17 23:58:09

Changing priority from major to minor.


---

Comment by jason created at 2009-09-19 02:57:02

Thanks! I learned a few things about writing in ReST from your patch.  I won't make those mistakes again (like enumerated lists).

This applied and looks fine.

I assume you merged the necessary patches to make the functions in these examples work.  They did not work for me with a copy of 4.1.1.alpha1.  So doctests really ought to be run on this file just to make sure that the examples are correct.


---

Comment by mvngu created at 2009-09-19 19:34:08

Resolution: fixed


---

Comment by mvngu created at 2009-09-19 19:34:08

Replying to [comment:3 jason]:
> I assume you merged the necessary patches to make the functions in these examples work. 
Yes, I tried that.




> So doctests really ought to be run on this file just to make sure that the examples are correct.
With other dependencies and this patch, all doctests in the tutorial pass.
