# Issue 8909: Coercion from Gap to cyclotomic fields; usage of GAP to improve computation of invariant rings

archive/issues_008909.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @wdjoyner\n\nKeywords: gap, cyclotomic fields, invariant rings\n\nWhen coercing from GAP to a cyclotomic field, it was assumed that the generator of a cyclotomic field is *always* called ``E(n)``. But this is not necessarily the case, in particular when the object in GAP was created from Sage.\n\nMoreover, GAP prints an additional exclamation mark in front of numbers if they are part of a matrix defined over a cyclotomic field.\n\nFor these two reasons, the following example used to fail, but now works with the patch:\n\n```\n            sage: F=CyclotomicField(8)\n            sage: z=F.gen()\n            sage: a=gap(z+1/z); a\n            -zeta8^3+zeta8\n            sage: F(a)\n            -zeta8^3 + zeta8\n            sage: b=gap(Matrix(F,[[z^2,1],[0,a+1]])); b\n            [ [ zeta8^2, !1 ], [ !0, -zeta8^3+zeta8+1 ] ]\n            sage: b[1,2]\n            !1\n            sage: F(b[1,2])\n            1\n            sage: Matrix(b,F)\n            [             zeta8^2                    1]\n            [                   0 -zeta8^3 + zeta8 + 1]\n```\n\nThe idea was\n* to remove the exclamation mark when it is attempted to coerce into the rationals\n* to test whether the generator name in GAP happens to coincide with the generator name in Sage (here: ``zeta8``).\n\nThe motivation for working on it is my attempt to improve the computation of non-modular invariant rings of finite groups: There is a doc test using a finite matrix group over a cyclotomic field.\n\nOne massive bottle neck for the computation of invariant rings with Singular is the computation of the Reynolds operator. It requires to enumerate the group elements, and Singular is not good at this task.\n\nThe patch uses GAP to enumerate the group elements and uses this to construct the Reynolds operator in Singular. For complicated groups, this should save a massive amount of resources.\n\nWith the patch, the enumeration of group elements in Singular has the status of a backup: If the transformation of the matrix group into GAP fails or if the transformation of the resulting GAP matrices back into Sage fails, then the old algorithm is used.\n\nI think this ticket is about \"interfaces\". I hope this labelling is correct.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8909\n\n",
    "closed_at": "2010-07-21T03:31:55Z",
    "created_at": "2010-05-07T10:58:12Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Coercion from Gap to cyclotomic fields; usage of GAP to improve computation of invariant rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8909",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @williamstein

CC:  @wdjoyner

Keywords: gap, cyclotomic fields, invariant rings

When coercing from GAP to a cyclotomic field, it was assumed that the generator of a cyclotomic field is *always* called ``E(n)``. But this is not necessarily the case, in particular when the object in GAP was created from Sage.

Moreover, GAP prints an additional exclamation mark in front of numbers if they are part of a matrix defined over a cyclotomic field.

For these two reasons, the following example used to fail, but now works with the patch:

```
            sage: F=CyclotomicField(8)
            sage: z=F.gen()
            sage: a=gap(z+1/z); a
            -zeta8^3+zeta8
            sage: F(a)
            -zeta8^3 + zeta8
            sage: b=gap(Matrix(F,[[z^2,1],[0,a+1]])); b
            [ [ zeta8^2, !1 ], [ !0, -zeta8^3+zeta8+1 ] ]
            sage: b[1,2]
            !1
            sage: F(b[1,2])
            1
            sage: Matrix(b,F)
            [             zeta8^2                    1]
            [                   0 -zeta8^3 + zeta8 + 1]
```

The idea was
* to remove the exclamation mark when it is attempted to coerce into the rationals
* to test whether the generator name in GAP happens to coincide with the generator name in Sage (here: ``zeta8``).

The motivation for working on it is my attempt to improve the computation of non-modular invariant rings of finite groups: There is a doc test using a finite matrix group over a cyclotomic field.

One massive bottle neck for the computation of invariant rings with Singular is the computation of the Reynolds operator. It requires to enumerate the group elements, and Singular is not good at this task.

The patch uses GAP to enumerate the group elements and uses this to construct the Reynolds operator in Singular. For complicated groups, this should save a massive amount of resources.

With the patch, the enumeration of group elements in Singular has the status of a backup: If the transformation of the matrix group into GAP fails or if the transformation of the resulting GAP matrices back into Sage fails, then the old algorithm is used.

I think this ticket is about "interfaces". I hope this labelling is correct.

Issue created by migration from https://trac.sagemath.org/ticket/8909





---

archive/issue_comments_081929.json:
```json
{
    "body": "Improve coercion from GAP into cyclotomic fields; use GAP to compute Reynolds operators for Singular",
    "created_at": "2010-05-07T11:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81929",
    "user": "https://github.com/simon-king-jena"
}
```

