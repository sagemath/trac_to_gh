# Issue 1471: moving a sage install breaks clisp

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-12 09:36:13

Assignee: mabshoff

Moving a Sage install breaks clisp. I moved `sage-2.9.alpha5` to `sage-2.9.alpha5-vg` and it broke clisp:

```
mabshoff`@`sage:/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5-vg$ clisp
clisp: /tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/local/lib/clisp/base/lisp.run: No such file or directory
```

I have no clue how Maxima still manages to work, but there must be a fix somehow.

Cheers,

Michael


---

Comment by jsp created at 2007-12-22 19:15:45

Since sage-2.9.1.alpha3 this issue seems to be gone, maybe earlier? My standard procedure now is to relocate my installed sage before I do a make check.

clisp just worked

Jaap


---

Comment by mabshoff created at 2008-01-02 21:41:59

I still see the problem with Sage 2.9.1.1. I assume you might have some other sage install in the right location, so you don't see the problem. I needed to adapt maxima to use `clisp.bin` instead of clisp (the default) to build. The following two spkgs fix the problem:

 * http://sage.math.washington.edu/home/mabshoff/clisp-2.41.p12.spkg
 * http://sage.math.washington.edu/home/mabshoff/maxima-5.13.0.p2.spkg

Cheers,

Michael


---

Comment by mhansen created at 2008-01-03 07:07:24

Michael, your spkgs fixed the problem for me.


---

Comment by mabshoff created at 2008-01-03 07:16:52

Resolution: fixed


---

Comment by mabshoff created at 2008-01-03 07:16:52

Merged in 2.9.2.alpha0
