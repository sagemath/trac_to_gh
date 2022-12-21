# Issue 5169: make it possible to set the default search path for the attach and load commands

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-03 23:34:10

Assignee: cwitty

This was requested by nihilalienumcredo in sage-support.  He wants to be able to do


```
sage: set_attach_path('/foo/bar/')
sage: attach file.sage
```

and have it work from any location so long as /foo/bar/file.sage exists. 


---

Comment by mabshoff created at 2009-02-03 23:36:12

See the thread at

 http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090128.spkg

for details.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 00:42:43

Oops, see the thread at

  http://groups.google.com/group/sage-support/t/37795251481402a1

for details. 

Note to self: First check post, *then* hit button :)

Cheers,

Michael


---

Comment by timdumol created at 2010-01-17 09:12:39

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-01-22 04:12:51

Closely related: #378, #1484


---

Comment by mpatel created at 2010-02-16 00:05:05

I'm closing this as a duplicate of !#378.


---

Comment by mpatel created at 2010-02-16 00:05:05

Resolution: duplicate
