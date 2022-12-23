# Issue 4210: [with spkg, needs review] Remove some deprecation warnings from numpy-1.2.spkg

archive/issues_004210.json:
```json
{
    "body": "Assignee: mabshoff\n\n#4205 depends on the new scipy-0.7svn.spkg and some other tickets which will not go into Sage 3.1.3. To still be able to update to numpy 1.2 we need to quiet some deprecation warnings in numpy itself for now. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/numpy-1.2.0.p0.spkg\n\nintroduces a couple work arounds for now that should be reverted once #3391, #3498 and #4005 go in.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4210\n\n",
    "created_at": "2008-09-27T22:18:16Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with spkg, needs review] Remove some deprecation warnings from numpy-1.2.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4210",
    "user": "mabshoff"
}
```
Assignee: mabshoff

#4205 depends on the new scipy-0.7svn.spkg and some other tickets which will not go into Sage 3.1.3. To still be able to update to numpy 1.2 we need to quiet some deprecation warnings in numpy itself for now. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/numpy-1.2.0.p0.spkg

introduces a couple work arounds for now that should be reverted once #3391, #3498 and #4005 go in.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4210





---

archive/issue_comments_030596.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-27T22:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4210#issuecomment-30596",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030597.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-27T22:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4210#issuecomment-30597",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_030598.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T22:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4210#issuecomment-30598",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030599.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T22:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4210#issuecomment-30599",
    "user": "mabshoff"
}
```

Resolution: fixed
