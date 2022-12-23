# Issue 1108: mysterious sfa doctest failure on OSX 10.5

Issue created by migration from https://trac.sagemath.org/ticket/1108

Original creator: mabshoff

Original creation time: 2007-11-05 23:17:05

Assignee: was

From rpw:

```
All my tests so far have shown that devel/sage-main/sage/combinat/
sfa.py fails with a SIGSEGV (both on ppc and Intel, both on 10.5 and  
10.4). Is this a known problem? I haven't been able to find any ticket  
about this in the TRAC.
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-05 23:17:38

Changing assignee from was to failure.


---

Comment by mabshoff created at 2007-11-05 23:17:38

Changing component from algebraic geometry to doctest.


---

Comment by mabshoff created at 2007-11-24 02:14:48

This is no longer an issue. So let's close this.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:38:39

This issue has been solved upstream some time ago. It works on OSX 10.5 and 10.5.1.

So close this,

Michael


---

Comment by mabshoff created at 2007-11-24 15:38:39

Resolution: fixed
