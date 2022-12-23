# Issue 7699: Delete OS X metadata in lcalc spkg

Issue created by migration from https://trac.sagemath.org/ticket/7699

Original creator: was

Original creation time: 2009-12-16 01:26:02

Assignee: tbd


```
      sage-4.3.rc0/spkg/standard/lcalc-20080205.p3/src/src/.DS_Store
      sage-4.3.rc0/spkg/standard/lcalc-20080205.p3/src/include/.DS_Store
```



---

Comment by was created at 2009-12-18 06:31:41

Changing status from new to needs_review.


---

Comment by was created at 2009-12-18 06:31:41

See http://wstein.org/home/wstein/patches/lcalc-20080205.p4.spkg for the new spkg.


---

Comment by drkirkby created at 2009-12-24 01:32:38

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2009-12-24 01:32:38

I'll give it a positive, as its clear you have just deleted some useless code. It builds on Solaris at least. 

I believe there was a comment on sage-devel about a lot of work being done on this package recently. Hopefully there will be another release, as this one generates a lot of warnings from g++. Sun's compiler will not compile it.


---

Comment by mhansen created at 2010-01-03 22:21:09

Resolution: fixed
