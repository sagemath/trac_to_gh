# Issue 6488: "sage -docbuild -help" doesn't mention the --jsmath option

Issue created by migration from https://trac.sagemath.org/ticket/6488

Original creator: rlm

Original creation time: 2009-07-08 20:20:40

Assignee: tba

CC:  mhansen mpatel

...so I don't know how to use it. :)


---

Comment by jhpalmieri created at 2009-07-22 02:51:11

Here's a patch.  Is it accurate (especially the part about having jsMath installed locally)?


---

Attachment

I apologize for not posting a note here earlier, but the latest changeset at #6187 "documents" the `--jsmath` flag and several new command-line options for `sage -docbuild`.  Of course, that approach may not be right, but if it's OK, should we modify it, instead?


---

Comment by jhpalmieri created at 2009-07-22 23:23:34

That's okay with me.


---

Comment by mhansen created at 2009-10-15 16:33:19

This can be closed since #6187 is closed.


---

Comment by mhansen created at 2009-10-15 16:33:19

Resolution: fixed
