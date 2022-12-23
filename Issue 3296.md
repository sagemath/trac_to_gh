# Issue 3296: polymake spkg needs "CDDLIB_VERSION='094b.p2" in spkg-install

Issue created by migration from https://trac.sagemath.org/ticket/3296

Original creator: mhampton

Original creation time: 2008-05-25 02:34:07

Assignee: mabshoff

Keywords: polymake, cddlib

The short summary describes both the problem and solution.  I could post a new spkg but its almost easier to change that one line.


---

Comment by mabshoff created at 2008-05-25 02:36:47

Instead of patching polymake each time cddlib changes you should use the following construct:

```
spkg/standard$ ./newest_version cddlib
cddlib-094b.p2
```

That way it keeps working ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-25 02:39:24

The same applies to the gmp, too. Either way, the polymake spkg-install is a mess. In fact the polymake.spkg violates a copious amount of other rules. So while I am at it I might as well update the the polymake 2.3 release.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-25 02:39:24

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-31 01:27:36

#3640 will shortly have a working polymake.spkg, so I am closing this as a duplicate.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 01:27:36

Resolution: duplicate
