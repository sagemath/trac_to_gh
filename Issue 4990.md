# Issue 4990: [with code, needs work] Add code to compute Hilber class polynomials

archive/issues_004990.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe attached Sage code has been written by\n\n* Eduardo Ocampo Alvarez\n* Andrey Timofeev\n\nfrom the University of Essen in Germany. It needs some integration, but other than that it should be ready to be merged.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4990\n\n",
    "created_at": "2009-01-17T08:47:24Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with code, needs work] Add code to compute Hilber class polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

The attached Sage code has been written by

* Eduardo Ocampo Alvarez
* Andrey Timofeev

from the University of Essen in Germany. It needs some integration, but other than that it should be ready to be merged.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4990





---

archive/issue_comments_038005.json:
```json
{
    "body": "This is the third verion of the code",
    "created_at": "2009-01-17T08:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is the third verion of the code



---

archive/issue_comments_038006.json:
```json
{
    "body": "Attachment [hcp3.sage.txt](tarball://root/attachments/some-uuid/ticket4990/hcp3.sage.txt) by @mwhansen created at 2009-01-17 22:04:59\n\nOne thing that needs to be done is to convert everything to four spaces.",
    "created_at": "2009-01-17T22:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38006",
    "user": "https://github.com/mwhansen"
}
```

Attachment [hcp3.sage.txt](tarball://root/attachments/some-uuid/ticket4990/hcp3.sage.txt) by @mwhansen created at 2009-01-17 22:04:59

One thing that needs to be done is to convert everything to four spaces.



---

archive/issue_comments_038007.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38007",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038008.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-04-03T10:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38008",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_038009.json:
```json
{
    "body": "Changing keywords from \"\" to \"hilbert class polynomial\".",
    "created_at": "2009-04-03T10:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38009",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "hilbert class polynomial".



---

archive/issue_comments_038010.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-03T10:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38010",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038011.json:
```json
{
    "body": "Attachment [trac_4990.patch](tarball://root/attachments/some-uuid/ticket4990/trac_4990.patch) by @aghitza created at 2009-04-04 07:18:21\n\nThe attached patch adds the method `hilbert_class_polynomial()` to `NumberField_quadratic` and cleans the code up a little bit.\n\nI cannot perform comparative timings since I don't have access to Magma at the moment.  Doing `%prun` with large discriminants indicates that the large majority of the time is spent in the Pari library computing the j-invariants of the representative tau's.  So I don't think rewriting the method in Cython will have a significant effect.\n\nSee also the discussion at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/6c9aedf63106cc2d",
    "created_at": "2009-04-04T07:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38011",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4990.patch](tarball://root/attachments/some-uuid/ticket4990/trac_4990.patch) by @aghitza created at 2009-04-04 07:18:21

The attached patch adds the method `hilbert_class_polynomial()` to `NumberField_quadratic` and cleans the code up a little bit.

I cannot perform comparative timings since I don't have access to Magma at the moment.  Doing `%prun` with large discriminants indicates that the large majority of the time is spent in the Pari library computing the j-invariants of the representative tau's.  So I don't think rewriting the method in Cython will have a significant effect.

See also the discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/6c9aedf63106cc2d



---

archive/issue_events_011548.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-04-04T07:18:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4990#event-11548"
}
```



---

archive/issue_comments_038012.json:
```json
{
    "body": "Alex, is your patch to be applied by itself, ignoring  the .txt file which it seems to be based on?  I assume so.  Is this intended to work on 3.4.1(.alpha0, say)?\n\nJohn",
    "created_at": "2009-04-04T15:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38012",
    "user": "https://github.com/JohnCremona"
}
```

Alex, is your patch to be applied by itself, ignoring  the .txt file which it seems to be based on?  I assume so.  Is this intended to work on 3.4.1(.alpha0, say)?

John



---

archive/issue_comments_038013.json:
```json
{
    "body": "Yes: apply only the patch, to 3.4.1.alpha0.",
    "created_at": "2009-04-04T21:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38013",
    "user": "https://github.com/aghitza"
}
```

Yes: apply only the patch, to 3.4.1.alpha0.



---

archive/issue_comments_038014.json:
```json
{
    "body": "Looks good to me.  I tested it with the following script, and found a lot of curves with the correct endomorphism rings :)\n\n```\nK.<a> = QuadraticField(-34)\nf = K.hilbert_class_polynomial()\nassert K.class_number() == f.degree()\n\nfor P in K.primes_of_degree_one_list(20):\n    p = P.norm()\n    k = GF(p)\n    rts = f.roots(k, multiplicities=False)\n    for jj in rts:\n        assert P.is_principal()\n        E = EllipticCurve(jj)\n        print E\n        assert E.frobenius_order().number_field().is_isomorphic(K)\n    if not rts:\n        print \"XXX\", p\n        assert not P.is_principal()\n```",
    "created_at": "2009-04-05T03:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38014",
    "user": "https://github.com/ncalexan"
}
```

Looks good to me.  I tested it with the following script, and found a lot of curves with the correct endomorphism rings :)

```
K.<a> = QuadraticField(-34)
f = K.hilbert_class_polynomial()
assert K.class_number() == f.degree()

