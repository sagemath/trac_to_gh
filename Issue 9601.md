# Issue 9601: Fix cvxopt on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/9601

Original creator: pjeremy

Original creation time: 2010-07-26 11:12:31

Assignee: pjeremy

cvxopt requires C99 math functions that are not part of the base FreeBSD libraries.  #9543 uses cephes to provide these missing functions but referencing them requires that cvxopt search $SAGE_LOCAL/include.  The attached patch modified spkg-install to
include this.

This patch is local to Sage and does not need to be reported upstream.


---

Attachment

hi, i think this should be coordinated with #6456


---

Comment by pjeremy created at 2010-07-27 23:03:46

An equivalent patch for cvxopt-1.1.2.p1 has been attached to #6456.  On the assumption that the newer cvxopt will supplant cvxopt-0.9, this ticket can be closed.


---

Comment by drkirkby created at 2010-07-28 01:00:38

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-28 01:00:49

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-07-28 01:02:51

Whilst I realise this should be coordinated with #6456, I thought it wise that this got positive review first, to make merging easier. 

The fix is clearly FreeBSD specific, so will not impact any other system.


---

Comment by mpatel created at 2010-10-03 09:35:31

There hasn't been very recent activity at #6456.  Does it make sense to put together a new p10 (based on the p9 in 4.6.alpha2), so we can merge this ticket?


---

Comment by mhansen created at 2010-10-12 00:35:45

I've just done some more work on #6456.


---

Comment by mpatel created at 2010-10-25 03:45:03

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-10-25 03:45:03

This ticket is not actionable without an updated spkg or a positive review at #6456, so I'm changing the status to "needs work".


---

Comment by kcrisman created at 2012-01-31 02:04:18

Apparently [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) has had some success with this recently as a "port"


---

Comment by drkirkby created at 2012-01-31 21:53:22

Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he called the 

"release it now, we'll make it work later" mentality.

(They are Peter's words, not mine. See #9601.)

Dave


---

Comment by drkirkby created at 2012-01-31 21:55:13

Replying to [comment:10 drkirkby]:
> Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he called the 
> 
> "release it now, we'll make it work later" mentality.
> 
> (They are Peter's words, not mine. See #9601.)
> 
> Dave 

Oops, Peter put his comments on #6456, not #9601 which is this ticket! 

Dave.


---

Comment by kcrisman created at 2012-02-01 01:46:35

> > Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he 
Well, a friend of one of the WeBWorK developers did manage to make a Sage that passed most tests not too long ago.   See the link in comment:9.


---

Comment by mhansen created at 2012-05-28 08:08:20

Changing status from needs_work to positive_review.


---

Comment by mhansen created at 2012-05-28 08:08:20

I think this can be closed now since this is in the current cvxopt.


---

Comment by mhansen created at 2012-05-28 08:08:30

Changing keywords from "" to "sd40.5".


---

Comment by jdemeyer created at 2012-06-02 12:44:24

Resolution: duplicate
