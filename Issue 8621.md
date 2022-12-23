# Issue 8621: New functions in lcalc wrapper

Issue created by migration from https://trac.sagemath.org/ticket/8621

Original creator: rishi

Original creation time: 2010-03-29 00:36:00

Assignee: was

CC:  bober cremona craigcitro

I have added access to two new functions in lcalc wrapper.

compute_rank and hardy_z_function


---

Comment by rishi created at 2010-03-29 00:36:25

Changing type from defect to enhancement.


---

Attachment

I have added two new functions

```
sage: from sage.libs.lcalc.lcalc_Lfunction import (Lfunction_from_character, Lfunction_from_elliptic_curve)
sage: chi=DirichletGroup(123)[31]
sage: L1=Lfunction_from_character(chi)
sage: L1.hardy_z_function(.5+5*I)
-0.462453973892362 - 7.93526871565814e-15*I
sage: L1.compute_rank()
0
sage: L2=Lfunction_from_elliptic_curve(EllipticCurve('37a'))
sage: L2.compute_rank()
1
sage: L2.hardy_z_function(.5+6*I)
-2.17184689048993 - 1.76053169785863e-15*I
sage: L2.hardy_z_function(-.5+6*I)
4.17981266933977 + 36.9688966864015*I
```


Although for elliptic curves, other programs will be better for analytic rank, I have added this because here it works for any L function


---

Attachment

rebase of rishi's patch


---

Comment by bober created at 2011-09-07 19:08:17

Changing status from new to needs_review.


---

Comment by bober created at 2011-09-07 19:08:17

I don't love everything about the way this patch or the lcalc wrapper do things, and maybe a better or at least newer wrapper is on the way, but this patch does improve on the functionality available in sage and doesn't break things.


---

Comment by bober created at 2011-09-07 19:08:31

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-09 01:15:25

