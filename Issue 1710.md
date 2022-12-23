# Issue 1710: switch default location of trac server away from http://www.sagemath.org:9002/

Issue created by migration from https://trac.sagemath.org/ticket/1710

Original creator: malb

Original creation time: 2008-01-07 11:15:24

Assignee: was

If you use trac's RSS feed or the e-mails sent out by the trac server you always end up with URLs involving http://www.sagemath.org:9002/sage_trac/ which the firewall at my university doesn't like ... i.e. it is blocked.


---

Comment by malb created at 2008-01-13 11:36:19

Changing assignee from was to mabshoff.


---

Comment by was created at 2008-01-19 17:55:45

I just made an attempt to fix this by setting base_url.  Let's see if it works.


---

Comment by was created at 2008-01-19 17:58:26

OK, that didn't work, but it was a good start.  Maybe this will work?


---

Comment by was created at 2008-01-19 17:59:15

Resolution: fixed


---

Comment by was created at 2008-01-19 17:59:15

Pow, got it!
