# Issue 4620: setup.py: if the cythonization fails then next "sage -b" starts to build extensions

Issue created by migration from https://trac.sagemath.org/ticket/4620

Original creator: mabshoff

Original creation time: 2008-11-25 23:19:49

Assignee: craigcitro

This is with 3.2.1.alpha1-current. To reproduce do a "sage -ba" and have a Cython process fail. Then the next "sage -b" will not pick up with the Cythonization again, but start building extensions.

Deleting .cython_deps does not fix the problem.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-11-26 08:49:30

The attached patch fixes the issue. The problem was that we were copying the files at one point in the code, and then running Cython later. Of course, if Cython failed, the code was still copied, which meant it would pass a timestamp comparison on later builds. The patch fixes this by only copying once the file is successfully built. 

In addition, it slightly expands the capabilities of William's parallel build code: now, in addition to accepting strings, it accepts pairs of the form `[f, v]`, and calls `f(v)`. The previous code did this with `f` always being `run_command`.


---

Comment by craigcitro created at 2008-11-26 08:49:30

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-26 09:35:06

Nice work. Thanks for fixing this quickly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-26 09:35:20

Merged in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-26 09:35:20

Resolution: fixed
