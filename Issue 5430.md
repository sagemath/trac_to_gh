# Issue 5430: [with patch, positive review] Coleman integrals of differential forms from different rings

archive/issues_005430.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @robertwb\n\nThe coercion seems to be fine, but the Coleman integral fails:\n\n```\nsage: R.<x> = QQ['x']\nsage: H = HyperellipticCurve(x*(x-1)*(x+9))\nsage: K = Qp(7,10)\nsage: HK = H.change_ring(K)\nsage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw\nsage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)\nsage: w = HK.invariant_differential()\nsage: x,y = HK.monsky_washnitzer_gens()\nsage: f = forms[0]\nsage: S= HK(9,36)\nsage: Q = HK.teichmuller(S)\nsage: P = HK(-1,4)\nsage: b = x*w*w._coeff.parent()(f)            #this is ok\nsage: HK.coleman_integral(b,P,Q)              #this is not\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5430\n\n",
    "closed_at": "2009-06-01T06:13:09Z",
    "created_at": "2009-03-03T18:10:24Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] Coleman integrals of differential forms from different rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5430",
    "user": "https://github.com/jbalakrishnan"
}
```
Assignee: @robertwb

CC:  @robertwb

The coercion seems to be fine, but the Coleman integral fails:

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x*(x-1)*(x+9))
sage: K = Qp(7,10)
sage: HK = H.change_ring(K)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)
sage: w = HK.invariant_differential()
sage: x,y = HK.monsky_washnitzer_gens()
sage: f = forms[0]
sage: S= HK(9,36)
sage: Q = HK.teichmuller(S)
sage: P = HK(-1,4)
sage: b = x*w*w._coeff.parent()(f)            #this is ok
sage: HK.coleman_integral(b,P,Q)              #this is not
```

Issue created by migration from https://trac.sagemath.org/ticket/5430





---

archive/issue_comments_041931.json:
```json
{
    "body": "The end of the traceback is \n\n```\n  File \"parent.pyx\", line 276, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)\n  File \"coerce_maps.pyx\", line 76, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)\n  File \"coerce_maps.pyx\", line 71, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)\n  File \"rational.pyx\", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4233)\n  File \"rational.pyx\", line 312, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:5261)\n  File \"padic_generic_element.pyx\", line 748, in sage.rings.padics.padic_generic_element.pAdicGenericElement.rational_reconstruction (sage/rings/padics/padic_generic_element.c:7584)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/arith.py\", line 1516, in rational_reconstruction\n    return ZZ(a).rational_reconstruction(m)\n  File \"integer.pyx\", line 1981, in sage.rings.integer.Integer.rational_reconstruction (sage/rings/integer.c:13544)\n  File \"rational.pyx\", line 2345, in sage.rings.rational.pyrex_rational_reconstruction (sage/rings/rational.c:15562)\n  File \"gmp.pxi\", line 144, in sage.rings.rational.mpq_rational_reconstruction (sage/rings/rational.c:3032)\nValueError: Rational reconstruction of 253015590 (mod 282475249) does not exist.\n```\n\nThe question is, should this be an error, or just work? \n\n```\nsage: K = Qp(5, 10)\nsage: a = K(1/250037); a\n3 + 4*5 + 3*5^2 + 3*5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 4*5^8 + 4*5^9 + O(5^10)\nsage: ZZ(a)\n9472973\nsage: QQ(a)\nTraceback (most recent call last):\n...\nValueError: Rational reconstruction of 9472973 (mod 9765625) does not exist.\n```",
    "created_at": "2009-03-03T22:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41931",
    "user": "https://github.com/robertwb"
}
```

The end of the traceback is 

```
  File "parent.pyx", line 276, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)
  File "coerce_maps.pyx", line 76, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)
  File "coerce_maps.pyx", line 71, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)
  File "rational.pyx", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4233)
  File "rational.pyx", line 312, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:5261)
  File "padic_generic_element.pyx", line 748, in sage.rings.padics.padic_generic_element.pAdicGenericElement.rational_reconstruction (sage/rings/padics/padic_generic_element.c:7584)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1516, in rational_reconstruction
    return ZZ(a).rational_reconstruction(m)
  File "integer.pyx", line 1981, in sage.rings.integer.Integer.rational_reconstruction (sage/rings/integer.c:13544)
  File "rational.pyx", line 2345, in sage.rings.rational.pyrex_rational_reconstruction (sage/rings/rational.c:15562)
  File "gmp.pxi", line 144, in sage.rings.rational.mpq_rational_reconstruction (sage/rings/rational.c:3032)
