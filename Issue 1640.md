# Issue 1640: missing documentation Elliptic Curve - heegner_discriminants

archive/issues_001640.json:
```json
{
    "body": "Assignee: tba\n\nDocumentation missing:\n\n```\nE = EllipticCurve('5077a')\nE.heegner_discriminants?\n```\n\n\n\nsays\n\n\n\n```\nFile:        /opt/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\nType:        <type 'instancemethod'>\nDefinition:  E.heegner_discriminants(bound)\nDocstring: \nx.__init__(...) initializes x; see x.__class__.__doc__ for signature\n```\n\n\n\nbut\n\n\n\n```\nE.heegner_index?\n```\n\n\n\nis ok.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1640\n\n",
    "created_at": "2007-12-30T14:27:11Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "missing documentation Elliptic Curve - heegner_discriminants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1640",
    "user": "@haraldschilly"
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

archive/issue_comments_010425.json:
```json
{
    "body": "Attachment [1640.patch](tarball://root/attachments/some-uuid/ticket1640/1640.patch) by @aghitza created at 2008-01-08 11:28:10",
    "created_at": "2008-01-08T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10425",
    "user": "@aghitza"
}
```

Attachment [1640.patch](tarball://root/attachments/some-uuid/ticket1640/1640.patch) by @aghitza created at 2008-01-08 11:28:10



---

archive/issue_comments_010426.json:
```json
{
    "body": "Changing component from documentation to algebraic geometry.",
    "created_at": "2008-01-08T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10426",
    "user": "@aghitza"
}
```

Changing component from documentation to algebraic geometry.



---

archive/issue_comments_010427.json:
```json
{
    "body": "Changing assignee from tba to @williamstein.",
    "created_at": "2008-01-08T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10427",
    "user": "@aghitza"
}
```

Changing assignee from tba to @williamstein.



---

archive/issue_comments_010428.json:
```json
{
    "body": "Looks very good!",
    "created_at": "2008-01-16T17:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10428",
    "user": "@williamstein"
}
```

Looks very good!



---

archive/issue_comments_010429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T17:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10429",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010430.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4",
    "created_at": "2008-01-16T17:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1640#issuecomment-10430",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha4
