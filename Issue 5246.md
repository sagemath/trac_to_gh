# Issue 5246: installing R package in r.console() doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/5246

Original creator: schilly

Original creation time: 2009-02-12 15:59:42

Assignee: mabshoff

CC:  mhansen

from [public "report a problem" bugtracker in the notebook](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1234453264894000&pt=1234453244894000&diffWidget=true&s=AJVazbUgzUp_UbQ1kyziS_LZuaCZwUhLGA)

Installing CRAN packages with `r.console()` and then `install.packages()` fails with the error: 

"Can't open /home/was/build/sage-3.1.4/local/lib/R/share/sh/dcf.sh". *Strange enough, as the Sage version is 3.2.3, not 3.1.4.* This can be "fixed" by creating a symlink from /home/was/build/sage-3.1.4 to the real Sage installation, but it would be better if it worked out of the box. R without CRAN is not very useful.

---

Note by me: seems like there is something linked absolutely!


---

Comment by mabshoff created at 2009-02-12 16:21:56

This is from a binary not build by that person that seems to have been upgraded in place. I am not sure this is reproducible, so unless someone can either reproduce this or get the original reporter to give additional info this is "invalid" for me.

R in general does stupid things like ignore RHOME and R_HOME when using cran, so this might very well be an upstream bug.

In general bugs reported via "report a problem" should go to the groups first before anyone opens a ticket.

And this certainly isn't critical.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-12 16:21:56

Changing priority from critical to major.


---

Comment by kcrisman created at 2009-12-11 20:06:20

To release manager: I recommend this be closed, as it seems to be a duplicate of #4959.


---

Comment by kcrisman created at 2010-01-25 19:17:13

This is apparently fixed by #6532.


---

Comment by mvngu created at 2010-01-25 23:24:49

Resolution: duplicate


---

Comment by mvngu created at 2010-01-25 23:24:49

Close as duplicate of #4959.
