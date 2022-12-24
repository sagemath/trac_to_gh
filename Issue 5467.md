# Issue 5467: The sage/macaulay2 interface doesn't work at all on large input

archive/issues_005467.json:
```json
{
    "body": "Assignee: mhansen\n\nON OS X and Linux with Macaulay 1.2.\n\n\n```\nteragon:~ wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: macaulay2(10^10000)\nsage0\nsage: macaulay2(10^10000)\nsage1\nsage: macaulay2(10^10000)\nsage2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5467\n\n",
    "created_at": "2009-03-10T18:03:16Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "The sage/macaulay2 interface doesn't work at all on large input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5467",
    "user": "was"
}
```
Assignee: mhansen

ON OS X and Linux with Macaulay 1.2.


```
teragon:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: macaulay2(10^10000)
sage0
sage: macaulay2(10^10000)
sage1
sage: macaulay2(10^10000)
sage2
```


Issue created by migration from https://trac.sagemath.org/ticket/5467





---

archive/issue_comments_042434.json:
```json
{
    "body": "This is a trivial fix - the problem was in a wrong file loading command passed to Macaulay2.\n\nThe tests in the modified function pass (although optional tests for the whole file give a bunch of unrelated mistakes).",
    "created_at": "2010-01-09T07:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42434",
    "user": "novoselt"
}
```

This is a trivial fix - the problem was in a wrong file loading command passed to Macaulay2.

The tests in the modified function pass (although optional tests for the whole file give a bunch of unrelated mistakes).



---

archive/issue_comments_042435.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T07:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42435",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042436.json:
```json
{
    "body": "Must be applied after the first patch.",
    "created_at": "2010-01-09T20:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42436",
    "user": "novoselt"
}
```

Must be applied after the first patch.



---

archive/issue_comments_042437.json:
```json
{
    "body": "Attachment [5467_long_input_to_Macaulay2_second_part.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2_second_part.patch) by novoselt created at 2010-01-09 20:42:36\n\nI managed to make a trivial mistake in this trivial fix - one of the test lines was not marked with #optional. Now it is.",
    "created_at": "2010-01-09T20:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42437",
    "user": "novoselt"
}
```

Attachment [5467_long_input_to_Macaulay2_second_part.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2_second_part.patch) by novoselt created at 2010-01-09 20:42:36

I managed to make a trivial mistake in this trivial fix - one of the test lines was not marked with #optional. Now it is.



---

archive/issue_comments_042438.json:
```json
{
    "body": "Converged patches into a single one and made the commit message of standard form.",
    "created_at": "2010-01-31T23:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42438",
    "user": "novoselt"
}
```

Converged patches into a single one and made the commit message of standard form.



---

archive/issue_comments_042439.json:
```json
{
    "body": "Only this patch should be applied.",
    "created_at": "2010-01-31T23:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42439",
    "user": "novoselt"
}
```

Only this patch should be applied.



---

archive/issue_comments_042440.json:
```json
{
    "body": "Attachment [5467_long_input_to_Macaulay2.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2.patch) by novoselt created at 2010-02-07 17:02:33",
    "created_at": "2010-02-07T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42440",
    "user": "novoselt"
}
```

Attachment [5467_long_input_to_Macaulay2.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2.patch) by novoselt created at 2010-02-07 17:02:33



---

archive/issue_comments_042441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-09T01:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42441",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042442.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-09T01:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42442",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_042443.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42443",
    "user": "mpatel"
}
```

Resolution: fixed
