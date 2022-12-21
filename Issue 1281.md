# Issue 1281: update compilation failure message with uptodate instructions

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-26 09:30:31

Assignee: mabshoff

CC:  was


```
[10:24] <mabshoff> I think we should change the failure message if Sage fails to compile to first check 
[10:24] <mabshoff> if it is the latest version and try that before contacting the lists
[10:25] <williamstein> sure.  make it so.
[10:25] <mabshoff> It should also mention to gzip up the log somewhere and post a link instead of sending 
[10:25] <mabshoff> a couple MB to 230+ people.
[10:25] <williamstein> agreed.
[10:25] <mabshoff> Ok, will open tichet.
```


Cheers,

Michael


---

Comment by timdumol created at 2010-01-16 07:59:17

Updates sage-spkg to ask the user to try installing the latest version of a package before asking for help.


---

Attachment

This patch should do the job.


---

Comment by timdumol created at 2010-01-16 07:59:54

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-17 18:20:08

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2010-01-17 18:20:08

I like the general idea, but if you're not online this gives a very verbose error message.


---

Comment by jdemeyer created at 2014-11-13 14:04:57

Changing component from packages: standard to build.


---

Comment by jdemeyer created at 2015-09-16 08:52:58

Is there currently still an easy way to determine if Sage is up-to-date?
