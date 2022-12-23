# Issue 9423: Gap interface for number fields

archive/issues_009423.json:
```json
{
    "body": "Assignee: was\n\nKeywords: gap interface number field\n\nOriginally motivated by work on #5618, I found two bugs in the Gap interface for number fields, reported [here](http://groups.google.com/group/sage-devel/browse_thread/thread/6518e7f30c02e534).\n\n#8909 has a positive review and seems partially relevant here, so, I started work with the patch from #8909 applied.\n\nWith the new patch, the following works (and is doctested):\n\n```\nsage: L.<tau> = NumberField(x^3-2)\nsage: gap(tau)^3  # note the exclamation mark used by GAP\n!2\nsage: L(gap(tau)^3) # this used to fail\n2\n```\n\n\n```\nsage: P.<z> = QQ[]  # Note: The var'name is z, not x\nsage: K.<zeta> = NumberField(z^2 - 2)\nsage: k = gap(K)  # this used to fail, as only var'name x was accepted\n```\n\n\nFixing the second problem, it is needed to avoid a conflict with an internal variable name of a GAP function, namely \"E\". This tests that the conflict is indeed avoided:\n\n```\nsage: P.<E> = QQ[]\nsage: L.<tau> = NumberField(E^3-2)\nsage: gap(L)\n<algebraic extension over the Rationals of degree 3>\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9423\n\n",
    "created_at": "2010-07-04T12:18:57Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Gap interface for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9423",
    "user": "SimonKing"
}
```
Assignee: was

Keywords: gap interface number field

Originally motivated by work on #5618, I found two bugs in the Gap interface for number fields, reported [here](http://groups.google.com/group/sage-devel/browse_thread/thread/6518e7f30c02e534).

#8909 has a positive review and seems partially relevant here, so, I started work with the patch from #8909 applied.

With the new patch, the following works (and is doctested):

```
sage: L.<tau> = NumberField(x^3-2)
sage: gap(tau)^3  # note the exclamation mark used by GAP
!2
sage: L(gap(tau)^3) # this used to fail
2
```


```
sage: P.<z> = QQ[]  # Note: The var'name is z, not x
sage: K.<zeta> = NumberField(z^2 - 2)
sage: k = gap(K)  # this used to fail, as only var'name x was accepted
```


Fixing the second problem, it is needed to avoid a conflict with an internal variable name of a GAP function, namely "E". This tests that the conflict is indeed avoided:

```
sage: P.<E> = QQ[]
sage: L.<tau> = NumberField(E^3-2)
sage: gap(L)
<algebraic extension over the Rationals of degree 3>
```



Issue created by migration from https://trac.sagemath.org/ticket/9423





---

archive/issue_comments_089874.json:
```json
{
    "body": "Fixing two bugs (doctested) in the GAP interface of number fields",
    "created_at": "2010-07-04T12:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89874",
    "user": "SimonKing"
}
```

Fixing two bugs (doctested) in the GAP interface of number fields



---

archive/issue_comments_089875.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-04T12:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89875",
    "user": "SimonKing"
}
```

Attachment



---

archive/issue_comments_089876.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-04T12:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89876",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089877.json:
```json
{
    "body": "The code corrects a couple of bugs in the gap interface of number fields. Since ! cannot be part of the name of a generator of a number field, then eliminating \"!\" from the gap representation is correct.\n\nThe solution to the \"E\" variable problem is correct, althought there should be a more system-wide solution to this kind of problems.\n\nI will not give it a positive review until #5618 is also ready to merge, since this patch eliminates a doctest that after #5618 will be obsolete.",
    "created_at": "2010-12-04T15:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89877",
    "user": "lftabera"
}
```

The code corrects a couple of bugs in the gap interface of number fields. Since ! cannot be part of the name of a generator of a number field, then eliminating "!" from the gap representation is correct.

The solution to the "E" variable problem is correct, althought there should be a more system-wide solution to this kind of problems.

I will not give it a positive review until #5618 is also ready to merge, since this patch eliminates a doctest that after #5618 will be obsolete.



---

archive/issue_comments_089878.json:
```json
{
    "body": "Attachment\n\nUpdated headers",
    "created_at": "2010-12-29T14:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89878",
    "user": "lftabera"
}
```

Attachment

Updated headers



---

archive/issue_comments_089879.json:
```json
{
    "body": "Positive review, I have only updated the patch header to add the ticket number\n\nApply: \n\ntrac_9423_gap_for_numberfields.2.patch\n\nNote to the release manager: ticket #5618 depends on this. This ticket should be merged together with #5618.",
    "created_at": "2010-12-29T14:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89879",
    "user": "lftabera"
}
```

Positive review, I have only updated the patch header to add the ticket number

Apply: 

trac_9423_gap_for_numberfields.2.patch

Note to the release manager: ticket #5618 depends on this. This ticket should be merged together with #5618.



---

archive/issue_comments_089880.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-29T14:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89880",
    "user": "lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9423#issuecomment-89881",
    "user": "jdemeyer"
}
```

Resolution: fixed
