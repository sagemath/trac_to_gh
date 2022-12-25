# Issue 1877: same range variables -- bug in 3d plotting (probably very very very easy to fix)

archive/issues_001877.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: var('x,y')\nsage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))\nboom!\n```\n\n\nThe problem is that both ranges use the variable x.  The fix is to make\nsure that the two variables are different and if not raise an exception (do this also in parametric_plot3d). \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1877\n\n",
    "created_at": "2008-01-21T06:40:06Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "same range variables -- bug in 3d plotting (probably very very very easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1877",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: var('x,y')
sage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))
boom!
```


The problem is that both ranges use the variable x.  The fix is to make
sure that the two variables are different and if not raise an exception (do this also in parametric_plot3d). 


Issue created by migration from https://trac.sagemath.org/ticket/1877





---

archive/issue_comments_011846.json:
```json
{
    "body": "Attachment [1877fix.hg](tarball://root/attachments/some-uuid/ticket1877/1877fix.hg) by thomag created at 2008-08-26 15:52:31\n\nplot3d and parametric_plot3d should fail a tiny bit more gracefully if they're given two ranges using the same variable:\n\n```\nsage: var('x,y')\nsage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))\nValueError: If the ranges in the argument of plot3d are 3-tuples, then the first components of those 3-tuples must be different.\nsage: var('u,v')\nsage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, 2*pi), (u, -pi, pi))\nValueError: If the ranges in the argument of parametric_plot3d are both 3-tuples, then the first components of those 3-tuples must be different.\n```\n",
    "created_at": "2008-08-26T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11846",
    "user": "https://trac.sagemath.org/admin/accounts/users/thomag"
}
```

Attachment [1877fix.hg](tarball://root/attachments/some-uuid/ticket1877/1877fix.hg) by thomag created at 2008-08-26 15:52:31

plot3d and parametric_plot3d should fail a tiny bit more gracefully if they're given two ranges using the same variable:

```
sage: var('x,y')
sage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))
ValueError: If the ranges in the argument of plot3d are 3-tuples, then the first components of those 3-tuples must be different.
sage: var('u,v')
sage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, 2*pi), (u, -pi, pi))
ValueError: If the ranges in the argument of parametric_plot3d are both 3-tuples, then the first components of those 3-tuples must be different.
```




---

archive/issue_comments_011847.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-26T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11847",
    "user": "https://trac.sagemath.org/admin/accounts/users/thomag"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011848.json:
```json
{
    "body": "Changing assignee from @williamstein to thomag.",
    "created_at": "2008-08-26T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11848",
    "user": "https://trac.sagemath.org/admin/accounts/users/thomag"
}
```

Changing assignee from @williamstein to thomag.



---

archive/issue_comments_011849.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-08-29T00:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_011850.json:
```json
{
    "body": "Please give a message with the raised value error. Pending that, I'd give a positive review.",
    "created_at": "2008-09-02T08:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11850",
    "user": "https://github.com/robertwb"
}
```

Please give a message with the raised value error. Pending that, I'd give a positive review.



---

archive/issue_comments_011851.json:
```json
{
    "body": "Attachment [trac_1877.patch](tarball://root/attachments/some-uuid/ticket1877/trac_1877.patch) by @jicama created at 2008-09-02 23:15:50\n\nthomag, your patch is along the right lines, but the implementation wasn't quite right.  You don't need to catch an error after raising it and then print something to the screen.  Just supply a message with the error, and it will show up unless it's caught somewhere else.  Also, when you fix a bug, you should add a doctest demonstrating the new, correct behavior.\n\nI've posted a new patch that raises an error in the usual way, and provides a briefer but still clear error message.  If this is accepted, only trac_1877.patch should be applied.",
    "created_at": "2008-09-02T23:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11851",
    "user": "https://github.com/jicama"
}
```

Attachment [trac_1877.patch](tarball://root/attachments/some-uuid/ticket1877/trac_1877.patch) by @jicama created at 2008-09-02 23:15:50

thomag, your patch is along the right lines, but the implementation wasn't quite right.  You don't need to catch an error after raising it and then print something to the screen.  Just supply a message with the error, and it will show up unless it's caught somewhere else.  Also, when you fix a bug, you should add a doctest demonstrating the new, correct behavior.

I've posted a new patch that raises an error in the usual way, and provides a briefer but still clear error message.  If this is accepted, only trac_1877.patch should be applied.



---

archive/issue_comments_011852.json:
```json
{
    "body": "Attachment [trac_1877_review.patch](tarball://root/attachments/some-uuid/ticket1877/trac_1877_review.patch) by anakha created at 2008-09-06 15:43:29\n\ntrac_1877_review.patch does some minor cosmetic adjustements on top of trac_1877.patch (like not starting the error messages with a capital).  Otherwise this gets a positive review from me.\n\nIt might still my part still needs to be reviewed so I'll leave it as needs review.",
    "created_at": "2008-09-06T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11852",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_1877_review.patch](tarball://root/attachments/some-uuid/ticket1877/trac_1877_review.patch) by anakha created at 2008-09-06 15:43:29

trac_1877_review.patch does some minor cosmetic adjustements on top of trac_1877.patch (like not starting the error messages with a capital).  Otherwise this gets a positive review from me.

It might still my part still needs to be reviewed so I'll leave it as needs review.



---

archive/issue_comments_011853.json:
```json
{
    "body": "Your review patch looks good to me, positive review.  Both trac_1877.patch and trac_1877_review.patch should be applied",
    "created_at": "2008-09-06T15:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11853",
    "user": "https://github.com/jicama"
}
```

Your review patch looks good to me, positive review.  Both trac_1877.patch and trac_1877_review.patch should be applied



---

archive/issue_comments_011854.json:
```json
{
    "body": "Oops, this won't pass it's doctests as written, since the review patch alters the error message thrown, but not the doctest.",
    "created_at": "2008-09-06T16:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11854",
    "user": "https://github.com/jicama"
}
```

Oops, this won't pass it's doctests as written, since the review patch alters the error message thrown, but not the doctest.



---

archive/issue_comments_011855.json:
```json
{
    "body": "Shame on me.  But with the new patch the doctests are changed and they pass.",
    "created_at": "2008-09-06T16:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11855",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Shame on me.  But with the new patch the doctests are changed and they pass.



---

archive/issue_comments_011856.json:
```json
{
    "body": "Attachment [trac_1877_doctests.patch](tarball://root/attachments/some-uuid/ticket1877/trac_1877_doctests.patch) by anakha created at 2008-09-06 16:14:40",
    "created_at": "2008-09-06T16:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11856",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_1877_doctests.patch](tarball://root/attachments/some-uuid/ticket1877/trac_1877_doctests.patch) by anakha created at 2008-09-06 16:14:40



---

archive/issue_comments_011857.json:
```json
{
    "body": "Merged trac_1877.patch, trac_1877_review.patch and trac_1877_doctests.patch in Sage 3.1.2.rc0.",
    "created_at": "2008-09-06T23:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_1877.patch, trac_1877_review.patch and trac_1877_doctests.patch in Sage 3.1.2.rc0.



---

archive/issue_comments_011858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-06T23:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002035.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-06T23:12:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1877#event-2035"
}
```
