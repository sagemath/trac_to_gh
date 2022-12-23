# Issue 1775: clicking on 'search worksheets' can log you out.

archive/issues_001775.json:
```json
{
    "body": "Assignee: boothby\n\nI have just succeeded in creating a personal id on my sage server (as opposed to admin).\nWhen I logged in I wondered what 'search worksheets' might do so I clicked on it\nand found I had been logged out! An error message which left me logged in would be\nmuch better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1775\n\n",
    "created_at": "2008-01-14T10:44:00Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "clicking on 'search worksheets' can log you out.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1775",
    "user": "bill.p"
}
```
Assignee: boothby

I have just succeeded in creating a personal id on my sage server (as opposed to admin).
When I logged in I wondered what 'search worksheets' might do so I clicked on it
and found I had been logged out! An error message which left me logged in would be
much better.

Issue created by migration from https://trac.sagemath.org/ticket/1775





---

archive/issue_comments_011238.json:
```json
{
    "body": "I can not replicate this.  You might have been confused about whether or not you were actually logged in or something?  Please give clear step-by-step directions that allow you to replicate tis problem every time.",
    "created_at": "2008-01-14T14:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11238",
    "user": "was"
}
```

I can not replicate this.  You might have been confused about whether or not you were actually logged in or something?  Please give clear step-by-step directions that allow you to replicate tis problem every time.



---

archive/issue_comments_011239.json:
```json
{
    "body": "William, I have just created a new user (charlie) via the 'Create new user' on\nthe login page method. Logged in as Charlie, then clicked on 'Search worksheets'\nand it logged me out:\n-------------------------------------------------------\nLogin failure\nYou have entered an invalid username. Please try again.\n\nValid login names:\nadmin,\ncharlie,\nbill \n-------------------------------------------------------",
    "created_at": "2008-01-14T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11239",
    "user": "bill.p"
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

archive/issue_comments_011240.json:
```json
{
    "body": "OK, I can definitely replicate this bug now, so we should easily be able to fix it.",
    "created_at": "2008-01-14T15:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11240",
    "user": "was"
}
```

OK, I can definitely replicate this bug now, so we should easily be able to fix it.



---

archive/issue_comments_011241.json:
```json
{
    "body": "I can't reproduce this at https://sage.math.washington.edu:8102",
    "created_at": "2008-08-27T16:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11241",
    "user": "TimothyClemans"
}
```

I can't reproduce this at https://sage.math.washington.edu:8102



---

archive/issue_comments_011242.json:
```json
{
    "body": "I cannot duplicate this in Sage 3.2.3 either.  I'm going to mark it as invalid at this point.",
    "created_at": "2009-01-23T12:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11242",
    "user": "mhansen"
}
```

I cannot duplicate this in Sage 3.2.3 either.  I'm going to mark it as invalid at this point.



---

archive/issue_comments_011243.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-23T12:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1775#issuecomment-11243",
    "user": "mhansen"
}
```

Resolution: invalid
