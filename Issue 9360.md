# Issue 9360: Sage 4.4.4 numerical noise in mwrank.pyx on 32-bit cicero

archive/issues_009360.json:
```json
{
    "body": "Assignee: jason, jkantor\n\n\n```\nHi folks,\n\nDoctesting Sage 4.4.4 on cicero.skynet, a 32-bit Pentium 4 machine, I\ngot the following numerical noise:\n\nsage -t -long \"devel/sage/sage/libs/mwrank/mwrank.pyx\"\n**********************************************************************\nFile \"/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx\",\nline 340:\n   sage: E.silverman_bound()\nExpected:\n   6.5222617951910102\nGot:\n   6.5222617951910111\n**********************************************************************\nFile \"/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx\",\nline 372:\n   sage: E.silverman_bound()\nExpected:\n   6.5222617951910102\nGot:\n   6.5222617951910111\n\n--\nRegards\nMinh Van Nguyen\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9360\n\n",
    "created_at": "2010-06-28T17:44:54Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Sage 4.4.4 numerical noise in mwrank.pyx on 32-bit cicero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9360",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, jkantor


```
Hi folks,

Doctesting Sage 4.4.4 on cicero.skynet, a 32-bit Pentium 4 machine, I
got the following numerical noise:

sage -t -long "devel/sage/sage/libs/mwrank/mwrank.pyx"
**********************************************************************
File "/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx",
line 340:
   sage: E.silverman_bound()
Expected:
   6.5222617951910102
Got:
   6.5222617951910111
**********************************************************************
File "/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx",
line 372:
   sage: E.silverman_bound()
Expected:
   6.5222617951910102
Got:
   6.5222617951910111

--
Regards
Minh Van Nguyen
```


Issue created by migration from https://trac.sagemath.org/ticket/9360





---

archive/issue_comments_088751.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T17:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88751",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088752.json:
```json
{
    "body": "Attachment [trac_9360.patch](tarball://root/attachments/some-uuid/ticket9360/trac_9360.patch) by @williamstein created at 2010-06-28 17:50:45",
    "created_at": "2010-06-28T17:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88752",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9360.patch](tarball://root/attachments/some-uuid/ticket9360/trac_9360.patch) by @williamstein created at 2010-06-28 17:50:45



---

archive/issue_comments_088753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-28T17:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88753",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088754.json:
```json
{
    "body": "Looks good.\n\nFor the pedants out there, this number is a no-way strict upper bound on something and it makes no sense to worry about the low order bits.",
    "created_at": "2010-06-28T17:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88754",
    "user": "https://github.com/JohnCremona"
}
```

Looks good.

For the pedants out there, this number is a no-way strict upper bound on something and it makes no sense to worry about the low order bits.



---

archive/issue_events_009513.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-06-29T16:16:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9360#event-9513"
}
```



---

archive/issue_comments_088755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88755",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
