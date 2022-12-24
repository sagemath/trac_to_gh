# Issue 6335: optional doctest failure -- kash interface (trivial to fix)

archive/issues_006335.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/interfaces/kash.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/kash.py\", line 68:\n    sage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash\nExpected nothing\nGot:\n    22\n**********************************************************************\n1 items had failures:\n   1 of 103 in __main__.example_0\n***Test Failed*** 1 failures.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6335\n\n",
    "created_at": "2009-06-16T15:18:16Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "optional doctest failure -- kash interface (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6335",
    "user": "was"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/interfaces/kash.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/kash.py", line 68:
    sage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash
Expected nothing
Got:
    22
**********************************************************************
1 items had failures:
   1 of 103 in __main__.example_0
***Test Failed*** 1 failures.

```


Issue created by migration from https://trac.sagemath.org/ticket/6335





---

archive/issue_comments_050566.json:
```json
{
    "body": "On my Sage 5.7.beta4, all tests pass. \n\n\n```\nsage -t  \"devel/sage-main/sage/interfaces/kash.py\"          \n\t [17.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 17.4 seconds\n```\n\n\nSo, I am marking this invalid.",
    "created_at": "2013-02-18T21:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6335#issuecomment-50566",
    "user": "knsam"
}
```

On my Sage 5.7.beta4, all tests pass. 


```
sage -t  "devel/sage-main/sage/interfaces/kash.py"          
	 [17.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.4 seconds
```


So, I am marking this invalid.



---

archive/issue_comments_050567.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-18T21:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6335#issuecomment-50567",
    "user": "knsam"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050568.json:
```json
{
    "body": "Oops!! There are two optional tests failing now!! So, not invalid.",
    "created_at": "2013-02-18T21:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6335#issuecomment-50568",
    "user": "knsam"
}
```

Oops!! There are two optional tests failing now!! So, not invalid.



---

archive/issue_comments_050569.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-02-18T21:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6335#issuecomment-50569",
    "user": "knsam"
}
```

Changing status from needs_review to needs_work.
