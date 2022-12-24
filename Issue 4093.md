# Issue 4093: [with patch, needs review] fix numerical fuzz in period_lattice for 3.1.2

archive/issues_004093.json:
```json
{
    "body": "Assignee: cremona\n\nKeywords: elliptic curve period lattice\n\n3.1.2.rc1 has this doctest failure:\n\n```\nFile \"/home/john/sage-3.1.2.rc1/tmp/period_lattice.py\", line 281:\n    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))\nExpected:\n    2.609121635701083769 - 0.20086508082458695134*I\nGot:\n    2.609121635701083769 - 0.20086508082458695200*I\n```\n\n\nThe patch fixes this by replacin the last 3 digits above by \"...\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4093\n\n",
    "created_at": "2008-09-09T19:28:19Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] fix numerical fuzz in period_lattice for 3.1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4093",
    "user": "cremona"
}
```
Assignee: cremona

Keywords: elliptic curve period lattice

3.1.2.rc1 has this doctest failure:

```
File "/home/john/sage-3.1.2.rc1/tmp/period_lattice.py", line 281:
    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))
Expected:
    2.609121635701083769 - 0.20086508082458695134*I
Got:
    2.609121635701083769 - 0.20086508082458695200*I
```


The patch fixes this by replacin the last 3 digits above by "...".


Issue created by migration from https://trac.sagemath.org/ticket/4093





---

archive/issue_comments_029529.json:
```json
{
    "body": "Attachment [10515.patch](tarball://root/attachments/some-uuid/ticket4093/10515.patch) by cremona created at 2008-09-09 19:28:32",
    "created_at": "2008-09-09T19:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29529",
    "user": "cremona"
}
```

Attachment [10515.patch](tarball://root/attachments/some-uuid/ticket4093/10515.patch) by cremona created at 2008-09-09 19:28:32



---

archive/issue_comments_029530.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29530",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_029531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-10T01:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29531",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029532.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-10T01:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29532",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc2
