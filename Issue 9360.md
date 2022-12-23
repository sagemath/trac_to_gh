# Issue 9360: Sage 4.4.4 numerical noise in mwrank.pyx on 32-bit cicero

archive/issues_009360.json:
```json
{
    "body": "Assignee: jason, jkantor\n\n\n```\nHi folks,\n\nDoctesting Sage 4.4.4 on cicero.skynet, a 32-bit Pentium 4 machine, I\ngot the following numerical noise:\n\nsage -t -long \"devel/sage/sage/libs/mwrank/mwrank.pyx\"\n**********************************************************************\nFile \"/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx\",\nline 340:\n   sage: E.silverman_bound()\nExpected:\n   6.5222617951910102\nGot:\n   6.5222617951910111\n**********************************************************************\nFile \"/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx\",\nline 372:\n   sage: E.silverman_bound()\nExpected:\n   6.5222617951910102\nGot:\n   6.5222617951910111\n\n--\nRegards\nMinh Van Nguyen\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9360\n\n",
    "created_at": "2010-06-28T17:44:54Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "Sage 4.4.4 numerical noise in mwrank.pyx on 32-bit cicero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9360",
    "user": "was"
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

archive/issue_comments_088891.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T17:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88891",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088892.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-28T17:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88892",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_088893.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-28T17:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88893",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088894.json:
```json
{
    "body": "Looks good.\n\nFor the pedants out there, this number is a no-way strict upper bound on something and it makes no sense to worry about the low order bits.",
    "created_at": "2010-06-28T17:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88894",
    "user": "cremona"
}
```

Looks good.

For the pedants out there, this number is a no-way strict upper bound on something and it makes no sense to worry about the low order bits.



---

archive/issue_comments_088895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9360#issuecomment-88895",
    "user": "rlm"
}
```

Resolution: fixed
