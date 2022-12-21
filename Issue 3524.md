# Issue 3524: Buildbot

Issue created by migration from Trac.

Original creator: ghtdak

Original creation time: 2008-06-27 23:58:11

Assignee: ghtdak

CC:  mhansen mvngu drkirkby leif jdemeyer kini

In general, buildbot can be nasty in that its hugely configurable.  However, there's the "shellcommand" element which can do just about anything.

To start, we could shell getting the tarball, unwind it, make and make test.  As time progresses we could get fancier.


---

Comment by was created at 2008-06-28 12:29:17

I do not think this is sufficiently precise to be a trac ticket.  This should be made into a single precise clear task that somebody volunteers to do or closed as invalid.


---

Comment by ghtdak created at 2008-06-28 16:49:44

Buildbot Implementation Plan

1) Setup Buildbot master and slaves for release testing: Implement shellcommand interfaces to download, build and test candidate tarballs

 - includes configuring status delivery via mail / web and irc

2) Integration with Hg: finer grained use of distributed testing through Hg pull

3) Twisted PB integration: Buildbot supports PB and can be used for real-time status

3) Integration with test framework: unittest and doctest


---

Comment by ghtdak created at 2008-06-28 17:34:51

Resolution: invalid


---

Comment by mpatel created at 2010-01-30 12:02:11

Changing priority from minor to critical.


---

Comment by mpatel created at 2010-01-30 12:02:11

Changing status from closed to new.


---

Comment by mpatel created at 2010-01-30 12:02:11

I'm reopening this, because it's important and overdue.  We can discuss possible approaches on sage-devel.


---

Comment by mpatel created at 2010-01-30 12:02:11

Resolution changed from invalid to 


---

Comment by mpatel created at 2010-08-30 08:45:25

Changing component from distribution to build.


---

Comment by drkirkby created at 2010-11-11 22:40:11

Can this now be closed, since the buildbot is working? 

Dave


---

Comment by mpatel created at 2010-11-11 23:53:47

Replying to [comment:15 drkirkby]:
> Can this now be closed, since the buildbot is working? 

"Sounds" good!


---

Comment by leif created at 2011-10-13 13:05:32

What IRC integration would be desirable?


---

Comment by kini created at 2011-10-13 13:35:49

Oh, I just wanted to improve sagebot's trac reporting. I also want to do some other stuff with trac tracking, but none of this is related to the buildbot.


---

Comment by jdemeyer created at 2011-11-02 14:28:47

Replying to [comment:15 drkirkby]:
> Can this now be closed, since the buildbot is working?

It's working, but not very well.

Anybody has any clue what's wrong with

```
http://build.sagemath.org/sage/builders/Skynet%20download
```



---

Comment by mderickx created at 2012-03-15 00:15:53

I'm putting this to needs review, since the buildbot is clearly already an active part of the release process. If there are things to be improved there should be a new ticket (not this one whose goal was to get something running in the first place).


---

Comment by mderickx created at 2012-03-15 00:15:53

Changing status from new to needs_review.


---

Comment by kini created at 2012-05-16 14:10:46

What is there to review? It seems to me like you are proposing to close this ticket outright, in which case the correct status should be positive_review (so the release manager sees it).


---

Comment by kini created at 2012-05-16 14:10:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-21 08:05:39

Resolution: worksforme
