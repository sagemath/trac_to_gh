# Issue 609: make lie part a standard SAGE package

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-07 01:04:33

Assignee: mabshoff

Either remove the dependency on curses, or make curses a standard sage package.  Test building on more architectures.

And, there should be some sort of voting on this in sage-devel by the people who would maintain it.


```
18:01 < sage> it's different.
18:01 < sage> getting it to build is different than moving it into standard.
18:01 < mabshoff> So we use ncurses for now, but once it becomes standard we should remove the dependency.
18:01 < sage> moving into standard presupposes removing dependencies, worrying about longterm quality and
              stability, etc.
}}}}


---

Comment by mabshoff created at 2007-09-07 01:05:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-02 03:07:19

I am not sure this is desired any longer. William?

Cheers,

Michael


---

Comment by wdj created at 2008-08-02 11:51:54

You could also ask, for example, Dan Bump or Mike Hansen how much the combinat code covers the computations implemented in lie.


---

Comment by was created at 2008-08-03 17:25:16

This is definitely not desired anymore.  Lie is not maintained or developed anymore.


---

Comment by was created at 2008-08-03 17:25:16

Resolution: invalid
