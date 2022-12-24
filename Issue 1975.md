# Issue 1975: elliptic curve method -- one should trivially be able to implement a toy version, but can't anymore, which sucks

archive/issues_001975.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\nThey definitely very useful sometimes.  E.g., there is something\ncalled the elliptic curve factorization method that is a brilliant trick\nto factor integers.  You want to factor an integer N so you pretend\nthat it is prime, do a bunch of arithmetic with N, and if something goes\nwrong, the error message gives just the information you need to factor N.\nBut it's important that the error message be an exception that you can\ncatch and that can contain some interesting Python data in it.  Custom\nexceptions work very nicely for that. \n\n(This used to be trivial to implement in Sage, but for some reason\nSage changed and now it is isn't... :-(\n\nsage: E = EllipticCurve(Integers(15),[1,-1])\nsage: P = E.point([1,0,1], check=False)\ngoes boom but didn't used to...\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1975\n\n",
    "created_at": "2008-01-30T03:38:42Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "elliptic curve method -- one should trivially be able to implement a toy version, but can't anymore, which sucks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1975",
    "user": "was"
}
```
Assignee: was


```

They definitely very useful sometimes.  E.g., there is something
called the elliptic curve factorization method that is a brilliant trick
to factor integers.  You want to factor an integer N so you pretend
that it is prime, do a bunch of arithmetic with N, and if something goes
wrong, the error message gives just the information you need to factor N.
But it's important that the error message be an exception that you can
catch and that can contain some interesting Python data in it.  Custom
exceptions work very nicely for that. 

