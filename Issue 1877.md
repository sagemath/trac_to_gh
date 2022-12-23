# Issue 1877: same range variables -- bug in 3d plotting (probably very very very easy to fix)

archive/issues_001877.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: var('x,y')\nsage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))\nboom!\n```\n\n\nThe problem is that both ranges use the variable x.  The fix is to make\nsure that the two variables are different and if not raise an exception (do this also in parametric_plot3d). \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1877\n\n",
    "created_at": "2008-01-21T06:40:06Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "same range variables -- bug in 3d plotting (probably very very very easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1877",
    "user": "was"
}
```
Assignee: was


```
sage: var('x,y')
sage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))
boom!
```


The problem is that both ranges use the variable x.  The fix is to make
sure that the two variables are different and if not raise an exception (do this also in parametric_plot3d). 


Issue created by migration from https://trac.sagemath.org/ticket/1877





---

archive/issue_comments_011875.json:
```json
{
    "body": "Attachment\n\nplot3d and parametric_plot3d should fail a tiny bit more gracefully if they're given two ranges using the same variable:\n\n```\nsage: var('x,y')\nsage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))\nValueError: If the ranges in the argument of plot3d are 3-tuples, then the first components of those 3-tuples must be different.\nsage: var('u,v')\nsage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, 2*pi), (u, -pi, pi))\nValueError: If the ranges in the argument of parametric_plot3d are both 3-tuples, then the first components of those 3-tuples must be different.\n```\n",
    "created_at": "2008-08-26T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11875",
    "user": "thomag"
}
```

Attachment

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

archive/issue_comments_011876.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-26T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11876",
    "user": "thomag"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011877.json:
```json
{
    "body": "Changing assignee from was to thomag.",
    "created_at": "2008-08-26T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11877",
    "user": "thomag"
}
```

Changing assignee from was to thomag.



---

archive/issue_comments_011878.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-08-29T00:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11878",
    "user": "mabshoff"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_011879.json:
```json
{
    "body": "Please give a message with the raised value error. Pending that, I'd give a positive review.",
    "created_at": "2008-09-02T08:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11879",
    "user": "robertwb"
}
```

Please give a message with the raised value error. Pending that, I'd give a positive review.



---

archive/issue_comments_011880.json:
```json
{
    "body": "Attachment\n\nthomag, your patch is along the right lines, but the implementation wasn't quite right.  You don't need to catch an error after raising it and then print something to the screen.  Just supply a message with the error, and it will show up unless it's caught somewhere else.  Also, when you fix a bug, you should add a doctest demonstrating the new, correct behavior.\n\nI've posted a new patch that raises an error in the usual way, and provides a briefer but still clear error message.  If this is accepted, only trac_1877.patch should be applied.",
    "created_at": "2008-09-02T23:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11880",
    "user": "jwmerrill"
}
```

Attachment

thomag, your patch is along the right lines, but the implementation wasn't quite right.  You don't need to catch an error after raising it and then print something to the screen.  Just supply a message with the error, and it will show up unless it's caught somewhere else.  Also, when you fix a bug, you should add a doctest demonstrating the new, correct behavior.

I've posted a new patch that raises an error in the usual way, and provides a briefer but still clear error message.  If this is accepted, only trac_1877.patch should be applied.



---

archive/issue_comments_011881.json:
```json
{
    "body": "Attachment\n\ntrac_1877_review.patch does some minor cosmetic adjustements on top of trac_1877.patch (like not starting the error messages with a capital).  Otherwise this gets a positive review from me.\n\nIt might still my part still needs to be reviewed so I'll leave it as needs review.",
    "created_at": "2008-09-06T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11881",
    "user": "anakha"
}
```

Attachment

trac_1877_review.patch does some minor cosmetic adjustements on top of trac_1877.patch (like not starting the error messages with a capital).  Otherwise this gets a positive review from me.

It might still my part still needs to be reviewed so I'll leave it as needs review.



---

archive/issue_comments_011882.json:
```json
{
    "body": "Your review patch looks good to me, positive review.  Both trac_1877.patch and trac_1877_review.patch should be applied",
    "created_at": "2008-09-06T15:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11882",
    "user": "jwmerrill"
}
```

Your review patch looks good to me, positive review.  Both trac_1877.patch and trac_1877_review.patch should be applied



---

archive/issue_comments_011883.json:
```json
{
    "body": "Oops, this won't pass it's doctests as written, since the review patch alters the error message thrown, but not the doctest.",
    "created_at": "2008-09-06T16:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11883",
    "user": "jwmerrill"
}
```

Oops, this won't pass it's doctests as written, since the review patch alters the error message thrown, but not the doctest.



---

archive/issue_comments_011884.json:
```json
{
    "body": "Shame on me.  But with the new patch the doctests are changed and they pass.",
    "created_at": "2008-09-06T16:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11884",
    "user": "anakha"
}
```

Shame on me.  But with the new patch the doctests are changed and they pass.



---

archive/issue_comments_011885.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-06T16:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11885",
    "user": "anakha"
}
```

Attachment



---

archive/issue_comments_011886.json:
```json
{
    "body": "Merged trac_1877.patch, trac_1877_review.patch and trac_1877_doctests.patch in Sage 3.1.2.rc0.",
    "created_at": "2008-09-06T23:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11886",
    "user": "mabshoff"
}
```

Merged trac_1877.patch, trac_1877_review.patch and trac_1877_doctests.patch in Sage 3.1.2.rc0.



---

archive/issue_comments_011887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-06T23:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1877#issuecomment-11887",
    "user": "mabshoff"
}
```

Resolution: fixed
