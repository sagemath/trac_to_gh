# Issue 4904: convert sage.categories.* docstrings to Sphinx

archive/issues_004904.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4904\n\n",
    "created_at": "2009-01-01T22:46:45Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "convert sage.categories.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4904",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4904





---

archive/issue_comments_037206.json:
```json
{
    "body": "Attachment [trac_4904.patch](tarball://root/attachments/some-uuid/ticket4904/trac_4904.patch) by mhansen created at 2009-01-02 02:28:14",
    "created_at": "2009-01-02T02:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4904#issuecomment-37206",
    "user": "mhansen"
}
```

Attachment [trac_4904.patch](tarball://root/attachments/some-uuid/ticket4904/trac_4904.patch) by mhansen created at 2009-01-02 02:28:14



---

archive/issue_comments_037207.json:
```json
{
    "body": "This is not your fault at all, but I just noticed this dubious line in a docstring for morphism.pyx:\n\n```\n134\t \t        function -- a Python function that takes elements of the domain as input \n135\t \t                    and returns elements of the domain. \n```\n\n\nI think the last \"domain\" should be \"codomain\".",
    "created_at": "2009-01-03T04:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4904#issuecomment-37207",
    "user": "was"
}
```

This is not your fault at all, but I just noticed this dubious line in a docstring for morphism.pyx:

```
134	 	        function -- a Python function that takes elements of the domain as input 
135	 	                    and returns elements of the domain. 
```


I think the last "domain" should be "codomain".



---

archive/issue_comments_037208.json:
```json
{
    "body": "Everything looks good here.",
    "created_at": "2009-01-07T22:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4904#issuecomment-37208",
    "user": "jhpalmieri"
}
```

Everything looks good here.



---

archive/issue_comments_037209.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4904#issuecomment-37209",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037210.json:
```json
{
    "body": "Attachment [sage.categories-final.patch](tarball://root/attachments/some-uuid/ticket4904/sage.categories-final.patch) by mabshoff created at 2009-02-24 18:43:20\n\nMerged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4904#issuecomment-37210",
    "user": "mabshoff"
}
```

Attachment [sage.categories-final.patch](tarball://root/attachments/some-uuid/ticket4904/sage.categories-final.patch) by mabshoff created at 2009-02-24 18:43:20

Merged in Sage 3.4.alpha0.

Cheers,

Michael
