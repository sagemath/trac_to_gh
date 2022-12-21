# Issue 4154: setting defaults for show options

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-09-19 22:28:23

Assignee: was

There ought to be a way to set defaults for the options to show.  Even just a dictionary in sage.plot.plot would be nice.

A use-case would be setting the default aspect ratio to 1 so that if you are plotting lots of circles, it looks okay.


---

Comment by jason created at 2008-09-26 22:39:17

See #4201 for a nice way to do this.


---

Comment by novoselt created at 2010-11-19 02:45:37

I guess

```
sage.plot.plot.Graphics.SHOW_OPTIONS["aspect_ratio"] = 1
```

does what was requested in this ticket (although I don't think that it is the best way).

I am switching this ticket to positive review so that release managers can close it appropriately.


---

Comment by novoselt created at 2010-11-19 02:45:37

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-11-19 02:45:48

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-11-19 02:50:56

I agree with your assessment.

If you're interested in reviewing a ticket that deals with setting aspect ratios to more sensible defaults, and clarifying what Sage/Matplotlib means by aspect ratio, #2100 is up for review.


---

Comment by jdemeyer created at 2010-11-21 08:59:19

Resolution: duplicate
