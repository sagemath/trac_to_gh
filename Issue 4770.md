# Issue 4770: [with patch, needs review] implement maxima.cputime()

archive/issues_004770.json:
```json
{
    "body": "Assignee: malb\n\nThis should work:\n\n\n```\nsage: t = maxima.cputime()\nsage: _ = maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])\nsage: maxima.cputime(t)\n0.568913\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4770\n\n",
    "created_at": "2008-12-12T16:34:29Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] implement maxima.cputime()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4770",
    "user": "malb"
}
```
Assignee: malb

This should work:


```
sage: t = maxima.cputime()
sage: _ = maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])
sage: maxima.cputime(t)
0.568913
```


Issue created by migration from https://trac.sagemath.org/ticket/4770





---

archive/issue_comments_036135.json:
```json
{
    "body": "Attachment [maxima_cputime.patch](tarball://root/attachments/some-uuid/ticket4770/maxima_cputime.patch) by malb created at 2008-12-12 16:34:39",
    "created_at": "2008-12-12T16:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36135",
    "user": "malb"
}
```

Attachment [maxima_cputime.patch](tarball://root/attachments/some-uuid/ticket4770/maxima_cputime.patch) by malb created at 2008-12-12 16:34:39



---

archive/issue_comments_036136.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima, cputime\".",
    "created_at": "2009-01-24T16:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36136",
    "user": "SimonKing"
}
```

Changing keywords from "" to "maxima, cputime".



---

archive/issue_comments_036137.json:
```json
{
    "body": "The patch applies cleanly, the doc test example works as expected, and it provides a useful functionality.\n\nHence, positive review!",
    "created_at": "2009-01-24T16:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36137",
    "user": "SimonKing"
}
```

The patch applies cleanly, the doc test example works as expected, and it provides a useful functionality.

Hence, positive review!



---

archive/issue_comments_036138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T16:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36138",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036139.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T16:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4770#issuecomment-36139",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
