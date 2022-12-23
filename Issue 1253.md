# Issue 1253: make sage compile on OSX 10.5.1

Issue created by migration from https://trac.sagemath.org/ticket/1253

Original creator: mabshoff

Original creation time: 2007-11-24 12:51:24

Assignee: mabshoff

The checks for workarounds we implemented for 10.5 fail on 10.5.1 because we usually check for 

```
Darwin-9.0.0
```

But 10.5.1 is

```
Darwin-9.1.0
```

So far we need fixes for
 * gmp
 * python
But probably some more down the road. I am taking care of those.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:28:57

Ok, here we go with fixed spkgs:

http://sage.math.washington.edu/home/mabshoff/gmp-4.2.1.p12.spkg
http://sage.math.washington.edu/home/mabshoff/python-2.5.1.p9.spkg
http://sage.math.washington.edu/home/mabshoff/clisp-2.41.p11.spkg

Those will all be in rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:28:57

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-24 15:47:07

Resolution: fixed


---

Comment by mabshoff created at 2007-11-24 15:47:07

Merged in 2.8.14.rc1. Let's hope it still works on OSX < 10.5.1 :)

Cheers,

Michael
