# Issue 2036: maxima is off by -5 with it's charpoly

archive/issues_002036.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: matrix(SR, 5, [1..5^2]).charpoly().expand()\n-x^5 + 65*x^4 + 250*x^3\nsage: matrix(QQ, 5, [1..5^2]).charpoly()\nx^5 - 65*x^4 - 250*x^3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2036\n\n",
    "created_at": "2008-02-03T04:18:45Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "maxima is off by -5 with it's charpoly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2036",
    "user": "@mwhansen"
}
```
Assignee: @williamstein


```
sage: matrix(SR, 5, [1..5^2]).charpoly().expand()
-x^5 + 65*x^4 + 250*x^3
sage: matrix(QQ, 5, [1..5^2]).charpoly()
x^5 - 65*x^4 - 250*x^3
```


Issue created by migration from https://trac.sagemath.org/ticket/2036





---

archive/issue_comments_013172.json:
```json
{
    "body": "Maxima defines the charpoly as:\n\ndeterminant (M - diagmatrix (length (M), x))\n\nSee http://maxima.sourceforge.net/docs/manual/en/maxima_25.html#SEC81",
    "created_at": "2008-02-04T16:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2036#issuecomment-13172",
    "user": "@jasongrout"
}
```

Maxima defines the charpoly as:

determinant (M - diagmatrix (length (M), x))

See http://maxima.sourceforge.net/docs/manual/en/maxima_25.html#SEC81



---

archive/issue_comments_013173.json:
```json
{
    "body": "That's a nonstandard definition so we have to work around it.\n\nWilliam",
    "created_at": "2008-02-04T18:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2036#issuecomment-13173",
    "user": "@williamstein"
}
```

That's a nonstandard definition so we have to work around it.

William



---

archive/issue_comments_013174.json:
```json
{
    "body": "Attachment [maxima-charpoly.patch](tarball://root/attachments/some-uuid/ticket2036/maxima-charpoly.patch) by @jasongrout created at 2008-02-04 21:00:40",
    "created_at": "2008-02-04T21:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2036#issuecomment-13174",
    "user": "@jasongrout"
}
```

Attachment [maxima-charpoly.patch](tarball://root/attachments/some-uuid/ticket2036/maxima-charpoly.patch) by @jasongrout created at 2008-02-04 21:00:40



---

archive/issue_comments_013175.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-07T10:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2036#issuecomment-13175",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_013176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T10:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2036#issuecomment-13176",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013177.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T10:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2036#issuecomment-13177",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
