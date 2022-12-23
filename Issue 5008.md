# Issue 5008: Solaris/gcc 4.3.2: fix matplotlib build

Issue created by migration from https://trac.sagemath.org/ticket/5008

Original creator: mabshoff

Original creation time: 2009-01-18 06:31:49

Assignee: mabshoff

Matplotlib has some build problems on Solaris when using gcc 4.3.2 that do not happen on other platforms.

Spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 06:31:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-19 11:54:48

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/matplotlib-0.98.3.p5.spkg

adds a Solaris 10 specific workaround. On other platforms the workaround is not applied.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-19 11:58:29

Works fine for me.


---

Comment by mabshoff created at 2009-01-19 12:01:43

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 12:01:43

Resolution: fixed
