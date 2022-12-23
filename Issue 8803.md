# Issue 8803: Bring doctest for plot/axes.py to 100% or remove it

Issue created by migration from https://trac.sagemath.org/ticket/8803

Original creator: kcrisman

Original creation time: 2010-04-28 15:18:52

Assignee: mvngu

Bring doctest coverage for plot/axes.py to 100% or remove it (since we now use matplotlib axes directly).


---

Comment by kcrisman created at 2010-04-29 01:03:38

See # 5448; this module has been deprecated since Sage 4.1.2, which was released on October 14, 2009.  It has not yet been one year, nor will it have been when Sage 5.0 is released (let's hope!).  On the other hand, the whole module was essentially internal functions for use in plot functions.  At any rate, there is no point in doing any more doctests for this, even if it "hurts" the coverage score.

Thoughts?


---

Comment by kcrisman created at 2010-04-29 01:03:38

Changing status from new to needs_info.


---

Comment by jason created at 2010-05-09 01:56:11

+1 for removing it if it causes any problems.  If it doesn't cause any problems, then we might as well leave it in for the sake of the deprecation policy.

Note that I don't know that anything has ever actually been removed after being deprecated.  For example, the warning that comes when evaluating an expression like (x<sup>2+y</sup>2)(1,2) has been there for well over a year, but still shows no signs of disappearing.


---

Comment by mvngu created at 2010-05-09 01:59:25

Replying to [comment:2 jason]:
> Note that I don't know that anything has ever actually been removed after being deprecated.  For example, the warning that comes when evaluating an expression like (x<sup>2+y</sup>2)(1,2) has been there for well over a year, but still shows no signs of disappearing.

With Sage 5.0 being the next major release, perhaps it's now time to remove any deprecated functions/classes/methods that are over 6 months old. Such removal could happen after Sage 4.4.2 is out next week.


---

Comment by jason created at 2010-05-09 02:09:35

I agree that it would be a good time to remove old deprecated code.

Since many of our users are on an academic cycle, maybe we ought to adjust the deprecation schedule so that deprecated things won't be removed during the academic year, but could be removed after the next big release after the later of 6 months or the end of the academic year?


---

Comment by kcrisman created at 2010-05-10 15:10:23

Oh, I didn't realize it was 6 months - somehow I read on a thread that it was 12 months.  I don't think that axes.py creates any problems other than lowering our sage -coverage score :)  But Sage 5.0 does seem like an allowable time to remove things that have been deprecated for the requisite time.


---

Comment by kcrisman created at 2011-02-16 22:02:16

We can really remove this now.


---

Comment by jason created at 2011-02-17 04:43:35

+1 to removing this whenever the developer's guide first allows it.  Just today I saw the file and was temporarily confused before I realized that it is just old cruft that was once useful, but now is not needed.


---

Comment by kcrisman created at 2011-02-17 14:18:16

Replying to [comment:1 kcrisman]:
> See # 5448; this module has been deprecated since Sage 4.1.2, which was released on October 14, 2009.  It has not yet been one year, nor will it have been when Sage 5.0 is released (let's hope!).  On the other hand, the whole module was essentially internal functions for use in plot functions.  At any rate, there is no point in doing any more doctests for this, even if it "hurts" the coverage score.

The developer guide certainly was not thinking 18 months, and since this is not some common mistake like `f=4*x; f(3)` there should be no harm in removing it.  Looks like 5.0 isn't coming any time soon, but we should do this.  Patch coming up.


---

Comment by kcrisman created at 2011-02-17 14:52:20

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2011-02-17 14:52:20

Ready for review.  Apply only attachment:trac_8803-remove-axes.patch

Jason, if you do this, might as well review #2100 at the same time ;)


---

Comment by ncohen created at 2011-05-02 15:57:00

Well, sounds safe to remove it after all this time, and all tests pass on 4.7.rc1

Good to go ! `:-)`

Nathann


---

Comment by ncohen created at 2011-05-02 15:57:00

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-05-02 16:00:32

Thank you!  It's really silly that we hadn't removed it before, given that the deprecation period long since passed and it doesn't change functionality, but it's gratifying to know that it's not just people who use the graphics code all the time who search these tickets :)


---

Comment by kcrisman created at 2011-05-03 13:12:24

The deprecation has been in place for a LONG time, (over 18 months), and this module does not have any remaining functionality, nor was it ever really very end-user available.  We thought at one point that 5.0 would be in the near future, so we thought that was a good goal for when to remove it, but that was over a year ago.    This should be removed.  Jason?


---

Comment by jdemeyer created at 2011-05-15 15:00:56

Please change the commit message of the patch such there aren't any very long lines.


---

Comment by jdemeyer created at 2011-05-15 15:06:08

Changing status from positive_review to needs_work.


---

Attachment

Hopefully this will do it.


---

Comment by kcrisman created at 2011-05-16 15:37:21

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-05-16 19:36:43

Replying to [comment:18 kcrisman]:
> Hopefully this will do it.  

Yep, thanks!


---

Comment by jdemeyer created at 2011-05-16 19:36:43

Resolution: fixed
