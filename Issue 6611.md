# Issue 6611: [with spkg, needs review] rename networkx-0.99.p1-fake_really-0.36.p0.spkg to networkx-0.36.p0.spkg

archive/issues_006611.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  rlm\n\nAs of Sage 4.1, the NetworkX SPKG is named `networkx-0.99.p1-fake_really-0.36.p0.spkg`, which was the result of #4860 and #5934. Let's now rename that SPKG as `networkx-0.36.p0.spkg`. The updated SPKG is up at \n\nhttp://sage.math.washington.edu/home/mvngu/patch/networkx-0.36.p0.spkg\n\nThere is no substantial difference between that SPKG and the one in Sage 4.1. I merely took the one from Sage 4.1 and renamed it as `networkx-0.36.p0.spkg`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6611\n\n",
    "created_at": "2009-07-24T07:22:33Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "[with spkg, needs review] rename networkx-0.99.p1-fake_really-0.36.p0.spkg to networkx-0.36.p0.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6611",
    "user": "mvngu"
}
```
Assignee: mabshoff

CC:  rlm

As of Sage 4.1, the NetworkX SPKG is named `networkx-0.99.p1-fake_really-0.36.p0.spkg`, which was the result of #4860 and #5934. Let's now rename that SPKG as `networkx-0.36.p0.spkg`. The updated SPKG is up at 

http://sage.math.washington.edu/home/mvngu/patch/networkx-0.36.p0.spkg

There is no substantial difference between that SPKG and the one in Sage 4.1. I merely took the one from Sage 4.1 and renamed it as `networkx-0.36.p0.spkg`.

Issue created by migration from https://trac.sagemath.org/ticket/6611





---

archive/issue_comments_054113.json:
```json
{
    "body": "I don't think this is a good idea-- there are scripts which determine the newest version of an SPKG, and if you change the name to `networkx-0.36*`, then the newest version will remain `networkx-0.99.p1-fake_really-0.36.p0.spkg`",
    "created_at": "2009-07-27T16:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6611#issuecomment-54113",
    "user": "rlm"
}
```

I don't think this is a good idea-- there are scripts which determine the newest version of an SPKG, and if you change the name to `networkx-0.36*`, then the newest version will remain `networkx-0.99.p1-fake_really-0.36.p0.spkg`



---

archive/issue_comments_054114.json:
```json
{
    "body": "Good catch! So can this ticket be closed as invalid?",
    "created_at": "2009-07-28T03:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6611#issuecomment-54114",
    "user": "mvngu"
}
```

Good catch! So can this ticket be closed as invalid?



---

archive/issue_comments_054115.json:
```json
{
    "body": "+1 to closing it as invalid.\n\n(+1 also for someone actually updating networkx :)",
    "created_at": "2009-07-30T09:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6611#issuecomment-54115",
    "user": "jason"
}
```

+1 to closing it as invalid.

(+1 also for someone actually updating networkx :)



---

archive/issue_comments_054116.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-07-30T09:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6611#issuecomment-54116",
    "user": "mvngu"
}
```

Resolution: invalid
