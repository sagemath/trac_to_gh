# Issue 3213: notebook -- Account Settings page for changing password and e-mail address

archive/issues_003213.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3213\n\n",
    "created_at": "2008-05-16T00:22:37Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- Account Settings page for changing password and e-mail address",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3213",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/3213





---

archive/issue_comments_022189.json:
```json
{
    "body": "I used sage-3.0.1 and applied http://sage.math.washington.edu/home/was/patches/bugday12.hg",
    "created_at": "2008-05-16T00:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3213#issuecomment-22189",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I used sage-3.0.1 and applied http://sage.math.washington.edu/home/was/patches/bugday12.hg



---

archive/issue_comments_022190.json:
```json
{
    "body": "Attachment [3213.patch](tarball://root/attachments/some-uuid/ticket3213/3213.patch) by TimothyClemans created at 2008-05-16 01:32:51",
    "created_at": "2008-05-16T01:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3213#issuecomment-22190",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [3213.patch](tarball://root/attachments/some-uuid/ticket3213/3213.patch) by TimothyClemans created at 2008-05-16 01:32:51



---

archive/issue_comments_022191.json:
```json
{
    "body": "REVIEW:\n\n  I think the code looks fine and this should be applied.\n\nI think the settings panel itself has a lot of work until it is the ultimate\nsettings panel, etc.  But this is a very good start, and additional work\nshould simply go in another patch.  Some comments for future work:\n\n* Instead of \"Cancel\" being the only way to leave the settings page, how about a \"Save\" button that saves all changes, and a \"cancel\" button that throws away all changes?\n* Currently changes are still saved even if you click cancel.\n* Make the thing a little more stylish. \n\nPlease do these as a separate ticket from this ticket, since I want #3213 to get\nin as is. \n\nThis patch I think depends on Tim's other patch for \"changing the password\".\n\n -- William",
    "created_at": "2008-05-16T05:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3213#issuecomment-22191",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

  I think the code looks fine and this should be applied.

I think the settings panel itself has a lot of work until it is the ultimate
settings panel, etc.  But this is a very good start, and additional work
should simply go in another patch.  Some comments for future work:

* Instead of "Cancel" being the only way to leave the settings page, how about a "Save" button that saves all changes, and a "cancel" button that throws away all changes?
* Currently changes are still saved even if you click cancel.
* Make the thing a little more stylish. 

Please do these as a separate ticket from this ticket, since I want #3213 to get
in as is. 

This patch I think depends on Tim's other patch for "changing the password".

 -- William



---

archive/issue_comments_022192.json:
```json
{
    "body": "Follow up ticket with patch needing review is #3228.",
    "created_at": "2008-05-16T20:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3213#issuecomment-22192",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Follow up ticket with patch needing review is #3228.



---

archive/issue_comments_022193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T20:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3213#issuecomment-22193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003430.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-17T20:25:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3213#event-3430"
}
```



---

archive/issue_comments_022194.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T20:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3213#issuecomment-22194",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
