# Issue 604: Number field element memory leak

archive/issues_000604.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe NTL structures in the number field are leaking.\n\nThe attached patch fixes this and some other matters with multiplication and division -- actually making them use NTL.\n\nIssue created by migration from https://trac.sagemath.org/ticket/604\n\n",
    "created_at": "2007-09-06T21:44:29Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Number field element memory leak",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/604",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

The NTL structures in the number field are leaking.

The attached patch fixes this and some other matters with multiplication and division -- actually making them use NTL.

Issue created by migration from https://trac.sagemath.org/ticket/604





---

archive/issue_comments_003098.json:
```json
{
    "body": "Attachment [number_field_element_2007_09_06.hg](tarball://root/attachments/some-uuid/ticket604/number_field_element_2007_09_06.hg) by jbmohler created at 2007-09-06 21:45:06",
    "created_at": "2007-09-06T21:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/604#issuecomment-3098",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [number_field_element_2007_09_06.hg](tarball://root/attachments/some-uuid/ticket604/number_field_element_2007_09_06.hg) by jbmohler created at 2007-09-06 21:45:06



---

archive/issue_comments_003099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/604#issuecomment-3099",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000661.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T04:43:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/604",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/604#event-661"
}
```
