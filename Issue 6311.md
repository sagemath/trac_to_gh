# Issue 6311: optional doctest failure -- supersingular_j

archive/issues_006311.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/modular/ssmod/ssmod.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modular/ssmod/ssmod.py\", line 571:\n    sage: supersingular_j(GF(15073^2,'a'))  # optional -- requires database\nExpected:\n    10630*a + 6033\nGot:\n    4443*a + 13964\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_ssmod.py\n\t [20.9 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6311\n\n",
    "created_at": "2009-06-16T14:40:29Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- supersingular_j",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6311",
    "user": "@williamstein"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/modular/ssmod/ssmod.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modular/ssmod/ssmod.py", line 571:
    sage: supersingular_j(GF(15073^2,'a'))  # optional -- requires database
Expected:
    10630*a + 6033
Got:
    4443*a + 13964
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_ssmod.py
	 [20.9 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6311





---

archive/issue_comments_050369.json:
```json
{
    "body": "This failure is still there in 5.12.beta4.\n\nThe results are related by the action of the Frobenius involution. So the problem is not too bad.",
    "created_at": "2013-09-21T12:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50369",
    "user": "@fchapoton"
}
```

This failure is still there in 5.12.beta4.

The results are related by the action of the Frobenius involution. So the problem is not too bad.



---

archive/issue_comments_050370.json:
```json
{
    "body": "Now the doctest is\n\n```\nsage -t --optional=all src/sage/modular/ssmod/ssmod.py\n```\n",
    "created_at": "2014-02-21T13:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50370",
    "user": "@fchapoton"
}
```

Now the doctest is

```
sage -t --optional=all src/sage/modular/ssmod/ssmod.py
```




---

archive/issue_comments_050371.json:
```json
{
    "body": "what should we do here ? just change the doctest result ?",
    "created_at": "2015-03-24T20:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50371",
    "user": "@fchapoton"
}
```

what should we do here ? just change the doctest result ?



---

archive/issue_comments_050372.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2015-03-24T20:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50372",
    "user": "@fchapoton"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_050373.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-03-24T22:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50373",
    "user": "@jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_050374.json:
```json
{
    "body": "Changing component from packages: optional to doctest framework.",
    "created_at": "2015-03-24T22:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50374",
    "user": "@jdemeyer"
}
```

Changing component from packages: optional to doctest framework.



---

archive/issue_comments_050375.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-03-24T22:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50375",
    "user": "@jdemeyer"
}
```

New commits:



---

archive/issue_comments_050376.json:
```json
{
    "body": "Remove `# optional` in #18049.",
    "created_at": "2015-03-24T22:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50376",
    "user": "@jdemeyer"
}
```

Remove `# optional` in #18049.



---

archive/issue_comments_050377.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-24T23:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50377",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050378.json:
```json
{
    "body": "Changing component from doctest framework to number theory.",
    "created_at": "2015-03-24T23:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50378",
    "user": "@jdemeyer"
}
```

Changing component from doctest framework to number theory.



---

archive/issue_comments_050379.json:
```json
{
    "body": "I think we can just close this as \"duplicate\" of #18049.",
    "created_at": "2015-03-24T23:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50379",
    "user": "@jdemeyer"
}
```

I think we can just close this as "duplicate" of #18049.



---

archive/issue_comments_050380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-24T23:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50380",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050381.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-03-25T00:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6311#issuecomment-50381",
    "user": "@vbraun"
}
```

Resolution: duplicate
