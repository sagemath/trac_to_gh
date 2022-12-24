# Issue 7348: speed up computation of multiplicative orders of finite field elements

archive/issues_007348.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  slelievre\n\nKeywords: Finite Field\n\nThe function `sage.rings.finite_field_element.multiplicative_order` should use\n`sage.groups.generic.order_from_multiple` (see the example in #7324), and \nthe factorization of the order of the multiplicative group of the field \nshould be cached; see the documentation for `order_from_multiple`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7348\n\n",
    "created_at": "2009-10-29T10:01:10Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "speed up computation of multiplicative orders of finite field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7348",
    "user": "fwclarke"
}
```
Assignee: tbd

CC:  slelievre

Keywords: Finite Field

The function `sage.rings.finite_field_element.multiplicative_order` should use
`sage.groups.generic.order_from_multiple` (see the example in #7324), and 
the factorization of the order of the multiplicative group of the field 
should be cached; see the documentation for `order_from_multiple`.

Issue created by migration from https://trac.sagemath.org/ticket/7348





---

archive/issue_comments_061573.json:
```json
{
    "body": "Changing keywords from \"Finite Field\" to \"finite field\".",
    "created_at": "2021-03-20T00:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7348#issuecomment-61573",
    "user": "slelievre"
}
```

Changing keywords from "Finite Field" to "finite field".



---

archive/issue_comments_061574.json:
```json
{
    "body": "Changing component from algebra to finite rings.",
    "created_at": "2021-03-20T00:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7348#issuecomment-61574",
    "user": "slelievre"
}
```

Changing component from algebra to finite rings.
