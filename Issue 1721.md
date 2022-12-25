# Issue 1721: Introduse SYSTEM_ATLAS to skip tuning of ATLAS

archive/issues_001721.json:
```json
{
    "body": "Assignee: mabshoff\n\nSince many people complain about the ATLAS build in case they end up with a system without pre-tuned CPUs add this end-variable to skip over the ATLAS build.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1721\n\n",
    "created_at": "2008-01-08T10:52:38Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Introduse SYSTEM_ATLAS to skip tuning of ATLAS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Since many people complain about the ATLAS build in case they end up with a system without pre-tuned CPUs add this end-variable to skip over the ATLAS build.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1721





---

archive/issue_comments_010877.json:
```json
{
    "body": "The following patch should solve the problem of Pentium Ms which are misrecognized as CoreDuo:\n\n```\n$ pwd\n/tmp/atlas-3.8.p6/src/ATLAS/CONFIG/src/backend\n$ diff -u archinfo_x86.c.orig archinfo_x86.c\n--- archinfo_x86.c.orig 2008-01-09 23:43:59.000000000 +0100\n+++ archinfo_x86.c      2008-01-09 23:44:11.000000000 +0100\n@@ -281,6 +281,7 @@\n       case  9:\n       case 13:\n          iret = IntPM;\n+        break;\n       case 14:\n          iret = IntCoreDuo;\n          break;\n```\n\nThis should also solve (partly) #1547.",
    "created_at": "2008-01-09T23:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10877",
    "user": "https://github.com/zimmermann6"
}
```

The following patch should solve the problem of Pentium Ms which are misrecognized as CoreDuo:

```
$ pwd
/tmp/atlas-3.8.p6/src/ATLAS/CONFIG/src/backend
$ diff -u archinfo_x86.c.orig archinfo_x86.c
--- archinfo_x86.c.orig 2008-01-09 23:43:59.000000000 +0100
+++ archinfo_x86.c      2008-01-09 23:44:11.000000000 +0100
@@ -281,6 +281,7 @@
       case  9:
       case 13:
          iret = IntPM;
+        break;
       case 14:
          iret = IntCoreDuo;
          break;
```

This should also solve (partly) #1547.



---

archive/issue_comments_010878.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-09T23:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10878",
    "user": "https://github.com/zimmermann6"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_010879.json:
```json
{
    "body": "Hello Paul,\n\nthis is really an orthogonal issue, so I took your patch and made it #1740.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T05:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello Paul,

this is really an orthogonal issue, so I took your patch and made it #1740.

Cheers,

Michael



---

archive/issue_comments_010880.json:
```json
{
    "body": "Removed [with patch] since Paul's patch is unrelated to this issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T18:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Removed [with patch] since Paul's patch is unrelated to this issue.

Cheers,

Michael



---

archive/issue_comments_010881.json:
```json
{
    "body": "This is an important thing to do, building ATLAS takes too much time!",
    "created_at": "2008-01-19T21:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10881",
    "user": "https://github.com/pdenapo"
}
```

This is an important thing to do, building ATLAS takes too much time!



---

archive/issue_comments_010882.json:
```json
{
    "body": "I add an optional SAGE_ATLAS_LIB keyword, which should be a directory containing\nlibatlas.so, liblapack.so, libcblas.so, libatlas.so\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p8.spkg",
    "created_at": "2008-01-20T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10882",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

I add an optional SAGE_ATLAS_LIB keyword, which should be a directory containing
libatlas.so, liblapack.so, libcblas.so, libatlas.so

http://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p8.spkg



---

archive/issue_comments_010883.json:
```json
{
    "body": "The script that did link the libraries failed to link the headers. The spkg at #1787 will fix that.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The script that did link the libraries failed to link the headers. The spkg at #1787 will fix that.

Cheers,

Michael



---

archive/issue_comments_010884.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-22T07:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_010885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-22T07:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1721#issuecomment-10885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001880.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-22T07:11:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1721",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1721#event-1880"
}
```
