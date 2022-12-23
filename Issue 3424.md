# Issue 3424: jordan_form gives incorrect results due to imprecise roots

archive/issues_003424.json:
```json
{
    "body": "Assignee: was\n\nmat.jordan_form(CDF) gives the wrong Jordan form for some matrices because mat.charpoly().roots() sometimes gives separate roots when it should give a single root. Attached is a patch that adds a new parameter to jordan_form so that users can specify a number of digits of rounding to the roots of the characteristic polynomial.\n\n\n```\nsage: m                            \n\n[1 1]\n[0 1]\nsage: m.jordan_form()              \n\n[1 1]\n[0 1]\nsage: m.jordan_form(CDF)\n\n[1.0|  0]\n[---+---]\n[  0|1.0]\nsage: m.jordan_form(CDF, digits=2)\n\n[1.0 1.0]\n[  0 1.0]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3424\n\n",
    "created_at": "2008-06-14T20:17:47Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "jordan_form gives incorrect results due to imprecise roots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3424",
    "user": "johnwilmes"
}
```
Assignee: was

mat.jordan_form(CDF) gives the wrong Jordan form for some matrices because mat.charpoly().roots() sometimes gives separate roots when it should give a single root. Attached is a patch that adds a new parameter to jordan_form so that users can specify a number of digits of rounding to the roots of the characteristic polynomial.


```
sage: m                            

[1 1]
[0 1]
sage: m.jordan_form()              

[1 1]
[0 1]
sage: m.jordan_form(CDF)

[1.0|  0]
[---+---]
[  0|1.0]
sage: m.jordan_form(CDF, digits=2)

[1.0 1.0]
[  0 1.0]
```


Issue created by migration from https://trac.sagemath.org/ticket/3424





---

archive/issue_comments_024093.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-14T20:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24093",
    "user": "johnwilmes"
}
```

Attachment



---

archive/issue_comments_024094.json:
```json
{
    "body": "I think that rounding is a bad way to do this... this would not merge roots 1.44999999 and 1.450000001, but would merge 1.45000001 and 1.549999999.  It would be better to specify some sort of relative error.",
    "created_at": "2008-06-15T06:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24094",
    "user": "cwitty"
}
```

I think that rounding is a bad way to do this... this would not merge roots 1.44999999 and 1.450000001, but would merge 1.45000001 and 1.549999999.  It would be better to specify some sort of relative error.



---

archive/issue_comments_024095.json:
```json
{
    "body": "I'm not sure I follow you. Using the rounding method from the patch:\n\n```\nsage: def do_round(eval, digits):\n....:     eval = CDF(eval) \n....:     r = CDF(round(eval.real(), digits), round(eval.imag(), digits))\n....:     return r\n....: \nsage: do_round(1.44999999, 3)\n1.45\nsage: do_round(1.45000001, 3)\n1.45\nsage: do_round(1.54999999, 3)\n1.55\n```\n\n\nThis seems to be the desired behavior.",
    "created_at": "2008-06-15T07:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24095",
    "user": "johnwilmes"
}
```

I'm not sure I follow you. Using the rounding method from the patch:

```
sage: def do_round(eval, digits):
....:     eval = CDF(eval) 
....:     r = CDF(round(eval.real(), digits), round(eval.imag(), digits))
....:     return r
....: 
sage: do_round(1.44999999, 3)
1.45
sage: do_round(1.45000001, 3)
1.45
sage: do_round(1.54999999, 3)
1.55
```


This seems to be the desired behavior.



---

archive/issue_comments_024096.json:
```json
{
    "body": "It depends on how many digits you round to.\n\n```\nsage: do_round(1.44999999, 1)\n1.4\nsage: do_round(1.45000001, 1)\n1.5\nsage: do_round(1.54999999, 1)\n1.5\nsage: 1.45000001 - 1.44999999\n1.99999998784506e-8\nsage: 1.54999999 - 1.45000001\n0.0999999800000002\n```\n\n\nHere the first and second numbers round differently, even though they differ by about 2e-8; and the second and third numbers round the same, even though they differ by about 0.1.  Similar examples could be found for rounding to any number of digits.",
    "created_at": "2008-06-15T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24096",
    "user": "cwitty"
}
```

It depends on how many digits you round to.

