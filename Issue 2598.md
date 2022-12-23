# Issue 2598: [with patch, needs review] allow ZZ element to be constructed from GF(2) list

archive/issues_002598.json:
```json
{
    "body": "Assignee: somebody\n\nThis works for some time now:\n\n\n```\nsage: ZZ([1,0], 2)\n1\n```\n\n\nand after the patch this also works:\n\n\n```\nsage: ZZ([GF(2)(1),GF(2)(0)], 2)\n1\n```\n\n\nIt is -- at least for my applications -- common to get a list of bits, do some bitstuff with them and combine them again to an integer.\n\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/2598\n\n",
    "created_at": "2008-03-19T16:04:10Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] allow ZZ element to be constructed from GF(2) list",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2598",
    "user": "malb"
}
```
Assignee: somebody

This works for some time now:


```
sage: ZZ([1,0], 2)
1
```


and after the patch this also works:


```
sage: ZZ([GF(2)(1),GF(2)(0)], 2)
1
```


It is -- at least for my applications -- common to get a list of bits, do some bitstuff with them and combine them again to an integer.

}}}

Issue created by migration from https://trac.sagemath.org/ticket/2598





---

archive/issue_comments_017785.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-20T03:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2598#issuecomment-17785",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_017786.json:
```json
{
    "body": "The patch does what it claims and adds an appropriate doc-test.  There is a small (maybe 7-8%) speed-hit, but I think it is worth it for the improved functionality.\n\nI say it should be applied.",
    "created_at": "2008-03-20T12:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2598#issuecomment-17786",
    "user": "jbmohler"
}
```

The patch does what it claims and adds an appropriate doc-test.  There is a small (maybe 7-8%) speed-hit, but I think it is worth it for the improved functionality.

I say it should be applied.



---

archive/issue_comments_017787.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T02:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2598#issuecomment-17787",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017788.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T02:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2598#issuecomment-17788",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1
