# Issue 5163: jsmath extensions for published webpages

archive/issues_005163.json:
```json
{
    "body": "Assignee: boothby\n\nThe extensions enabled in #5021 don't work for published web pages, I think because js.py isn't loaded.\n\nWe could move the extensions to be invoked right after jsmath is loaded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5163\n\n",
    "created_at": "2009-02-03T04:55:31Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "jsmath extensions for published webpages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5163",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

The extensions enabled in #5021 don't work for published web pages, I think because js.py isn't loaded.

We could move the extensions to be invoked right after jsmath is loaded.

Issue created by migration from https://trac.sagemath.org/ticket/5163





---

archive/issue_comments_039492.json:
```json
{
    "body": "Attachment [trac_5163-jsmath-extensions-published.patch](tarball://root/attachments/some-uuid/ticket5163/trac_5163-jsmath-extensions-published.patch) by @jasongrout created at 2009-02-03 05:10:45",
    "created_at": "2009-02-03T05:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39492",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5163-jsmath-extensions-published.patch](tarball://root/attachments/some-uuid/ticket5163/trac_5163-jsmath-extensions-published.patch) by @jasongrout created at 2009-02-03 05:10:45



---

archive/issue_comments_039493.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-02-03T09:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39493",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_039494.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T09:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39494",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039495.json:
```json
{
    "body": "Looks good to me.  I was wondering if there was a better place to put these extensions when I wrote the patch for #5021...",
    "created_at": "2009-02-04T21:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39495",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  I was wondering if there was a better place to put these extensions when I wrote the patch for #5021...



---

archive/issue_comments_039496.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_events_005413.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-05T10:49:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5163#event-5413"
}
```



---

archive/issue_comments_039497.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T10:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
