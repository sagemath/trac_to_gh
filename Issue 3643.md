# Issue 3643: re-enable dsage/testdoc.py

archive/issues_003643.json:
```json
{
    "body": "Assignee: yi\n\nI disabled dsage/testdoc.py for sage-3.0.5, since that system for doctesting dsage is BROKEN.\nFor example\n\n```\nsage -t  devel/sage/sage/dsage/tests/testdoc.py\n********************************************************************\nFile \"/home/was/build/sage-3.0.4/tmp/testdoc.py\", line 14:\n   sage: a\nExpected:\n   5\nGot:\n   No output.\n```\n\nand this is just a typical timing issue.  We have unit tests after all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3643\n\n",
    "created_at": "2008-07-11T18:41:37Z",
    "labels": [
        "dsage",
        "blocker",
        "bug"
    ],
    "title": "re-enable dsage/testdoc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3643",
    "user": "was"
}
```
Assignee: yi

I disabled dsage/testdoc.py for sage-3.0.5, since that system for doctesting dsage is BROKEN.
For example

```
sage -t  devel/sage/sage/dsage/tests/testdoc.py
********************************************************************
File "/home/was/build/sage-3.0.4/tmp/testdoc.py", line 14:
   sage: a
Expected:
   5
Got:
   No output.
```

and this is just a typical timing issue.  We have unit tests after all.

Issue created by migration from https://trac.sagemath.org/ticket/3643





---

archive/issue_comments_025755.json:
```json
{
    "body": "This is fine. I am working hard to fix this in ticket #3600.",
    "created_at": "2008-07-11T19:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25755",
    "user": "yi"
}
```

This is fine. I am working hard to fix this in ticket #3600.



---

archive/issue_comments_025756.json:
```json
{
    "body": "Attachment [trac_3643.patch](tarball://root/attachments/some-uuid/ticket3643/trac_3643.patch) by gfurnish created at 2008-12-09 18:43:35\n\nThis seems to work correctly with #4745 applied, so after discussion with mabshoff perhaps we should reenable the doctest after #4745 to see if we can get it to fail again.",
    "created_at": "2008-12-09T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25756",
    "user": "gfurnish"
}
```

Attachment [trac_3643.patch](tarball://root/attachments/some-uuid/ticket3643/trac_3643.patch) by gfurnish created at 2008-12-09 18:43:35

This seems to work correctly with #4745 applied, so after discussion with mabshoff perhaps we should reenable the doctest after #4745 to see if we can get it to fail again.



---

archive/issue_comments_025757.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-09T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25757",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025758.json:
```json
{
    "body": "Changing assignee from yi to gfurnish.",
    "created_at": "2008-12-09T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25758",
    "user": "gfurnish"
}
```

Changing assignee from yi to gfurnish.



---

archive/issue_comments_025759.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T15:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25759",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_025760.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25760",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_comments_025761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25761",
    "user": "mabshoff"
}
```

Resolution: fixed
