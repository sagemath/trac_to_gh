# Issue 9372: implement regulator function for elliptic curves over number fields

archive/issues_009372.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  robertwb\n\nNow that we have canonical heights over number fields, the regulator_of_points code can be moved up from ell_rational_field to ell_number_field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9372\n\n",
    "created_at": "2010-06-29T04:58:30Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "implement regulator function for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9372",
    "user": "cremona"
}
```
Assignee: AlexGhitza

CC:  robertwb

Now that we have canonical heights over number fields, the regulator_of_points code can be moved up from ell_rational_field to ell_number_field.

Issue created by migration from https://trac.sagemath.org/ticket/9372





---

archive/issue_comments_089056.json:
```json
{
    "body": "Changing component from algebra to elliptic curves.",
    "created_at": "2010-06-29T04:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89056",
    "user": "cremona"
}
```

Changing component from algebra to elliptic curves.



---

archive/issue_comments_089057.json:
```json
{
    "body": "Changing assignee from AlexGhitza to cremona.",
    "created_at": "2010-06-29T04:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89057",
    "user": "cremona"
}
```

Changing assignee from AlexGhitza to cremona.



---

archive/issue_comments_089058.json:
```json
{
    "body": "Applies to 4.4.4",
    "created_at": "2010-06-29T05:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89058",
    "user": "cremona"
}
```

Applies to 4.4.4



---

archive/issue_comments_089059.json:
```json
{
    "body": "Attachment\n\nThe patch moves the two functions height_pairing_matrix and regulator_of_points, and adds doctests over number fields.",
    "created_at": "2010-06-29T05:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89059",
    "user": "cremona"
}
```

Attachment

The patch moves the two functions height_pairing_matrix and regulator_of_points, and adds doctests over number fields.



---

archive/issue_comments_089060.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T05:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89060",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089061.json:
```json
{
    "body": "I'm getting a couple of doctest failures -- something is off by a sign in the `height_pairing_matrix` code:\n\n```\nsage -t -long ell_number_field.py\n**********************************************************************\nFile \"/storage/masiao/sage-4.4.4/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py\", line 308:\n    sage: E.height_pairing_matrix([P,Q])\nExpected:\n    [ 0.686667083305587 -0.268478098806726]\n    [-0.268478098806726  0.327000773651605]\nGot:\n    [0.686667083305587 0.268478098806726]\n    [0.268478098806726 0.327000773651605]\n**********************************************************************\nFile \"/storage/masiao/sage-4.4.4/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py\", line 317:\n    sage: EK.height_pairing_matrix([EK(P),EK(Q)])\nExpected:\n    [ 0.686667083305586 -0.268478098806726]\n    [-0.268478098806726  0.327000773651605]\nGot:\n    [0.686667083305586 0.268478098806726]\n    [0.268478098806726 0.327000773651605]\n**********************************************************************\n1 items had failures:\n   2 of  23 in __main__.example_4\n***Test Failed*** 2 failures.\n```\n\n\nAlso, a very tiny quibble: the second argument \"precision\" to `height_pairing_matrix` is missing its bullet point in the docstring.",
    "created_at": "2010-06-29T13:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89061",
    "user": "davidloeffler"
}
```

I'm getting a couple of doctest failures -- something is off by a sign in the `height_pairing_matrix` code:

```
sage -t -long ell_number_field.py
**********************************************************************
File "/storage/masiao/sage-4.4.4/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py", line 308:
    sage: E.height_pairing_matrix([P,Q])
Expected:
    [ 0.686667083305587 -0.268478098806726]
    [-0.268478098806726  0.327000773651605]
Got:
    [0.686667083305587 0.268478098806726]
    [0.268478098806726 0.327000773651605]
**********************************************************************
File "/storage/masiao/sage-4.4.4/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py", line 317:
    sage: EK.height_pairing_matrix([EK(P),EK(Q)])
Expected:
    [ 0.686667083305586 -0.268478098806726]
    [-0.268478098806726  0.327000773651605]
