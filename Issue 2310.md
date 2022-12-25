# Issue 2310: [with patch; needs review] bug attaching files in files that are attached

archive/issues_002310.json:
```json
{
    "body": "Assignee: cwitty\n\nI found this bug when testing #1964.  To replicate, create a file a.sage and put \n\n```\nattach b.sage\n```\n\nin it.  This fails, but {{{attach \"b.sage\"} works.  This was a problem before this patch, so it is NOT the fault of this patch.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2310\n\n",
    "created_at": "2008-02-26T04:15:27Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch; needs review] bug attaching files in files that are attached",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2310",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

I found this bug when testing #1964.  To replicate, create a file a.sage and put 

```
attach b.sage
```

in it.  This fails, but {{{attach "b.sage"} works.  This was a problem before this patch, so it is NOT the fault of this patch.  

Issue created by migration from https://trac.sagemath.org/ticket/2310





---

archive/issue_comments_015340.json:
```json
{
    "body": "Attachment [sage-2310.patch](tarball://root/attachments/some-uuid/ticket2310/sage-2310.patch) by @williamstein created at 2008-02-26 04:17:06\n\nThis likely depends on #1964.",
    "created_at": "2008-02-26T04:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2310#issuecomment-15340",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2310.patch](tarball://root/attachments/some-uuid/ticket2310/sage-2310.patch) by @williamstein created at 2008-02-26 04:17:06

This likely depends on #1964.



---

archive/issue_comments_015341.json:
```json
{
    "body": "NOTE: This could likely be done better after #1964 is done by using the method split_file_names(line): in interpreter.py?",
    "created_at": "2008-02-26T04:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2310#issuecomment-15341",
    "user": "https://github.com/williamstein"
}
```

NOTE: This could likely be done better after #1964 is done by using the method split_file_names(line): in interpreter.py?



---

archive/issue_comments_015342.json:
```json
{
    "body": "Regarding my comment about split_file_names -- yes it could be done that way, but split_file_names is a VERY complicated function whereas _strip_quotes which is included in this patch is very simple and easy to use/understand. So I'm not convinced by my previous suggestion.",
    "created_at": "2008-02-26T04:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2310#issuecomment-15342",
    "user": "https://github.com/williamstein"
}
```

Regarding my comment about split_file_names -- yes it could be done that way, but split_file_names is a VERY complicated function whereas _strip_quotes which is included in this patch is very simple and easy to use/understand. So I'm not convinced by my previous suggestion.



---

archive/issue_comments_015343.json:
```json
{
    "body": "Works for me in 2.10.3.rc1",
    "created_at": "2008-03-05T00:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2310#issuecomment-15343",
    "user": "https://github.com/mwhansen"
}
```

Works for me in 2.10.3.rc1



---

archive/issue_comments_015344.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T05:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2310#issuecomment-15344",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002487.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-05T05:33:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2310#event-2487"
}
```



---

archive/issue_comments_015345.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T05:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2310#issuecomment-15345",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc2
