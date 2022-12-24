# Issue 9926: non-squarefree Hecke operators on BrandtModule

archive/issues_009926.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: brandt module, hecke operator\n\nThis was reported by Nicol\u00e1s Sirolli on sage-nt:\n\n\n`BrandtModule` has a problem when calculating the n-th Hecke operator\nwhen n is not squarefree, and is smaller than the prime where the\nalgebra ramifies.\n\nFor example, I get a \"not implemented\" error if I run this\n\n\n```\nsage: B=BrandtModule(13)\nsage: B.hecke_matrix(4)\n```\n\n\nGonzalo Tornar\u00eda told me that the 'direct' algorithm is not\nimplemented when n is not squarefree; hence I found that\n\n\n```\nsage: B.hecke_matrix(4,algorithm='brandt')\n```\n\n\ninstead, there is no trouble. A workaround could be (I'm not sure\nwhether this is the best to do) changing line 852 of brandt.py,\n\n\n```\nif self.level().gcd(n) != 1:\n```\n\n\nfor\n\n\n```\nif self.level().gcd(n) != 1 or is_squarefree(n)==False:\n```\n\n\n(and adding `is_squarefree` to the \"imports\" block).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9927\n\n",
    "created_at": "2010-09-17T01:19:51Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "non-squarefree Hecke operators on BrandtModule",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9926",
    "user": "@aghitza"
}
```
Assignee: @craigcitro

Keywords: brandt module, hecke operator

This was reported by Nicolás Sirolli on sage-nt:


`BrandtModule` has a problem when calculating the n-th Hecke operator
when n is not squarefree, and is smaller than the prime where the
algebra ramifies.

For example, I get a "not implemented" error if I run this


```
sage: B=BrandtModule(13)
sage: B.hecke_matrix(4)
```


Gonzalo Tornaría told me that the 'direct' algorithm is not
implemented when n is not squarefree; hence I found that


```
sage: B.hecke_matrix(4,algorithm='brandt')
```


instead, there is no trouble. A workaround could be (I'm not sure
whether this is the best to do) changing line 852 of brandt.py,


```
if self.level().gcd(n) != 1:
```


for


```
if self.level().gcd(n) != 1 or is_squarefree(n)==False:
```


(and adding `is_squarefree` to the "imports" block).


Issue created by migration from https://trac.sagemath.org/ticket/9927





---

archive/issue_comments_098856.json:
```json
{
    "body": "The reason why the 'direct' algorithm is broken for non-squarefree n is that the base class `AmbientHeckeModule` needs to know the character of the modular form.\n\nSince the `BrandtModule` corresponds to modular forms with trivial character, a fix is to just implement the character() method returning a trivial character.",
    "created_at": "2014-08-25T22:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98856",
    "user": "@tornaria"
}
```

The reason why the 'direct' algorithm is broken for non-squarefree n is that the base class `AmbientHeckeModule` needs to know the character of the modular form.

Since the `BrandtModule` corresponds to modular forms with trivial character, a fix is to just implement the character() method returning a trivial character.



---

archive/issue_comments_098857.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-25T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98857",
    "user": "@tornaria"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098858.json:
```json
{
    "body": "This fix solves the problem and (unlike the one proposed by me) is reasonable. All tests run fine.\n\nIt would be nice to include, in the hecke_matrix method, an example of a n-th Hecke matrix with non-squarefree n.",
    "created_at": "2014-12-29T14:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98858",
    "user": "@nsirolli"
}
```

This fix solves the problem and (unlike the one proposed by me) is reasonable. All tests run fine.

It would be nice to include, in the hecke_matrix method, an example of a n-th Hecke matrix with non-squarefree n.



---

archive/issue_comments_098859.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-29T14:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98859",
    "user": "@nsirolli"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098860.json:
```json
{
    "body": "Author/Reviewer name should be real names, not trac usernames.",
    "created_at": "2015-01-02T15:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98860",
    "user": "@vbraun"
}
```

Author/Reviewer name should be real names, not trac usernames.



---

archive/issue_comments_098861.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2015-01-02T15:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98861",
    "user": "@vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_098862.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-01-02T15:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98862",
    "user": "@nsirolli"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_098863.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-04T12:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9926#issuecomment-98863",
    "user": "@vbraun"
}
```

Resolution: fixed