(This used to be trivial to implement in Sage, but for some reason
Sage changed and now it is isn't... :-(

sage: E = EllipticCurve(Integers(15),[1,-1])
sage: P = E.point([1,0,1], check=False)
goes boom but didn't used to...

William
```


Issue created by migration from https://trac.sagemath.org/ticket/1975





---

archive/issue_comments_012795.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12795",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_012796.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12796",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_012797.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12797",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_012798.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12798",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_012799.json:
```json
{
    "body": "See also this [sage-support discussion](http://groups.google.com/group/sage-support/browse_thread/thread/e2a5a329c0699379)",
    "created_at": "2010-04-12T18:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12799",
    "user": "wuthrich"
}
```

See also this [sage-support discussion](http://groups.google.com/group/sage-support/browse_thread/thread/e2a5a329c0699379)



---

archive/issue_comments_012800.json:
```json
{
    "body": "The simplest workaround, I think, is to set \n\n```\nE._point_class = sage.schemes.elliptic_curves.ell_field.EllipticCurve_field\n```\n\nafter creating E and before attempting to create points.",
    "created_at": "2010-05-04T17:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12800",
    "user": "cremona"
}
```

The simplest workaround, I think, is to set 

```
E._point_class = sage.schemes.elliptic_curves.ell_field.EllipticCurve_field
```

after creating E and before attempting to create points.



---

archive/issue_comments_012801.json:
```json
{
    "body": "Attachment [trac_1975-points-mod-N.patch](tarball://root/attachments/some-uuid/ticket1975/trac_1975-points-mod-N.patch) by cremona created at 2010-05-05 19:27:05\n\nApplies to 4.4.1",
    "created_at": "2010-05-05T19:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12801",
    "user": "cremona"
}
```

Attachment [trac_1975-points-mod-N.patch](tarball://root/attachments/some-uuid/ticket1975/trac_1975-points-mod-N.patch) by cremona created at 2010-05-05 19:27:05

Applies to 4.4.1



---

archive/issue_comments_012802.json:
```json
{
    "body": "The patch makes possible what is wanted here.  It does two things:\n1. in creating an instance of `EllipticCurve_generic`, if the base ring is an `IntegerModRing` it sets the point_class to be `EllipticCurvePoint_finite_field`.  The is a class with a lot of functionality, eheras the code previous set this to the class `EllipticCurvePoint` (the default for generic elliptic curves) which has no functionality at all (not even an initialiser!).\n2. When a `ZeroDivisionError` is raised on trying to invert a non-invertible element of the base ring during point arithmetic, the error message is expanded when the base ring is an `IntegerModRing` so that it shows a factorization of the modulus.",
    "created_at": "2010-05-05T19:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12802",
    "user": "cremona"
}
```

The patch makes possible what is wanted here.  It does two things:
1. in creating an instance of `EllipticCurve_generic`, if the base ring is an `IntegerModRing` it sets the point_class to be `EllipticCurvePoint_finite_field`.  The is a class with a lot of functionality, eheras the code previous set this to the class `EllipticCurvePoint` (the default for generic elliptic curves) which has no functionality at all (not even an initialiser!).
2. When a `ZeroDivisionError` is raised on trying to invert a non-invertible element of the base ring during point arithmetic, the error message is expanded when the base ring is an `IntegerModRing` so that it shows a factorization of the modulus.



---

archive/issue_comments_012803.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T19:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12803",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012804.json:
```json
{
    "body": "I'd really like to see this behavior, but I'm not sure this is the right fix--probably what should happen is that most of the generic, missing code should be moved up to a higher level. That would probably be a bit more invasive though.",
    "created_at": "2010-05-05T21:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12804",
    "user": "robertwb"
}
```

I'd really like to see this behavior, but I'm not sure this is the right fix--probably what should happen is that most of the generic, missing code should be moved up to a higher level. That would probably be a bit more invasive though.



---

archive/issue_comments_012805.json:
```json
{
    "body": "Replying to [comment:7 robertwb]:\n> I'd really like to see this behavior, but I'm not sure this is the right fix--probably what should happen is that most of the generic, missing code should be moved up to a higher level. That would probably be a bit more invasive though. \n\nI rather expected this reaction -- but look, the *only* cases where this makes any difference is precisely the case of an \"elliptic curve over Z/NZ\".  Since ECM is something many people want to teach, why not allow this in now, pending a more rigorous implementation?  There is absolutely no effect from this patch on any elliptic curve defined over a field;  and I think this is much less dangerous than William's fix of telling a non-field to pretend that it is a field, surely?\n\nWe could ask for a vote...",
    "created_at": "2010-05-05T21:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12805",
    "user": "cremona"
}
```

Replying to [comment:7 robertwb]:
> I'd really like to see this behavior, but I'm not sure this is the right fix--probably what should happen is that most of the generic, missing code should be moved up to a higher level. That would probably be a bit more invasive though. 

I rather expected this reaction -- but look, the *only* cases where this makes any difference is precisely the case of an "elliptic curve over Z/NZ".  Since ECM is something many people want to teach, why not allow this in now, pending a more rigorous implementation?  There is absolutely no effect from this patch on any elliptic curve defined over a field;  and I think this is much less dangerous than William's fix of telling a non-field to pretend that it is a field, surely?

We could ask for a vote...



---

archive/issue_comments_012806.json:
```json
{
    "body": "That's why I didn't mark this as needs work, because half of me wants to fix this the (pedantically) correct way, and the other half just wants to get this in. \n\nThe code looks good, I haven't run tests as I don't have a clean install handy, but I can't see anything going wrong.",
    "created_at": "2010-05-05T21:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12806",
    "user": "robertwb"
}
```

That's why I didn't mark this as needs work, because half of me wants to fix this the (pedantically) correct way, and the other half just wants to get this in. 

The code looks good, I haven't run tests as I don't have a clean install handy, but I can't see anything going wrong.



---

archive/issue_comments_012807.json:
```json
{
    "body": "Here is an idea (which should not be a show stopper for this patch, but could be for later): Can you change the exceptions so that they include the information about the prime factor found?  I.e., make a class that derives from ZeroDivisionError, and set an attribute that contains extra info.  You can raise class instances in exceptions.",
    "created_at": "2010-05-06T00:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12807",
    "user": "was"
}
```

Here is an idea (which should not be a show stopper for this patch, but could be for later): Can you change the exceptions so that they include the information about the prime factor found?  I.e., make a class that derives from ZeroDivisionError, and set an attribute that contains extra info.  You can raise class instances in exceptions.



---

archive/issue_comments_012808.json:
```json
{
    "body": "The exception error messages do include this info, but not in such a sophisticated way -- they give a nontrivial factorisation of the modulus.\n\nIf what you're suggesting would be better, I am open to the idea but not sure how to implement it (didn't know that ZeroDivisionError was a class at all!)",
    "created_at": "2010-05-06T08:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12808",
    "user": "cremona"
}
```

The exception error messages do include this info, but not in such a sophisticated way -- they give a nontrivial factorisation of the modulus.

If what you're suggesting would be better, I am open to the idea but not sure how to implement it (didn't know that ZeroDivisionError was a class at all!)



---

archive/issue_comments_012809.json:
```json
{
    "body": "I had a look at this patch and it seems ok to me. All tests passed and it does what it promises.\n\nI agree with the fact that this may not be the best way to do it, but I propose to accept this as a temporary solution. I leave it to someone else to open a new ticket requesting for a better solution.",
    "created_at": "2010-05-23T23:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12809",
    "user": "wuthrich"
}
```

I had a look at this patch and it seems ok to me. All tests passed and it does what it promises.

I agree with the fact that this may not be the best way to do it, but I propose to accept this as a temporary solution. I leave it to someone else to open a new ticket requesting for a better solution.



---

archive/issue_comments_012810.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-23T23:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12810",
    "user": "wuthrich"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012811.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T21:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1975#issuecomment-12811",
    "user": "mhansen"
}
```

Resolution: fixed
