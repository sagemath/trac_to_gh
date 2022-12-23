# Issue 3655: left multiplication in piecewise does not work

archive/issues_003655.json:
```json
{
    "body": "Assignee: gfurnish\n\nThis was reported by C Boncelet.\n\n\n```\nsage: x = PolynomialRing(QQ,'x').gen()\nsage: f = Piecewise([[(0,1),1*x^0]])\nsage: r = f*2\nsage: r = 2*f\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call\nlast)\n/Users/boncelet/<ipython console> in <module>()\n/Users/boncelet/element.pyx in\nsage.structure.element.RingElement.__mul__ (sage/structure/element.c:\n8545)()\n/Users/boncelet/coerce.pyx in\nsage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/\nstructure/coerce.c:5338)()\nTypeError: unsupported operand parent(s) for '*': 'Integer Ring' and\n'<type 'instance'>'\n```\n\n\nHe then suggested simply defining __rmul__ = __mul__:\n\n\n```\nsage: f.__rmul__ = f.__mul__\nsage: r = f*2\nsage: r = 2*f\nsage: r\nPiecewise defined function with 1 parts, [[(0, 1), 2]]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3655\n\n",
    "created_at": "2008-07-15T01:46:22Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "left multiplication in piecewise does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3655",
    "user": "wdj"
}
```
Assignee: gfurnish

This was reported by C Boncelet.


```
sage: x = PolynomialRing(QQ,'x').gen()
sage: f = Piecewise([[(0,1),1*x^0]])
sage: r = f*2
sage: r = 2*f
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)
/Users/boncelet/<ipython console> in <module>()
/Users/boncelet/element.pyx in
sage.structure.element.RingElement.__mul__ (sage/structure/element.c:
8545)()
/Users/boncelet/coerce.pyx in
sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/
structure/coerce.c:5338)()
TypeError: unsupported operand parent(s) for '*': 'Integer Ring' and
'<type 'instance'>'
```


He then suggested simply defining __rmul__ = __mul__:


```
sage: f.__rmul__ = f.__mul__
sage: r = f*2
sage: r = 2*f
sage: r
Piecewise defined function with 1 parts, [[(0, 1), 2]]
```



Issue created by migration from https://trac.sagemath.org/ticket/3655





---

archive/issue_comments_025842.json:
```json
{
    "body": "Attachment\n\nbased on 3.0.4",
    "created_at": "2008-07-15T10:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3655#issuecomment-25842",
    "user": "wdj"
}
```

Attachment

based on 3.0.4



---

archive/issue_comments_025843.json:
```json
{
    "body": "I added a patch implementing the suggestion above. It is just a few lines. Passes sage -testall.",
    "created_at": "2008-07-15T10:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3655#issuecomment-25843",
    "user": "wdj"
}
```

I added a patch implementing the suggestion above. It is just a few lines. Passes sage -testall.



---

archive/issue_comments_025844.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-26T22:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3655#issuecomment-25844",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_025845.json:
```json
{
    "body": "Looks good to me.  Apply both patches.",
    "created_at": "2008-08-26T22:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3655#issuecomment-25845",
    "user": "mhansen"
}
```

Looks good to me.  Apply both patches.



---

archive/issue_comments_025846.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T22:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3655#issuecomment-25846",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha1



---

archive/issue_comments_025847.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T22:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3655#issuecomment-25847",
    "user": "mabshoff"
}
```

Resolution: fixed
