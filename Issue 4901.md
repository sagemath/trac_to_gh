# Issue 4901: bug in elliptic logarithm

archive/issues_004901.json:
```json
{
    "body": "Assignee: was\n\nCC:  alexghitza\n\nKeywords: elliptic logarithm\n\n#4214 introduced something which causes this example to fail:\n\n```\nsage: EllipticCurve(\"4390c2\").gens()[0].elliptic_logarithm()\n---------------------------------------------------------------------------\nMemoryError                               Traceback (most recent call last)\n\n/home/john/sage-3.2.2.rc1/devel/sage-elllog/<ipython console> in <module>()\n\n/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in elliptic_logarithm(self, embedding, precision, algorithm)\n   1211             E_pari = ER.pari_curve(prec=precision)\n   1212             pt_pari = [pari(emb(self[0])), pari(emb(self[1]))]\n-> 1213             log_pari = E_pari.ellpointtoz(pt_pari, precision=precision)\n   1214             while prec_words_to_bits(log_pari.precision()) < precision:\n   1215                 working_prec = 2*precision\n\n/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38603)()\n\n/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.allocatemem (sage/libs/pari/gen.c:34732)()\n\n/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.init_stack (sage/libs/pari/gen.c:37647)()\n\nMemoryError: Unable to allocate 4096000000 bytes memory for PARI.\n```\n\ncaused by an infinite loop.\n\nThe problem has been diagnosed by me and Alex and I'll post a patch shortly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4901\n\n",
    "created_at": "2009-01-01T16:28:39Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bug in elliptic logarithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4901",
    "user": "cremona"
}
```
Assignee: was

CC:  alexghitza

Keywords: elliptic logarithm

#4214 introduced something which causes this example to fail:

```
sage: EllipticCurve("4390c2").gens()[0].elliptic_logarithm()
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)

/home/john/sage-3.2.2.rc1/devel/sage-elllog/<ipython console> in <module>()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in elliptic_logarithm(self, embedding, precision, algorithm)
   1211             E_pari = ER.pari_curve(prec=precision)
   1212             pt_pari = [pari(emb(self[0])), pari(emb(self[1]))]
-> 1213             log_pari = E_pari.ellpointtoz(pt_pari, precision=precision)
   1214             while prec_words_to_bits(log_pari.precision()) < precision:
   1215                 working_prec = 2*precision

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38603)()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.allocatemem (sage/libs/pari/gen.c:34732)()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.init_stack (sage/libs/pari/gen.c:37647)()

MemoryError: Unable to allocate 4096000000 bytes memory for PARI.
```

caused by an infinite loop.

The problem has been diagnosed by me and Alex and I'll post a patch shortly.


Issue created by migration from https://trac.sagemath.org/ticket/4901





---

archive/issue_comments_037181.json:
```json
{
    "body": "Attachment [elllog-2.patch](tarball://root/attachments/some-uuid/ticket4901/elllog-2.patch) by cremona created at 2009-01-01 18:41:00",
    "created_at": "2009-01-01T18:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4901#issuecomment-37181",
    "user": "cremona"
}
```

Attachment [elllog-2.patch](tarball://root/attachments/some-uuid/ticket4901/elllog-2.patch) by cremona created at 2009-01-01 18:41:00



---

archive/issue_comments_037182.json:
```json
{
    "body": "The infinite loop was fixed by Alex, who then said\n\n```\nWe seem to have run into a different problem, though:\n\nsage: E = EllipticCurve(\"4390c2\")\nsage: P = E.gens()[0]\nsage: P.elliptic_logarithm(precision=64)\n0.000256387258865202254\nsage: P.elliptic_logarithm(precision=65)\n0.0002563872588652022535 + 0.004614954316673684681*I\nsage: P.elliptic_logarithm(precision=128)\n0.00025638725886520225353198932528666427412 + 0.0046149543166736846806755335569568366865*I\nsage: P.elliptic_logarithm(precision=129)\n0.00025638725886520225353198932528666427412\nsage: P.elliptic_logarithm(precision=256)\n0.0002563872588652022535319893252866642741168388008346370015005142128009610936373\nsage: P.elliptic_logarithm(precision=257)\n0.00025638725886520225353198932528666427411683880083463700150051421280096109363730 + 0.0046149543166736846806755335569568366865361459796795879146958143680521472570409*I\n\nThis is quite upsetting.\n```\n\nto which John replied\n\n```\nThe explanation is that  0.004614954316673684681*I is the imaginary\nperiod.  the point P is on the identity component so its e-log should\nbe a real multiple of the real period, but is obviously only\ndetermined up to addition of any period.  Clearly the pari code does\nnot bother about that.\n\nHere's one fix:  if P.is_on_identity_component(emb) is True then we\nknow that the result should be real, so we can kill the imaginary\npart, and also normalise by making sure that the real part divided by\nthe real period is in [0,1).  That's not hard.  And if P is not on the\nid. component, do the same but set the imaginary part to equal exactly\nhalf the imaginary period.\n```\n\n\nThe attached patch does both.  Based on 3.2.2, tested on 32-bit and 64-bit.",
    "created_at": "2009-01-01T18:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4901#issuecomment-37182",
    "user": "cremona"
}
```

The infinite loop was fixed by Alex, who then said

```
We seem to have run into a different problem, though:

sage: E = EllipticCurve("4390c2")
sage: P = E.gens()[0]
sage: P.elliptic_logarithm(precision=64)
0.000256387258865202254
sage: P.elliptic_logarithm(precision=65)
0.0002563872588652022535 + 0.004614954316673684681*I
sage: P.elliptic_logarithm(precision=128)
0.00025638725886520225353198932528666427412 + 0.0046149543166736846806755335569568366865*I
sage: P.elliptic_logarithm(precision=129)
0.00025638725886520225353198932528666427412
sage: P.elliptic_logarithm(precision=256)
0.0002563872588652022535319893252866642741168388008346370015005142128009610936373
sage: P.elliptic_logarithm(precision=257)
0.00025638725886520225353198932528666427411683880083463700150051421280096109363730 + 0.0046149543166736846806755335569568366865361459796795879146958143680521472570409*I

This is quite upsetting.
```

to which John replied

```
The explanation is that  0.004614954316673684681*I is the imaginary
period.  the point P is on the identity component so its e-log should
be a real multiple of the real period, but is obviously only
determined up to addition of any period.  Clearly the pari code does
not bother about that.

Here's one fix:  if P.is_on_identity_component(emb) is True then we
know that the result should be real, so we can kill the imaginary
part, and also normalise by making sure that the real part divided by
the real period is in [0,1).  That's not hard.  And if P is not on the
id. component, do the same but set the imaginary part to equal exactly
half the imaginary period.
```


The attached patch does both.  Based on 3.2.2, tested on 32-bit and 64-bit.



---

archive/issue_comments_037183.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-03T17:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4901#issuecomment-37183",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_037184.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T01:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4901#issuecomment-37184",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_037185.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T01:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4901#issuecomment-37185",
    "user": "mabshoff"
}
```

Resolution: fixed