Got:
    [0.686667083305586 0.268478098806726]
    [0.268478098806726 0.327000773651605]
**********************************************************************
1 items had failures:
   2 of  23 in __main__.example_4
***Test Failed*** 2 failures.
```


Also, a very tiny quibble: the second argument "precision" to `height_pairing_matrix` is missing its bullet point in the docstring.



---

archive/issue_comments_089062.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-29T13:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89062",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089063.json:
```json
{
    "body": "Probably I used E.gens() which is a bad idea in odctests, better to enter the points manually.\n\nNo time to fix now, about to leave SD22 for home.... but thanks all the same!  Put this patch up from a coffee shop last night just before it closed (about a dozen Sagers being chased out!)",
    "created_at": "2010-06-29T14:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89063",
    "user": "cremona"
}
```

Probably I used E.gens() which is a bad idea in odctests, better to enter the points manually.

No time to fix now, about to leave SD22 for home.... but thanks all the same!  Put this patch up from a coffee shop last night just before it closed (about a dozen Sagers being chased out!)



---

archive/issue_comments_089064.json:
```json
{
    "body": "`@`cremona: You did you E.gens().  I get:\n\n```\nsage: E = EllipticCurve('389a1')\nsage: E.gens()\n[(-1 : 1 : 1), (0 : -1 : 1)]\n```\n\n\nShould I change the doc test to the following?\n\n\n```\nsage: E = EllipticCurve('389a1')\nsage: P,Q = E.point([-1,1,1]),E.point([0,-1,1])\nsage: E.height_pairing_matrix([P,Q])\n[0.686667083305587 0.268478098806726]\n[0.268478098806726 0.327000773651605]\n```\n\n\n}}}",
    "created_at": "2010-06-29T23:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89064",
    "user": "aly.deines"
}
```

`@`cremona: You did you E.gens().  I get:

```
sage: E = EllipticCurve('389a1')
sage: E.gens()
[(-1 : 1 : 1), (0 : -1 : 1)]
```


Should I change the doc test to the following?


```
sage: E = EllipticCurve('389a1')
sage: P,Q = E.point([-1,1,1]),E.point([0,-1,1])
sage: E.height_pairing_matrix([P,Q])
[0.686667083305587 0.268478098806726]
[0.268478098806726 0.327000773651605]
```


}}}



---

archive/issue_comments_089065.json:
```json
{
    "body": "doctest fixed -- replaces previous patch",
    "created_at": "2010-06-30T03:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89065",
    "user": "aly.deines"
}
```

doctest fixed -- replaces previous patch



---

archive/issue_comments_089066.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T03:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89066",
    "user": "aly.deines"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089067.json:
```json
{
    "body": "Attachment\n\nIf the only problem was that the doctest called E.gens(), this fixes those doctests and you can give this a positive review.",
    "created_at": "2010-06-30T03:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89067",
    "user": "aly.deines"
}
```

Attachment

If the only problem was that the doctest called E.gens(), this fixes those doctests and you can give this a positive review.



---

archive/issue_comments_089068.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-30T07:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89068",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089069.json:
```json
{
    "body": "Thanks to all for sorting that out.  I should have known better.  Even for curves in the database, it is not safe to use gens() since unless you have the larger database installed the gens are computed on the fly and are not unique.  (And doctests definitely should not assume an optional spkg is installed!).",
    "created_at": "2010-06-30T11:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89069",
    "user": "cremona"
}
```

Thanks to all for sorting that out.  I should have known better.  Even for curves in the database, it is not safe to use gens() since unless you have the larger database installed the gens are computed on the fly and are not unique.  (And doctests definitely should not assume an optional spkg is installed!).



---

archive/issue_comments_089070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89070",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_089071.json:
```json
{
    "body": "I'm updating the Reviewer(s) field.  Please correct me if I'm wrong.",
    "created_at": "2010-07-20T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9372#issuecomment-89071",
    "user": "mpatel"
}
```

I'm updating the Reviewer(s) field.  Please correct me if I'm wrong.
