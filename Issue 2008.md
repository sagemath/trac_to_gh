# Issue 2008: crap -- cython contains a stupid OSX file

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 23:20:03

Assignee: mabshoff

in Sage-2.10.1.rc3:


```
sage-2.10.1.rc3/spkg/standard/cython-0.9.6.11b/Includes/._.DS_Store
```



---

Comment by mabshoff created at 2008-01-31 23:32:01

An updated spkg with the offending file removed is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/cython-0.9.6.11b.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-31 23:32:08

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-01 02:00:47

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 02:00:47

Merged in Sage 2.10.1.rc4
