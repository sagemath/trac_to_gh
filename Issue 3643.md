# Issue 3643: re-enable dsage/testdoc.py

archive/issues_003643.json:
```json
{
    "body": "Assignee: @yqiang\n\nI disabled dsage/testdoc.py for sage-3.0.5, since that system for doctesting dsage is BROKEN.\nFor example\n\n```\nsage -t  devel/sage/sage/dsage/tests/testdoc.py\n********************************************************************\nFile \"/home/was/build/sage-3.0.4/tmp/testdoc.py\", line 14:\n   sage: a\nExpected:\n   5\nGot:\n   No output.\n```\n\nand this is just a typical timing issue.  We have unit tests after all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3643\n\n",
    "created_at": "2008-07-11T18:41:37Z",
    "labels": [
        "component: dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "re-enable dsage/testdoc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3643",
    "user": "https://github.com/williamstein"
}
```
Assignee: @yqiang

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

archive/issue_comments_025702.json:
```json
{
    "body": "This is fine. I am working hard to fix this in ticket #3600.",
    "created_at": "2008-07-11T19:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25702",
    "user": "https://github.com/yqiang"
}
```

This is fine. I am working hard to fix this in ticket #3600.



---

archive/issue_comments_025703.json:
```json
{
    "body": "Attachment [trac_3643.patch](tarball://root/attachments/some-uuid/ticket3643/trac_3643.patch) by @garyfurnish created at 2008-12-09 18:43:35\n\nThis seems to work correctly with #4745 applied, so after discussion with mabshoff perhaps we should reenable the doctest after #4745 to see if we can get it to fail again.",
    "created_at": "2008-12-09T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25703",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3643.patch](tarball://root/attachments/some-uuid/ticket3643/trac_3643.patch) by @garyfurnish created at 2008-12-09 18:43:35

This seems to work correctly with #4745 applied, so after discussion with mabshoff perhaps we should reenable the doctest after #4745 to see if we can get it to fail again.



---

archive/issue_comments_025704.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-09T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25704",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025705.json:
```json
{
    "body": "Changing assignee from @yqiang to @garyfurnish.",
    "created_at": "2008-12-09T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25705",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @yqiang to @garyfurnish.



---

archive/issue_comments_025706.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T15:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_025707.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_events_008356.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-11T15:27:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3643#event-8356"
}
```



---

archive/issue_comments_025708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3643#issuecomment-25708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
