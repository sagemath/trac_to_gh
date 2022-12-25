# Issue 4770: [with patch, needs review] implement maxima.cputime()

archive/issues_004770.json:
```json
{
    "body": "Assignee: @malb\n\nThis should work:\n\n\n```\nsage: t = maxima.cputime()\nsage: _ = maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])\nsage: maxima.cputime(t)\n0.568913\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4770\n\n",
    "created_at": "2008-12-12T16:34:29Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] implement maxima.cputime()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4770",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

This should work:


```
sage: t = maxima.cputime()
sage: _ = maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])
sage: maxima.cputime(t)
0.568913
```


Issue created by migration from https://trac.sagemath.org/ticket/4770





---

archive/issue_comments_036064.json:
```json
{
    "body": "Attachment [maxima_cputime.patch](tarball://root/attachments/some-uuid/ticket4770/maxima_cputime.patch) by @malb created at 2008-12-12 16:34:39",
    "created_at": "2008-12-12T16:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36064",
    "user": "https://github.com/malb"
}
```

Attachment [maxima_cputime.patch](tarball://root/attachments/some-uuid/ticket4770/maxima_cputime.patch) by @malb created at 2008-12-12 16:34:39



---

archive/issue_comments_036065.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima, cputime\".",
    "created_at": "2009-01-24T16:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36065",
    "user": "https://github.com/simon-king-jena"
}
```

Changing keywords from "" to "maxima, cputime".



---

archive/issue_comments_036066.json:
```json
{
    "body": "The patch applies cleanly, the doc test example works as expected, and it provides a useful functionality.\n\nHence, positive review!",
    "created_at": "2009-01-24T16:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36066",
    "user": "https://github.com/simon-king-jena"
}
```

The patch applies cleanly, the doc test example works as expected, and it provides a useful functionality.

Hence, positive review!



---

archive/issue_comments_036067.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T16:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036068.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T16:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_events_005012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T16:16:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4770#event-5012"
}
```
