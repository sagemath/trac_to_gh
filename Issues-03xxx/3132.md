# Issue 3132: [with patch, positive review] Add computation of multinomial coefficients

archive/issues_003132.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  sage-combinat\n\nKeywords: editor_cwitty\n\nThe attached code computes multinomial coefficients using products of binomial coefficients, which is reasonably fast even for large inputs.\n\n(However, MMA is about 3-4x times faster on my machine.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3132\n\n",
    "closed_at": "2008-06-23T06:43:04Z",
    "created_at": "2008-05-08T13:16:47Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, positive review] Add computation of multinomial coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3132",
    "user": "https://trac.sagemath.org/admin/accounts/users/gebner"
}
```
Assignee: somebody

CC:  sage-combinat

Keywords: editor_cwitty

The attached code computes multinomial coefficients using products of binomial coefficients, which is reasonably fast even for large inputs.

(However, MMA is about 3-4x times faster on my machine.)

Issue created by migration from https://trac.sagemath.org/ticket/3132





---

archive/issue_events_007083.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-08T13:30:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "milestone": "sage-3.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3132#event-7083"
}
```



---

archive/issue_comments_021706.json:
```json
{
    "body": "Attachment [trac3132.diff](tarball://root/attachments/some-uuid/ticket3132/trac3132.diff) by mabshoff created at 2008-05-08 13:30:41",
    "created_at": "2008-05-08T13:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac3132.diff](tarball://root/attachments/some-uuid/ticket3132/trac3132.diff) by mabshoff created at 2008-05-08 13:30:41



---

archive/issue_comments_021707.json:
```json
{
    "body": "Code looks good, but the doctest fails on a 32-bit platform (due to #3134).  Either the doctest needs to be changed to use smaller numbers, or #3134 needs to be fixed.",
    "created_at": "2008-05-10T20:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21707",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, but the doctest fails on a 32-bit platform (due to #3134).  Either the doctest needs to be changed to use smaller numbers, or #3134 needs to be fixed.



---

archive/issue_comments_021708.json:
```json
{
    "body": "Attachment [trac3132-2.diff](tarball://root/attachments/some-uuid/ticket3132/trac3132-2.diff) by gebner created at 2008-05-12 08:58:11\n\nfix doctest not to hit #3134",
    "created_at": "2008-05-12T08:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21708",
    "user": "https://trac.sagemath.org/admin/accounts/users/gebner"
}
```

Attachment [trac3132-2.diff](tarball://root/attachments/some-uuid/ticket3132/trac3132-2.diff) by gebner created at 2008-05-12 08:58:11

fix doctest not to hit #3134



---

archive/issue_comments_021709.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_cwitty\".",
    "created_at": "2008-06-20T04:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21709",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_cwitty".



---

archive/issue_comments_021710.json:
```json
{
    "body": "Looks good.  Thanks for fixing the doctest, and sorry it took so long to re-review.\n\nApply only the second patch.",
    "created_at": "2008-06-20T07:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21710",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good.  Thanks for fixing the doctest, and sorry it took so long to re-review.

Apply only the second patch.



---

archive/issue_events_007084.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T06:43:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3132#event-7084"
}
```



---

archive/issue_comments_021711.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T06:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021712.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0\n\nGabriel,\n\nplease post hg patches and not diffs in the future, i.e. hg export instead of hg diff. I committed the patch in your name in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T06:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha0

Gabriel,

please post hg patches and not diffs in the future, i.e. hg export instead of hg diff. I committed the patch in your name in this case.

Cheers,

Michael



---

archive/issue_events_007085.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T06:49:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "milestone": "sage-3.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3132#event-7085"
}
```



---

archive/issue_events_007086.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T06:49:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3132#event-7086"
}
```
