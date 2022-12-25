# Issue 2039: [with patch, positve review] add sage version const

archive/issues_002039.json:
```json
{
    "body": "Assignee: cwitty\n\nHow does one determine the SAGE version? I can't find any information on this, so I propose that SAGE_VERSION (hex) and SAGE_VERSION_STR constants be added giving current running version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2039\n\n",
    "closed_at": "2008-10-31T23:26:48Z",
    "created_at": "2008-02-03T20:16:32Z",
    "labels": [
        "component: misc",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positve review] add sage version const",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2039",
    "user": "https://trac.sagemath.org/admin/accounts/users/benjamin.peterson"
}
```
Assignee: cwitty

How does one determine the SAGE version? I can't find any information on this, so I propose that SAGE_VERSION (hex) and SAGE_VERSION_STR constants be added giving current running version.

Issue created by migration from https://trac.sagemath.org/ticket/2039





---

archive/issue_comments_013168.json:
```json
{
    "body": "Do you mean from a running Sage?  Just use the version command. \n\n```\nteragon:~ was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.1, Release Date: 2008-02-02                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: version()\n'SAGE Version 2.10.1, Release Date: 2008-02-02'\n```",
    "created_at": "2008-02-03T20:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13168",
    "user": "https://github.com/williamstein"
}
```

Do you mean from a running Sage?  Just use the version command. 

```
teragon:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: version()
'SAGE Version 2.10.1, Release Date: 2008-02-02'
```



---

archive/issue_comments_013169.json:
```json
{
    "body": "I was thinking from a SAGE program.",
    "created_at": "2008-02-03T20:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13169",
    "user": "https://trac.sagemath.org/admin/accounts/users/benjamin.peterson"
}
```

I was thinking from a SAGE program.



---

archive/issue_comments_013170.json:
```json
{
    "body": "If you wanted to compare versions, then you'd have to parse out the version for the string. Correct?",
    "created_at": "2008-02-03T20:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13170",
    "user": "https://trac.sagemath.org/admin/accounts/users/benjamin.peterson"
}
```

If you wanted to compare versions, then you'd have to parse out the version for the string. Correct?



---

archive/issue_comments_013171.json:
```json
{
    "body": "I think a function, maybe a variety of version(), should return some tuple with [major, minor, tiny]. We should also offer some functions, say something like require_version(X,Y,Z), that would return false for any sage release before X.Y.Z and print a helpful error message, i.e. \n\n```\nThe code needs at least Sage version X.Y.Z to work correctly. You are \nrunning Sage version K.P.L. To upgrade yada, yada, yada ...\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-02-04T04:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think a function, maybe a variety of version(), should return some tuple with [major, minor, tiny]. We should also offer some functions, say something like require_version(X,Y,Z), that would return false for any sage release before X.Y.Z and print a helpful error message, i.e. 

```
The code needs at least Sage version X.Y.Z to work correctly. You are 
running Sage version K.P.L. To upgrade yada, yada, yada ...
```

Cheers,

Michael



---

archive/issue_events_004898.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-04T04:57:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2039#event-4898"
}
```



---

archive/issue_comments_013172.json:
```json
{
    "body": "That's a great idea. require_version is just what I need.",
    "created_at": "2008-02-04T17:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13172",
    "user": "https://trac.sagemath.org/admin/accounts/users/benjamin.peterson"
}
```

That's a great idea. require_version is just what I need.



---

archive/issue_comments_013173.json:
```json
{
    "body": "Here's a patch, which also provides 100% coverage for the file banner.py.  The patch introduces functions `version_dict` and `require_version`.  I don't know if this is the sort of thing people had in mind...\n\n  John",
    "created_at": "2008-10-31T19:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13173",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch, which also provides 100% coverage for the file banner.py.  The patch introduces functions `version_dict` and `require_version`.  I don't know if this is the sort of thing people had in mind...

  John



---

archive/issue_comments_013174.json:
```json
{
    "body": "Attachment [version.patch](tarball://root/attachments/some-uuid/ticket2039/version.patch) by mabshoff created at 2008-10-31 23:24:40\n\nPositive review. Nice work, I am considering importing version_dict() and require_version() into the global namespace, but we can do that via another ticket if there is demand.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T23:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [version.patch](tarball://root/attachments/some-uuid/ticket2039/version.patch) by mabshoff created at 2008-10-31 23:24:40

Positive review. Nice work, I am considering importing version_dict() and require_version() into the global namespace, but we can do that via another ticket if there is demand.

Cheers,

Michael



---

archive/issue_events_004899.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T23:24:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2039#event-4899"
}
```



---

archive/issue_events_004900.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T23:24:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2039#event-4900"
}
```



---

archive/issue_events_004901.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T23:26:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2039#event-4901"
}
```



---

archive/issue_comments_013175.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T23:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_013176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T23:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013177.json:
```json
{
    "body": "Oh yeah, I forgot: Should we expose some of the functions into the global namespace we should also add the banner.py to list of files where documentation is automatically extracted from.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T23:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oh yeah, I forgot: Should we expose some of the functions into the global namespace we should also add the banner.py to list of files where documentation is automatically extracted from.

Cheers,

Michael