ValueError: Rational reconstruction of 253015590 (mod 282475249) does not exist.
```

The question is, should this be an error, or just work? 

```
sage: K = Qp(5, 10)
sage: a = K(1/250037); a
3 + 4*5 + 3*5^2 + 3*5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 4*5^8 + 4*5^9 + O(5^10)
sage: ZZ(a)
9472973
sage: QQ(a)
Traceback (most recent call last):
...
ValueError: Rational reconstruction of 9472973 (mod 9765625) does not exist.
```



---

archive/issue_comments_041932.json:
```json
{
    "body": "No patch -> better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

No patch -> better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_events_012674.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-04T19:34:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5430#event-12674"
}
```



---

archive/issue_comments_041933.json:
```json
{
    "body": "> The question is, should this be an error, or just work? \n> \n> \n> ```\n> sage: K = Qp(5, 10)\n> sage: a = K(1/250037); a\n> 3 + 4*5 + 3*5^2 + 3*5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 4*5^8 + 4*5^9 + O(5^10)\n> sage: ZZ(a)\n> 9472973\n> sage: QQ(a)\n> Traceback (most recent call last):\n> ...\n> ValueError: Rational reconstruction of 9472973 (mod 9765625) does not exist.\n> ```\n\n\nIt seems like a valid error: 250037 is too large compared to 5^10.",
    "created_at": "2009-03-17T05:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41933",
    "user": "https://github.com/roed314"
}
```

> The question is, should this be an error, or just work? 
> 
> 
> ```
> sage: K = Qp(5, 10)
> sage: a = K(1/250037); a
> 3 + 4*5 + 3*5^2 + 3*5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 4*5^8 + 4*5^9 + O(5^10)
> sage: ZZ(a)
> 9472973
> sage: QQ(a)
> Traceback (most recent call last):
> ...
> ValueError: Rational reconstruction of 9472973 (mod 9765625) does not exist.
> ```


It seems like a valid error: 250037 is too large compared to 5^10.



---

archive/issue_comments_041934.json:
```json
{
    "body": "THe question is, should QQ(a) be the same as QQ(ZZ(a)) if rational reconstruction isn't possible? (I'm not convinced either way yet.)",
    "created_at": "2009-03-17T05:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41934",
    "user": "https://github.com/robertwb"
}
```

THe question is, should QQ(a) be the same as QQ(ZZ(a)) if rational reconstruction isn't possible? (I'm not convinced either way yet.)



---

archive/issue_comments_041935.json:
```json
{
    "body": "I'd say (and I think Robert agrees) that the correct way to fix the original problem is to do all the arithmetic for Coleman integration in the p-adics, eliminating the casting to/from the rationals altogether. That was a hack from back when p-adic arithmetic was unusably slow.\n\nIf there is an issue with rational reconstruction, I'd say make that a separate ticket.",
    "created_at": "2009-05-20T19:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41935",
    "user": "https://github.com/kedlaya"
}
```

I'd say (and I think Robert agrees) that the correct way to fix the original problem is to do all the arithmetic for Coleman integration in the p-adics, eliminating the casting to/from the rationals altogether. That was a hack from back when p-adic arithmetic was unusably slow.

If there is an issue with rational reconstruction, I'd say make that a separate ticket.



---

archive/issue_comments_041936.json:
```json
{
    "body": "Attachment [5430.patch](tarball://root/attachments/some-uuid/ticket5430/5430.patch) by @kedlaya created at 2009-05-21 06:14:30",
    "created_at": "2009-05-21T06:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41936",
    "user": "https://github.com/kedlaya"
}
```

Attachment [5430.patch](tarball://root/attachments/some-uuid/ticket5430/5430.patch) by @kedlaya created at 2009-05-21 06:14:30



---

archive/issue_comments_041937.json:
```json
{
    "body": "Attachment [5430-2.patch](tarball://root/attachments/some-uuid/ticket5430/5430-2.patch) by @kedlaya created at 2009-05-21 06:24:04\n\nSee attached patches. The first one eliminates all casting to/from QQ (I think). The second one adds a doctest to confirm that the above example now works:\n\n```\nsage: R.<x> = QQ['x']\nsage: H = HyperellipticCurve(x*(x-1)*(x+9))\nsage: K = Qp(7,10)\nsage: HK = H.change_ring(K)\nsage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw\nsage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)\nsage: w = HK.invariant_differential()\nsage: x,y = HK.monsky_washnitzer_gens()\nsage: f = forms[0]\nsage: S= HK(9,36)\nsage: Q = HK.teichmuller(S)\nsage: P = HK(-1,4)\nsage: b = x*w*w._coeff.parent()(f)\nsage: HK.coleman_integral(b,P,Q)\n7 + 7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^6 + 5*7^7 + 3*7^8 + 4*7^9 + 4*7^10 + O(7^11)\n```",
    "created_at": "2009-05-21T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41937",
    "user": "https://github.com/kedlaya"
}
```

Attachment [5430-2.patch](tarball://root/attachments/some-uuid/ticket5430/5430-2.patch) by @kedlaya created at 2009-05-21 06:24:04

See attached patches. The first one eliminates all casting to/from QQ (I think). The second one adds a doctest to confirm that the above example now works:

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x*(x-1)*(x+9))
sage: K = Qp(7,10)
sage: HK = H.change_ring(K)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)
sage: w = HK.invariant_differential()
sage: x,y = HK.monsky_washnitzer_gens()
sage: f = forms[0]
sage: S= HK(9,36)
sage: Q = HK.teichmuller(S)
sage: P = HK(-1,4)
sage: b = x*w*w._coeff.parent()(f)
sage: HK.coleman_integral(b,P,Q)
7 + 7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^6 + 5*7^7 + 3*7^8 + 4*7^9 + 4*7^10 + O(7^11)
```



