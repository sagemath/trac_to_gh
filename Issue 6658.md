# Issue 6658: digits() claims it defaults to base 2, but it defaults to base 10

archive/issues_006658.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: x = 1729\nsage: x.digits()\n[9, 2, 7, 1]\n```\n\nbut the docstring for `digits()` claims it defaults to base 2. The attached patch fixes this; thanks to Yasuhide NUMATA at the *-combinat meeting for noticing this. I would have shown him how to make a patch and upload it to trac, but their wireless network was down at the time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6658\n\n",
    "created_at": "2009-07-30T03:03:24Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "digits() claims it defaults to base 2, but it defaults to base 10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6658",
    "user": "@dandrake"
}
```
Assignee: somebody


```
sage: x = 1729
sage: x.digits()
[9, 2, 7, 1]
```

but the docstring for `digits()` claims it defaults to base 2. The attached patch fixes this; thanks to Yasuhide NUMATA at the *-combinat meeting for noticing this. I would have shown him how to make a patch and upload it to trac, but their wireless network was down at the time.

Issue created by migration from https://trac.sagemath.org/ticket/6658





---

archive/issue_comments_054657.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-30T03:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6658#issuecomment-54657",
    "user": "@dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054658.json:
```json
{
    "body": "Changing assignee from somebody to @dandrake.",
    "created_at": "2009-07-30T03:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6658#issuecomment-54658",
    "user": "@dandrake"
}
```

Changing assignee from somebody to @dandrake.



---

archive/issue_comments_054659.json:
```json
{
    "body": "Attachment [trac_6658_integer_digits.patch](tarball://root/attachments/some-uuid/ticket6658/trac_6658_integer_digits.patch) by @dandrake created at 2009-07-30 03:34:12\n\nI also edited a bit of the docstring.",
    "created_at": "2009-07-30T03:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6658#issuecomment-54659",
    "user": "@dandrake"
}
```

Attachment [trac_6658_integer_digits.patch](tarball://root/attachments/some-uuid/ticket6658/trac_6658_integer_digits.patch) by @dandrake created at 2009-07-30 03:34:12

I also edited a bit of the docstring.



---

archive/issue_comments_054660.json:
```json
{
    "body": "Changing component from basic arithmetic to documentation.",
    "created_at": "2009-07-30T03:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6658#issuecomment-54660",
    "user": "@dandrake"
}
```

Changing component from basic arithmetic to documentation.



---

archive/issue_comments_054661.json:
```json
{
    "body": "Applied the patch on r12658. Doctest passed, seems ok.",
    "created_at": "2009-07-30T12:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6658#issuecomment-54661",
    "user": "@TimDumol"
}
```

Applied the patch on r12658. Doctest passed, seems ok.



---

archive/issue_comments_054662.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T06:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6658#issuecomment-54662",
    "user": "mvngu"
}
```

Resolution: fixed
