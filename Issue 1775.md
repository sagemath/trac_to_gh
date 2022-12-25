# Issue 1775: clicking on 'search worksheets' can log you out.

archive/issues_001775.json:
```json
{
    "body": "Assignee: boothby\n\nI have just succeeded in creating a personal id on my sage server (as opposed to admin).\nWhen I logged in I wondered what 'search worksheets' might do so I clicked on it\nand found I had been logged out! An error message which left me logged in would be\nmuch better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1775\n\n",
    "created_at": "2008-01-14T10:44:00Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "clicking on 'search worksheets' can log you out.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1775",
    "user": "https://trac.sagemath.org/admin/accounts/users/bill.p"
}
```
Assignee: boothby

I have just succeeded in creating a personal id on my sage server (as opposed to admin).
When I logged in I wondered what 'search worksheets' might do so I clicked on it
and found I had been logged out! An error message which left me logged in would be
much better.

Issue created by migration from https://trac.sagemath.org/ticket/1775





---

archive/issue_comments_011211.json:
```json
{
    "body": "I can not replicate this.  You might have been confused about whether or not you were actually logged in or something?  Please give clear step-by-step directions that allow you to replicate tis problem every time.",
    "created_at": "2008-01-14T14:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11211",
    "user": "https://github.com/williamstein"
}
```

I can not replicate this.  You might have been confused about whether or not you were actually logged in or something?  Please give clear step-by-step directions that allow you to replicate tis problem every time.



---

archive/issue_comments_011212.json:
```json
{
    "body": "William, I have just created a new user (charlie) via the 'Create new user' on\nthe login page method. Logged in as Charlie, then clicked on 'Search worksheets'\nand it logged me out:\n-------------------------------------------------------\nLogin failure\nYou have entered an invalid username. Please try again.\n\nValid login names:\nadmin,\ncharlie,\nbill \n-------------------------------------------------------",
    "created_at": "2008-01-14T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11212",
    "user": "https://trac.sagemath.org/admin/accounts/users/bill.p"
}
```

William, I have just created a new user (charlie) via the 'Create new user' on
the login page method. Logged in as Charlie, then clicked on 'Search worksheets'
and it logged me out:
-------------------------------------------------------
Login failure
You have entered an invalid username. Please try again.

Valid login names:
admin,
charlie,
bill 
-------------------------------------------------------



---

archive/issue_comments_011213.json:
```json
{
    "body": "OK, I can definitely replicate this bug now, so we should easily be able to fix it.",
    "created_at": "2008-01-14T15:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11213",
    "user": "https://github.com/williamstein"
}
```

OK, I can definitely replicate this bug now, so we should easily be able to fix it.



---

archive/issue_comments_011214.json:
```json
{
    "body": "I can't reproduce this at https://sage.math.washington.edu:8102",
    "created_at": "2008-08-27T16:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11214",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I can't reproduce this at https://sage.math.washington.edu:8102



---

archive/issue_comments_011215.json:
```json
{
    "body": "I cannot duplicate this in Sage 3.2.3 either.  I'm going to mark it as invalid at this point.",
    "created_at": "2009-01-23T12:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11215",
    "user": "https://github.com/mwhansen"
}
```

I cannot duplicate this in Sage 3.2.3 either.  I'm going to mark it as invalid at this point.



---

archive/issue_events_001932.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-23T12:43:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1775#event-1932"
}
```



---

archive/issue_comments_011216.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-23T12:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11216",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