---

archive/issue_comments_041938.json:
```json
{
    "body": "Attachment [5430-v2.patch](tarball://root/attachments/some-uuid/ticket5430/5430-v2.patch) by @kedlaya created at 2009-05-22 21:09:20\n\nRebased against the revised patch to #5948. You may ignore the previous two patches.",
    "created_at": "2009-05-22T21:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41938",
    "user": "https://github.com/kedlaya"
}
```

Attachment [5430-v2.patch](tarball://root/attachments/some-uuid/ticket5430/5430-v2.patch) by @kedlaya created at 2009-05-22 21:09:20

Rebased against the revised patch to #5948. You may ignore the previous two patches.



---

archive/issue_comments_041939.json:
```json
{
    "body": "It's nice to have decent enough p-adics to use them!",
    "created_at": "2009-05-22T21:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41939",
    "user": "https://github.com/robertwb"
}
```

It's nice to have decent enough p-adics to use them!



---

archive/issue_comments_041940.json:
```json
{
    "body": "So it looks like I didn't manage to get out all of the casting; there is still some in matrix_of_frobenius_hyperelliptic. But I'd say we should wait until #6084 is resolved before looking into that; in the interim, this suffices to fix the bug in question.",
    "created_at": "2009-05-23T18:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41940",
    "user": "https://github.com/kedlaya"
}
```

So it looks like I didn't manage to get out all of the casting; there is still some in matrix_of_frobenius_hyperelliptic. But I'd say we should wait until #6084 is resolved before looking into that; in the interim, this suffices to fix the bug in question.



---

archive/issue_comments_041941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41941",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_041942.json:
```json
{
    "body": "Merged 5430-v2.patch in 4.0.1.alpha0.",
    "created_at": "2009-06-01T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5430#issuecomment-41942",
    "user": "https://github.com/mwhansen"
}
```

Merged 5430-v2.patch in 4.0.1.alpha0.



---

archive/issue_events_012675.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-01T06:13:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5430",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5430#event-12675"
}
```