Improve coercion from GAP into cyclotomic fields; use GAP to compute Reynolds operators for Singular



---

archive/issue_comments_081930.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-08T12:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81930",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081931.json:
```json
{
    "body": "Attachment [8909_gap2cyclotomic.patch](tarball://root/attachments/some-uuid/ticket8909/8909_gap2cyclotomic.patch) by @simon-king-jena created at 2010-05-08 12:16:57\n\nSorry, I forgot to label it \"needs review\"",
    "created_at": "2010-05-08T12:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81931",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [8909_gap2cyclotomic.patch](tarball://root/attachments/some-uuid/ticket8909/8909_gap2cyclotomic.patch) by @simon-king-jena created at 2010-05-08 12:16:57

Sorry, I forgot to label it "needs review"



---

archive/issue_comments_081932.json:
```json
{
    "body": "When this is merged we can probably close #5618 too.",
    "created_at": "2010-07-03T08:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81932",
    "user": "https://github.com/loefflerd"
}
```

When this is merged we can probably close #5618 too.



---

archive/issue_comments_081933.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-03T10:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81933",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081934.json:
```json
{
    "body": "Patch applies fine to 4.5.alpha1, code looks plausible, and all doctests pass. Contrary to my earlier hope, however, it does not fix #5618 which seems to be a separate problem.",
    "created_at": "2010-07-03T10:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81934",
    "user": "https://github.com/loefflerd"
}
```

Patch applies fine to 4.5.alpha1, code looks plausible, and all doctests pass. Contrary to my earlier hope, however, it does not fix #5618 which seems to be a separate problem.



---

archive/issue_comments_081935.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-04T18:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81935",
    "user": "https://github.com/mwhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081936.json:
```json
{
    "body": "There's a bare except clause at 6767 which should be fixed.",
    "created_at": "2010-07-04T18:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81936",
    "user": "https://github.com/mwhansen"
}
```

There's a bare except clause at 6767 which should be fixed.



---

archive/issue_comments_081937.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> There's a bare except clause at 6767 which should be fixed.\n\n\nBy 'bare', you mean that it is not specified what error is raised? So, `except TypeError:` instead of `except:`? Well this would be easy enough to fix.",
    "created_at": "2010-07-04T19:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81937",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:4 mhansen]:
> There's a bare except clause at 6767 which should be fixed.


By 'bare', you mean that it is not specified what error is raised? So, `except TypeError:` instead of `except:`? Well this would be easy enough to fix.



---

archive/issue_comments_081938.json:
```json
{
    "body": "Specify an exception to be caught",
    "created_at": "2010-07-04T19:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81938",
    "user": "https://github.com/simon-king-jena"
}
```

Specify an exception to be caught



---

archive/issue_comments_081939.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-04T19:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81939",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081940.json:
```json
{
    "body": "Attachment [trac_8909_catch_exception.patch](tarball://root/attachments/some-uuid/ticket8909/trac_8909_catch_exception.patch) by @simon-king-jena created at 2010-07-04 19:12:30\n\nReplying to [comment:5 SimonKing]:\n> Replying to [comment:4 mhansen]:\n> > There's a bare except clause at 6767 which should be fixed.\n\n> \n> By 'bare', you mean that it is not specified what error is raised? So, `except TypeError:` instead of `except:`? Well this would be easy enough to fix.\n> \n\n\nUnder the assumption that I understood you correctly, I provided a second patch that specifies that we only want to catch a `TypeError`, and return to needs_review.",
    "created_at": "2010-07-04T19:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81940",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_8909_catch_exception.patch](tarball://root/attachments/some-uuid/ticket8909/trac_8909_catch_exception.patch) by @simon-king-jena created at 2010-07-04 19:12:30

Replying to [comment:5 SimonKing]:
> Replying to [comment:4 mhansen]:
> > There's a bare except clause at 6767 which should be fixed.

> 
> By 'bare', you mean that it is not specified what error is raised? So, `except TypeError:` instead of `except:`? Well this would be easy enough to fix.
> 


Under the assumption that I understood you correctly, I provided a second patch that specifies that we only want to catch a `TypeError`, and return to needs_review.



---

archive/issue_comments_081941.json:
```json
{
    "body": "Yep, looks good to me.  If you didn't specify that, the except clause would also catch things like KeyboardInterrupt (Ctrl-C) which probably isn't intended.\n\nApply both patches.",
    "created_at": "2010-07-04T19:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81941",
    "user": "https://github.com/mwhansen"
}
```

Yep, looks good to me.  If you didn't specify that, the except clause would also catch things like KeyboardInterrupt (Ctrl-C) which probably isn't intended.

Apply both patches.



---

archive/issue_comments_081942.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-04T19:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81942",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021767.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T03:31:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8909#event-21767"
}
```



---

archive/issue_comments_081943.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8909#issuecomment-81943",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
