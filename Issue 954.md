# Issue 954: [with script] Make sure compiler is C99 capable

archive/issues_000954.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: gcc, flint, C99\n\nFlint requires C99 capable compilers. gcc 3.4.x and later are, but gcc 3.3 and earlier are not. There are still a number of those older compilers around, so error out early right away with an understandable error message to avoid bug reports with flint compiling to fail.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/954\n\n",
    "closed_at": "2007-12-20T21:32:01Z",
    "created_at": "2007-10-21T03:43:10Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "[with script] Make sure compiler is C99 capable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Keywords: gcc, flint, C99

Flint requires C99 capable compilers. gcc 3.4.x and later are, but gcc 3.3 and earlier are not. There are still a number of those older compilers around, so error out early right away with an understandable error message to avoid bug reports with flint compiling to fail.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/954





---

archive/issue_comments_005790.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T03:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_002629.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:09:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/954#event-2629"
}
```



---

archive/issue_comments_005791.json:
```json
{
    "body": "At least for gcc we can probably use\n\n```\ngcc -dumpversion\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-10-28T11:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

At least for gcc we can probably use

```
gcc -dumpversion
```

Cheers,

Michael



---

archive/issue_comments_005792.json:
```json
{
    "body": "This can't be written using python, so...\nmaybe in perl?",
    "created_at": "2007-11-03T22:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5792",
    "user": "https://github.com/williamstein"
}
```

This can't be written using python, so...
maybe in perl?



---

archive/issue_comments_005793.json:
```json
{
    "body": "perl script to test gcc version",
    "created_at": "2007-11-04T01:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5793",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

perl script to test gcc version



---

archive/issue_comments_005794.json:
```json
{
    "body": "Attachment [test_gcc_version.pl](tarball://root/attachments/some-uuid/ticket954/test_gcc_version.pl) by jkantor created at 2007-11-04 01:21:07\n\nI wrote a perl script to test if gcc version is greater than or equal to 3.4.0. \nIt exits 0 if this is the case and 1 otherwise. \n\nThe flint spkg-install should be easily modified to run this script and test the exit code and\ntake appropriate action. I didn't know what the desired behavior was so I didn't do this yet.",
    "created_at": "2007-11-04T01:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5794",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Attachment [test_gcc_version.pl](tarball://root/attachments/some-uuid/ticket954/test_gcc_version.pl) by jkantor created at 2007-11-04 01:21:07

I wrote a perl script to test if gcc version is greater than or equal to 3.4.0. 
It exits 0 if this is the case and 1 otherwise. 

The flint spkg-install should be easily modified to run this script and test the exit code and
take appropriate action. I didn't know what the desired behavior was so I didn't do this yet.



---

archive/issue_comments_005795.json:
```json
{
    "body": "More specifically adding this to the top of the flint spkg-install should be enough\n\n```\n./test_gcc_version.pl\nif [ $? -ne 0 ]; then\n   echo \"GCC version less than 3.4.0\"\n   echo \"Flint will not be able to compile successfully\"\n   exit 1\nfi\n```",
    "created_at": "2007-11-04T01:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5795",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

More specifically adding this to the top of the flint spkg-install should be enough

```
./test_gcc_version.pl
if [ $? -ne 0 ]; then
   echo "GCC version less than 3.4.0"
   echo "Flint will not be able to compile successfully"
   exit 1
fi
```



---

archive/issue_events_002630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-23T10:27:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/954#event-2630"
}
```



---

archive/issue_events_002631.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-23T10:27:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "milestone": "sage-2.8.14",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/954#event-2631"
}
```



---

archive/issue_events_002632.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-20T21:32:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/954#event-2632"
}
```



---

archive/issue_comments_005796.json:
```json
{
    "body": "Merged in 1.9.1 alpha2",
    "created_at": "2007-12-20T21:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5796",
    "user": "https://github.com/rlmill"
}
```

Merged in 1.9.1 alpha2



---

archive/issue_comments_005797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-20T21:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5797",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_005798.json:
```json
{
    "body": "rather 2.9.1 alpha2...",
    "created_at": "2007-12-20T21:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5798",
    "user": "https://github.com/rlmill"
}
```

rather 2.9.1 alpha2...
