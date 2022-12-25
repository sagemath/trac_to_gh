# Issue 1696: osx 10.4 2.9.2 instructions don't work.

archive/issues_001696.json:
```json
{
    "body": "Assignee: cwitty\n\nI tried the 2.9.2 dmg for osx 10.4. There were two major issue\n\n1. Graphically dragging and dropping the sage folder didn't work. about halfway through the copy \n   failed with the message \n\n(You cannot copy \"singular\" to the destination because its name is the \nsame as the name of an item on the destination except for the case of \nsome characters) \n\n2. From the command line I was able to do \n\ncp -R -P /Volumes/sage-2.9.2-OSX10.4-intel-i386-Darwin/sage . \n\nThis worked modulo a missing libintl (see 1695).\n\nIf you only do cp -r, every symbolic link breaks.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1696\n\n",
    "created_at": "2008-01-05T23:48:32Z",
    "labels": [
        "component: relocation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "osx 10.4 2.9.2 instructions don't work.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1696",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: cwitty

I tried the 2.9.2 dmg for osx 10.4. There were two major issue

1. Graphically dragging and dropping the sage folder didn't work. about halfway through the copy 
   failed with the message 

(You cannot copy "singular" to the destination because its name is the 
same as the name of an item on the destination except for the case of 
some characters) 

2. From the command line I was able to do 

cp -R -P /Volumes/sage-2.9.2-OSX10.4-intel-i386-Darwin/sage . 

This worked modulo a missing libintl (see 1695).

If you only do cp -r, every symbolic link breaks.

Issue created by migration from https://trac.sagemath.org/ticket/1696





---

archive/issue_comments_010737.json:
```json
{
    "body": "What is the current status? I think the problems have been resolved, but can somebody confirm?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1696#issuecomment-10737",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the current status? I think the problems have been resolved, but can somebody confirm?

Cheers,

Michael



---

archive/issue_comments_010738.json:
```json
{
    "body": "This can be closed.  The issue is that my osx 10.4 intel build machine had a case-sensitive filesystem.  This is now a non-issue because that machine no longer exists (more precisely it was upgraded to 10.5; it's not my machine).  \n\nWilliam",
    "created_at": "2008-02-16T06:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1696#issuecomment-10738",
    "user": "https://github.com/williamstein"
}
```

This can be closed.  The issue is that my osx 10.4 intel build machine had a case-sensitive filesystem.  This is now a non-issue because that machine no longer exists (more precisely it was upgraded to 10.5; it's not my machine).  

William



---

archive/issue_events_004149.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-02-16T06:11:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1696",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1696#event-4149"
}
```



---

archive/issue_comments_010739.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-02-16T06:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1696#issuecomment-10739",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix
