# Issue 8078: Fix algsys in Maxima

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-01-26 12:37:46

Assignee: burcin

CC:  kcrisman mjo

Keywords: solve, inequality

Sage with patch #7325 fails to solve some simple ineqaulitites

```
sage: solve(x^4+2>0,x)
[This is the Trac macro *x > -* that was inherited from the migration called with arguments (-1)^)](https://trac.sagemath.org/wiki/WikiMacros#x > --macro)
```

This should be fixed in Maxima and has been reported on [maxima list](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593). Update Maxima (has been fixed in CVS in [solve_rat_ineq](http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/share/contrib/solve_rat_ineq.mac?view=log)).


---

Comment by kcrisman created at 2011-02-07 15:35:43

Looks like this was indeed fixed in the Maxima upgrade.  We just need a patch to confirm this.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: plotpatches
sage: solve(x^4+2>0,x)
[x < +Infinity]
sage: 
```



---

Comment by kcrisman created at 2011-06-14 18:07:18

Changing keywords from "solve, inequality" to "solve, inequality, beginner".


---

Comment by mjo created at 2011-12-14 00:14:31

Patch to add a doctest for the correct behaviour.


---

Comment by mjo created at 2011-12-14 00:15:46

Changing status from new to needs_review.


---

Attachment

This is already fixed in sage-4.8.alpha4, so I've added a doctest for it.


---

Comment by mhansen created at 2011-12-18 10:12:38

Looks good to me.


---

Comment by mhansen created at 2011-12-18 10:12:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-22 13:06:21

Resolution: fixed
