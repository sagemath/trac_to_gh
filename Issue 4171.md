# Issue 4171: SR + long broken

archive/issues_004171.json:
```json
{
    "body": "Assignee: somebody\n\nAdding a long to a symbolic variable is broken:\n\n\n```\nOK\nsage: x + int(5) \nx + 5\n\nNot OK:\nsage: x + long(5)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/wstein/<ipython console> in <module>()\n\n/home/wstein/element.pyx in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5748)()\n\n/home/wstein/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6364)()\n\nTypeError: unsupported operand parent(s) for '+': 'Symbolic Ring' and '<type 'long'>'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4171\n\n",
    "created_at": "2008-09-23T01:12:46Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "SR + long broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4171",
    "user": "@williamstein"
}
```
Assignee: somebody

Adding a long to a symbolic variable is broken:


```
OK
sage: x + int(5) 
x + 5

Not OK:
sage: x + long(5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/element.pyx in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5748)()

/home/wstein/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6364)()

TypeError: unsupported operand parent(s) for '+': 'Symbolic Ring' and '<type 'long'>'
```


Issue created by migration from https://trac.sagemath.org/ticket/4171





---

archive/issue_comments_030273.json:
```json
{
    "body": "Related (and maybe the root of the problem): \n\n\n```\nsage: SR(long(2))     \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/plot/<ipython console> in <module>()\n\n/home/grout/downloads/sage-3.1.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, x)\n\n/home/grout/downloads/sage-3.1.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _coerce_impl(self, x)\n\nTypeError: cannot coerce type '<type 'long'>' into a SymbolicExpression.\n```\n",
    "created_at": "2008-09-23T01:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4171#issuecomment-30273",
    "user": "@jasongrout"
}
```

Related (and maybe the root of the problem): 


```
sage: SR(long(2))     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/plot/<ipython console> in <module>()

/home/grout/downloads/sage-3.1.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, x)

/home/grout/downloads/sage-3.1.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _coerce_impl(self, x)

TypeError: cannot coerce type '<type 'long'>' into a SymbolicExpression.
```




---

archive/issue_comments_030274.json:
```json
{
    "body": "This is a dupe if #4170 which robertwb opened. Since that ticket has a patch I am closing this one as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T01:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4171#issuecomment-30274",
    "user": "mabshoff"
}
```

This is a dupe if #4170 which robertwb opened. Since that ticket has a patch I am closing this one as a dupe.

Cheers,

Michael



---

archive/issue_comments_030275.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-23T01:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4171#issuecomment-30275",
    "user": "mabshoff"
}
```

Resolution: duplicate
