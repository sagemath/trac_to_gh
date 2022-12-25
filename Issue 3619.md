# Issue 3619: notebook -- record date & time each user logs in

archive/issues_003619.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3619\n\n",
    "created_at": "2008-07-08T23:33:58Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook -- record date & time each user logs in",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3619",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/3619





---

archive/issue_comments_025482.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-07-08T23:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25482",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_025483.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-08T23:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25483",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025484.json:
```json
{
    "body": "I couldn't seem to figure out how to get AdminToplevel to be the toplevel for admins.",
    "created_at": "2008-07-10T13:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25484",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I couldn't seem to figure out how to get AdminToplevel to be the toplevel for admins.



---

archive/issue_comments_025485.json:
```json
{
    "body": "I don't understand what the final comment, about AdminToplevel, is about.\n\nI worry that we will hang on to thousands of login times with this, which could be memory/disk intensive.  Could we agree on the last fifty login times, or the first time ever and then the next 100 or something similar?\n\nAlso, there is no way to view this information.  Why are we keeping it?",
    "created_at": "2008-08-10T23:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25485",
    "user": "https://github.com/ncalexan"
}
```

I don't understand what the final comment, about AdminToplevel, is about.

I worry that we will hang on to thousands of login times with this, which could be memory/disk intensive.  Could we agree on the last fifty login times, or the first time ever and then the next 100 or something similar?

Also, there is no way to view this information.  Why are we keeping it?



---

archive/issue_comments_025486.json:
```json
{
    "body": "Replying to [comment:3 ncalexan]:\n> I don't understand what the final comment, about AdminToplevel, is about.\n\n\nSomehow the user account type for the user admin was getting changed to 'user'. This is no longer a problem because a patch was merged which has account_type returning 'admin' for user admin no matter what.\n\n> I worry that we will hang on to thousands of login times with this, which could be memory/disk intensive.  Could we agree on the last fifty login times, or the first time ever and then the next 100 or something similar?\n> \n\n\nWe could, but I am very interested in being able to look up all login times for a given user. \n\n> Also, there is no way to view this information.  Why are we keeping it?\n\n\nThere will be. I just didn't do it because at the time I couldn't figure out the AdminToplevel problem.\n\nI'll get back to this ticket after thinking more about it. Thanks for reviewing.",
    "created_at": "2008-08-11T04:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25486",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Replying to [comment:3 ncalexan]:
> I don't understand what the final comment, about AdminToplevel, is about.


Somehow the user account type for the user admin was getting changed to 'user'. This is no longer a problem because a patch was merged which has account_type returning 'admin' for user admin no matter what.

> I worry that we will hang on to thousands of login times with this, which could be memory/disk intensive.  Could we agree on the last fifty login times, or the first time ever and then the next 100 or something similar?
> 


We could, but I am very interested in being able to look up all login times for a given user. 

> Also, there is no way to view this information.  Why are we keeping it?


There will be. I just didn't do it because at the time I couldn't figure out the AdminToplevel problem.

I'll get back to this ticket after thinking more about it. Thanks for reviewing.



---

archive/issue_comments_025487.json:
```json
{
    "body": "How I test this:\n\n(1) I login and then go to sage.math.washington.edu:8999/users # Table of users with two links next to each of them if login recording is on. \n\n(2) I click on \"Access\" in third column to see login times. The page should be blank if no login times have been recorded.\n\nLogin recording is turned off by default. In order to turn it on I do:\n\n```\n*** WARNING: Notebook must not be running! ***\n\nsage: nb = load('.sage/sage_notebook/nb.sobj', compress=False)\nsage: nb.conf()['record_logins'] = True\nsage: nb.save(filename='/home/tclemans/.sage/sage_notebook/nb.sobj')\n```",
    "created_at": "2008-08-12T21:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25487",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

How I test this:

(1) I login and then go to sage.math.washington.edu:8999/users # Table of users with two links next to each of them if login recording is on. 

(2) I click on "Access" in third column to see login times. The page should be blank if no login times have been recorded.

Login recording is turned off by default. In order to turn it on I do:

```
*** WARNING: Notebook must not be running! ***

sage: nb = load('.sage/sage_notebook/nb.sobj', compress=False)
sage: nb.conf()['record_logins'] = True
sage: nb.save(filename='/home/tclemans/.sage/sage_notebook/nb.sobj')
```



---

archive/issue_comments_025488.json:
```json
{
    "body": "Depends on #3776",
    "created_at": "2008-08-13T02:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25488",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Depends on #3776



---

archive/issue_comments_025489.json:
```json
{
    "body": "Attachment [sage-3619.patch](tarball://root/attachments/some-uuid/ticket3619/sage-3619.patch) by TimothyClemans created at 2008-08-13 02:28:39",
    "created_at": "2008-08-13T02:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25489",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3619.patch](tarball://root/attachments/some-uuid/ticket3619/sage-3619.patch) by TimothyClemans created at 2008-08-13 02:28:39



---

archive/issue_comments_025490.json:
```json
{
    "body": "Attachment [sagenb-3619.patch](tarball://root/attachments/some-uuid/ticket3619/sagenb-3619.patch) by @williamstein created at 2009-11-19 22:43:29\n\nnew patch against sagenb that simply adds calls to log.msg in a few places, which will properly log user login attempts using the standard twisted loging facility",
    "created_at": "2009-11-19T22:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25490",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb-3619.patch](tarball://root/attachments/some-uuid/ticket3619/sagenb-3619.patch) by @williamstein created at 2009-11-19 22:43:29

new patch against sagenb that simply adds calls to log.msg in a few places, which will properly log user login attempts using the standard twisted loging facility



---

archive/issue_comments_025491.json:
```json
{
    "body": "I've attached a new patch against sagenb that simply adds calls to log.msg in a few places, which will properly log user login attempts using the standard twisted loging facility.  I also deleted some cruft from guard.py that wasn't used.",
    "created_at": "2009-11-19T22:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25491",
    "user": "https://github.com/williamstein"
}
```

I've attached a new patch against sagenb that simply adds calls to log.msg in a few places, which will properly log user login attempts using the standard twisted loging facility.  I also deleted some cruft from guard.py that wasn't used.



---

archive/issue_comments_025492.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-19T22:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25492",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025493.json:
```json
{
    "body": "Applied and the patch works perfectly. I wonder though whether a configuration setting should be added?",
    "created_at": "2009-12-06T11:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25493",
    "user": "https://github.com/TimDumol"
}
```

Applied and the patch works perfectly. I wonder though whether a configuration setting should be added?



---

archive/issue_comments_025494.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-06T11:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25494",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025495.json:
```json
{
    "body": "> Applied and the patch works perfectly. I wonder though whether a \n> configuration setting should be added? \n\n\nYes, definitely.  However, I don't think that has to be done in this patch.  Little steps are best.",
    "created_at": "2009-12-07T17:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25495",
    "user": "https://github.com/williamstein"
}
```

> Applied and the patch works perfectly. I wonder though whether a 
> configuration setting should be added? 


Yes, definitely.  However, I don't think that has to be done in this patch.  Little steps are best.



---

archive/issue_events_008304.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-07T17:38:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3619#event-8304"
}
```



---

archive/issue_comments_025496.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-07T17:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3619#issuecomment-25496",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
