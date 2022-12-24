# Issue 4262: Elliptic curve a_invariants command returns a list reference (BAD!!)

archive/issues_004262.json:
```json
{
    "body": "Assignee: was\n\nThis sucks:\n\n```\nsage: E = EllipticCurve([1,0,0,0,1])\nsage: E.a_invariants()[0] = 100000000\nsage: E\nElliptic Curve defined by y^2 + 100000000*x*y  = x^3 +1 over Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4262\n\n",
    "created_at": "2008-10-11T08:25:23Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Elliptic curve a_invariants command returns a list reference (BAD!!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4262",
    "user": "was"
}
```
Assignee: was

This sucks:

```
sage: E = EllipticCurve([1,0,0,0,1])
sage: E.a_invariants()[0] = 100000000
sage: E
Elliptic Curve defined by y^2 + 100000000*x*y  = x^3 +1 over Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/4262





---

archive/issue_comments_031083.json:
```json
{
    "body": "Attachment [sage-4262.patch](tarball://root/attachments/some-uuid/ticket4262/sage-4262.patch) by was created at 2008-10-11 08:31:58",
    "created_at": "2008-10-11T08:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31083",
    "user": "was"
}
```

Attachment [sage-4262.patch](tarball://root/attachments/some-uuid/ticket4262/sage-4262.patch) by was created at 2008-10-11 08:31:58



---

archive/issue_comments_031084.json:
```json
{
    "body": "\n",
    "created_at": "2008-10-11T08:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31084",
    "user": "was"
}
```






---

archive/issue_comments_031085.json:
```json
{
    "body": "Shouldn't we just return a tuple to emphasise that this is invariant?",
    "created_at": "2008-10-11T08:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31085",
    "user": "malb"
}
```

Shouldn't we just return a tuple to emphasise that this is invariant?



---

archive/issue_comments_031086.json:
```json
{
    "body": "Changing to tuples should be another ticket.",
    "created_at": "2008-10-11T09:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31086",
    "user": "was"
}
```

Changing to tuples should be another ticket.



---

archive/issue_comments_031087.json:
```json
{
    "body": "See #4264 for changing to return a tuple.",
    "created_at": "2008-10-11T09:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31087",
    "user": "was"
}
```

See #4264 for changing to return a tuple.



---

archive/issue_comments_031088.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-11T12:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31088",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.rc0



---

archive/issue_comments_031089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-11T12:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4262#issuecomment-31089",
    "user": "mabshoff"
}
```

Resolution: fixed
