# Issue 2431: [optional spkg] polymake-2.2.p3.spkg fix

archive/issues_002431.json:
```json
{
    "body": "Assignee: mhampton\n\nTwo issues: the install script needs to be changed to use cddlib-094b.p1 instead of p0; a version with this change is at:\nhttp://www.d.umn.edu/~mhampton/polymake-2.2.p3.spkg\n\nThe install also fails on a binary installation since its relies on the cddlib spkg being in spkg/standard, instead of the dummy version.  I will try to fix this; I am a little puzzled about it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2431\n\n",
    "created_at": "2008-03-08T22:59:37Z",
    "labels": [
        "packages",
        "minor",
        "bug"
    ],
    "title": "[optional spkg] polymake-2.2.p3.spkg fix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2431",
    "user": "mhampton"
}
```
Assignee: mhampton

Two issues: the install script needs to be changed to use cddlib-094b.p1 instead of p0; a version with this change is at:
http://www.d.umn.edu/~mhampton/polymake-2.2.p3.spkg

The install also fails on a binary installation since its relies on the cddlib spkg being in spkg/standard, instead of the dummy version.  I will try to fix this; I am a little puzzled about it.

Issue created by migration from https://trac.sagemath.org/ticket/2431





---

archive/issue_comments_016448.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2008-03-19T10:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16448",
    "user": "mabshoff"
}
```

Changing component from packages to optional packages.



---

archive/issue_comments_016449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T11:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16449",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016450.json:
```json
{
    "body": "I fixed some small issues with the SPKG:\n\n* added an hg repo and .hgignore\n* rename SAGE.txt to SPKG.txt\n\nThe new spkg builds fine for me and is at\n\nhttp://sage.math.washington.edu/home/mabshoff/SPKG/polymake-2.2.p4.spkg\n\nPositive review, I will upload the new spkg to the optional package repo shortly. It already seems to be there, so I am not sure why this ticket was never closed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T11:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16450",
    "user": "mabshoff"
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

archive/issue_comments_016451.json:
```json
{
    "body": "Merged in the optional package repo and mirrored out.",
    "created_at": "2008-03-19T11:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2431#issuecomment-16451",
    "user": "mabshoff"
}
```

Merged in the optional package repo and mirrored out.
