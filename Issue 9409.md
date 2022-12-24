# Issue 9409: Bug in elliptic curves method .count_points() over finite fields

archive/issues_009409.json:
```json
{
    "body": "Assignee: cremona\n\nKeywords: Elliptic Curves .count_points()\n\nThere is some bug in the method .count_points() which belongs to elliptic curves defined over finite fields. This might be specific to EC defined over number fields - I only get this error when I take an EC over a number field, reduce at a good prime and then count points. In fact, I get the correct answer the first time, but if I define a second EC over a possibly different number field and count points at a good reduction, then the method .count_points() fails. I suspect this has to do with the cacheing...\n\nIf you want to reproduce the behavior, try the following code:\n\n\n### this just runs through the method outlined above:\n\ndef test(curve, bound):\n    for i in primes(bound):\n        print \"Checking primes over %d:        \"%i\n        factors = curve.base_field().ideal(i).factor()\n        for j in range(len(factors)):\n            if  curve.has_good_reduction(factors[j][0]):\n                if factors[j][0].divides(curve.discriminant()):\n                    print \"Curve has good reduction, but this isn't not a minimal model\",\n                    print \"at %s with %d points in the reduced curve\"%(factors[j][0], curve.local_minimal_model(factors[j][0]).reduction(factors[j][0]).count_points() )\n                else:                 \n                    print \"Curve has good reduction and is a minimal model\"\n                    print \"at %s with %d points in the reduced curve\"%(factors[j][0],  curve.reduction(factors[j][0]).count_points() )\n            else:\n                print \"Curve has bad reduction over %s\"%factors[j][0]\n    return\n\n\n### sample 1\nK.<t> = NumberField(x^2 + 1); E = EllipticCurve(K, [0, 1, 0, -2*t - 2, 2*t]); E\n### sample 2\nL.<u> = NumberField(x^2 - 2); F = EllipticCurve(L, [0,2,0, 2*u +4, 2*u + 3]); F\n\ntest(E, 100)\n\n## now the error will happen\ntest(F, 100)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9409\n\n",
    "created_at": "2010-07-02T16:23:51Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Bug in elliptic curves method .count_points() over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9409",
    "user": "adam"
}
```
Assignee: cremona

Keywords: Elliptic Curves .count_points()

There is some bug in the method .count_points() which belongs to elliptic curves defined over finite fields. This might be specific to EC defined over number fields - I only get this error when I take an EC over a number field, reduce at a good prime and then count points. In fact, I get the correct answer the first time, but if I define a second EC over a possibly different number field and count points at a good reduction, then the method .count_points() fails. I suspect this has to do with the cacheing...

If you want to reproduce the behavior, try the following code:


### this just runs through the method outlined above:

def test(curve, bound):
    for i in primes(bound):
        print "Checking primes over %d:        "%i
        factors = curve.base_field().ideal(i).factor()
        for j in range(len(factors)):
            if  curve.has_good_reduction(factors[j][0]):
                if factors[j][0].divides(curve.discriminant()):
                    print "Curve has good reduction, but this isn't not a minimal model",
                    print "at %s with %d points in the reduced curve"%(factors[j][0], curve.local_minimal_model(factors[j][0]).reduction(factors[j][0]).count_points() )
                else:                 
                    print "Curve has good reduction and is a minimal model"
                    print "at %s with %d points in the reduced curve"%(factors[j][0],  curve.reduction(factors[j][0]).count_points() )
            else:
                print "Curve has bad reduction over %s"%factors[j][0]
    return


### sample 1
K.<t> = NumberField(x^2 + 1); E = EllipticCurve(K, [0, 1, 0, -2*t - 2, 2*t]); E
### sample 2
L.<u> = NumberField(x^2 - 2); F = EllipticCurve(L, [0,2,0, 2*u +4, 2*u + 3]); F

test(E, 100)

## now the error will happen
test(F, 100)

Issue created by migration from https://trac.sagemath.org/ticket/9409





---

