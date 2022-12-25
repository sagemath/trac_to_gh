# Issue 1640: missing documentation Elliptic Curve - heegner_discriminants

archive/issues_001640.json:
```json
{
    "body": "Assignee: tba\n\nDocumentation missing:\n\n```\nE = EllipticCurve('5077a')\nE.heegner_discriminants?\n```\n\n\n\nsays\n\n\n\n```\nFile:        /opt/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\nType:        <type 'instancemethod'>\nDefinition:  E.heegner_discriminants(bound)\nDocstring: \nx.__init__(...) initializes x; see x.__class__.__doc__ for signature\n```\n\n\n\nbut\n\n\n\n```\nE.heegner_index?\n```\n\n\n\nis ok.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1640\n\n",
    "created_at": "2007-12-30T14:27:11Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "missing documentation Elliptic Curve - heegner_discriminants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1640",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: tba

Documentation missing:

```
E = EllipticCurve('5077a')
E.heegner_discriminants?
```



says



```
File:        /opt/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py
Type:        <type 'instancemethod'>
Definition:  E.heegner_discriminants(bound)
Docstring: 
x.__init__(...) initializes x; see x.__class__.__doc__ for signature
```



but



```
E.heegner_index?
```



is ok.

Issue created by migration from https://trac.sagemath.org/ticket/1640





---

archive/issue_comments_010398.json:
```json
{
    "body": "Attachment [1640.patch](tarball://root/attachments/some-uuid/ticket1640/1640.patch) by @aghitza created at 2008-01-08 11:28:10",
    "created_at": "2008-01-08T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10398",
    "user": "https://github.com/aghitza"
}
```

Attachment [1640.patch](tarball://root/attachments/some-uuid/ticket1640/1640.patch) by @aghitza created at 2008-01-08 11:28:10



---

archive/issue_comments_010399.json:
```json
{
    "body": "Changing component from documentation to algebraic geometry.",
    "created_at": "2008-01-08T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10399",
    "user": "https://github.com/aghitza"
}
```

Changing component from documentation to algebraic geometry.



---

archive/issue_comments_010400.json:
```json
{
    "body": "Changing assignee from tba to @williamstein.",
    "created_at": "2008-01-08T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10400",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tba to @williamstein.



---

archive/issue_comments_010401.json:
```json
{
    "body": "Looks very good!",
    "created_at": "2008-01-16T17:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10401",
    "user": "https://github.com/williamstein"
}
```

Looks very good!



---

archive/issue_comments_010402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T17:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001798.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-16T17:05:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1640#event-1798"
}
```



---

archive/issue_comments_010403.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4",
    "created_at": "2008-01-16T17:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha4
