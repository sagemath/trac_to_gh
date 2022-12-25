# Issue 2431: [optional spkg] polymake-2.2.p3.spkg fix

archive/issues_002431.json:
```json
{
    "body": "Assignee: mhampton\n\nTwo issues: the install script needs to be changed to use cddlib-094b.p1 instead of p0; a version with this change is at:\nhttp://www.d.umn.edu/~mhampton/polymake-2.2.p3.spkg\n\nThe install also fails on a binary installation since its relies on the cddlib spkg being in spkg/standard, instead of the dummy version.  I will try to fix this; I am a little puzzled about it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2431\n\n",
    "created_at": "2008-03-08T22:59:37Z",
    "labels": [
        "component: packages",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[optional spkg] polymake-2.2.p3.spkg fix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Two issues: the install script needs to be changed to use cddlib-094b.p1 instead of p0; a version with this change is at:
http://www.d.umn.edu/~mhampton/polymake-2.2.p3.spkg

The install also fails on a binary installation since its relies on the cddlib spkg being in spkg/standard, instead of the dummy version.  I will try to fix this; I am a little puzzled about it.

Issue created by migration from https://trac.sagemath.org/ticket/2431





---

archive/issue_comments_016413.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2008-03-19T10:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to optional packages.



---

archive/issue_comments_016414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T11:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16414",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016415.json:
```json
{
    "body": "I fixed some small issues with the SPKG:\n\n* added an hg repo and .hgignore\n* rename SAGE.txt to SPKG.txt\n\nThe new spkg builds fine for me and is at\n\nhttp://sage.math.washington.edu/home/mabshoff/SPKG/polymake-2.2.p4.spkg\n\nPositive review, I will upload the new spkg to the optional package repo shortly. It already seems to be there, so I am not sure why this ticket was never closed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T11:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16415",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed some small issues with the SPKG:

* added an hg repo and .hgignore
* rename SAGE.txt to SPKG.txt

The new spkg builds fine for me and is at

http://sage.math.washington.edu/home/mabshoff/SPKG/polymake-2.2.p4.spkg

Positive review, I will upload the new spkg to the optional package repo shortly. It already seems to be there, so I am not sure why this ticket was never closed.

Cheers,

Michael



---

archive/issue_events_002608.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-19T11:12:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2431#event-2608"
}
```



---

archive/issue_comments_016416.json:
```json
{
    "body": "Merged in the optional package repo and mirrored out.",
    "created_at": "2008-03-19T11:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16416",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in the optional package repo and mirrored out.
