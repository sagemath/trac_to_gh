# Issue 2666: ncalexan's enhancements to emacs sage mode

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-25 20:43:45

Assignee: was

CC:  iandrus

ncalexan has been talking about his sage-mode.el enhancements---it'd be great to include his great wizardry into the sage distribution.


---

Comment by jason created at 2009-02-12 00:10:14

Apparently Nick is distributing this as an spkg now.  See http://wiki.sagemath.org/sage-mode  Should this ticket be closed, then?  Is that spkg in at least the optional repository, if not the standard repository?


---

Comment by mabshoff created at 2009-02-12 00:19:58

Replying to [comment:1 jason]:
> Apparently Nick is distributing this as an spkg now.  See http://wiki.sagemath.org/sage-mode  Should this ticket be closed, then?  Is that spkg in at least the optional repository, if not the standard repository?

There is still the plan to make this part of standard Sage, just like SageTeX, so I am changing the summary to reflect this even though this was not the original motivation for this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-12 00:19:58

Changing assignee from was to ncalexan.


---

Comment by mvngu created at 2009-08-12 16:01:16

I have been using Nick Alexander's Sage Emacs mode package for months now. My only pet peeve is that the status bar at the bottom says "SAGE" instead of "Sage". We have moved beyond that acronym. Now "Sage" is the name of the game :-)


---

Comment by kcrisman created at 2012-06-28 13:33:34

Just FYI, sage-mode is in the meantime at least an optional spkg.  See also:
 * [the optional spkg list](http://sagemath.org/packages/optional/)
 * [the sage-mode on the wiki](http://wiki.sagemath.org/sage-mode)
 * [sage-mode on bitbucket](https://bitbucket.org/ncalexan/sage-mode)

I think that Ivan Andrus is currently taking over for sage-mode responsibilities?


---

Comment by kcrisman created at 2012-06-28 13:59:10

Changing keywords from "" to "sage-mode".


---

Comment by kcrisman created at 2012-06-28 13:59:10

Also, the current version on the wiki and bitbucket is 0.7, but it is 0.6 on the optional spkg list.  This should be dealt with.

This could still become a standard spkg, in theory (though I don't see the point), so maybe that would be another ticket.  If so, SPKG.txt should be changed a little so it's not just a copy of the wiki page (since all the `attachment:` directives make no sense.  In fact, that should be done for any upgrade anyway.


---

Comment by kcrisman created at 2012-06-28 13:59:10

Changing component from interfaces to user interface.


---

Comment by kcrisman created at 2012-06-28 13:59:42

Ok, I've opened #13176 to upgrade, so this is separate for making it standard.

See also #1861.


---

Comment by kcrisman created at 2012-06-28 16:12:33

Changing priority from major to minor.


---

Comment by jdemeyer created at 2013-06-13 12:15:57

Why should this be a standard package? I think it fits very well as optional package.


---

Comment by iandrus created at 2013-06-13 17:10:23

There was some discussion of this [on sage-devel](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/2AOjLX0brQ8) a while ago.  IIRC it was not a clear win either way.  Personally, I slightly prefer optional, but mostly I just want it to be updated to the latest version (see #13182).   :-)


---

Comment by iandrus created at 2014-06-10 06:30:32

I think we should just close this.  I read the discussion on sage-devel again, and I think there's no reason to make it standard.  I've been maintaining it for a while now and don't plan on stopping in the next few years.


---

Comment by iandrus created at 2014-06-10 06:30:32

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-06-10 17:12:30

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2014-06-10 17:12:30

I think that based on how people are using it (and I've seen a lot of activity over the years) this is fine to keep optional.


---

Comment by vbraun created at 2014-06-14 13:18:12

Resolution: wontfix
