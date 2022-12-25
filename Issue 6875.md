# Issue 6875: [with patch, needs review] fill option is broken for polar_plot

archive/issues_006875.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: polar_plot, fill\n\nThe fill option for polar_plot does not work correctly anymore.\n\nThe following two doctests don't produce the supposed output:\n\n* Fill the area between two functions:\n\n```\nsage: polar_plot(cos(4*x) + 1.5, 0, 2*pi, fill=0.5 * cos(4*x) + 2.5, fillcolor='orange').show(aspect_ratio=1)\n```\n\n* Fill the area between several spirals:\n\n```\nsage: polar_plot([(1.2+k*0.2)*log(x) for k in range(6)], 1, 3 * pi, fill = {0: [1], 2: [3], 4: [5]})\n```\n\nThis regression has been introduced with the changeset 12287 (Ticket: #5930).\n\nSage really needs a test framework for plots. Otherwise more and more regressions will creep in, without anybody noticing.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6875\n\n",
    "created_at": "2009-09-03T11:03:40Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] fill option is broken for polar_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6875",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: @williamstein

Keywords: polar_plot, fill

The fill option for polar_plot does not work correctly anymore.

The following two doctests don't produce the supposed output:

* Fill the area between two functions:

```
sage: polar_plot(cos(4*x) + 1.5, 0, 2*pi, fill=0.5 * cos(4*x) + 2.5, fillcolor='orange').show(aspect_ratio=1)
```

* Fill the area between several spirals:

```
sage: polar_plot([(1.2+k*0.2)*log(x) for k in range(6)], 1, 3 * pi, fill = {0: [1], 2: [3], 4: [5]})
```

This regression has been introduced with the changeset 12287 (Ticket: #5930).

Sage really needs a test framework for plots. Otherwise more and more regressions will creep in, without anybody noticing.


Issue created by migration from https://trac.sagemath.org/ticket/6875





---

archive/issue_comments_056649.json:
```json
{
    "body": "Attachment [trac_6875_fill_regression.patch](tarball://root/attachments/some-uuid/ticket6875/trac_6875_fill_regression.patch) by whuss created at 2009-09-03 11:06:29",
    "created_at": "2009-09-03T11:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56649",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [trac_6875_fill_regression.patch](tarball://root/attachments/some-uuid/ticket6875/trac_6875_fill_regression.patch) by whuss created at 2009-09-03 11:06:29



---

archive/issue_comments_056650.json:
```json
{
    "body": "It still doesn't seem like the first example above works for me---I get a single solid figure.  Is it supposed to have a band around it's edge?",
    "created_at": "2009-09-15T09:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56650",
    "user": "https://github.com/jasongrout"
}
```

It still doesn't seem like the first example above works for me---I get a single solid figure.  Is it supposed to have a band around it's edge?



---

archive/issue_comments_056651.json:
```json
{
    "body": "Attachment [polar_1.png](tarball://root/attachments/some-uuid/ticket6875/polar_1.png) by whuss created at 2009-09-15 09:20:33\n\nThe correct output of the first example",
    "created_at": "2009-09-15T09:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56651",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [polar_1.png](tarball://root/attachments/some-uuid/ticket6875/polar_1.png) by whuss created at 2009-09-15 09:20:33

The correct output of the first example



---

archive/issue_comments_056652.json:
```json
{
    "body": "Attachment [polar_2.png](tarball://root/attachments/some-uuid/ticket6875/polar_2.png) by whuss created at 2009-09-15 09:21:50\n\nThe correct output of the second example",
    "created_at": "2009-09-15T09:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56652",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [polar_2.png](tarball://root/attachments/some-uuid/ticket6875/polar_2.png) by whuss created at 2009-09-15 09:21:50

The correct output of the second example



---

archive/issue_comments_056653.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> It still doesn't seem like the first example above works for me---I get a single solid figure.  Is it supposed to have a band around it's edge?\n\n\nI've attached two images with the correct output of the two examples.\nIs this what you get with the patch?",
    "created_at": "2009-09-15T09:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56653",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:1 jason]:
> It still doesn't seem like the first example above works for me---I get a single solid figure.  Is it supposed to have a band around it's edge?


I've attached two images with the correct output of the two examples.
Is this what you get with the patch?



---

archive/issue_comments_056654.json:
```json
{
    "body": "I compiled a fresh version of 4.1.1.alpha1 overnight, and everything seems to work on that.  So positive review!\n\n(Note to everyone else: the functions above were already in the doctests, but just were not working).\n\nI wish this would have been working last week when I taught finding areas in polar coordinates! I'm glad you found the fix.",
    "created_at": "2009-09-15T15:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56654",
    "user": "https://github.com/jasongrout"
}
```

I compiled a fresh version of 4.1.1.alpha1 overnight, and everything seems to work on that.  So positive review!

(Note to everyone else: the functions above were already in the doctests, but just were not working).

I wish this would have been working last week when I taught finding areas in polar coordinates! I'm glad you found the fix.



---

archive/issue_comments_056655.json:
```json
{
    "body": "Merged `trac_6875_fill_regression.patch`.",
    "created_at": "2009-09-15T23:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6875_fill_regression.patch`.



---

archive/issue_comments_056656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-15T23:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6875#issuecomment-56656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016174.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-15T23:30:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6875",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6875#event-16174"
}
```
