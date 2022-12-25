# Issue 987: integrate(1/sqrt(9+x^2)) fails

archive/issues_000987.json:
```json
{
    "body": "Assignee: @mwhansen\n\nintegrate(1/sqrt(9+x^2))\nx/3\n\nI tried this at home and numerous times on sagenb.org.  Every other\nplausible syntax of this integral I tried (-1 power, more parentheses,\nswitch the summands, etc.) yields the same result\n\nHere's the reason\n\n```\n(%i1) integrate(1/sqrt(9+x^2),x)\n;\n                                         x\n(%o1)                              asinh(-)\n                                         3\n\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/987\n\n",
    "created_at": "2007-10-25T01:03:00Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "integrate(1/sqrt(9+x^2)) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/987",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

integrate(1/sqrt(9+x^2))
x/3

I tried this at home and numerous times on sagenb.org.  Every other
plausible syntax of this integral I tried (-1 power, more parentheses,
switch the summands, etc.) yields the same result

Here's the reason

```
(%i1) integrate(1/sqrt(9+x^2),x)
;
                                         x
(%o1)                              asinh(-)
                                         3


```

Issue created by migration from https://trac.sagemath.org/ticket/987





---

archive/issue_events_002727.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-25T01:16:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/987#event-2727"
}
```



---

archive/issue_comments_006009.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-10-25T01:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6009",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_006010.json:
```json
{
    "body": "fixes this problem.",
    "created_at": "2007-10-25T01:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6010",
    "user": "https://github.com/williamstein"
}
```

fixes this problem.



---

archive/issue_comments_006011.json:
```json
{
    "body": "Attachment [987.patch](tarball://root/attachments/some-uuid/ticket987/987.patch) by @williamstein created at 2007-10-25 01:49:34",
    "created_at": "2007-10-25T01:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6011",
    "user": "https://github.com/williamstein"
}
```

Attachment [987.patch](tarball://root/attachments/some-uuid/ticket987/987.patch) by @williamstein created at 2007-10-25 01:49:34



---

archive/issue_comments_006012.json:
```json
{
    "body": "Attachment [987b.patch](tarball://root/attachments/some-uuid/ticket987/987b.patch) by @williamstein created at 2007-10-25 02:34:53",
    "created_at": "2007-10-25T02:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6012",
    "user": "https://github.com/williamstein"
}
```

Attachment [987b.patch](tarball://root/attachments/some-uuid/ticket987/987b.patch) by @williamstein created at 2007-10-25 02:34:53



---

archive/issue_comments_006013.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-25T06:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6013",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002728.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-25T06:44:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/987#event-2728"
}
```
