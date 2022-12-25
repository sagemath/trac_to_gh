# Issue 8078: Fix algsys in Maxima

archive/issues_008078.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman @orlitzky\n\nKeywords: solve, inequality\n\nSage with patch #7325 fails to solve some simple ineqaulitites\n\n```\nsage: solve(x^4+2>0,x)\n[[x > -(-1)^(1/4)*2^(1/4), x < (-1)^(1/4)*2^(1/4)]]\n```\n\nThis should be fixed in Maxima and has been reported on [maxima list](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593). Update Maxima (has been fixed in CVS in [solve_rat_ineq](http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/share/contrib/solve_rat_ineq.mac?view=log)).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8078\n\n",
    "created_at": "2010-01-26T12:37:46Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "Fix algsys in Maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8078",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

CC:  @kcrisman @orlitzky

Keywords: solve, inequality

Sage with patch #7325 fails to solve some simple ineqaulitites

```
sage: solve(x^4+2>0,x)
[[x > -(-1)^(1/4)*2^(1/4), x < (-1)^(1/4)*2^(1/4)]]
```

This should be fixed in Maxima and has been reported on [maxima list](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593). Update Maxima (has been fixed in CVS in [solve_rat_ineq](http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/share/contrib/solve_rat_ineq.mac?view=log)).

Issue created by migration from https://trac.sagemath.org/ticket/8078





---

archive/issue_comments_070675.json:
```json
{
    "body": "Looks like this was indeed fixed in the Maxima upgrade.  We just need a patch to confirm this.\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: plotpatches\nsage: solve(x^4+2>0,x)\n[x < +Infinity]\nsage: \n```\n",
    "created_at": "2011-02-07T15:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70675",
    "user": "https://github.com/kcrisman"
}
```

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

archive/issue_comments_070676.json:
```json
{
    "body": "Changing keywords from \"solve, inequality\" to \"solve, inequality, beginner\".",
    "created_at": "2011-06-14T18:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70676",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "solve, inequality" to "solve, inequality, beginner".



---

archive/issue_comments_070677.json:
```json
{
    "body": "Patch to add a doctest for the correct behaviour.",
    "created_at": "2011-12-14T00:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70677",
    "user": "https://github.com/orlitzky"
}
```

Patch to add a doctest for the correct behaviour.



---

archive/issue_comments_070678.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-14T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70678",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070679.json:
```json
{
    "body": "Attachment [sage-trac_8078.patch](tarball://root/attachments/some-uuid/ticket8078/sage-trac_8078.patch) by @orlitzky created at 2011-12-14 00:15:46\n\nThis is already fixed in sage-4.8.alpha4, so I've added a doctest for it.",
    "created_at": "2011-12-14T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70679",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_8078.patch](tarball://root/attachments/some-uuid/ticket8078/sage-trac_8078.patch) by @orlitzky created at 2011-12-14 00:15:46

This is already fixed in sage-4.8.alpha4, so I've added a doctest for it.



---

archive/issue_comments_070680.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2011-12-18T10:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70680",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_070681.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-18T10:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70681",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008284.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-12-22T13:06:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8078#event-8284"
}
```



---

archive/issue_comments_070682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-22T13:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8078#issuecomment-70682",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
