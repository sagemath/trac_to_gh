# Issue 5984: cmp related doctest failure in sage/modular/arithgroup/arithgroup_perm.py

archive/issues_005984.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long devel/sage/sage/modular/arithgroup/arithgroup_perm.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage-main/sage/modular/arithgroup/arithgroup_perm.py\", line 204:\n    sage: cmp(G, Gamma0(8))\nExpected:\n    1\nGot:\n    -1\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5984\n\n",
    "created_at": "2009-05-05T04:33:53Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "cmp related doctest failure in sage/modular/arithgroup/arithgroup_perm.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5984",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t -long devel/sage/sage/modular/arithgroup/arithgroup_perm.py
**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage-main/sage/modular/arithgroup/arithgroup_perm.py", line 204:
    sage: cmp(G, Gamma0(8))
Expected:
    1
Got:
    -1
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5984





---

archive/issue_comments_047544.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T04:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5984#issuecomment-47544",
    "user": "mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_047545.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-05T04:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5984#issuecomment-47545",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047546.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-05T05:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5984#issuecomment-47546",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_047547.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-05T05:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5984#issuecomment-47547",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047548.json:
```json
{
    "body": "Merged in Sage 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T05:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5984#issuecomment-47548",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.

Cheers,

Michael
