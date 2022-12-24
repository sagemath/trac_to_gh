# Issue 8682: Improve AlgebraicScheme_subscheme.__init__ and AmbientSpace._validate

archive/issues_008682.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCreation of a subscheme given by polynomial equations in some ambient space involves converting the input to polynomials in the correct ring and checking that these polynomials are \"OK\", e.g. that they are homogeneous for the projective space. There are the following (little) problems with the current realization:\n* converting to the coordinate ring is done in _validate method of ambient spaces, but it is the same for all of them and in general I would expect that a method with such a name just checks something without modifying the input\n* if a subscheme is constructed using an ideal of a wrong ring, but polynomials can be converted into the coordinate ring of the ambient space, then wrong ideal will be saved for later use\n* _validate is not listed as a mandatory method for overriding by subclasses of AmbientSpace\n\nThe attached patch makes the following:\n* all conversions are done in !__init!__ of the subscheme\n* _validate of AmbientSpace's must check that the polynomials are OK, but they are already guaranteed to lie in the correct ring\n* _validate is listed as a method which must be overridden \n* error messages in exceptions include only the polynomial that lead to the error, not the whole input\n\nApply on top of #8675.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8682\n\n",
    "created_at": "2010-04-13T21:19:45Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Improve AlgebraicScheme_subscheme.__init__ and AmbientSpace._validate",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8682",
    "user": "novoselt"
}
```
Assignee: AlexGhitza

Creation of a subscheme given by polynomial equations in some ambient space involves converting the input to polynomials in the correct ring and checking that these polynomials are "OK", e.g. that they are homogeneous for the projective space. There are the following (little) problems with the current realization:
* converting to the coordinate ring is done in _validate method of ambient spaces, but it is the same for all of them and in general I would expect that a method with such a name just checks something without modifying the input
* if a subscheme is constructed using an ideal of a wrong ring, but polynomials can be converted into the coordinate ring of the ambient space, then wrong ideal will be saved for later use
* _validate is not listed as a mandatory method for overriding by subclasses of AmbientSpace

The attached patch makes the following:
* all conversions are done in !__init!__ of the subscheme
* _validate of AmbientSpace's must check that the polynomials are OK, but they are already guaranteed to lie in the correct ring
* _validate is listed as a method which must be overridden 
* error messages in exceptions include only the polynomial that lead to the error, not the whole input

Apply on top of #8675.

Issue created by migration from https://trac.sagemath.org/ticket/8682





---

archive/issue_comments_079125.json:
```json
{
    "body": "Attachment [trac_8682_improve_algebraic_subscheme_init.patch](tarball://root/attachments/some-uuid/ticket8682/trac_8682_improve_algebraic_subscheme_init.patch) by novoselt created at 2010-04-13 21:42:12",
    "created_at": "2010-04-13T21:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8682#issuecomment-79125",
    "user": "novoselt"
}
```

Attachment [trac_8682_improve_algebraic_subscheme_init.patch](tarball://root/attachments/some-uuid/ticket8682/trac_8682_improve_algebraic_subscheme_init.patch) by novoselt created at 2010-04-13 21:42:12



---

archive/issue_comments_079126.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-13T21:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8682#issuecomment-79126",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079127.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T12:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8682#issuecomment-79127",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079128.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-18T12:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8682#issuecomment-79128",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_079129.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8682#issuecomment-79129",
    "user": "mhansen"
}
```

Resolution: fixed
