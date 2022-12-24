# Issue 5746: rational points over subfields of the (finite) field of definition

archive/issues_005746.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: rational points finite field\n\nRight now, if X is a scheme over a finite field F and we ask for the list of rational points over a subfield K of F, Sage raises an error because it tries to base change X to K first.\n\nIt would be very easy to implement this as follows: take the list of all rational points over F and find the ones that are fixed by the appropriate power of the Frobenius morphism.  These are then the K-rational points.\n\nA sample of what this would return:\n\n\n```\nsage: P = ProjectiveSpace(1, GF(3^2, 'b'))\nsage: P.rational_points()\n[(0 : 1),\n (2*b : 1),\n (b + 1 : 1),\n (b + 2 : 1),\n (2 : 1),\n (b : 1),\n (2*b + 2 : 1),\n (2*b + 1 : 1),\n (1 : 1),\n (1 : 0)]\nsage: P.rational_points(GF(3))  # this doesn't work right now\n[(0 : 1),\n (2 : 1),\n (1 : 1),\n (1 : 0)]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5746\n\n",
    "created_at": "2009-04-11T05:08:48Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rational points over subfields of the (finite) field of definition",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5746",
    "user": "@aghitza"
}
```
Assignee: @williamstein

Keywords: rational points finite field

Right now, if X is a scheme over a finite field F and we ask for the list of rational points over a subfield K of F, Sage raises an error because it tries to base change X to K first.

It would be very easy to implement this as follows: take the list of all rational points over F and find the ones that are fixed by the appropriate power of the Frobenius morphism.  These are then the K-rational points.

A sample of what this would return:


```
sage: P = ProjectiveSpace(1, GF(3^2, 'b'))
sage: P.rational_points()
[(0 : 1),
 (2*b : 1),
 (b + 1 : 1),
 (b + 2 : 1),
 (2 : 1),
 (b : 1),
 (2*b + 2 : 1),
 (2*b + 1 : 1),
 (1 : 1),
 (1 : 0)]
sage: P.rational_points(GF(3))  # this doesn't work right now
[(0 : 1),
 (2 : 1),
 (1 : 1),
 (1 : 0)]
```



Issue created by migration from https://trac.sagemath.org/ticket/5746





---

archive/issue_comments_044921.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-05-05T07:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44921",
    "user": "@aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_044922.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-05T07:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44922",
    "user": "@aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044923.json:
```json
{
    "body": "Is this mathematically correct? In terms of categories of schemes, X/F has no K-points, because K is not in the category of F-schemes.",
    "created_at": "2009-05-21T02:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44923",
    "user": "@antieau"
}
```

Is this mathematically correct? In terms of categories of schemes, X/F has no K-points, because K is not in the category of F-schemes.



---

archive/issue_comments_044924.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-08T04:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44924",
    "user": "@koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044925.json:
```json
{
    "body": "I indeed think this should not be done since this is mathematically incorrect even in the broader category of schemes. \n\nBy definition X has a morphism to spec F since it is an F scheme and if X would have a spec K point then we would get a morphism from spec K to spec F which is not possible since this would give is a field map from F to K.\n\nIf X does happen to be the base change of some X' from K to F and a user wants the K rational points of X', then I think it is good to force the user to construct X' explicitly. This is because it is not necessarily unique (sometimes one can twist X') nor does X' need to exist.\n\nI am putting it up for review so it can be closed as won't fix.",
    "created_at": "2017-09-08T04:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44925",
    "user": "@koffie"
}
```

I indeed think this should not be done since this is mathematically incorrect even in the broader category of schemes. 

By definition X has a morphism to spec F since it is an F scheme and if X would have a spec K point then we would get a morphism from spec K to spec F which is not possible since this would give is a field map from F to K.

If X does happen to be the base change of some X' from K to F and a user wants the K rational points of X', then I think it is good to force the user to construct X' explicitly. This is because it is not necessarily unique (sometimes one can twist X') nor does X' need to exist.

I am putting it up for review so it can be closed as won't fix.



---

archive/issue_comments_044926.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-09-08T05:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44926",
    "user": "@pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044927.json:
```json
{
    "body": "Asking for points over a subfield of the field of definition is indeed not well defined and trying to implement this would probably only cause confusion.",
    "created_at": "2017-09-08T05:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44927",
    "user": "@pjbruin"
}
```

Asking for points over a subfield of the field of definition is indeed not well defined and trying to implement this would probably only cause confusion.



---

archive/issue_comments_044928.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-09-25T13:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5746#issuecomment-44928",
    "user": "@koffie"
}
```

Resolution: wontfix
