# Issue 2009: crap -- networkx spkg in sage-2.10.1.rc3 contains a bunch of .svn directories

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 23:20:41

Assignee: mabshoff


```
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/scripts/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/tests/readwrite/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/tests/generators/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/tests/drawing/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/tests/data/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/tests/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/readwrite/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/generators/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/drawing/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/networkx/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/doc/NEP/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/doc/examples/.svn
sage-2.10.1.rc3/spkg/standard/networkx-0.36.p0/src/doc/.svn
```



---

Comment by mabshoff created at 2008-01-31 23:41:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-31 23:41:40

An update spkg with the .svn directories removed is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/networkx-0.36.p1.spkg

The .svn directories totaled 3MB uncompressed!

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-01 02:01:01

Merged in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-02-01 02:01:01

Resolution: fixed
