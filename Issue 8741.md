# Issue 8741: Upgrade Twisted to 10.0

Issue created by migration from https://trac.sagemath.org/ticket/8741

Original creator: timdumol

Original creation time: 2010-04-21 19:31:17

Assignee: tbd

Twisted is now version [10.0](http://twistedmatrix.com/trac/browser/tags/releases/twisted-10.0.0/NEWS?format=raw), bringing a bunch of bug fixes.


---

Comment by timdumol created at 2010-04-21 20:08:26

Changing status from new to needs_review.


---

Comment by jason created at 2010-10-07 17:26:30

Note that 10.1 is out now as well; I don't know if we should just upgrade to 10.1 (maybe on another ticket?)


---

Comment by jason created at 2010-10-07 19:41:40

I updated it to 10.1, the web2 directory to the SVN current version, and zope interfaces to 3.6.1.

Tim, do you want to review my update to your spkg?


---

Comment by ltw created at 2011-06-02 19:51:02

Now that Twisted 11.0 is out, perhaps we should close this ticket quickly and open a new one?

Trac, I did NOT delete `dependencies`; it was blank to begin with!


---

Comment by kcrisman created at 2011-06-23 03:38:40

See also #11497, just to be aware.  

Also, don't forget to include the web2 by hand!  Unless we finally don't need that any more...


---

Comment by jason created at 2011-12-13 16:09:16

The new flask notebook upgrades twisted to 11.0, so this ticket can be


---

Comment by jason created at 2011-12-13 16:10:17

The new flask notebook upgrades twisted to 11.0, so I updated this ticket.


---

Comment by jason created at 2011-12-13 17:51:02

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-12-13 17:51:02

This ticket is now obsolete and superseded by #11874.


---

Comment by jdemeyer created at 2011-12-14 22:30:42

Replying to [comment:10 jason]:
> This ticket is now obsolete and superseded by #11874.
Please explain what you mean with this.


---

Comment by jdemeyer created at 2011-12-14 22:30:49

Changing status from positive_review to needs_info.


---

Comment by jason created at 2011-12-14 22:49:42

This ticket should be closed as a duplicate of #11874.


---

Comment by thisch created at 2012-09-11 13:25:27

Any reason why this ticket is still not closed?


---

Comment by jdemeyer created at 2013-05-16 07:38:14

Resolution: invalid
