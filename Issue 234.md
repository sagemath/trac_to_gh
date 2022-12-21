# Issue 234: Lie -- create a SAGE wrapper for computing with lie groups

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-30 19:47:12

Assignee: was

There is an amazing program called Lie for computing with compact Lie groups.
It's available as an optional sage package, e.g., 

```
   sage -i lie-2.2
```


(But check to see if this is the latest version...)

Anyway, for this project, research ways to make a SAGE <--> Lie interface.
Via pexpect?  Via C library? ???


---

Comment by mabshoff created at 2007-08-24 21:41:25

Hello,

Mike Hansen opened ticket #489 about the same issue. That ticket now has some more info on issues regarding compilation. So I close this ticket as a duplicate instead of the other way around.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-24 21:41:25

Resolution: duplicate
