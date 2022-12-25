# Issue 5741: Detect Atom CPUs as Core2 in the ATLAS detection script

archive/issues_005741.json:
```json
{
    "body": "Assignee: mabshoff\n\nBuild time on Sage for Atom hardware is insane since ATLAS does not identify Atom CPUs as known hardware and does a full tune, i.e. building Sage takes half a day :(\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5741\n\n",
    "created_at": "2009-04-11T01:21:48Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Detect Atom CPUs as Core2 in the ATLAS detection script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5741",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Build time on Sage for Atom hardware is insane since ATLAS does not identify Atom CPUs as known hardware and does a full tune, i.e. building Sage takes half a day :(

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5741





---

archive/issue_comments_044808.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-11T01:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5741#issuecomment-44808",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044809.json:
```json
{
    "body": "This works fine for me.\n\n\n```\nreal    13m57.018s\nuser    8m13.339s\nsys     4m13.032s\nSuccessfully installed gmp-mpir-1.0.rc8\n```\n",
    "created_at": "2009-04-11T05:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5741#issuecomment-44809",
    "user": "https://github.com/williamstein"
}
```

This works fine for me.


```
real    13m57.018s
user    8m13.339s
sys     4m13.032s
Successfully installed gmp-mpir-1.0.rc8
```




---

archive/issue_comments_044810.json:
```json
{
    "body": "Well, this is about ATLAS :)\n\nCheer,\n\nMichael",
    "created_at": "2009-04-11T05:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5741#issuecomment-44810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, this is about ATLAS :)

Cheer,

Michael



---

archive/issue_comments_044811.json:
```json
{
    "body": "This is basically the fix to make ATLAS detect an Atom as a Core2. There is 32 and 64 bit tuning info:\n\n```\ndiff -r 0de046c62166 patches/archinfo_x86.c\n--- a/patches/archinfo_x86.c\tSat Feb 21 00:57:22 2009 -0800\n+++ b/patches/archinfo_x86.c\tFri Apr 17 19:09:51 2009 -0700\n@@ -301,6 +301,7 @@\n          break;\n       case 15:\n       case 23:\n+      case 28:\n       case 29:\n          iret = IntCore2;\n          break;\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T02:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5741#issuecomment-44811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is basically the fix to make ATLAS detect an Atom as a Core2. There is 32 and 64 bit tuning info:

```
diff -r 0de046c62166 patches/archinfo_x86.c
--- a/patches/archinfo_x86.c	Sat Feb 21 00:57:22 2009 -0800
+++ b/patches/archinfo_x86.c	Fri Apr 17 19:09:51 2009 -0700
@@ -301,6 +301,7 @@
          break;
       case 15:
       case 23:
+      case 28:
       case 29:
          iret = IntCore2;
          break;
```


Cheers,

Michael



---

archive/issue_events_013470.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-18T23:24:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5741#event-13470"
}
```



---

archive/issue_comments_044812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T23:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5741#issuecomment-44812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044813.json:
```json
{
    "body": "Fixed in Sage 3.4.1.rc4 via #5219.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T23:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5741#issuecomment-44813",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.4.1.rc4 via #5219.

Cheers,

Michael