```
sage: do_round(1.44999999, 1)
1.4
sage: do_round(1.45000001, 1)
1.5
sage: do_round(1.54999999, 1)
1.5
sage: 1.45000001 - 1.44999999
1.99999998784506e-8
sage: 1.54999999 - 1.45000001
0.0999999800000002
```


Here the first and second numbers round differently, even though they differ by about 2e-8; and the second and third numbers round the same, even though they differ by about 0.1.  Similar examples could be found for rounding to any number of digits.



---

archive/issue_comments_024097.json:
```json
{
    "body": "Replying to [comment:4 cwitty]:\n> It depends on how many digits you round to.\n\nI see what you mean now, and that does seem like a significant problem. However, I can't see a way of using the distance between roots without using a more complicated clustering algorithm that introduces its own problems. So for example, suppose we start with the roots 1.45, 1.50, and 1.55, and the user specifies an error tolerance of 0.05. It's not clear to be what the correct way to group the roots would be. Do we treat them all as the same root? Do we arbitrarily put them into two different categories, or leave them all separate?",
    "created_at": "2008-06-20T00:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24097",
    "user": "johnwilmes"
}
```

Replying to [comment:4 cwitty]:
> It depends on how many digits you round to.

I see what you mean now, and that does seem like a significant problem. However, I can't see a way of using the distance between roots without using a more complicated clustering algorithm that introduces its own problems. So for example, suppose we start with the roots 1.45, 1.50, and 1.55, and the user specifies an error tolerance of 0.05. It's not clear to be what the correct way to group the roots would be. Do we treat them all as the same root? Do we arbitrarily put them into two different categories, or leave them all separate?



---

archive/issue_comments_024098.json:
```json
{
    "body": "Or we can just throw a numerical precision warning that says that the jordan form is pretty much nonsense when computing with imprecise numbers.  I don't know if there is an easy way to get around the issue you are point out.\n\nMaybe one way to do it would be to surround each root with an interval with radius = your tolerance.  If two roots intersect, then consider them the same.  This might lead to problems, but in the end, I think it will be more helpful than hurtful.  I'd also put out the warning that the results probably are nonsense because of numerical issues.",
    "created_at": "2008-11-14T05:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24098",
    "user": "jason"
}
```

Or we can just throw a numerical precision warning that says that the jordan form is pretty much nonsense when computing with imprecise numbers.  I don't know if there is an easy way to get around the issue you are point out.

Maybe one way to do it would be to surround each root with an interval with radius = your tolerance.  If two roots intersect, then consider them the same.  This might lead to problems, but in the end, I think it will be more helpful than hurtful.  I'd also put out the warning that the results probably are nonsense because of numerical issues.



---

archive/issue_comments_024099.json:
```json
{
    "body": "in other words, in the extreme case you point out, group all the roots as the same.  In practice, people should not be specifying intervals that large.  In practice, I don't think you will see a huge chain of roots that are all within some tolerance of their neighbors (for reasonable tolerances).",
    "created_at": "2008-11-14T05:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24099",
    "user": "jason"
}
```

in other words, in the extreme case you point out, group all the roots as the same.  In practice, people should not be specifying intervals that large.  In practice, I don't think you will see a huge chain of roots that are all within some tolerance of their neighbors (for reasonable tolerances).



---

archive/issue_comments_024100.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-06-08T15:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24100",
    "user": "johnwilmes"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_024101.json:
```json
{
    "body": "I thought I should finally take care of this, but now (8 years later) sage very sensibly refuses to compute Jordan forms over inexact fields. So the \"defect\" is no longer present, and I guess this can be closed? (Or if anyone actually wants this over inexact fields, I can submit a new patch...)",
    "created_at": "2016-06-08T15:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24101",
    "user": "johnwilmes"
}
```

I thought I should finally take care of this, but now (8 years later) sage very sensibly refuses to compute Jordan forms over inexact fields. So the "defect" is no longer present, and I guess this can be closed? (Or if anyone actually wants this over inexact fields, I can submit a new patch...)



---

archive/issue_comments_024102.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2016-08-22T13:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24102",
    "user": "rws"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_024103.json:
```json
{
    "body": "Setting to needs_info because no code is to be reviewed.",
    "created_at": "2016-08-22T13:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3424#issuecomment-24103",
    "user": "rws"
}
```

Setting to needs_info because no code is to be reviewed.
