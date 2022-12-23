# Issue 8331: BipartiteGraph constructor does not create partitions for dict inputs

archive/issues_008331.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  jason rlm\n\nKeywords: BipartiteGraph\n\nThe BipartiteGraph constructor does not create partitions for dict inputs.\n\n\n```\nsage: t1 = BipartiteGraph({'a': ['b'], 'b':['c']})\nsage: t1.left\n...\nAttributeError: 'BipartiteGraph' object has no attribute 'left'\n```\n\n\nThe problem comes in the constructor in the \"other inputs\" case.  A Graph object is created, but not all the control paths find a bipartition.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8331\n\n",
    "created_at": "2010-02-23T01:04:44Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "BipartiteGraph constructor does not create partitions for dict inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8331",
    "user": "rhinton"
}
```
Assignee: rlm

CC:  jason rlm

Keywords: BipartiteGraph

The BipartiteGraph constructor does not create partitions for dict inputs.


```
sage: t1 = BipartiteGraph({'a': ['b'], 'b':['c']})
sage: t1.left
...
AttributeError: 'BipartiteGraph' object has no attribute 'left'
```


The problem comes in the constructor in the "other inputs" case.  A Graph object is created, but not all the control paths find a bipartition.


Issue created by migration from https://trac.sagemath.org/ticket/8331





---

archive/issue_comments_074187.json:
```json
{
    "body": "another duplicate of part of #1941.",
    "created_at": "2010-02-23T01:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74187",
    "user": "rlm"
}
```

another duplicate of part of #1941.



---

archive/issue_comments_074188.json:
```json
{
    "body": "Attachment\n\nThe patch trac_8331-... fixes the bug, adds a doctest, and slightly improves the ReST markup for the constructor.  (I am certainly not an expert.)",
    "created_at": "2010-02-23T01:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74188",
    "user": "rhinton"
}
```

Attachment

The patch trac_8331-... fixes the bug, adds a doctest, and slightly improves the ReST markup for the constructor.  (I am certainly not an expert.)



---

archive/issue_comments_074189.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T01:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74189",
    "user": "rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074190.json:
```json
{
    "body": "Changing assignee from rlm to rhinton.",
    "created_at": "2010-02-23T01:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74190",
    "user": "rhinton"
}
```

Changing assignee from rlm to rhinton.



---

archive/issue_comments_074191.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-02T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74191",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074192.json:
```json
{
    "body": "Works for me :-)",
    "created_at": "2010-03-02T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74192",
    "user": "rlm"
}
```

Works for me :-)



---

archive/issue_comments_074193.json:
```json
{
    "body": "Ryan: remember to put a sensible commit message in your patch, together with the ticket number.",
    "created_at": "2010-03-03T14:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74193",
    "user": "mvngu"
}
```

Ryan: remember to put a sensible commit message in your patch, together with the ticket number.



---

archive/issue_comments_074194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74194",
    "user": "mvngu"
}
```

Resolution: fixed
