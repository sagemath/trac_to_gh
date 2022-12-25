# Issue 8621: New functions in lcalc wrapper

archive/issues_008621.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  bober @JohnCremona @craigcitro\n\nI have added access to two new functions in lcalc wrapper.\n\ncompute_rank and hardy_z_function\n\nIssue created by migration from https://trac.sagemath.org/ticket/8621\n\n",
    "created_at": "2010-03-29T00:36:00Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "New functions in lcalc wrapper",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8621",
    "user": "https://github.com/rishikesha"
}
```
Assignee: @williamstein

CC:  bober @JohnCremona @craigcitro

I have added access to two new functions in lcalc wrapper.

compute_rank and hardy_z_function

Issue created by migration from https://trac.sagemath.org/ticket/8621





---

archive/issue_comments_077991.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-29T00:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77991",
    "user": "https://github.com/rishikesha"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_077992.json:
```json
{
    "body": "Attachment [trac_8621.patch](tarball://root/attachments/some-uuid/ticket8621/trac_8621.patch) by @rishikesha created at 2010-03-29 00:44:13\n\nI have added two new functions\n\n```\nsage: from sage.libs.lcalc.lcalc_Lfunction import (Lfunction_from_character, Lfunction_from_elliptic_curve)\nsage: chi=DirichletGroup(123)[31]\nsage: L1=Lfunction_from_character(chi)\nsage: L1.hardy_z_function(.5+5*I)\n-0.462453973892362 - 7.93526871565814e-15*I\nsage: L1.compute_rank()\n0\nsage: L2=Lfunction_from_elliptic_curve(EllipticCurve('37a'))\nsage: L2.compute_rank()\n1\nsage: L2.hardy_z_function(.5+6*I)\n-2.17184689048993 - 1.76053169785863e-15*I\nsage: L2.hardy_z_function(-.5+6*I)\n4.17981266933977 + 36.9688966864015*I\n```\n\n\nAlthough for elliptic curves, other programs will be better for analytic rank, I have added this because here it works for any L function",
    "created_at": "2010-03-29T00:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77992",
    "user": "https://github.com/rishikesha"
}
```

Attachment [trac_8621.patch](tarball://root/attachments/some-uuid/ticket8621/trac_8621.patch) by @rishikesha created at 2010-03-29 00:44:13

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

archive/issue_comments_077993.json:
```json
{
    "body": "Attachment [trac_8621.2.patch](tarball://root/attachments/some-uuid/ticket8621/trac_8621.2.patch) by bober created at 2011-09-06 11:05:27\n\nrebase of rishi's patch",
    "created_at": "2011-09-06T11:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77993",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Attachment [trac_8621.2.patch](tarball://root/attachments/some-uuid/ticket8621/trac_8621.2.patch) by bober created at 2011-09-06 11:05:27

rebase of rishi's patch



---

archive/issue_comments_077994.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-09-07T19:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77994",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077995.json:
```json
{
    "body": "I don't love everything about the way this patch or the lcalc wrapper do things, and maybe a better or at least newer wrapper is on the way, but this patch does improve on the functionality available in sage and doesn't break things.",
    "created_at": "2011-09-07T19:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77995",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

I don't love everything about the way this patch or the lcalc wrapper do things, and maybe a better or at least newer wrapper is on the way, but this patch does improve on the functionality available in sage and doesn't break things.



---

archive/issue_comments_077996.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-07T19:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77996",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077997.json:
```json
{
    "body": "Jonathan, you can add yourself to [http://trac.sagemath.org/sage_trac/wiki#AccountNamesMappedtoRealNames](http://trac.sagemath.org/sage_trac/wiki#AccountNamesMappedtoRealNames).",
    "created_at": "2011-09-09T01:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77997",
    "user": "https://github.com/nexttime"
}
```

Jonathan, you can add yourself to [http://trac.sagemath.org/sage_trac/wiki#AccountNamesMappedtoRealNames](http://trac.sagemath.org/sage_trac/wiki#AccountNamesMappedtoRealNames).



---

archive/issue_comments_077998.json:
```json
{
    "body": "I do get doctest errors due to numerical noise.\n\nThis is on a Core2 Penryn (Ubuntu 10.04.3 x86_64):\n\n```\n**********************************************************************\nFile \".../sage/libs/lcalc/lcalc_Lfunction.pyx\", line 181:\n    sage: L.hardy_z_function(.2+.4*I)\nExpected:\n    0.2166144222685... - 0.004081871278504...*I\nGot:\n    0.216614422268554 - 0.00408187127850235*I\n**********************************************************************\nFile \".../sage/libs/lcalc/lcalc_Lfunction.pyx\", line 191:\n    sage: L.hardy_z_function(.5+2.1*I)\nExpected:\n    -0.0064317917686980...\nGot:\n    -0.00643179176869426 - 3.93820653320273e-19*I\n**********************************************************************\n1 items had failures:\n   2 of  17 in __main__.example_4\n***Test Failed*** 2 failures.\n```\n\n\nI've seen almost the same on redhawk, an Opteron 8439 SE:\n\n```\n**********************************************************************\nFile \".../sage/libs/lcalc/lcalc_Lfunction.pyx\", line 181:\n    sage: L.hardy_z_function(.2+.4*I)\nExpected:\n    0.2166144222685... - 0.004081871278504...*I\nGot:\n    0.216614422268554 - 0.00408187127850235*I\n**********************************************************************\nFile \".../sage/libs/lcalc/lcalc_Lfunction.pyx\", line 191:\n    sage: L.hardy_z_function(.5+2.1*I)\nExpected:\n    -0.0064317917686980...\nGot:\n    -0.00643179176869423 - 3.93820653320271e-19*I\n**********************************************************************\n1 items had failures:\n   2 of  17 in __main__.example_4\n***Test Failed*** 2 failures.\n```\n",
    "created_at": "2011-09-15T12:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77998",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_077999.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-09-15T12:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-77999",
    "user": "https://github.com/nexttime"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_078000.json:
```json
{
    "body": "fixing the numerical noise",
    "created_at": "2011-09-15T22:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78000",
    "user": "https://github.com/kiwifb"
}
```

fixing the numerical noise



---

archive/issue_comments_078001.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-15T22:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78001",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078002.json:
```json
{
    "body": "Attachment [trac_8621-review.patch](tarball://root/attachments/some-uuid/ticket8621/trac_8621-review.patch) by @kiwifb created at 2011-09-15 22:25:11\n\nI am attaching a patch to deal with this.",
    "created_at": "2011-09-15T22:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78002",
    "user": "https://github.com/kiwifb"
}
```

Attachment [trac_8621-review.patch](tarball://root/attachments/some-uuid/ticket8621/trac_8621-review.patch) by @kiwifb created at 2011-09-15 22:25:11

I am attaching a patch to deal with this.



---

archive/issue_comments_078003.json:
```json
{
    "body": "The documentation formatting can be improved, see [http://sagemath.org/doc/developer/conventions.html#documentation-strings](http://sagemath.org/doc/developer/conventions.html#documentation-strings)\n\nThere should be an example for the \"rotate\" option.\n\nAlso, you should probably change the `EllipticCurve.analytic_rank()` function to use the `compute_rank` library call if `algoritm=rubenstein`.",
    "created_at": "2011-10-15T13:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78003",
    "user": "https://github.com/jdemeyer"
}
```

The documentation formatting can be improved, see [http://sagemath.org/doc/developer/conventions.html#documentation-strings](http://sagemath.org/doc/developer/conventions.html#documentation-strings)

There should be an example for the "rotate" option.

Also, you should probably change the `EllipticCurve.analytic_rank()` function to use the `compute_rank` library call if `algoritm=rubenstein`.



---

archive/issue_comments_078004.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-15T13:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78004",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078005.json:
```json
{
    "body": "Attachment [trac8621.patch](tarball://root/attachments/some-uuid/ticket8621/trac8621.patch) by @rishikesha created at 2012-04-15 20:00:46",
    "created_at": "2012-04-15T20:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78005",
    "user": "https://github.com/rishikesha"
}
```

Attachment [trac8621.patch](tarball://root/attachments/some-uuid/ticket8621/trac8621.patch) by @rishikesha created at 2012-04-15 20:00:46



---

archive/issue_comments_078006.json:
```json
{
    "body": "I have attached a patch which corrects some horrible typos, and uses the standard definition of hardy Z function. This builds on patches which came earlier. Only the last patch is needed.",
    "created_at": "2012-04-15T20:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78006",
    "user": "https://github.com/rishikesha"
}
```

I have attached a patch which corrects some horrible typos, and uses the standard definition of hardy Z function. This builds on patches which came earlier. Only the last patch is needed.



---

archive/issue_comments_078007.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-17T11:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78007",
    "user": "https://github.com/rishikesha"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078008.json:
```json
{
    "body": "To address Joroen's comments:\n\nEvery example in hardy_z_function is an example for rotate option.\n\nThe anaytic rank computation using Dokchitser's program is superior to lcalc's.",
    "created_at": "2012-04-17T11:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78008",
    "user": "https://github.com/rishikesha"
}
```

To address Joroen's comments:

Every example in hardy_z_function is an example for rotate option.

The anaytic rank computation using Dokchitser's program is superior to lcalc's.



---

archive/issue_comments_078009.json:
```json
{
    "body": "Attachment [trac8621_review.patch](tarball://root/attachments/some-uuid/ticket8621/trac8621_review.patch) by bober created at 2012-05-29 04:32:50",
    "created_at": "2012-05-29T04:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78009",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Attachment [trac8621_review.patch](tarball://root/attachments/some-uuid/ticket8621/trac8621_review.patch) by bober created at 2012-05-29 04:32:50



---

archive/issue_comments_078010.json:
```json
{
    "body": "Replying to [comment:14 bober]:\n\nDear patchbot,\n\nApply: [attachment:trac8621.patch] [attachment:trac8621_review.patch]",
    "created_at": "2012-05-29T04:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78010",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Replying to [comment:14 bober]:

Dear patchbot,

Apply: [attachment:trac8621.patch] [attachment:trac8621_review.patch]



---

archive/issue_comments_078011.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78011",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_078012.json:
```json
{
    "body": "Replying to [comment:16 jdemeyer]:\n> Please fill in your real name as Author.\n\nIs that for me or Jonathan? My real name is indeed \"Rishikesh\". Jonathan should also be added as an author since he really improved the documentation more than I did.",
    "created_at": "2012-07-27T21:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78012",
    "user": "https://github.com/rishikesha"
}
```

Replying to [comment:16 jdemeyer]:
> Please fill in your real name as Author.

Is that for me or Jonathan? My real name is indeed "Rishikesh". Jonathan should also be added as an author since he really improved the documentation more than I did.



---

archive/issue_comments_078013.json:
```json
{
    "body": "Replying to [comment:17 rishi]:\n> Is that for me or Jonathan? My real name is indeed \"Rishikesh\".\nReally?  So it seems that I am \"culturally challenged\" in thinking that names should always consist of at least two parts: first name and last name.  Just for curiosity: where do you come from?",
    "created_at": "2012-10-05T19:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78013",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:17 rishi]:
> Is that for me or Jonathan? My real name is indeed "Rishikesh".
Really?  So it seems that I am "culturally challenged" in thinking that names should always consist of at least two parts: first name and last name.  Just for curiosity: where do you come from?



---

archive/issue_comments_078014.json:
```json
{
    "body": "In any case: Jonathan and Rishikesh, could you review each other's patches?  These patches almost got merged and it would be a pity to waste the work.",
    "created_at": "2012-10-05T19:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78014",
    "user": "https://github.com/jdemeyer"
}
```

In any case: Jonathan and Rishikesh, could you review each other's patches?  These patches almost got merged and it would be a pity to waste the work.



---

archive/issue_comments_078015.json:
```json
{
    "body": "replace previous (rebased for 5.11.rc1)",
    "created_at": "2013-08-11T16:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78015",
    "user": "https://github.com/JohnCremona"
}
```

replace previous (rebased for 5.11.rc1)



---

archive/issue_comments_078016.json:
```json
{
    "body": "Attachment [trac8621_review_rebase.patch](tarball://root/attachments/some-uuid/ticket8621/trac8621_review_rebase.patch) by @JohnCremona created at 2013-08-11 16:18:49\n\nI replaced the review patch with one which applies to 5.11.rc1.  The only change was in the index entry to the reference manual, which has since been rearranged.",
    "created_at": "2013-08-11T16:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78016",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac8621_review_rebase.patch](tarball://root/attachments/some-uuid/ticket8621/trac8621_review_rebase.patch) by @JohnCremona created at 2013-08-11 16:18:49

I replaced the review patch with one which applies to 5.11.rc1.  The only change was in the index entry to the reference manual, which has since been rearranged.



---

archive/issue_comments_078017.json:
```json
{
    "body": "apply trac8621.patch trac8621_review_rebase.patch",
    "created_at": "2013-08-21T09:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78017",
    "user": "https://github.com/fchapoton"
}
```

apply trac8621.patch trac8621_review_rebase.patch



---

archive/issue_comments_078018.json:
```json
{
    "body": "Ping ? This ticket looks good to go, can somebody confirm ?",
    "created_at": "2013-10-23T18:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78018",
    "user": "https://github.com/fchapoton"
}
```

Ping ? This ticket looks good to go, can somebody confirm ?



---

archive/issue_comments_078019.json:
```json
{
    "body": "Hello ! What about this one ?",
    "created_at": "2013-11-25T20:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78019",
    "user": "https://github.com/fchapoton"
}
```

Hello ! What about this one ?



---

archive/issue_comments_078020.json:
```json
{
    "body": "Replying to [comment:24 chapoton]:\n> Hello ! What about this one ? \n\nI will have a look at it again and get back by Thursday.",
    "created_at": "2013-11-26T06:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78020",
    "user": "https://github.com/rishikesha"
}
```

Replying to [comment:24 chapoton]:
> Hello ! What about this one ? 

I will have a look at it again and get back by Thursday.



---

archive/issue_comments_078021.json:
```json
{
    "body": "For what it's worth: all ok on the buildbots...",
    "created_at": "2013-12-05T08:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78021",
    "user": "https://github.com/jdemeyer"
}
```

For what it's worth: all ok on the buildbots...



---

archive/issue_comments_078022.json:
```json
{
    "body": "Changing keywords from \"\" to \"lcalc\".",
    "created_at": "2014-01-06T15:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78022",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "lcalc".



---

archive/issue_comments_078023.json:
```json
{
    "body": "I have made a git branch. Needs review.\n----\nNew commits:",
    "created_at": "2014-01-12T20:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78023",
    "user": "https://github.com/fchapoton"
}
```

I have made a git branch. Needs review.
----
New commits:



---

archive/issue_comments_078024.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-17T10:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78024",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078025.json:
```json
{
    "body": "Positive review.  I have tested this by itself and also checked that when this branch is used to run a copy of the lmfdb website (www.lmfdb.org) the Z-plots work.  Note that the latches on which thie review branch was based have been running on the lmfdb website for more than a year already.\n\nPlease can we have this in Sage-6.1!  It will help lmfdb development a lot.",
    "created_at": "2014-01-17T10:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78025",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  I have tested this by itself and also checked that when this branch is used to run a copy of the lmfdb website (www.lmfdb.org) the Z-plots work.  Note that the latches on which thie review branch was based have been running on the lmfdb website for more than a year already.

Please can we have this in Sage-6.1!  It will help lmfdb development a lot.



---

archive/issue_events_008792.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-02-03T22:59:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8621#event-8792"
}
```



---

archive/issue_comments_078026.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-03T22:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8621#issuecomment-78026",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
