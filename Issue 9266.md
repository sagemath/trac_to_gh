# Issue 9266: bug in global_integral_model for Elliptic Curves over Number Fields

archive/issues_009266.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nThe following illustrates the bug. It should be easy to fix.\n\n```\nsage: K.<s> = NumberField(x^2-5)\nsage: w = (1+s)/2\nsage: E = EllipticCurve(K,[2,w])\nsage: E.global_integral_model()\n...sage/schemes/elliptic_curves/ell_number_field.pyc in global_integral_model(self)\n    377                    ai = [ai[i]/pi**(e*[1,2,3,4,6][i]) for i in range(5)]\n    378         for z in ai:\n--> 379             assert z.denominator() == 1, \"bug in global_integral_model: %s\" % ai\n    380         return EllipticCurve(list(ai))\n    381\n\nTypeError: not all arguments converted during string formatting\n```\n\nSo there are two problems. One that the string is not correctly formatted, the other that it is raised. The latter, I believe, is just because the wrong thing is tested:\n\n```\nsage: w.denominator()\n2\nsage: w.is_integral()\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9266\n\n",
    "closed_at": "2010-07-20T07:17:51Z",
    "created_at": "2010-06-18T13:08:05Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "bug in global_integral_model for Elliptic Curves over Number Fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9266",
    "user": "https://github.com/categorie"
}
```
Assignee: @JohnCremona

The following illustrates the bug. It should be easy to fix.

```
sage: K.<s> = NumberField(x^2-5)
sage: w = (1+s)/2
sage: E = EllipticCurve(K,[2,w])
sage: E.global_integral_model()
...sage/schemes/elliptic_curves/ell_number_field.pyc in global_integral_model(self)
    377                    ai = [ai[i]/pi**(e*[1,2,3,4,6][i]) for i in range(5)]
    378         for z in ai:
--> 379             assert z.denominator() == 1, "bug in global_integral_model: %s" % ai
    380         return EllipticCurve(list(ai))
    381

TypeError: not all arguments converted during string formatting
```

So there are two problems. One that the string is not correctly formatted, the other that it is raised. The latter, I believe, is just because the wrong thing is tested:

```
sage: w.denominator()
2
sage: w.is_integral()
True
```


Issue created by migration from https://trac.sagemath.org/ticket/9266





---

archive/issue_comments_087135.json:
```json
{
    "body": "The test would be better written as\n\n```\nif not all([z.denominator()==1 for z in ai]):\n    raise error\n```\n\nThe problem with the string is that it worked when ai was a list, but now it's a tuple.\n\nI don't understand the last part -- what is w here?",
    "created_at": "2010-06-18T15:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87135",
    "user": "https://github.com/JohnCremona"
}
```

The test would be better written as

```
if not all([z.denominator()==1 for z in ai]):
    raise error
```

The problem with the string is that it worked when ai was a list, but now it's a tuple.

I don't understand the last part -- what is w here?



---

archive/issue_comments_087136.json:
```json
{
    "body": "*w* is the algebraic integer (1+sqrt(5))/2 and it is the coefficient of this integral Weierstrass equation. So this is a global_integral_model. We should not check if the denominator in some basis is 1, but rather if the coefficients are integers.",
    "created_at": "2010-06-18T16:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87136",
    "user": "https://github.com/categorie"
}
```

*w* is the algebraic integer (1+sqrt(5))/2 and it is the coefficient of this integral Weierstrass equation. So this is a global_integral_model. We should not check if the denominator in some basis is 1, but rather if the coefficients are integers.



---

archive/issue_comments_087137.json:
```json
{
    "body": "Replying to [comment:2 wuthrich]:\n> *w* is the algebraic integer (1+sqrt(5))/2 and it is the coefficient of this integral Weierstrass equation. So this is a global_integral_model. We should not check if the denominator in some basis is 1, but rather if the coefficients are integers.\n\n\nOK then so we should do \n\n```\nif not all([z.is_integral() for z in ai]):\n```\n\nI'm too busy writing lectures for SD22 to make the patch myself!",
    "created_at": "2010-06-18T16:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87137",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 wuthrich]:
> *w* is the algebraic integer (1+sqrt(5))/2 and it is the coefficient of this integral Weierstrass equation. So this is a global_integral_model. We should not check if the denominator in some basis is 1, but rather if the coefficients are integers.


OK then so we should do 

```
if not all([z.is_integral() for z in ai]):
```

I'm too busy writing lectures for SD22 to make the patch myself!



---

archive/issue_comments_087138.json:
```json
{
    "body": "That holds for me too :)\nWe will do it in California !\n\nSee you soon.",
    "created_at": "2010-06-18T16:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87138",
    "user": "https://github.com/categorie"
}
```

That holds for me too :)
We will do it in California !

See you soon.



---

archive/issue_comments_087139.json:
```json
{
    "body": "Milestone sage-4.4.5 deleted",
    "created_at": "2010-06-22T04:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87139",
    "user": "https://github.com/williamstein"
}
```

Milestone sage-4.4.5 deleted



---

archive/issue_events_022834.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-22T04:36:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9266#event-22834"
}
```



---

archive/issue_comments_087140.json:
```json
{
    "body": "Attachment [trac_9266.patch](tarball://root/attachments/some-uuid/ticket9266/trac_9266.patch) by @categorie created at 2010-06-22 23:19:26\n\nexported against 4.4.4.alpha0",
    "created_at": "2010-06-22T23:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87140",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9266.patch](tarball://root/attachments/some-uuid/ticket9266/trac_9266.patch) by @categorie created at 2010-06-22 23:19:26

exported against 4.4.4.alpha0



---

archive/issue_comments_087141.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-22T23:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87141",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087142.json:
```json
{
    "body": "Looks good and tests pass on 4.4.4.alpha0",
    "created_at": "2010-06-23T04:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87142",
    "user": "https://github.com/JohnCremona"
}
```

Looks good and tests pass on 4.4.4.alpha0



---

archive/issue_comments_087143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T04:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87143",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022835.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T07:17:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9266#event-22835"
}
```



---

archive/issue_comments_087144.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9266#issuecomment-87144",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
