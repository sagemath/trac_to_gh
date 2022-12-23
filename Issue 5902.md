# Issue 5902: [with patch, needs review] Try SAGE_ROOT as base of argument to "sage -t"

Issue created by migration from https://trac.sagemath.org/ticket/5902

Original creator: tabbott

Original creation time: 2009-04-26 05:51:28

Assignee: mabshoff

Running

```
sage -t devel/sage/sage/rings/polynomial/pbori.pyx
```

seems to not work for me sometimes when the current working directory is not SAGE_ROOT.  I don't really understand what is going wrong here, since there is a "cd" in $SAGE_ROOT/sage, but I've heard other people complain about issues with this.

The attached patch caused the problems to go away for me.


---

Comment by mhansen created at 2009-06-20 01:57:34

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-20 01:57:34

Changing status from new to assigned.


---

Attachment

Looks good to me!


---

Comment by was created at 2009-06-20 14:44:23

> Running
>
> sage -t devel/sage/sage/rings/polynomial/pbori.pyx
>
> seems to not work for me sometimes when the current working directory is not SAGE_ROOT.

It should not work.  "sage -t" is supposed to take the path to a file.  If you're not in SAGE_ROOT, then devel/sage/sage/rings/polynomial/pbori.pyx is not a file.  It's like with any other unix command.  E.g., you wouldn't expect 

```
cat devel/sage/sage/rings/polynomial/pbori.pyx
```

to magically work if you're not in SAGE_ROOT.

Note that Mike Hansen just gave this a positive review.  I strongly disagree.


---

Comment by tabbott created at 2009-06-20 15:33:35

Hi William,

My motivation for this change was that when you run "sage -testall", for each test it prints out what it is running as 

sage -t devel/sage/sage/rings/polynomial/pbori.py

since $SAGE_ROOT/sage changes directory to SAGE_ROOT before proceeding.

So that if you copy-and-paste that output from "sage -testall" to run the test a second time, it doesn't work.


---

Comment by boothby created at 2009-06-26 17:46:36

Resolution: fixed
