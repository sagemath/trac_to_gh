# Issue 7917: [with patch, needs review] make gauss_sum() work for dirichlet characters when the base ring is CC

archive/issues_007917.json:
```json
{
    "body": "Assignee: was\n\nCC:  rishi\n\nKeywords: dirichlet character gauss sum\n\nThis is a pretty small change. We add three lines to gauss_sum_numerical() to make it work when the base ring is a complex field, and change gauss_sum() to call gauss_sum_numerical() when the base ring is a complex field.\n\nNote that it is actually much faster to compute the (approximate) gauss sum when the base ring is CC, as compared to when the base ring is a cyclotomic field.\n\n\n\n```\nsage: G = DirichletGroup(2981)\nsage: chi = G.0\nsage: timeit('chi.gauss_sum_numerical()')\n5 loops, best of 3: 1.82 s per loop\nsage: G = DirichletGroup(2981, ComplexField(200))\nsage: chi = G.0                                  \nsage: timeit('chi.gauss_sum_numerical()')        \n25 loops, best of 3: 23.5 ms per loop\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7917\n\n",
    "created_at": "2010-01-13T06:22:56Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] make gauss_sum() work for dirichlet characters when the base ring is CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7917",
    "user": "bober"
}
```
Assignee: was

CC:  rishi

Keywords: dirichlet character gauss sum

This is a pretty small change. We add three lines to gauss_sum_numerical() to make it work when the base ring is a complex field, and change gauss_sum() to call gauss_sum_numerical() when the base ring is a complex field.

Note that it is actually much faster to compute the (approximate) gauss sum when the base ring is CC, as compared to when the base ring is a cyclotomic field.



```
sage: G = DirichletGroup(2981)
sage: chi = G.0
sage: timeit('chi.gauss_sum_numerical()')
5 loops, best of 3: 1.82 s per loop
sage: G = DirichletGroup(2981, ComplexField(200))
sage: chi = G.0                                  
sage: timeit('chi.gauss_sum_numerical()')        
25 loops, best of 3: 23.5 ms per loop
```



Issue created by migration from https://trac.sagemath.org/ticket/7917





---

archive/issue_comments_068892.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-02T21:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68892",
    "user": "rishi"
}
```

Attachment



---

archive/issue_comments_068893.json:
```json
{
    "body": "Should this be marked as needs review?",
    "created_at": "2012-09-17T05:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68893",
    "user": "roed"
}
```

Should this be marked as needs review?



---

archive/issue_comments_068894.json:
```json
{
    "body": "This is superseded by #7191; I propose to close this as a duplicate.  There is only one small problem, namely that in the lines\n\n```python\nif rings.is_ComplexField(K):\n    return self.gauss_sum_numerical(a=a)\n```\n\nthe argument `a` was omitted in #7191.  This will be fixed in #19056.",
    "created_at": "2015-08-19T14:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68894",
    "user": "pbruin"
}
```

This is superseded by #7191; I propose to close this as a duplicate.  There is only one small problem, namely that in the lines

```python
if rings.is_ComplexField(K):
    return self.gauss_sum_numerical(a=a)
```

the argument `a` was omitted in #7191.  This will be fixed in #19056.



---

archive/issue_comments_068895.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-08-19T14:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68895",
    "user": "pbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068896.json:
```json
{
    "body": "Now that #19056 is closed, I see no reason to keep this ticket open.",
    "created_at": "2015-09-07T11:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68896",
    "user": "pbruin"
}
```

Now that #19056 is closed, I see no reason to keep this ticket open.



---

archive/issue_comments_068897.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-07T11:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68897",
    "user": "pbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068898.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2015-09-12T13:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7917#issuecomment-68898",
    "user": "vbraun"
}
```

Resolution: invalid