archive/issue_comments_089670.json:
```json
{
    "body": "You do not actually say what the error is -- can you paste in the relevant part of the output?\n\nThis is one of a number of tickets which claim to be about elliptic curves but are almost certainly about the caching of finite fields (as you suggest).  the trouble is that because of this, elliptic curves people (like me) look at the ticket and do nothing, while the finite fields people who need to fix code do not look at it!",
    "created_at": "2010-07-05T16:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89670",
    "user": "cremona"
}
```

You do not actually say what the error is -- can you paste in the relevant part of the output?

This is one of a number of tickets which claim to be about elliptic curves but are almost certainly about the caching of finite fields (as you suggest).  the trouble is that because of this, elliptic curves people (like me) look at the ticket and do nothing, while the finite fields people who need to fix code do not look at it!



---

archive/issue_comments_089671.json:
```json
{
    "body": "Changing keywords from \"Elliptic Curves .count_points()\" to \"Elliptic Curves .count_points() finite fields\".",
    "created_at": "2010-07-05T19:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89671",
    "user": "adam"
}
```

Changing keywords from "Elliptic Curves .count_points()" to "Elliptic Curves .count_points() finite fields".



---

archive/issue_comments_089672.json:
```json
{
    "body": "This should be tested after #9315 is in as that may well fix it.",
    "created_at": "2010-08-14T16:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89672",
    "user": "cremona"
}
```

This should be tested after #9315 is in as that may well fix it.



---

archive/issue_comments_089673.json:
```json
{
    "body": "Attachment [9409.sage](tarball://root/attachments/some-uuid/ticket9409/9409.sage) by cremona created at 2010-08-14 17:15:13\n\nTest script",
    "created_at": "2010-08-14T17:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89673",
    "user": "cremona"
}
```

Attachment [9409.sage](tarball://root/attachments/some-uuid/ticket9409/9409.sage) by cremona created at 2010-08-14 17:15:13

Test script



---

archive/issue_comments_089674.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> This should be tested after #9315 is in as that may well fix it.\n\nUnfortunately not.  After loading the attached script, running either testE() or testF() in a fresh Sage (so no cached fields) works fine, but then running the other one fails (at p=59).",
    "created_at": "2010-08-14T17:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89674",
    "user": "cremona"
}
```

Replying to [comment:4 cremona]:
> This should be tested after #9315 is in as that may well fix it.

Unfortunately not.  After loading the attached script, running either testE() or testF() in a fresh Sage (so no cached fields) works fine, but then running the other one fails (at p=59).



---

archive/issue_comments_089675.json:
```json
{
    "body": "This now seems to work fine (both functions testE() and testF() in the test script now run without errors) in 4.6.alpha2 (not alpha1!).\n\nIf the reviewer agrees, this can be set to fixed and the closed.",
    "created_at": "2010-10-03T16:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89675",
    "user": "cremona"
}
```

This now seems to work fine (both functions testE() and testF() in the test script now run without errors) in 4.6.alpha2 (not alpha1!).

If the reviewer agrees, this can be set to fixed and the closed.



---

archive/issue_comments_089676.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-03T16:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89676",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089677.json:
```json
{
    "body": "(Editing description because the entire ticket webpage appears stuck in a rogue `<sup>` tag!)",
    "created_at": "2010-10-03T16:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89677",
    "user": "davidloeffler"
}
```

(Editing description because the entire ticket webpage appears stuck in a rogue `<sup>` tag!)



---

archive/issue_comments_089678.json:
```json
{
    "body": "Looks fine to me. I'm flagging this as positive review so the release manager can close it as fixed.",
    "created_at": "2010-10-03T16:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89678",
    "user": "davidloeffler"
}
```

Looks fine to me. I'm flagging this as positive review so the release manager can close it as fixed.



---

archive/issue_comments_089679.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-03T16:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89679",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089680.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-10-04T01:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9409#issuecomment-89680",
    "user": "mpatel"
}
```

Resolution: worksforme
