# Issue 5356: 100r returns a Sage integer in the notebook (but commandline works fine)

archive/issues_005356.json:
```json
{
    "body": "Assignee: boothby\n\ntype(100r) returns\n\n<type 'sage.rings.integer.Integer'>\n\nin the notebook in 3.3.  Similarly, type(1.0r) returns\n\n<type 'sage.rings.real_mpfr.RealLiteral'>\n\nBoth of these examples work fine on the command line (i.e., return python int and float, respectively).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5356\n\n",
    "created_at": "2009-02-24T07:53:16Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "100r returns a Sage integer in the notebook (but commandline works fine)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5356",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

type(100r) returns

<type 'sage.rings.integer.Integer'>

in the notebook in 3.3.  Similarly, type(1.0r) returns

<type 'sage.rings.real_mpfr.RealLiteral'>

Both of these examples work fine on the command line (i.e., return python int and float, respectively).



Issue created by migration from https://trac.sagemath.org/ticket/5356





---

archive/issue_events_012489.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-02-24T07:53:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5356#event-12489"
}
```



---

archive/issue_comments_041181.json:
```json
{
    "body": "Attachment [5356-notebook-preparser.patch](tarball://root/attachments/some-uuid/ticket5356/5356-notebook-preparser.patch) by @robertwb created at 2009-02-24 08:13:37",
    "created_at": "2009-02-24T08:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5356#issuecomment-41181",
    "user": "https://github.com/robertwb"
}
```

Attachment [5356-notebook-preparser.patch](tarball://root/attachments/some-uuid/ticket5356/5356-notebook-preparser.patch) by @robertwb created at 2009-02-24 08:13:37



---

archive/issue_comments_041182.json:
```json
{
    "body": "This patch fixes the problem and passes doctests in preparser.py.  Someone more familiar with the preparse might look at it, but it's a positive review for me.",
    "created_at": "2009-02-24T08:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5356#issuecomment-41182",
    "user": "https://github.com/jasongrout"
}
```

This patch fixes the problem and passes doctests in preparser.py.  Someone more familiar with the preparse might look at it, but it's a positive review for me.



---

archive/issue_comments_041183.json:
```json
{
    "body": "+1 from me.",
    "created_at": "2009-02-24T14:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5356#issuecomment-41183",
    "user": "https://github.com/williamstein"
}
```

+1 from me.



---

archive/issue_comments_041184.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5356#issuecomment-41184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_events_012490.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-24T19:53:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5356#event-12490"
}
```



---

archive/issue_comments_041185.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5356#issuecomment-41185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
