# Issue 2907: polynomials lack content method

archive/issues_002907.json:
```json
{
    "body": "Assignee: somebody\n\nATM, there is no efficient way of getting the content of a polynomial in Sage.\n\n\n```\ngcd(p.list())\n```\n\n\nis a workaround, but this can be done much more efficiently.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2907\n\n",
    "created_at": "2008-04-13T17:46:06Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "polynomials lack content method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2907",
    "user": "https://github.com/burcin"
}
```
Assignee: somebody

ATM, there is no efficient way of getting the content of a polynomial in Sage.


```
gcd(p.list())
```


is a workaround, but this can be done much more efficiently.

Issue created by migration from https://trac.sagemath.org/ticket/2907





---

archive/issue_comments_019993.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19993",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_019994.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-17T11:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19994",
    "user": "https://github.com/bgrenet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019995.json:
```json
{
    "body": "That is not true anymore!\n\n\n```python\nsage: R.<x> = ZZ[]\nsage: p = R.random_element(10)\nsage: p.content()\n1\nsage: p *= 13\nsage: p.content()\n13\n```\n\n\n(There is a consistency problem though between different implementations of `content()`, see #16613, but this ticket can be closed now I think.)",
    "created_at": "2014-12-17T11:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19995",
    "user": "https://github.com/bgrenet"
}
```

That is not true anymore!


```python
sage: R.<x> = ZZ[]
sage: p = R.random_element(10)
sage: p.content()
1
sage: p *= 13
sage: p.content()
13
```


(There is a consistency problem though between different implementations of `content()`, see #16613, but this ticket can be closed now I think.)



---

archive/issue_comments_019996.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-19T15:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19996",
    "user": "https://github.com/bgrenet"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019997.json:
```json
{
    "body": "one still needs to fill in the names of the author(s) and reviewer(s), IMHO",
    "created_at": "2014-12-19T15:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19997",
    "user": "https://github.com/dimpase"
}
```

one still needs to fill in the names of the author(s) and reviewer(s), IMHO



---

archive/issue_comments_019998.json:
```json
{
    "body": "Technically the one who sets the ticket to invalid should not set it to a positive review (as a \"review\"), but usually it's okay because things like this are non-controversial.",
    "created_at": "2014-12-20T00:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19998",
    "user": "https://github.com/tscrim"
}
```

Technically the one who sets the ticket to invalid should not set it to a positive review (as a "review"), but usually it's okay because things like this are non-controversial.



---

archive/issue_comments_019999.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2907#issuecomment-19999",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
