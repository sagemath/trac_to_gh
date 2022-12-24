# Issue 8252: names parameter in optimized_representation is tweaked,

archive/issues_008252.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: number fields\n\nHere is a bit of annoyance:\n\n```\nsage: K.<a>=NumberField(x^2+1)\nsage: L.<b>=K.extension(x^2+5)\nsage: Labs.<tau> = L.absolute_field()\nsage: Lnice = Labs.optimized_representation(names='t')\nsage: Lnice[0]\nNumber Field in t3 with defining polynomial x^4 + 3*x^2 + 1\n```\n\n\nWhile the more reasonable output should be \n\n```\nNumber Field in t with defining polynomial x^4 + 3*x^2 + 1\n```\n\n\nI've looked at the code, and the problem is that the helper function that finds the optimized number field calculates all sorts of other fields, and needs to make sure the names don't conflict with each other, so the output makes sense in that front. However, the output is still unexpected for the user. \n\nThere is an obvious hack that can solve this problem (edit Lnice._names before returning from optimized_representation), but I'm not sure if that's the best approach (side effects scare me).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8252\n\n",
    "created_at": "2010-02-12T22:17:51Z",
    "labels": [
        "number fields",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "names parameter in optimized_representation is tweaked,",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8252",
    "user": "@syazdani77"
}
```
Assignee: @loefflerd

Keywords: number fields

Here is a bit of annoyance:

```
sage: K.<a>=NumberField(x^2+1)
sage: L.<b>=K.extension(x^2+5)
sage: Labs.<tau> = L.absolute_field()
sage: Lnice = Labs.optimized_representation(names='t')
sage: Lnice[0]
Number Field in t3 with defining polynomial x^4 + 3*x^2 + 1
```


While the more reasonable output should be 

```
Number Field in t with defining polynomial x^4 + 3*x^2 + 1
```


I've looked at the code, and the problem is that the helper function that finds the optimized number field calculates all sorts of other fields, and needs to make sure the names don't conflict with each other, so the output makes sense in that front. However, the output is still unexpected for the user. 

There is an obvious hack that can solve this problem (edit Lnice._names before returning from optimized_representation), but I'm not sure if that's the best approach (side effects scare me).

Issue created by migration from https://trac.sagemath.org/ticket/8252





---

archive/issue_comments_073008.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-18T05:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8252#issuecomment-73008",
    "user": "@aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073009.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-04-18T05:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8252#issuecomment-73009",
    "user": "@aghitza"
}
```

New commits:



---

archive/issue_comments_073010.json:
```json
{
    "body": "\n```\nsage -t --long src/sage/schemes/elliptic_curves/heegner.py  # 2 doctests failed\n```\n",
    "created_at": "2014-05-20T13:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8252#issuecomment-73010",
    "user": "@rwst"
}
```


```
sage -t --long src/sage/schemes/elliptic_curves/heegner.py  # 2 doctests failed
```




---

archive/issue_comments_073011.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-20T13:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8252#issuecomment-73011",
    "user": "@rwst"
}
```

Changing status from needs_review to needs_work.
