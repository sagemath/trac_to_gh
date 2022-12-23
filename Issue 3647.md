# Issue 3647: [with spkg, needs review] remove "- static-libgcc" from lcalc's CFLAGS

Issue created by migration from https://trac.sagemath.org/ticket/3647

Original creator: mabshoff

Original creation time: 2008-07-12 13:44:20

Assignee: mabshoff

At some point we added "-static-libgcc" to lcalc's CFLAGS. I am not so sure why we did it since the reasoning behind it is undocumented and I cannot imagine any reason why we should use it. This is causing trouble on some build platoforms, see

https://groups.google.com/group/sage-support/browse_thread/thread/a0e26173803f11d4/92f2602b2c448b59#92f2602b2c448b59

The spkg at

http://sage.math.washington.edu/home/mabshoff/lcalc-20080205.p2.spkg

removes that option.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-12 13:47:39

There is some interesting discussion why "-static-libgcc" seem to be a can of worms at

http://www.trilithium.com/johan/2005/06/static-libstdc/

Cheers,

Michael


---

Comment by mhansen created at 2008-07-16 04:51:56

+1


---

Comment by mabshoff created at 2008-07-16 05:12:41

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 05:12:41

Merged in Sage 3.0.6.alpha0
