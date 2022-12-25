# Issue 8180: sh: kpsewhich: not found reported on 4.3.0.1.alpha3 on Solaris 10.

archive/issues_008180.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  mvngu @jaapspies\n\nMinh created a 4.3.0.1.alpha3 which should have really been called 4.3.0.2.alpha3, as it was based on the 4.3.0.1 sources, with patches applied. It was  created to sort out what broke the Sage build between 4.3.0 and 4.3.1. \n\nThe previous version, 4.3.0.1.alpha2 did not have this issue, but 4.3.0.1.alpha3 is reporting the error message about kpsewhich is not found. From what I can gather, this kpsewhich is part of Latex. Since Latex is not a requirement to build Sage, this error should not be happening. It would appear one of the following patches is causing this, though none of them look as though they are likely to caused the problem. \n\n#5174, #1321, #6595, #6820, #6965\n\n\nBut these are the only patches applied between a version which did not generate the error, and one which does. \n\n\n```\nUpon loading this alpha3, it now shows that kpsewhich is not found:\n\n[mvngu@t2 sage-4.3.0.1.alpha3-32-bit-t2.math-gcc]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsh: kpsewhich: not found\nsh: kpsewhich: not found\nsage: 2 + 3\n5\n```\n\n| Sage Version 4.3.0.1.alpha3, Release Date: 2010-01-28              |\n| Type notebook() for the GUI, and license() for information.        |\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/8180\n\n",
    "created_at": "2010-02-03T20:06:36Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "sh: kpsewhich: not found reported on 4.3.0.1.alpha3 on Solaris 10.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8180",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  mvngu @jaapspies

Minh created a 4.3.0.1.alpha3 which should have really been called 4.3.0.2.alpha3, as it was based on the 4.3.0.1 sources, with patches applied. It was  created to sort out what broke the Sage build between 4.3.0 and 4.3.1. 

The previous version, 4.3.0.1.alpha2 did not have this issue, but 4.3.0.1.alpha3 is reporting the error message about kpsewhich is not found. From what I can gather, this kpsewhich is part of Latex. Since Latex is not a requirement to build Sage, this error should not be happening. It would appear one of the following patches is causing this, though none of them look as though they are likely to caused the problem. 

#5174, #1321, #6595, #6820, #6965


But these are the only patches applied between a version which did not generate the error, and one which does. 


```
Upon loading this alpha3, it now shows that kpsewhich is not found:

[mvngu@t2 sage-4.3.0.1.alpha3-32-bit-t2.math-gcc]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sh: kpsewhich: not found
sh: kpsewhich: not found
sage: 2 + 3
5
```

| Sage Version 4.3.0.1.alpha3, Release Date: 2010-01-28              |
| Type notebook() for the GUI, and license() for information.        |
Dave

Issue created by migration from https://trac.sagemath.org/ticket/8180





---

archive/issue_comments_071967.json:
```json
{
    "body": "I think the culprit is #1321.  If you want evidence: in `sage/graphs/all.py`, change the end of the file from\n\n```\nfrom graph_database import graph_db_info\nfrom graph_editor import graph_editor\n```\n\nto\n\n```\nfrom graph_database import graph_db_info\n\nprint \"no kpsewhich error message yet\"\n\nfrom graph_editor import graph_editor\n\nprint \"now you just saw the error message\"\n```\n\nNote that if you use the version of graph_editor in Sage 4.3.2.alpha1, then I think you don't get this message, so the problem seems to have been fixed at some point.  I can't find the ticket, though...",
    "created_at": "2010-02-03T23:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71967",
    "user": "https://github.com/jhpalmieri"
}
```

I think the culprit is #1321.  If you want evidence: in `sage/graphs/all.py`, change the end of the file from

```
from graph_database import graph_db_info
from graph_editor import graph_editor
```

to

```
from graph_database import graph_db_info

print "no kpsewhich error message yet"

from graph_editor import graph_editor

print "now you just saw the error message"
```

Note that if you use the version of graph_editor in Sage 4.3.2.alpha1, then I think you don't get this message, so the problem seems to have been fixed at some point.  I can't find the ticket, though...



---

archive/issue_comments_071968.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-04T02:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71968",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071969.json:
```json
{
    "body": "Actually, I think using the newer version of graph_editor just delays the error message until you run some graph theory command like `graphs.CompleteGraph(2)`.  \n\nHere's a patch which does fix the problem, I think.",
    "created_at": "2010-02-04T02:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71969",
    "user": "https://github.com/jhpalmieri"
}
```

Actually, I think using the newer version of graph_editor just delays the error message until you run some graph theory command like `graphs.CompleteGraph(2)`.  

Here's a patch which does fix the problem, I think.



---

archive/issue_comments_071970.json:
```json
{
    "body": "Attachment [trac_8180-kpsewhich.patch](tarball://root/attachments/some-uuid/ticket8180/trac_8180-kpsewhich.patch) by @williamstein created at 2010-02-04 02:57:57",
    "created_at": "2010-02-04T02:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71970",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8180-kpsewhich.patch](tarball://root/attachments/some-uuid/ticket8180/trac_8180-kpsewhich.patch) by @williamstein created at 2010-02-04 02:57:57



---

archive/issue_comments_071971.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T02:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71971",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008383.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T15:01:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8180#event-8383"
}
```



---

archive/issue_comments_071972.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71972",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_071973.json:
```json
{
    "body": "The patch does not prevent this error message occuring on Solaris. I have created another ticket, #8445 to preport the same problem still existing. \n\nDave",
    "created_at": "2010-03-05T13:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8180#issuecomment-71973",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The patch does not prevent this error message occuring on Solaris. I have created another ticket, #8445 to preport the same problem still existing. 

Dave
