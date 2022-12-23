# Issue 2007: crap -- the R spkg contains precompiled java files

Issue created by migration from https://trac.sagemath.org/ticket/2007

Original creator: was

Original creation time: 2008-01-31 23:17:21

Assignee: mabshoff


```
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/tools/getsp.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/share/java/getsp.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/doc/html/search/Value.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/doc/html/search/Tracer.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/doc/html/search/SearchEngine.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/doc/html/search/IndexTable.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/doc/html/search/IndexStream.class
sage-2.10.1.rc3/spkg/standard/r-2.6.1.p14/src/doc/html/search/IndexEntry.class
```



---

Comment by mabshoff created at 2008-01-31 23:32:41

Changing status from new to assigned.


---

Comment by was created at 2008-03-12 05:00:02

This must be fixed!!


---

Comment by was created at 2008-03-12 05:00:02

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-07-19 13:17:44

William did remove the offending Java files in Sage 3.0.5.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-19 13:17:44

Resolution: fixed
