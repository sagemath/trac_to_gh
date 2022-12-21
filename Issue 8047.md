# Issue 8047: Sage 4.3.1 has both lapack-20071123.p0.spkg and lapack-20071123.p1.spkg

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-24 00:11:55

Assignee: tbd

CC:  georgsweber

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5dd9110f797f81d3):

```
I just noticed the following. In the Sage-4.3.1 source tarball, there
are both the packages "lapack-20071123.p0.spkg" as well as
"lapack-20071123.p1.spkg". If you build Sage from source, no problem
(yet), under /spkg/installed/ there will be only the newer "p1" spkg.
But if you "sage -bdist ..." a binary Sage distribution, then, under /
spkg/standard/, for both the "p0" and the "p1" spkg, a placeholder
file will be created (that shouldn't happen).

Worse, if I take this binary distribution, install Sage (elsewhere)
from that one, and issue "make test", then happily the "p0" lapack
spkg will not be found as installed (it isn't, "p1" is installed ---
but the "p0" shouldn't be looked for, which is bad), and then Sage
begins to download the "p0" one from the web and begins to build it
(deleting the files from the "p1" spkg first, according to the logs).
That should not happen at all!

I hardly got accustomed to the fact that "make test" in the above
situation will, at the beginning, output quite some crap, e.g. about
"circular dependencies dropped", and then rebuild just all of the
documentation files (taking a long time), for nothing --- these were
already provided. But trying to download older packages than the ones
provided, and installing these older ones over the newer ones is a bit
too ugly for my taste.

Did anyone experience the same problem(s)? We should create some
tickets, then.

Cheers,
Georg 
```



---

Comment by mvngu created at 2010-01-24 14:03:34

Here's a fix from [sage-devel](http://groups.google.com/group/sage-devel/msg/c566520ce6f51bb7):

```
This is now ticket #8047 [2]. Like the recent problem with Sage
4.3.1.alpha0 [3], a fix here is to delete lapack-20071123.p0.spkg from
SAGE_ROOT/spkg/standard (in the source tarball) and leave
lapack-20071123.p1.spkg alone.

[1] http://trac.sagemath.org/sage_trac/ticket/7943

[2] http://trac.sagemath.org/sage_trac/ticket/8047

[3] http://groups.google.com/group/sage-devel/msg/08cf0bd4afb3cf01 
```



---

Comment by mvngu created at 2010-01-24 14:05:27

I deleted lapack-20071123.p0.spkg per the above instructions.


---

Comment by mvngu created at 2010-01-24 14:05:27

Resolution: fixed
