# Issue 3451: inaccurate error message in scheme morphisms

archive/issues_003451.json:
```json
{
    "body": "Assignee: @bobmoretti\n\nCC:  alexghitza\n\nKeywords: affine, scheme, morphism\n\n\n```\nR.<x,y> = QQ[]\nA = AffineSpace(R)\nH = A.Hom(A)\nf = H([x-y, x*y])\nf([0,1])\nTraceback (click to the left for traceback)\n...\nTypeError: x (=[0, 1]) must be a projective point given by coordinates\n```\n\n\nWhen of course the error message should say that x must be an affine point...\n\nThe fix would be trivial, but would it be acceptable to make scheme morphisms try converting their input to elements of their domain, first, so that the above would not raise an error?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3451\n\n",
    "created_at": "2008-06-17T22:17:24Z",
    "labels": [
        "algebraic geometry",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "inaccurate error message in scheme morphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3451",
    "user": "@bobmoretti"
}
```
Assignee: @bobmoretti

CC:  alexghitza

Keywords: affine, scheme, morphism


```
R.<x,y> = QQ[]
A = AffineSpace(R)
H = A.Hom(A)
f = H([x-y, x*y])
f([0,1])
Traceback (click to the left for traceback)
...
TypeError: x (=[0, 1]) must be a projective point given by coordinates
```


When of course the error message should say that x must be an affine point...

The fix would be trivial, but would it be acceptable to make scheme morphisms try converting their input to elements of their domain, first, so that the above would not raise an error?


Issue created by migration from https://trac.sagemath.org/ticket/3451





---

archive/issue_comments_024335.json:
```json
{
    "body": "Attachment [3451_scheme_morphism.patch](tarball://root/attachments/some-uuid/ticket3451/3451_scheme_morphism.patch) by @aghitza created at 2008-08-27 08:54:33",
    "created_at": "2008-08-27T08:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24335",
    "user": "@aghitza"
}
```

Attachment [3451_scheme_morphism.patch](tarball://root/attachments/some-uuid/ticket3451/3451_scheme_morphism.patch) by @aghitza created at 2008-08-27 08:54:33



---

archive/issue_comments_024336.json:
```json
{
    "body": "I have changed things in the following way: if we try to evaluate f(p), then the first step is to coerce p into the domain of f.  If that works, then the evaluation goes forth.  Otherwise, there is of course an error message saying that p has no business being there in the first place.\n\nThe change is in the generic scheme morphism code, so it should work for affine spaces, projective spaces, and whatever else inherits from schemes.",
    "created_at": "2008-08-27T08:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24336",
    "user": "@aghitza"
}
```

I have changed things in the following way: if we try to evaluate f(p), then the first step is to coerce p into the domain of f.  If that works, then the evaluation goes forth.  Otherwise, there is of course an error message saying that p has no business being there in the first place.

The change is in the generic scheme morphism code, so it should work for affine spaces, projective spaces, and whatever else inherits from schemes.



---

archive/issue_comments_024337.json:
```json
{
    "body": "Changing assignee from @bobmoretti to @aghitza.",
    "created_at": "2008-09-01T09:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24337",
    "user": "@aghitza"
}
```

Changing assignee from @bobmoretti to @aghitza.



---

archive/issue_comments_024338.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-01T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24338",
    "user": "@aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024339.json:
```json
{
    "body": "Looks ok to me.  I see that you are relying on whatever error message is produced by \"dom(x)\" in case x cannot be coerced into dom rather than supplying your own, of the form \"... cannot be coerced into the domain\", but that is ok.\n\nPatch applies cleanly to 3.1.2.alpha3 and all doctests in sage.schemes.generic pass.",
    "created_at": "2008-09-01T19:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24339",
    "user": "@JohnCremona"
}
```

Looks ok to me.  I see that you are relying on whatever error message is produced by "dom(x)" in case x cannot be coerced into dom rather than supplying your own, of the form "... cannot be coerced into the domain", but that is ok.

Patch applies cleanly to 3.1.2.alpha3 and all doctests in sage.schemes.generic pass.



---

archive/issue_comments_024340.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T11:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24340",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_024341.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T11:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3451#issuecomment-24341",
    "user": "mabshoff"
}
```

Resolution: fixed
