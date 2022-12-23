# Issue 5884: OpenSuse 11/x86-64: doctest failure in groups/perm_gps/permgroup.py

archive/issues_005884.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  wdj\n\nThis might be a side effect of me screwing up at #5697:\n\n```\nsage -t -long \"devel/sage/sage/groups/perm_gps/permgroup.py\"\n********************************************************************\nFile \"/space/wstein/farm/sage-3.4.1/devel/sage/sage/groups/perm_gps/permgroup.py\", line 914:\n   sage: G.random_element()\nExpected:\n   (1,2)(4,5)\nGot:\n   (2,3)(4,5)\n********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5884\n\n",
    "created_at": "2009-04-24T00:43:57Z",
    "labels": [
        "doctest coverage",
        "critical",
        "bug"
    ],
    "title": "OpenSuse 11/x86-64: doctest failure in groups/perm_gps/permgroup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5884",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  wdj

This might be a side effect of me screwing up at #5697:

```
sage -t -long "devel/sage/sage/groups/perm_gps/permgroup.py"
********************************************************************
File "/space/wstein/farm/sage-3.4.1/devel/sage/sage/groups/perm_gps/permgroup.py", line 914:
   sage: G.random_element()
Expected:
   (1,2)(4,5)
Got:
   (2,3)(4,5)
********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5884





---

archive/issue_comments_046524.json:
```json
{
    "body": "Hmm, this seems to be gone, so \"invalid\" until we find a reproducible test case.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5884#issuecomment-46524",
    "user": "mabshoff"
}
```

Hmm, this seems to be gone, so "invalid" until we find a reproducible test case.

Cheers,

Michael



---

archive/issue_comments_046525.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-05-15T14:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5884#issuecomment-46525",
    "user": "mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_046526.json:
```json
{
    "body": "This has cropped up again in 4.1.2.rc2 -- see #7206.",
    "created_at": "2009-10-14T03:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5884#issuecomment-46526",
    "user": "ddrake"
}
```

This has cropped up again in 4.1.2.rc2 -- see #7206.
