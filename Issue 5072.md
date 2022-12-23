# Issue 5072: segfault in libsingular gcd when base rings aren't identical

archive/issues_005072.json:
```json
{
    "body": "Assignee: malb\n\nIf you take the gcd of a polynomial over GF(9) with one over GF(3), Sage SEGFAULTS.\n\n\n```\nteragon:sage-3.3.alpha0 wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: k.<a> = GF(9)\nsage: sage: R.<x,y> = PolynomialRing(k)\nsage: k.<a> = GF(9); R.<x,y> = PolynomialRing(k)\nsage: f = R.change_ring(GF(3)).gen()\nsage: g = x+y\nsage: g.gcd(f)\n| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\nteragon:sage-3.3.alpha0 wstein$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5072\n\n",
    "created_at": "2009-01-23T13:08:23Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "title": "segfault in libsingular gcd when base rings aren't identical",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5072",
    "user": "was"
}
```
Assignee: malb

If you take the gcd of a polynomial over GF(9) with one over GF(3), Sage SEGFAULTS.


```
teragon:sage-3.3.alpha0 wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: k.<a> = GF(9)
sage: sage: R.<x,y> = PolynomialRing(k)
sage: k.<a> = GF(9); R.<x,y> = PolynomialRing(k)
sage: f = R.change_ring(GF(3)).gen()
sage: g = x+y
sage: g.gcd(f)
| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

teragon:sage-3.3.alpha0 wstein$ 
```


Issue created by migration from https://trac.sagemath.org/ticket/5072





---

archive/issue_comments_038623.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T23:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5072#issuecomment-38623",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_038624.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T14:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5072#issuecomment-38624",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_038625.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T14:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5072#issuecomment-38625",
    "user": "mabshoff"
}
```

Resolution: fixed
