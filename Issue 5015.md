# Issue 5015: Horrible bug in old (and new) symbolic calculus: f(x)=1; f*e --> BOOM!

archive/issues_005015.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\n\n\nOn Sun, Jan 18, 2009 at 7:08 AM, YannLC  wrote:\n>\n> but in fact the same error occurs without ns=1...\n>\n> ----------------------------------------------------------------------\n> | Sage Version 3.2.3, Release Date: 2009-01-05                       |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> sage: f(x)=1\n> sage: f*e\n> [...]\n> RuntimeError: maximum recursion depth exceeded\n\nThat is weird.  What a horrible bug!   Thanks for reporting this.  It is now trac #\n```\n\n\nIt also happens with ns=1.  I've verified this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5015\n\n",
    "created_at": "2009-01-18T15:18:36Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Horrible bug in old (and new) symbolic calculus: f(x)=1; f*e --> BOOM!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5015",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin


```


On Sun, Jan 18, 2009 at 7:08 AM, YannLC  wrote:
>
> but in fact the same error occurs without ns=1...
>
> ----------------------------------------------------------------------
> | Sage Version 3.2.3, Release Date: 2009-01-05                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: f(x)=1
> sage: f*e
> [...]
> RuntimeError: maximum recursion depth exceeded

That is weird.  What a horrible bug!   Thanks for reporting this.  It is now trac #
```


It also happens with ns=1.  I've verified this.

Issue created by migration from https://trac.sagemath.org/ticket/5015





---

archive/issue_comments_038144.json:
```json
{
    "body": "Attachment [trac_5015.patch](tarball://root/attachments/some-uuid/ticket5015/trac_5015.patch) by @mwhansen created at 2009-01-18 19:53:15\n\nNote that the new code doesn't get run as doing\n\nf(x) = 1\n\noverwrites the old x (which was created with var('x',ns=1)) with just var('x').  The infinite recursion is due the CallableSymbolicExpression ring assuming that all elements of SR were instances of SymbolicExpression.",
    "created_at": "2009-01-18T19:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5015#issuecomment-38144",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5015.patch](tarball://root/attachments/some-uuid/ticket5015/trac_5015.patch) by @mwhansen created at 2009-01-18 19:53:15

Note that the new code doesn't get run as doing

f(x) = 1

overwrites the old x (which was created with var('x',ns=1)) with just var('x').  The infinite recursion is due the CallableSymbolicExpression ring assuming that all elements of SR were instances of SymbolicExpression.



---

archive/issue_comments_038145.json:
```json
{
    "body": "Looks good.  Great work fixing this so quickly!",
    "created_at": "2009-01-18T20:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5015#issuecomment-38145",
    "user": "https://github.com/williamstein"
}
```

Looks good.  Great work fixing this so quickly!



---

archive/issue_comments_038146.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T04:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5015#issuecomment-38146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038147.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T04:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5015#issuecomment-38147",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
