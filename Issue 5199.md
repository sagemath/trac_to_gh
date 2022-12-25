# Issue 5199: [with patch, needs review] new symbolics can treat floats as integers inappropriately

archive/issues_005199.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @burcin\n\nConsider the following, in 3.3.alpha5:\n\n```\nsage: from sage.symbolic.ring import NSR\nsage: NSR(10.0).gamma()\n362880\n```\nWe have produced an exact integral result of .gamma() on a floating-point number.\n\nAfter #2898, this behavior makes doctests fail; but the above happens even before #2898.\n\nI don't know if this is the \"right\" patch, but it does make all doctests pass after #2898.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5199\n\n",
    "created_at": "2009-02-07T05:15:40Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] new symbolics can treat floats as integers inappropriately",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5199",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @burcin

CC:  @burcin

Consider the following, in 3.3.alpha5:

```
sage: from sage.symbolic.ring import NSR
sage: NSR(10.0).gamma()
362880
```
We have produced an exact integral result of .gamma() on a floating-point number.

After #2898, this behavior makes doctests fail; but the above happens even before #2898.

I don't know if this is the "right" patch, but it does make all doctests pass after #2898.

Issue created by migration from https://trac.sagemath.org/ticket/5199





---

archive/issue_comments_039762.json:
```json
{
    "body": "Attachment [pynac_is_integer.patch](tarball://root/attachments/some-uuid/ticket5199/pynac_is_integer.patch) by @burcin created at 2009-02-08 13:24:32\n\nThe patch looks good. \n\nWe might think about optimizing this function for speed later. Specialcasing Integer and Rational, and using the _parent attribute should help here.",
    "created_at": "2009-02-08T13:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5199#issuecomment-39762",
    "user": "https://github.com/burcin"
}
```

Attachment [pynac_is_integer.patch](tarball://root/attachments/some-uuid/ticket5199/pynac_is_integer.patch) by @burcin created at 2009-02-08 13:24:32

The patch looks good. 

We might think about optimizing this function for speed later. Specialcasing Integer and Rational, and using the _parent attribute should help here.



---

archive/issue_events_012034.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-09T07:53:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5199",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5199#event-12034"
}
```



---

archive/issue_comments_039763.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T07:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5199#issuecomment-39763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_comments_039764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-09T07:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5199#issuecomment-39764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
