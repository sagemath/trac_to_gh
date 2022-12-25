# Issue 1444: [with patch] some serious hard-coding issues that break all binary installs

archive/issues_001444.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nHi,\n\nThere are a few very serious (but easy to fix)\nproblems with the current sage and upcoming packages\nthat involving hardcoding of paths.  These\nwill cause problems if you move a sage install.\n\nPOLYBORI:\nI noticed this in a SAGE_ROOT/local/bin/:\n\n   lrwxr-xr-x  1 was  was       47 Dec  4 10:52 ipbori -> /Users/was/s/local/share/polybori/ipbori/ipbori\n\nThat link *must* not be hard coded.  Make sure this gets fixed before polybori is in sage.\n\nSINGULAR (very serious):\n   Several Singular-related files in SAGE_ROOT/local/bin/ have hardcoded paths.\n   This makes it so singular will fail to work for everybody who downloads a sage\n   binary right now :-(. \n\n   The package singular-3-0-4-1-20071209.spkg fixes the problem.  Just do \n   sage -upgrade to get it, or download it from \n       http://sagemath.org/packages/standard/singular-3-0-4-1-20071209.spkg\n\nBZIP2:\n   Some minor path hardcoding problems.  Easy to fix.  I've put the file that needs\nto be replaced here...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1444\n\n",
    "created_at": "2007-12-10T01:11:39Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] some serious hard-coding issues that break all binary installs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1444",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff


```
Hi,

There are a few very serious (but easy to fix)
problems with the current sage and upcoming packages
that involving hardcoding of paths.  These
will cause problems if you move a sage install.

POLYBORI:
I noticed this in a SAGE_ROOT/local/bin/:

   lrwxr-xr-x  1 was  was       47 Dec  4 10:52 ipbori -> /Users/was/s/local/share/polybori/ipbori/ipbori

That link *must* not be hard coded.  Make sure this gets fixed before polybori is in sage.

SINGULAR (very serious):
   Several Singular-related files in SAGE_ROOT/local/bin/ have hardcoded paths.
   This makes it so singular will fail to work for everybody who downloads a sage
   binary right now :-(. 

   The package singular-3-0-4-1-20071209.spkg fixes the problem.  Just do 
   sage -upgrade to get it, or download it from 
       http://sagemath.org/packages/standard/singular-3-0-4-1-20071209.spkg

BZIP2:
   Some minor path hardcoding problems.  Easy to fix.  I've put the file that needs
to be replaced here...
```


Issue created by migration from https://trac.sagemath.org/ticket/1444





---

archive/issue_comments_009291.json:
```json
{
    "body": "Attachment [bzip2-1.0.4-install](tarball://root/attachments/some-uuid/ticket1444/bzip2-1.0.4-install) by @williamstein created at 2007-12-10 01:12:42\n\nput this file in spkg/base/   overwriting the one there already.",
    "created_at": "2007-12-10T01:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1444#issuecomment-9291",
    "user": "https://github.com/williamstein"
}
```

Attachment [bzip2-1.0.4-install](tarball://root/attachments/some-uuid/ticket1444/bzip2-1.0.4-install) by @williamstein created at 2007-12-10 01:12:42

put this file in spkg/base/   overwriting the one there already.



---

archive/issue_comments_009292.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T03:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1444#issuecomment-9292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009293.json:
```json
{
    "body": "Merged in 2.9.alpha3.",
    "created_at": "2007-12-10T03:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1444#issuecomment-9293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha3.
