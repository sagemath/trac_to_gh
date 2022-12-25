# Issue 2334: $SAGE_LOCAL/include/eclib has wrong permissions

archive/issues_002334.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\ndrwx------ 2 malb georgesk 4.0K 2008-01-29 14:33 eclib\n^^^^^^^^^^^\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2334\n\n",
    "created_at": "2008-02-27T19:08:17Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "$SAGE_LOCAL/include/eclib has wrong permissions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2334",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff


```
drwx------ 2 malb georgesk 4.0K 2008-01-29 14:33 eclib
^^^^^^^^^^^
```


Issue created by migration from https://trac.sagemath.org/ticket/2334





---

archive/issue_comments_015576.json:
```json
{
    "body": "It boils down to a stupid thinko in spkg-install:\n\n```\ndiff -r 06dc1250f0ad spkg-install\n--- a/spkg-install      Sat Feb 09 12:45:02 2008 -0800\n+++ b/spkg-install      Sat Mar 08 22:49:06 2008 -0800\n@@ -88,5 +88,5 @@ strip \"$SAGE_LOCAL\"/bin/tconic\"$EXE_NAME\n strip \"$SAGE_LOCAL\"/bin/tconic\"$EXE_NAME\"\n\n cd \"$SAGE_LOCAL\"/include\n-chown 755 eclib\n+chmod 755 eclib\n chmod 644 eclib/*\n```\n\n\nThe updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc3/eclib-20080127.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-09T06:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2334#issuecomment-15576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It boils down to a stupid thinko in spkg-install:

```
diff -r 06dc1250f0ad spkg-install
--- a/spkg-install      Sat Feb 09 12:45:02 2008 -0800
+++ b/spkg-install      Sat Mar 08 22:49:06 2008 -0800
@@ -88,5 +88,5 @@ strip "$SAGE_LOCAL"/bin/tconic"$EXE_NAME
 strip "$SAGE_LOCAL"/bin/tconic"$EXE_NAME"

 cd "$SAGE_LOCAL"/include
-chown 755 eclib
+chmod 755 eclib
 chmod 644 eclib/*
```


The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc3/eclib-20080127.p1.spkg

Cheers,

Michael



---

archive/issue_comments_015577.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-09T06:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2334#issuecomment-15577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015578.json:
```json
{
    "body": "With the new spkg I get:\n\n```\nsage-2.10.3.rc3$ ls -ald local/include/eclib/\ndrwxr-xr-x 2 mabshoff 1090 4096 2008-03-08 22:59 local/include/eclib/\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-09T07:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2334#issuecomment-15578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the new spkg I get:

```
sage-2.10.3.rc3$ ls -ald local/include/eclib/
drwxr-xr-x 2 mabshoff 1090 4096 2008-03-08 22:59 local/include/eclib/
```


Cheers,

Michael



---

archive/issue_comments_015579.json:
```json
{
    "body": "Positive review",
    "created_at": "2008-03-09T07:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2334#issuecomment-15579",
    "user": "https://github.com/garyfurnish"
}
```

Positive review



---

archive/issue_comments_015580.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc3",
    "created_at": "2008-03-09T07:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2334#issuecomment-15580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc3



---

archive/issue_events_005512.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-09T07:40:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2334#event-5512"
}
```



---

archive/issue_comments_015581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-09T07:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2334#issuecomment-15581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
