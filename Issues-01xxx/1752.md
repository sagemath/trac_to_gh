# Issue 1752: [with spkg] sage make install bug

archive/issues_001752.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen calling \n\n```\nDESTDIR=$sagedir make install\n```\nthe following library files will be created with 555 permissions. When causes problems when trying to strip those files. To change that, deliver the files with 755 permissions.\n\n$sagedir/sage/local/lib/libhistory.so.*\n$sagedir/sage/local/lib/libreadline.so.*\n\nIssue created by migration from https://trac.sagemath.org/ticket/1752\n\n",
    "closed_at": "2008-01-11T19:21:01Z",
    "created_at": "2008-01-10T22:14:38Z",
    "labels": [
        "component: relocation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with spkg] sage make install bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1752",
    "user": "https://trac.sagemath.org/admin/accounts/users/pgrinber"
}
```
Assignee: mabshoff

When calling 

```
DESTDIR=$sagedir make install
```
the following library files will be created with 555 permissions. When causes problems when trying to strip those files. To change that, deliver the files with 755 permissions.

$sagedir/sage/local/lib/libhistory.so.*
$sagedir/sage/local/lib/libreadline.so.*

Issue created by migration from https://trac.sagemath.org/ticket/1752





---

archive/issue_events_004233.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-10T22:26:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1752#event-4233"
}
```



---

archive/issue_comments_011025.json:
```json
{
    "body": "Hi Paul,\n\nyou should assign a milestone for each ticket you open. The next milestone is usually a good default. Same for #1753.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T22:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Paul,

you should assign a milestone for each ticket you open. The next milestone is usually a good default. Same for #1753.

Cheers,

Michael



---

archive/issue_comments_011026.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-01-11T19:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11026",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_011027.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-11T19:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011028.json:
```json
{
    "body": "The updated spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha2/readline-5.2.p0.spkg\n\nfixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-11T19:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11028",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha2/readline-5.2.p0.spkg

fixes the issue.

Cheers,

Michael



---

archive/issue_comments_011029.json:
```json
{
    "body": "It looks like the issue itself is in the original readline install process. I will investigate this.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-11T19:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11029",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It looks like the issue itself is in the original readline install process. I will investigate this.

Cheers,

Michael



---

archive/issue_comments_011030.json:
```json
{
    "body": "Merged in Sage 2.10.alpha2.",
    "created_at": "2008-01-11T19:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha2.



---

archive/issue_comments_011031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-11T19:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1752#issuecomment-11031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004234.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-11T19:21:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1752",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1752#event-4234"
}
```
