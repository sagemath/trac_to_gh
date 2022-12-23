# Issue 8025: artificially bump the version number of the scipy and scipy_sandbox spkg's

Issue created by migration from https://trac.sagemath.org/ticket/8025

Original creator: was

Original creation time: 2010-01-21 16:05:00

Assignee: GeorgSWeber




---

Comment by was created at 2010-01-21 16:08:17

Definitely "sage -upgrade" doesn't work right now (from 4.3 to 4.3.1).  
Definitely doing


```
  sage -f spkg/standard/scipy_sandbox-20071020.p4.spkg
  sage -f spkg/standard/scipy-0.7.p3.spkg
```

fixes the problem.  But I'm confused since scipy and scipy_sandbox depend on fortran, so they should be forced to be rebuilt anyways.  Hmm..


---

Comment by was created at 2010-01-21 16:20:49

More precisely, the following fixes the problem:

```
./sage -f numpy-1.3.0.p2.spkg scipy_sandbox-20071020.p4.spkg scipy-0.7.p3.spkg
```



---

Comment by jhpalmieri created at 2010-04-23 04:57:06

Deferred to Sage 5.0 since I don't see a patch or new spkg's.


---

Comment by was created at 2010-06-03 03:57:22

Resolution: fixed


---

Comment by was created at 2010-06-03 03:57:22

I've bumped both spkg version numbers, as requested, for sage-4.4.3.alpha2.
