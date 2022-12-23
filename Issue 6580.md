# Issue 6580: ratpoints -- this must be fixed to build with gcc-3.4.x

Issue created by migration from https://trac.sagemath.org/ticket/6580

Original creator: was

Original creation time: 2009-07-21 16:40:22

Assignee: rlmillster

We let ratpoints get in, and nobody thought to check that it actually builds with gcc-3.4.x.  Well, it doesn't.  This needs to get fixed. 


---

Comment by rlm created at 2009-07-21 20:30:58

If someone would like to point me to a machine with gcc-3.4.x, I'd gladly troubleshoot this.


---

Comment by rlm created at 2009-07-21 20:30:58

Changing assignee from rlmillster to rlm.


---

Comment by cremona created at 2009-08-16 20:21:43

I want to start using ratpoints in some elliptic curve code as it is so efficient.  Should I wait until it compiles on these other machines?

In the meantime the interface to ratpoints which rlm wrote can be enhanced in various ways, (e.g. to list only integral points) and that need not wait.


---

Comment by mvngu created at 2009-09-27 06:20:04

At #7021, drkirkby updates prereq to 0.4 and writes "If gcc is used as the C compiler, the configure script checks it is at least gcc 4.0.1." Does this updated spkg invalidate this ticket? Here's a conversation on IRC:

```
23:14 < mvngu> williamstein: At #7021, I see drkirkby's note "If gcc is used as 
               the C compiler, the configure script checks it is at least gcc 
               4.0.1". This makes me wonder about the GCC 3.4.x requirement at 
               #6580.
23:14 < williamstein> good point.
23:15 < williamstein> maybe we should just move ahead and forget about 
                      supporting gcc-3.4.
23:15 < williamstein> I would be ok with that.
23:15 < williamstein> in which case 6580 could be invalidated.
23:15 < mvngu> williamstein: I don't know of any machine using GCC 3.4.x.
23:15 < williamstein> yep
23:15 < williamstein> that's why we didn't notice until after the release.
```



---

Comment by drkirkby created at 2009-09-28 10:50:01

If anyone wants to find a machine with gcc 3.4.x, then 't2' has it. Just make sure that the GNU compilers at /usr/sfw/bin/ are first in your path, as specifying CC and CXX will not work, as numerous packages ignore CC and CXX.

Dave


---

Comment by kcrisman created at 2012-06-01 19:08:29

Given that this is three years old and Sage does now build on Solaris and that Sage even builds its own GCC if we have too old of a GCC (in fact, even for newer ones than 4.0.1), this ticket should probably be closed.


---

Comment by kcrisman created at 2012-06-01 19:08:29

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-06-01 19:08:43

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:32:18

Resolution: wontfix
