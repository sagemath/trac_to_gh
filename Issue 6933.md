# Issue 6933: readline-5.2.p7 builds as 32-bit on Solaris even if SAGE64=yes

archive/issues_006933.json:
```json
{
    "body": "Assignee: tbd\n\nThe title pretty much says it all. The spkg-install is ignoring SAGE64 unless the OS is Darwin (OS X). \n\nit currently has:\n\n```\n\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n   echo \"Building 64 bit OSX version of Sage\"\n   CFLAGS=\"-O2 -g -m64 \" && export CFLAGS\n   LDFLAGS=\"-m64\"\nfi\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6933\n\n",
    "created_at": "2009-09-15T09:27:56Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "readline-5.2.p7 builds as 32-bit on Solaris even if SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6933",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

The title pretty much says it all. The spkg-install is ignoring SAGE64 unless the OS is Darwin (OS X). 

it currently has:

```

if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "Building 64 bit OSX version of Sage"
   CFLAGS="-O2 -g -m64 " && export CFLAGS
   LDFLAGS="-m64"
fi

```


Issue created by migration from https://trac.sagemath.org/ticket/6933





---

archive/issue_events_016313.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-17T22:13:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6933",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6933#event-16313"
}
```



---

archive/issue_comments_057183.json:
```json
{
    "body": "Fixed by #6945.",
    "created_at": "2009-09-17T22:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6933#issuecomment-57183",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Fixed by #6945.



---

archive/issue_comments_057184.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-17T22:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6933#issuecomment-57184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_events_016314.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-17T22:13:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6933",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6933#event-16314"
}
```
