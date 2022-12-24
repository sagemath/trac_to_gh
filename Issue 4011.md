# Issue 4011: notebook -- copying a worksheet on worksheet listings page results in the new worksheet being listed as running

archive/issues_004011.json:
```json
{
    "body": "Assignee: boothby\n\nWhy is the new worksheet, copy of another worksheet, running? It hasn't been accessed by the user.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4011\n\n",
    "created_at": "2008-08-31T01:08:02Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- copying a worksheet on worksheet listings page results in the new worksheet being listed as running",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4011",
    "user": "TimothyClemans"
}
```
Assignee: boothby

Why is the new worksheet, copy of another worksheet, running? It hasn't been accessed by the user.

Issue created by migration from https://trac.sagemath.org/ticket/4011





---

archive/issue_comments_028944.json:
```json
{
    "body": "Please delete sage-4011_1.patch.\n\nPatch sage-4011_1.patch doesn't seem to resolve the problem.",
    "created_at": "2008-09-09T16:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28944",
    "user": "TimothyClemans"
}
```

Please delete sage-4011_1.patch.

Patch sage-4011_1.patch doesn't seem to resolve the problem.



---

archive/issue_comments_028945.json:
```json
{
    "body": "Attachment [trac_4011.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.patch) by mhansen created at 2009-01-24 06:20:35",
    "created_at": "2009-01-24T06:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28945",
    "user": "mhansen"
}
```

Attachment [trac_4011.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.patch) by mhansen created at 2009-01-24 06:20:35



---

archive/issue_comments_028946.json:
```json
{
    "body": "I've added a test to my Selenium test suite for this since it requires the Javascript to run.",
    "created_at": "2009-01-24T06:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28946",
    "user": "mhansen"
}
```

I've added a test to my Selenium test suite for this since it requires the Javascript to run.



---

archive/issue_comments_028947.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T06:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28947",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028948.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-01-24T06:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28948",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_028949.json:
```json
{
    "body": "This might be really nitpicky, but can we make the code not have a double negative?  I.e., `if no_load is in ctx`, rather than `if no_load not in ctx`.  Having a double negative makes the code a bit more confusing.",
    "created_at": "2009-02-07T17:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28949",
    "user": "jason"
}
```

This might be really nitpicky, but can we make the code not have a double negative?  I.e., `if no_load is in ctx`, rather than `if no_load not in ctx`.  Having a double negative makes the code a bit more confusing.



---

archive/issue_comments_028950.json:
```json
{
    "body": "And if you're modifying the patch anyway, you might fix the typo in the docs in js.py for this function: worsheet -> worksheet.",
    "created_at": "2009-02-07T17:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28950",
    "user": "jason"
}
```

And if you're modifying the patch anyway, you might fix the typo in the docs in js.py for this function: worsheet -> worksheet.



---

archive/issue_comments_028951.json:
```json
{
    "body": "Attachment [trac_4135.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4135.2.patch) by TimothyClemans created at 2009-03-16 19:58:10",
    "created_at": "2009-03-16T19:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28951",
    "user": "TimothyClemans"
}
```

Attachment [trac_4135.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4135.2.patch) by TimothyClemans created at 2009-03-16 19:58:10



---

archive/issue_comments_028952.json:
```json
{
    "body": "Attachment [trac_4011.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.2.patch) by TimothyClemans created at 2009-03-16 19:59:22\n\nApply trac_4011.2.patch",
    "created_at": "2009-03-16T19:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28952",
    "user": "TimothyClemans"
}
```

Attachment [trac_4011.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.2.patch) by TimothyClemans created at 2009-03-16 19:59:22

Apply trac_4011.2.patch



---

archive/issue_comments_028953.json:
```json
{
    "body": "Merged trac_4011.2.patch in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-24T23:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28953",
    "user": "mabshoff"
}
```

Merged trac_4011.2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_028954.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-24T23:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28954",
    "user": "mabshoff"
}
```

Resolution: fixed
