# Issue 2039: add sage version const

archive/issues_002039.json:
```json
{
    "body": "Assignee: cwitty\n\nHow does one determine the SAGE version? I can't find any information on this, so I propose that SAGE_VERSION (hex) and SAGE_VERSION_STR constants be added giving current running version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2039\n\n",
    "created_at": "2008-02-03T20:16:32Z",
    "labels": [
        "misc",
        "trivial",
        "enhancement"
    ],
    "title": "add sage version const",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2039",
    "user": "benjamin.peterson"
}
```
Assignee: cwitty

How does one determine the SAGE version? I can't find any information on this, so I propose that SAGE_VERSION (hex) and SAGE_VERSION_STR constants be added giving current running version.

Issue created by migration from https://trac.sagemath.org/ticket/2039





---

archive/issue_comments_013199.json:
```json
{
    "body": "Do you mean from a running Sage?  Just use the version command. \n\n\n```\nteragon:~ was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.1, Release Date: 2008-02-02                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: version()\n'SAGE Version 2.10.1, Release Date: 2008-02-02'\n```\n",
    "created_at": "2008-02-03T20:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13199",
    "user": "was"
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

archive/issue_comments_013200.json:
```json
{
    "body": "I was thinking from a SAGE program.",
    "created_at": "2008-02-03T20:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13200",
    "user": "benjamin.peterson"
}
```

I was thinking from a SAGE program.



---

archive/issue_comments_013201.json:
```json
{
    "body": "If you wanted to compare versions, then you'd have to parse out the version for the string. Correct?",
    "created_at": "2008-02-03T20:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13201",
    "user": "benjamin.peterson"
}
```

If you wanted to compare versions, then you'd have to parse out the version for the string. Correct?



---

archive/issue_comments_013202.json:
```json
{
    "body": "I think a function, maybe a variety of version(), should return some tuple with [major, minor, tiny]. We should also offer some functions, say something like require_version(X,Y,Z), that would return false for any sage release before X.Y.Z and print a helpful error message, i.e. \n\n\n```\nThe code needs at least Sage version X.Y.Z to work correctly. You are \nrunning Sage version K.P.L. To upgrade yada, yada, yada ...\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-04T04:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13202",
    "user": "mabshoff"
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

archive/issue_comments_013203.json:
```json
{
    "body": "That's a great idea. require_version is just what I need.",
    "created_at": "2008-02-04T17:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13203",
    "user": "benjamin.peterson"
}
```

That's a great idea. require_version is just what I need.



---

archive/issue_comments_013204.json:
```json
{
    "body": "Here's a patch, which also provides 100% coverage for the file banner.py.  The patch introduces functions `version_dict` and `require_version`.  I don't know if this is the sort of thing people had in mind...\n\n  John",
    "created_at": "2008-10-31T19:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13204",
    "user": "jhpalmieri"
}
```

Here's a patch, which also provides 100% coverage for the file banner.py.  The patch introduces functions `version_dict` and `require_version`.  I don't know if this is the sort of thing people had in mind...

  John



---

archive/issue_comments_013205.json:
```json
{
    "body": "Attachment [version.patch](tarball://root/attachments/some-uuid/ticket2039/version.patch) by mabshoff created at 2008-10-31 23:24:40\n\nPositive review. Nice work, I am considering importing version_dict() and require_version() into the global namespace, but we can do that via another ticket if there is demand.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T23:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13205",
    "user": "mabshoff"
}
```

Attachment [version.patch](tarball://root/attachments/some-uuid/ticket2039/version.patch) by mabshoff created at 2008-10-31 23:24:40

Positive review. Nice work, I am considering importing version_dict() and require_version() into the global namespace, but we can do that via another ticket if there is demand.

Cheers,

Michael



---

archive/issue_comments_013206.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T23:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13206",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_013207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T23:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13207",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013208.json:
```json
{
    "body": "Oh yeah, I forgot: Should we expose some of the functions into the global namespace we should also add the banner.py to list of files where documentation is automatically extracted from.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T23:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2039#issuecomment-13208",
    "user": "mabshoff"
}
```

Oh yeah, I forgot: Should we expose some of the functions into the global namespace we should also add the banner.py to list of files where documentation is automatically extracted from.

Cheers,

Michael