Jonathan, you can add yourself to [http://trac.sagemath.org/sage_trac/wiki#AccountNamesMappedtoRealNames](http://trac.sagemath.org/sage_trac/wiki#AccountNamesMappedtoRealNames).


---

Comment by leif created at 2011-09-15 12:15:56

I do get doctest errors due to numerical noise.

This is on a Core2 Penryn (Ubuntu 10.04.3 x86_64):

```
**********************************************************************
File ".../sage/libs/lcalc/lcalc_Lfunction.pyx", line 181:
    sage: L.hardy_z_function(.2+.4*I)
Expected:
    0.2166144222685... - 0.004081871278504...*I
Got:
    0.216614422268554 - 0.00408187127850235*I
**********************************************************************
File ".../sage/libs/lcalc/lcalc_Lfunction.pyx", line 191:
    sage: L.hardy_z_function(.5+2.1*I)
Expected:
    -0.0064317917686980...
Got:
    -0.00643179176869426 - 3.93820653320273e-19*I
**********************************************************************
1 items had failures:
   2 of  17 in __main__.example_4
***Test Failed*** 2 failures.
```


I've seen almost the same on redhawk, an Opteron 8439 SE:

```
**********************************************************************
File ".../sage/libs/lcalc/lcalc_Lfunction.pyx", line 181:
    sage: L.hardy_z_function(.2+.4*I)
Expected:
    0.2166144222685... - 0.004081871278504...*I
Got:
    0.216614422268554 - 0.00408187127850235*I
**********************************************************************
File ".../sage/libs/lcalc/lcalc_Lfunction.pyx", line 191:
    sage: L.hardy_z_function(.5+2.1*I)
Expected:
    -0.0064317917686980...
Got:
    -0.00643179176869423 - 3.93820653320271e-19*I
**********************************************************************
1 items had failures:
   2 of  17 in __main__.example_4
***Test Failed*** 2 failures.
```



---

Comment by leif created at 2011-09-15 12:15:56

Changing status from positive_review to needs_work.


---

Comment by fbissey created at 2011-09-15 22:23:33

fixing the numerical noise


---

Comment by fbissey created at 2011-09-15 22:25:11

Changing status from needs_work to needs_review.


---

Attachment

I am attaching a patch to deal with this.


---

Comment by jdemeyer created at 2011-10-15 13:03:46

The documentation formatting can be improved, see [http://sagemath.org/doc/developer/conventions.html#documentation-strings](http://sagemath.org/doc/developer/conventions.html#documentation-strings)

There should be an example for the "rotate" option.

Also, you should probably change the `EllipticCurve.analytic_rank()` function to use the `compute_rank` library call if `algoritm=rubenstein`.


---

Comment by jdemeyer created at 2011-10-15 13:03:46

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by rishi created at 2012-04-15 20:02:32

I have attached a patch which corrects some horrible typos, and uses the standard definition of hardy Z function. This builds on patches which came earlier. Only the last patch is needed.


---

Comment by rishi created at 2012-04-17 11:12:23

Changing status from needs_work to needs_review.


---

Comment by rishi created at 2012-04-17 11:12:23

To address Joroen's comments:

Every example in hardy_z_function is an example for rotate option.

The anaytic rank computation using Dokchitser's program is superior to lcalc's.


---

Attachment


---

Comment by bober created at 2012-05-29 04:38:57

Replying to [comment:14 bober]:

Dear patchbot,

Apply: [attachment:trac8621.patch] [attachment:trac8621_review.patch]


---

Comment by jdemeyer created at 2012-07-27 20:42:40

Please fill in your real name as Author.


---

Comment by rishi created at 2012-07-27 21:25:46

Replying to [comment:16 jdemeyer]:
> Please fill in your real name as Author.

Is that for me or Jonathan? My real name is indeed "Rishikesh". Jonathan should also be added as an author since he really improved the documentation more than I did.


---

Comment by jdemeyer created at 2012-10-05 19:38:42

Replying to [comment:17 rishi]:
> Is that for me or Jonathan? My real name is indeed "Rishikesh".
Really?  So it seems that I am "culturally challenged" in thinking that names should always consist of at least two parts: first name and last name.  Just for curiosity: where do you come from?


---

Comment by jdemeyer created at 2012-10-05 19:41:11

In any case: Jonathan and Rishikesh, could you review each other's patches?  These patches almost got merged and it would be a pity to waste the work.


---

Comment by cremona created at 2013-08-11 16:17:32

replace previous (rebased for 5.11.rc1)


---

Attachment

I replaced the review patch with one which applies to 5.11.rc1.  The only change was in the index entry to the reference manual, which has since been rearranged.


---

Comment by chapoton created at 2013-08-21 09:32:58

apply trac8621.patch trac8621_review_rebase.patch


---

Comment by chapoton created at 2013-10-23 18:30:51

Ping ? This ticket looks good to go, can somebody confirm ?


---

Comment by chapoton created at 2013-11-25 20:02:44

Hello ! What about this one ?


---

Comment by rishi created at 2013-11-26 06:04:11

Replying to [comment:24 chapoton]:
> Hello ! What about this one ? 

I will have a look at it again and get back by Thursday.


---

Comment by jdemeyer created at 2013-12-05 08:03:54

For what it's worth: all ok on the buildbots...


---

Comment by chapoton created at 2014-01-06 15:49:14

Changing keywords from "" to "lcalc".


---

Comment by chapoton created at 2014-01-12 20:20:20

I have made a git branch. Needs review.
----
New commits:


---

Comment by cremona created at 2014-01-17 10:42:44

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2014-01-17 10:42:44

Positive review.  I have tested this by itself and also checked that when this branch is used to run a copy of the lmfdb website (www.lmfdb.org) the Z-plots work.  Note that the latches on which thie review branch was based have been running on the lmfdb website for more than a year already.

Please can we have this in Sage-6.1!  It will help lmfdb development a lot.


---

Comment by vbraun created at 2014-02-03 22:59:12

Resolution: fixed
