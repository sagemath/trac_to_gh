# Issue 6489: [with patch, work in progress ...] Allow Sage to call R (statistics)

archive/issues_006489.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: statistics, R,\n\nHere we have the start of a \"bridge\" between Sage and R.\n\nThe R c language api is used to call R functions from Python.\n\nThis code mostly handles converting between Sage (Python) and R types.\n\nThe way it works is Python calls the callTypedArgs function defined in this module, passing in the name of the R function to call, a string specifying types of the parameters the function expects and what the function returns, then a list of Python Objects (such Sage integers, or vectors or matrices) for the parameters. R_bridge then creates the equivalent simple expressions in R for the passed Python objects, calls the given function in R, and then converts back from the returned R simple expression to a Python Object.\n\nThe way to expose R's functionality nicely in Sage using this is then to create a Sage file (like statistics.py) that uses R_bridge to call R functions. This file would wrap up the ugly parameter and return type specifier string.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6489\n\n",
    "created_at": "2009-07-08T20:27:49Z",
    "labels": [
        "component: statistics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, work in progress ...] Allow Sage to call R (statistics)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6489",
    "user": "https://trac.sagemath.org/admin/accounts/users/sjanke"
}
```
Assignee: mhampton

Keywords: statistics, R,

Here we have the start of a "bridge" between Sage and R.

The R c language api is used to call R functions from Python.

This code mostly handles converting between Sage (Python) and R types.

The way it works is Python calls the callTypedArgs function defined in this module, passing in the name of the R function to call, a string specifying types of the parameters the function expects and what the function returns, then a list of Python Objects (such Sage integers, or vectors or matrices) for the parameters. R_bridge then creates the equivalent simple expressions in R for the passed Python objects, calls the given function in R, and then converts back from the returned R simple expression to a Python Object.

The way to expose R's functionality nicely in Sage using this is then to create a Sage file (like statistics.py) that uses R_bridge to call R functions. This file would wrap up the ugly parameter and return type specifier string.

Issue created by migration from https://trac.sagemath.org/ticket/6489





---

archive/issue_comments_052370.json:
```json
{
    "body": "Attachment [R_bridge.c](tarball://root/attachments/some-uuid/ticket6489/R_bridge.c) by sjanke created at 2009-07-08 20:28:27",
    "created_at": "2009-07-08T20:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6489#issuecomment-52370",
    "user": "https://trac.sagemath.org/admin/accounts/users/sjanke"
}
```

Attachment [R_bridge.c](tarball://root/attachments/some-uuid/ticket6489/R_bridge.c) by sjanke created at 2009-07-08 20:28:27



---

archive/issue_comments_052371.json:
```json
{
    "body": "Attachment [statistics.py](tarball://root/attachments/some-uuid/ticket6489/statistics.py) by sjanke created at 2009-07-08 20:33:33",
    "created_at": "2009-07-08T20:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6489#issuecomment-52371",
    "user": "https://trac.sagemath.org/admin/accounts/users/sjanke"
}
```

Attachment [statistics.py](tarball://root/attachments/some-uuid/ticket6489/statistics.py) by sjanke created at 2009-07-08 20:33:33



---

archive/issue_comments_052372.json:
```json
{
    "body": "Attachment [callTypedArgs_spec](tarball://root/attachments/some-uuid/ticket6489/callTypedArgs_spec) by sjanke created at 2009-07-08 20:36:00",
    "created_at": "2009-07-08T20:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6489#issuecomment-52372",
    "user": "https://trac.sagemath.org/admin/accounts/users/sjanke"
}
```

Attachment [callTypedArgs_spec](tarball://root/attachments/some-uuid/ticket6489/callTypedArgs_spec) by sjanke created at 2009-07-08 20:36:00



---

archive/issue_comments_052373.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-07-08T20:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6489#issuecomment-52373",
    "user": "https://trac.sagemath.org/admin/accounts/users/sjanke"
}
```

Changing priority from major to minor.



---

archive/issue_events_006725.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-23T15:01:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6489#event-6725"
}
```



---

archive/issue_comments_052374.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T15:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6489#issuecomment-52374",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_052375.json:
```json
{
    "body": "I think duplicating the work in rpy (which is quite effective) isn't a good plan.",
    "created_at": "2013-07-23T15:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6489#issuecomment-52375",
    "user": "https://github.com/mwhansen"
}
```

I think duplicating the work in rpy (which is quite effective) isn't a good plan.
