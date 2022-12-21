# Issue 298: autotesting of examples

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-27 02:21:54

Assignee: was

CC:  kini jdemeyer

** get Rishi's autotesting of examples directory to work: He developed it under OS X, but it doesn't work on Linux because of differences in how they run scripts, etc.  Plus, it's a really hard challenge to create such automated testing, so it needs to be looked over again.  
 


---

Comment by mabshoff created at 2008-04-19 21:38:24

Changing priority from major to critical.


---

Comment by mabshoff created at 2008-04-19 21:38:24

Where is that code? Does that mean that we want to be able to run the doctests in examples? Then certainly this ought to be of much higher priority since the examples *must* work with the version of Sage that shipped it.

Cheers,

Michael


---

Comment by jason created at 2009-11-19 22:42:37

This looks invalid or maybe even done.


---

Comment by was created at 2009-11-19 22:46:36


```
wstein:
Why do you think #298 should be closed?
[2:45pm] wstein:
It's more important than ever to fix.
[2:45pm] jason-:
I thought it was talking about doctesting, basically
[2:45pm] wstein:
There is a directory SAGE_ROOT/examples.
[2:45pm] wstein:
That code isn't tested at all.
[2:45pm] jason-:
to quote the comment, "where is that code"?
[2:45pm] wstein:
It's a terrifying disaster.
[2:45pm] jason-:
oh, okay
[2:45pm] jason-:
never mind
[2:46pm] wstein:
I can't believe I still haven't dealt with this... but oh well.
[2:46pm] wstein:
It's one of those things that looks easy until you try it.
```



---

Comment by was created at 2009-11-19 23:27:57

See the related ticket #7494.  If that is closed, then this ticket is certainly invalid.


---

Comment by jhpalmieri created at 2011-10-08 17:14:17

Since #7494 has been closed, I think this can be, too.


---

Comment by kini created at 2011-10-10 09:10:43

Yes.


---

Comment by kini created at 2011-10-10 09:10:43

Changing status from new to needs_review.


---

Comment by kini created at 2011-10-10 09:10:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-10-10 13:35:27

Resolution: wontfix
