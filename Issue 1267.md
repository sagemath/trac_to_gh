# Issue 1267: [with patch] documentation for piecewise does not show up in notebook

archive/issues_001267.json:
```json
{
    "body": "Assignee: @mwhansen\n\nIn the public notebook (on www.sagenb.org), when I evaluate a cell with `piecewise?`, I get this:\n\n```\nFile:        /usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/functions/piecewise.py\nType:        <type 'classobj'>\nDefinition:  piecewise(x0)\nDocstring:\n```\nwith no actual docstring.  (Doing the same thing from the command line does give a useful docstring.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1267\n\n",
    "closed_at": "2007-12-09T13:13:17Z",
    "created_at": "2007-11-25T15:09:41Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] documentation for piecewise does not show up in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1267",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @mwhansen

In the public notebook (on www.sagenb.org), when I evaluate a cell with `piecewise?`, I get this:

```
File:        /usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/functions/piecewise.py
Type:        <type 'classobj'>
Definition:  piecewise(x0)
Docstring:
```
with no actual docstring.  (Doing the same thing from the command line does give a useful docstring.)


Issue created by migration from https://trac.sagemath.org/ticket/1267





---

archive/issue_events_003334.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-25T17:56:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1267#event-3334"
}
```



---

archive/issue_comments_007919.json:
```json
{
    "body": "After some testing it turns out that cwitty is right and it does work in console mode with 2.8.14 So was is wrong and change it back.",
    "created_at": "2007-11-25T17:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7919",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

After some testing it turns out that cwitty is right and it does work in console mode with 2.8.14 So was is wrong and change it back.



---

archive/issue_comments_007920.json:
```json
{
    "body": "I can confirm and replicate this problem:\n\n```\n[10:09am] was_: It does fail on my ocally-running notebook.\n[10:09am] was_: Ipython does the help on the command line.\n[10:09am] was_: *I* wrote what does the help in the notebook.\n[10:09am] DenisG_: (my locally running notebook)\n[10:09am] was_: It's separate code; I think it is is sage/server/support.py or something like that\n[10:10am] was_: And there is definitely a bug.\n```",
    "created_at": "2007-11-25T18:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7920",
    "user": "https://github.com/williamstein"
}
```

I can confirm and replicate this problem:

```
[10:09am] was_: It does fail on my ocally-running notebook.
[10:09am] was_: Ipython does the help on the command line.
[10:09am] was_: *I* wrote what does the help in the notebook.
[10:09am] DenisG_: (my locally running notebook)
[10:09am] was_: It's separate code; I think it is is sage/server/support.py or something like that
[10:10am] was_: And there is definitely a bug.
```



---

archive/issue_comments_007921.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T00:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7921",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007922.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2007-12-06T00:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7922",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_007923.json:
```json
{
    "body": "Actually, I don't think anything wrong with the ? or ?? notation.  What was happening was roughly the following:\n\n```\nclass PiecewisePolynomial:\n    def __init__(self, list_of_pairs):\n        \"\"\"docstring\"\"\"\n\n    ...\n\npiecewise = PiecewisePolynomial\n```\n\nThe result of piecewise? was correct since PiecewisePolynomial didn't have a class docstring.",
    "created_at": "2007-12-06T00:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7923",
    "user": "https://github.com/mwhansen"
}
```

Actually, I don't think anything wrong with the ? or ?? notation.  What was happening was roughly the following:

```
class PiecewisePolynomial:
    def __init__(self, list_of_pairs):
        """docstring"""

    ...

piecewise = PiecewisePolynomial
```

The result of piecewise? was correct since PiecewisePolynomial didn't have a class docstring.



---

archive/issue_comments_007924.json:
```json
{
    "body": "Attachment [1267.patch](tarball://root/attachments/some-uuid/ticket1267/1267.patch) by @mwhansen created at 2007-12-06 00:28:42",
    "created_at": "2007-12-06T00:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7924",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1267.patch](tarball://root/attachments/some-uuid/ticket1267/1267.patch) by @mwhansen created at 2007-12-06 00:28:42



---

archive/issue_comments_007925.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T12:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_007926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T13:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007927.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T13:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7927",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha2.



---

archive/issue_events_003335.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-09T13:13:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1267#event-3335"
}
```
