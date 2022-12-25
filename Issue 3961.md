# Issue 3961: bug in ell_finite_field.abelian_group()

archive/issues_003961.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  alexghitza\n\nKeywords: elliptic curve fineite field\n\nThis works in 3.1.1:\n\n```\nsage: p=10^4+7; p       \n10007\nsage: F.<i>=GF(p^2)\nsage: E = EllipticCurve([0,0,0,i,i+3]); E\nElliptic Curve defined by y^2  = x^3 + i*x + (i+3) over Finite Field in i of size 10007^2\nsage: E.abelian_group()\n\n(Multiplicative Abelian Group isomorphic to C100130006,\n ((8287*i + 5423 : 9131*i + 6741 : 1),))\n```\n\nbut this does not:\n\n```\nsage: K.<i> = QuadraticField(-1)\nsage: P=K.factor(p)[0][0]; P\nFractional ideal (10007)\nsage: E = EllipticCurve([0,0,0,i,i+3]); E\nElliptic Curve defined by y^2  = x^3 + i*x + (i+3) over Number Field in i with defining polynomial x^2 + 1            \nsage: Emod = E.change_ring(K.ring_of_integers().residue_field(P)); Emod\nElliptic Curve defined by y^2  = x^3 + ibar*x + (ibar+3) over Residue field in ibar of Fractional ideal (10007)\nsage: Emod.abelian_group()\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n\n/home/john/sage-3.1.final/<ipython console> in <module>()\n\n/home/john/sage-3.1.final/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in abelian_group(self, debug)\n   1121                 if debug: print \"n1a=\",n1a\n   1122                 a = None\n-> 1123                 for m in (N//n1).divisors():\n   1124                     try:\n   1125                         a = generic.bsgs(m*P1a,m*Q,(0,(n1b//m)-1),operation='+')\n\nUnboundLocalError: local variable 'N' referenced before assignment\n```\n\nThat's a bug in code I wrote, and I will fix it.  But it's a mystery why it only arises when the same (abstract) finite field is defined as a quotient field of ZZ[i].\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3961\n\n",
    "created_at": "2008-08-26T19:48:12Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bug in ell_finite_field.abelian_group()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3961",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

CC:  alexghitza

Keywords: elliptic curve fineite field

This works in 3.1.1:

```
sage: p=10^4+7; p       
10007
sage: F.<i>=GF(p^2)
sage: E = EllipticCurve([0,0,0,i,i+3]); E
Elliptic Curve defined by y^2  = x^3 + i*x + (i+3) over Finite Field in i of size 10007^2
sage: E.abelian_group()

(Multiplicative Abelian Group isomorphic to C100130006,
 ((8287*i + 5423 : 9131*i + 6741 : 1),))
```

but this does not:

```
sage: K.<i> = QuadraticField(-1)
sage: P=K.factor(p)[0][0]; P
Fractional ideal (10007)
sage: E = EllipticCurve([0,0,0,i,i+3]); E
Elliptic Curve defined by y^2  = x^3 + i*x + (i+3) over Number Field in i with defining polynomial x^2 + 1            
sage: Emod = E.change_ring(K.ring_of_integers().residue_field(P)); Emod
Elliptic Curve defined by y^2  = x^3 + ibar*x + (ibar+3) over Residue field in ibar of Fractional ideal (10007)
sage: Emod.abelian_group()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/home/john/sage-3.1.final/<ipython console> in <module>()

/home/john/sage-3.1.final/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in abelian_group(self, debug)
   1121                 if debug: print "n1a=",n1a
   1122                 a = None
-> 1123                 for m in (N//n1).divisors():
   1124                     try:
   1125                         a = generic.bsgs(m*P1a,m*Q,(0,(n1b//m)-1),operation='+')

UnboundLocalError: local variable 'N' referenced before assignment
```

That's a bug in code I wrote, and I will fix it.  But it's a mystery why it only arises when the same (abstract) finite field is defined as a quotient field of ZZ[i].


Issue created by migration from https://trac.sagemath.org/ticket/3961





---

archive/issue_comments_028393.json:
```json
{
    "body": "Attachment [sage-trac3926.patch](tarball://root/attachments/some-uuid/ticket3961/sage-trac3926.patch) by @JohnCremona created at 2008-08-27 09:55:13",
    "created_at": "2008-08-27T09:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28393",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-trac3926.patch](tarball://root/attachments/some-uuid/ticket3961/sage-trac3926.patch) by @JohnCremona created at 2008-08-27 09:55:13



---

archive/issue_comments_028394.json:
```json
{
    "body": "The attached patch fixes the bug (and at the same time slightly improves the debug output, and also introduces a small speedup).  The bug was in the line now number 1135.\n\nThe apparent inconsistency noted at the end of the bug report is bogus:  the default generator for `GF(10007^2)` is not sqrt(-1) so the two curves are actually different.\n\nPatch is based on 3.1.1, and all doctests in sage.schemes.elliptic_curves pass.",
    "created_at": "2008-08-27T09:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28394",
    "user": "https://github.com/JohnCremona"
}
```

The attached patch fixes the bug (and at the same time slightly improves the debug output, and also introduces a small speedup).  The bug was in the line now number 1135.

The apparent inconsistency noted at the end of the bug report is bogus:  the default generator for `GF(10007^2)` is not sqrt(-1) so the two curves are actually different.

Patch is based on 3.1.1, and all doctests in sage.schemes.elliptic_curves pass.



---

archive/issue_comments_028395.json:
```json
{
    "body": "Changing keywords from \"elliptic curve fineite field\" to \"elliptic curve finite field\".",
    "created_at": "2008-08-27T09:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28395",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "elliptic curve fineite field" to "elliptic curve finite field".



---

archive/issue_comments_028396.json:
```json
{
    "body": "Changing component from algebra to number theory.",
    "created_at": "2008-08-27T09:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28396",
    "user": "https://github.com/JohnCremona"
}
```

Changing component from algebra to number theory.



---

archive/issue_comments_028397.json:
```json
{
    "body": "The patch indeed fixes the bug, and there is a small speed gain.",
    "created_at": "2008-08-29T04:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28397",
    "user": "https://github.com/aghitza"
}
```

The patch indeed fixes the bug, and there is a small speed gain.



---

archive/issue_comments_028398.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T06:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_events_009090.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-29T06:29:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3961#event-9090"
}
```



---

archive/issue_comments_028399.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T06:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3961#issuecomment-28399",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
