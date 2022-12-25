# Issue 1503: [with patch] calculus -- formal function calls don't coerce correctly to Mathematica

archive/issues_001503.json:
```json
{
    "body": "Assignee: @williamstein\n\nBefore this patch if you make a formal function it will\nnot coerce into Mathematica.  E.g..\n\n\n```\nsage: f = function('Foo', var('x'), var('y'))\nsage: mathematica(f)\nFoo[x, y]\n```\n\n\nWith this patch it does work. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1503\n\n",
    "created_at": "2007-12-14T05:50:21Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] calculus -- formal function calls don't coerce correctly to Mathematica",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1503",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Before this patch if you make a formal function it will
not coerce into Mathematica.  E.g..


```
sage: f = function('Foo', var('x'), var('y'))
sage: mathematica(f)
Foo[x, y]
```


With this patch it does work. 

Issue created by migration from https://trac.sagemath.org/ticket/1503





---

archive/issue_comments_009610.json:
```json
{
    "body": "Attachment [trac-1503.patch](tarball://root/attachments/some-uuid/ticket1503/trac-1503.patch) by mabshoff created at 2007-12-15 23:37:20",
    "created_at": "2007-12-15T23:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1503#issuecomment-9610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-1503.patch](tarball://root/attachments/some-uuid/ticket1503/trac-1503.patch) by mabshoff created at 2007-12-15 23:37:20



---

archive/issue_comments_009611.json:
```json
{
    "body": "\n```\n[00:32] <mabshoff> about 1503: Shoudln't the mathematica doctests require mathematica?\n[00:32] <rlm> was-1464: it was a rewrite or nice, line by line, so actually it's a little cleaner\n[00:32] <rlm> the memory management for example\n[00:33] <was-1464> yes, put # optional there.\n[00:33] <mabshoff> ok, will do.\n[00:33] <was-1464> But *only* in the two lines with mathematica(...)\n[00:33] <was-1464> Matheamtica is *not* needed for the _mathematica_init_ lines\n[00:33] <mabshoff> Yep, I was about to ask for clarification on that.\n```\n",
    "created_at": "2007-12-15T23:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1503#issuecomment-9611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[00:32] <mabshoff> about 1503: Shoudln't the mathematica doctests require mathematica?
[00:32] <rlm> was-1464: it was a rewrite or nice, line by line, so actually it's a little cleaner
[00:32] <rlm> the memory management for example
[00:33] <was-1464> yes, put # optional there.
[00:33] <mabshoff> ok, will do.
[00:33] <was-1464> But *only* in the two lines with mathematica(...)
[00:33] <was-1464> Matheamtica is *not* needed for the _mathematica_init_ lines
[00:33] <mabshoff> Yep, I was about to ask for clarification on that.
```




---

archive/issue_comments_009612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T01:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1503#issuecomment-9612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009613.json:
```json
{
    "body": "Merged in 2.9.rc2.",
    "created_at": "2007-12-16T01:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1503#issuecomment-9613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc2.
