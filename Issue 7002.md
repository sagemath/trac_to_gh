# Issue 7002: Notebook documentation says to use "#auto", but should be "%auto"

Issue created by migration from https://trac.sagemath.org/ticket/7002

Original creator: jason

Original creation time: 2009-09-23 13:29:00

Assignee: tba

CC:  mvngu kcrisman

#auto was the old way, %auto was the new way.  Plus, we should say % directives need to happen above the input. 

To see the problem, click the "Help" in the upper right corner.  The second row is:

Any cells with "#auto" in the input is automatically evaluated when the worksheet is first opened.

This should be changed to:

Any cells with "%auto" above the input is automatically evaluated when the worksheet is first opened.


---

Comment by kcrisman created at 2009-09-23 15:50:47

I hate to say this... is a deprecation period in order here?  Or was #auto never the way to do it in the first place?  I have to admit I was always confused by it, which probably led to very few worksheets using it in classes!


---

Comment by jason created at 2009-09-23 16:16:57

Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.

"#auto" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  

What I am suggesting is just that the documentation be changed to reflect the new way.  The "#auto" still works.  I'd just like to get new people using "%auto".


---

Attachment


---

Comment by kcrisman created at 2009-09-23 16:42:07

Replying to [comment:3 jason]:
> Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.
> 
> "#auto" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  
> 
> What I am suggesting is just that the documentation be changed to reflect the new way.  The "#auto" still works.  I'd just like to get new people using "%auto".

Oh, if it still works and we aren't getting rid of it, then probably just making the change is okay.  

Incidentally, this doesn't apply cleanly due to someone having added something about HTML above the Shell scripts thingie.  Does this patch depend on something?


---

Comment by jason created at 2009-09-23 16:58:28

No, it doesn't depend on anything, but it was a patch based on the last version I have on my laptop, so something like 4.1.1 or 4.1.2.alpha1 or something.


---

Comment by kcrisman created at 2009-09-23 17:45:33

Based on 4.1.2.alpha2


---

Attachment

Positive review, since I just tested that %auto still works (as well as #auto); apply rebase patch only.


---

Comment by mvngu created at 2009-09-24 07:16:13

Resolution: fixed


---

Comment by mvngu created at 2009-09-24 07:16:53

Merged `trac-7002-autoevaluate-rebase.patch`.


---

Comment by mvngu created at 2009-09-27 09:58:43

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.


---

Comment by jason created at 2011-05-30 17:49:51

I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.


---

Attachment


---

Comment by kcrisman created at 2011-06-01 03:14:48

Replying to [comment:11 jason]:
> I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.

Correct.  Thanks for checking on this also, Jeroen.

I do remember that there is a different ticket open for "really" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.


---

Comment by kcrisman created at 2011-06-20 15:44:58

Replying to [comment:13 kcrisman]:
> Replying to [comment:11 jason]:
> > I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.
> 
> Correct.  Thanks for checking on this also, Jeroen.
> 
> I do remember that there is a different ticket open for "really" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.

It's #8956, apparently.  I've requested that one be closed, since the issue is dealt with here.
