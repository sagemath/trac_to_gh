# Issue 5362: [with patch, needs review] bug in transpose for matrix_double_dense

archive/issues_005362.json:
```json
{
    "body": "Assignee: was\n\nKeywords: transpose\n\nA copy is missing:\n\n```\nsage: m=matrix(RDF,2,2,range(4))\nsage: m2=m.transpose()\nsage: m2\n\n[0.0 2.0]\n[1.0 3.0]\nsage: m[0,0]=1\nsage: m2\n\n[1.0 2.0]\n[1.0 3.0]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5362\n\n",
    "created_at": "2009-02-24T22:27:41Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "title": "[with patch, needs review] bug in transpose for matrix_double_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5362",
    "user": "ylchapuy"
}
```
Assignee: was

Keywords: transpose

A copy is missing:

```
sage: m=matrix(RDF,2,2,range(4))
sage: m2=m.transpose()
sage: m2

[0.0 2.0]
[1.0 3.0]
sage: m[0,0]=1
sage: m2

[1.0 2.0]
[1.0 3.0]
```


Issue created by migration from https://trac.sagemath.org/ticket/5362





---

archive/issue_comments_041315.json:
```json
{
    "body": "I updated the formatting of the docstring to be compatible with the new documentation system.  Other than that, looks good.  Good catch!",
    "created_at": "2009-02-24T23:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5362#issuecomment-41315",
    "user": "mhansen"
}
```

I updated the formatting of the docstring to be compatible with the new documentation system.  Other than that, looks good.  Good catch!



---

archive/issue_comments_041316.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-25T18:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5362#issuecomment-41316",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_041317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T17:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5362#issuecomment-41317",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041318.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T17:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5362#issuecomment-41318",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
