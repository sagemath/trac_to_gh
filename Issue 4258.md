# Issue 4258: switch multiplication of dense matrices over finite prime fields to LinBox

archive/issues_004258.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @ClementPernet @burcin @jasongrout simonking\n\nKeywords: linbox, linear algebra\n\n\n```\nsage: A = random_matrix(GF(3),2000,2000)\nsage: %time A*A\n2000 x 2000 dense matrix over Finite Field of size 3\nCPU time: 14.69 s,  Wall time: 15.08 s\n```\n\n\n\n```\nsage: %time A._multiply_linbox(A)\n2000 x 2000 dense matrix over Finite Field of size 3\nCPU time: 2.47 s,  Wall time: 2.55 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4258\n\n",
    "created_at": "2008-10-10T08:50:02Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "switch multiplication of dense matrices over finite prime fields to LinBox",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4258",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @ClementPernet @burcin @jasongrout simonking

Keywords: linbox, linear algebra


```
sage: A = random_matrix(GF(3),2000,2000)
sage: %time A*A
2000 x 2000 dense matrix over Finite Field of size 3
CPU time: 14.69 s,  Wall time: 15.08 s
```



```
sage: %time A._multiply_linbox(A)
2000 x 2000 dense matrix over Finite Field of size 3
CPU time: 2.47 s,  Wall time: 2.55 s
```


Issue created by migration from https://trac.sagemath.org/ticket/4258





---

archive/issue_comments_030987.json:
```json
{
    "body": "Just for the record: Burcin came pretty far during SD16 and IIRC Cl\u00e9ment then too over?",
    "created_at": "2009-08-25T19:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30987",
    "user": "@malb"
}
```

Just for the record: Burcin came pretty far during SD16 and IIRC Clément then too over?



---

archive/issue_comments_030988.json:
```json
{
    "body": "Changing component from linear algebra to linbox.",
    "created_at": "2011-08-02T16:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30988",
    "user": "@burcin"
}
```

Changing component from linear algebra to linbox.



---

archive/issue_comments_030989.json:
```json
{
    "body": "see #4260 for ongoing work. Shall we close this as a duplicate?",
    "created_at": "2011-08-02T16:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30989",
    "user": "@burcin"
}
```

see #4260 for ongoing work. Shall we close this as a duplicate?



---

archive/issue_comments_030990.json:
```json
{
    "body": "This is a duplicate of #4260 and should be closed.",
    "created_at": "2011-08-30T15:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30990",
    "user": "@malb"
}
```

This is a duplicate of #4260 and should be closed.



---

archive/issue_comments_030991.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-02T09:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30991",
    "user": "@simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030992.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-02T09:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30992",
    "user": "@simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030993.json:
```json
{
    "body": "Martin suggested to close this ticket as a duplicate of #4260, and I agree. So, I'm inserting Martin as a reviewer and change it into a positive review (with the suggested resolution \"duplicate\").",
    "created_at": "2012-03-02T09:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30993",
    "user": "@simon-king-jena"
}
```

Martin suggested to close this ticket as a duplicate of #4260, and I agree. So, I'm inserting Martin as a reviewer and change it into a positive review (with the suggested resolution "duplicate").



---

archive/issue_comments_030994.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-03-02T13:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4258#issuecomment-30994",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
