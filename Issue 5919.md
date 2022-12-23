# Issue 5919: [with patch, needs review] bug in conversion of polys over GF(2,e) from NTL to singular

archive/issues_005919.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexghitza malb\n\nKeywords: polynomial finite field\n\nIn 3.4.2.alpha0 we have\n\n```\nsage: F.<a> = GF(2^16)\nsage: R.<x, y> = F[]\nsage: R({(1,2):1})\n0*x*y^2\n```\n\nwhich Alex Ghitza tracked down to a line in libs/singular/singular.pyx and which I fixed by replacing one character in that line from 'i' to '0'.  After that:\n\n```\nsage: sage: F.<a> = GF(2^16)\nsage: sage: R.<x, y> = F[]\nsage: sage: R({(1,2):1})\nx*y^2\n```\n\nand hence also\n\n```\nsage: Fx.<b>=GF(2^(4*5))\nsage: Ex=EllipticCurve(Fx,[0,0,1,1,1])\nsage: Ex.defining_polynomial()\nx^3 + y^2*z + x*z^2 + y*z^2 + z^3\n```\n\nwhich was not working properly (as reported to sage-devel).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5919\n\n",
    "created_at": "2009-04-28T15:40:18Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] bug in conversion of polys over GF(2,e) from NTL to singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5919",
    "user": "cremona"
}
```
Assignee: tbd

CC:  alexghitza malb

Keywords: polynomial finite field

In 3.4.2.alpha0 we have

```
sage: F.<a> = GF(2^16)
sage: R.<x, y> = F[]
sage: R({(1,2):1})
0*x*y^2
```

which Alex Ghitza tracked down to a line in libs/singular/singular.pyx and which I fixed by replacing one character in that line from 'i' to '0'.  After that:

```
sage: sage: F.<a> = GF(2^16)
sage: sage: R.<x, y> = F[]
sage: sage: R({(1,2):1})
x*y^2
```

and hence also

```
sage: Fx.<b>=GF(2^(4*5))
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
sage: Ex.defining_polynomial()
x^3 + y^2*z + x*z^2 + y*z^2 + z^3
```

which was not working properly (as reported to sage-devel).



Issue created by migration from https://trac.sagemath.org/ticket/5919





---

archive/issue_comments_046783.json:
```json
{
    "body": "Attachment\n\napplies to 3.4.2.alpha0",
    "created_at": "2009-04-28T15:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5919#issuecomment-46783",
    "user": "cremona"
}
```

Attachment

applies to 3.4.2.alpha0



---

archive/issue_comments_046784.json:
```json
{
    "body": "Patch looks good.",
    "created_at": "2009-04-28T15:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5919#issuecomment-46784",
    "user": "malb"
}
```

Patch looks good.



---

archive/issue_comments_046785.json:
```json
{
    "body": "Thanks -- I did not add a doctest, since the function in which the bug was is a long way (it seems) from the user level where the above examples make sense.\n\nSpecifically, the bug is in the cdef function  Conversion.*sa2si_GFqNTLGF2E(self, FiniteField_ntl_gf2eElement elem, ring *_ring) which has an empty docstring!",
    "created_at": "2009-04-28T15:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5919#issuecomment-46785",
    "user": "cremona"
}
```

Thanks -- I did not add a doctest, since the function in which the bug was is a long way (it seems) from the user level where the above examples make sense.

Specifically, the bug is in the cdef function  Conversion.*sa2si_GFqNTLGF2E(self, FiniteField_ntl_gf2eElement elem, ring *_ring) which has an empty docstring!



---

archive/issue_comments_046786.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T22:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5919#issuecomment-46786",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046787.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-29T22:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5919#issuecomment-46787",
    "user": "mabshoff"
}
```

Resolution: fixed