for P in K.primes_of_degree_one_list(20):
    p = P.norm()
    k = GF(p)
    rts = f.roots(k, multiplicities=False)
    for jj in rts:
        assert P.is_principal()
        E = EllipticCurve(jj)
        print E
        assert E.frobenius_order().number_field().is_isomorphic(K)
    if not rts:
        print "XXX", p
        assert not P.is_principal()
```



---

archive/issue_comments_038015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-05T23:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38015",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038016.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T23:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc1.

Cheers,

Michael



---

archive/issue_events_011549.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-05T23:16:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4990#event-11549"
}
```



---

archive/issue_comments_038017.json:
```json
{
    "body": "Posted to sage-nt 2009-04-20:\n\nTicket #4990 implemented a hilbert_class_polynomial() method for\nimaginary quadratic fields.  It is actually a function of the field's\ndiscriminant, i.e. of a fundamental (negative) discriminant.  It was\nwritten by      Eduardo Ocampo Alvarez and  Andrey Timofeev  from\nEssen and is in sage/rings/number_field/number_field.py.\n\nWe also have a function in sage/schemes/elliptic_curves/cm.py called\nhilbert_class_polynomial(D), which uses Magma to find more general\nH.C.polys (D is any negative integer congruent to 0,1 mod 4).\n\nFor fundamental discriminants D, these give the same answer, i.e.\nQuadraticField(D,'a').hilbert_class_polynomial() ==\nhilbert_class_polynomial(D).\n\nQuestion 1: does the code at #4990 (now merged actually work for\nnon-fundamental discriminants?  Someone might know;  testing it would\nneed a bit of coding, and I haven't done so.\n\nAssuming that the answer is \"yes\",\n\nQuestion 2: should we re-write the stand-alone function which takes as\nits argument any negative discriminant (not necessarily fundamental)\nand returns the appropriate H.C.poly, using the code now in\nnumber_field.py instead of calling Magma;  and then change the current\nmethod in number_field.py to just call that?  If so, where should the\nstand-alone function go:  (a) where it now is, in\nsage/schemes/elliptic_curves/cm.py, (b) in\nsage/rings/number_field/somewhere, (c) somewhere else ?  We could then\nalso make the H.C.poly a function of (possibly non-maximal) orders in\n(imaginary quadratic) number fields.\n\nJohn\n\nPS I found this out while converting cm.py to ReST for inclusion in\nthe manual.  Isn't it amazing what you find!",
    "created_at": "2009-04-20T12:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4990#issuecomment-38017",
    "user": "https://github.com/JohnCremona"
}
```

Posted to sage-nt 2009-04-20:

Ticket #4990 implemented a hilbert_class_polynomial() method for
imaginary quadratic fields.  It is actually a function of the field's
discriminant, i.e. of a fundamental (negative) discriminant.  It was
written by      Eduardo Ocampo Alvarez and  Andrey Timofeev  from
Essen and is in sage/rings/number_field/number_field.py.

We also have a function in sage/schemes/elliptic_curves/cm.py called
hilbert_class_polynomial(D), which uses Magma to find more general
H.C.polys (D is any negative integer congruent to 0,1 mod 4).

For fundamental discriminants D, these give the same answer, i.e.
QuadraticField(D,'a').hilbert_class_polynomial() ==
hilbert_class_polynomial(D).

Question 1: does the code at #4990 (now merged actually work for
non-fundamental discriminants?  Someone might know;  testing it would
need a bit of coding, and I haven't done so.

Assuming that the answer is "yes",

Question 2: should we re-write the stand-alone function which takes as
its argument any negative discriminant (not necessarily fundamental)
and returns the appropriate H.C.poly, using the code now in
number_field.py instead of calling Magma;  and then change the current
method in number_field.py to just call that?  If so, where should the
stand-alone function go:  (a) where it now is, in
sage/schemes/elliptic_curves/cm.py, (b) in
sage/rings/number_field/somewhere, (c) somewhere else ?  We could then
also make the H.C.poly a function of (possibly non-maximal) orders in
(imaginary quadratic) number fields.

John

PS I found this out while converting cm.py to ReST for inclusion in
the manual.  Isn't it amazing what you find!
