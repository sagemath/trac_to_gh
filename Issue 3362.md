# Issue 3362: lmul is broken for modules.

archive/issues_003362.json:
```json
{
    "body": "Assignee: robertwb\n\n\n```\nInteger(5)._lmul_(Integer(3))\n```\n\n should produce 15, but instead throws\n\n```\nNotImplementedError: parents Integer Ring Integer Ring True\n```\n\nThis makes it hard to write general code that works with noncomutative multiplication.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3362\n\n",
    "created_at": "2008-06-04T16:19:22Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "lmul is broken for modules.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3362",
    "user": "gfurnish"
}
```
Assignee: robertwb


```
Integer(5)._lmul_(Integer(3))
```

 should produce 15, but instead throws

```
NotImplementedError: parents Integer Ring Integer Ring True
```

This makes it hard to write general code that works with noncomutative multiplication.  

Issue created by migration from https://trac.sagemath.org/ticket/3362





---

archive/issue_comments_023526.json:
```json
{
    "body": "If a._lmul_(b) is desired, why can't one simply write a*b? \n\nThe raising of a NotImplementedError in _lmul_ signifies that _lmul_ is not implemented, and the two elements should be coerced into a common parent where the normal _mul_ should be used instead.",
    "created_at": "2008-06-05T10:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3362#issuecomment-23526",
    "user": "robertwb"
}
```

If a._lmul_(b) is desired, why can't one simply write a*b? 

The raising of a NotImplementedError in _lmul_ signifies that _lmul_ is not implemented, and the two elements should be coerced into a common parent where the normal _mul_ should be used instead.



---

archive/issue_comments_023527.json:
```json
{
    "body": "Robert, any idea what is going on here? \n\nThis is still broken with \"new\" coercion:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: Integer(5)._lmul_(Integer(3))\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement._lmul_ (sage/structure/element.c:8032)()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement._lmul_ (sage/structure/element.c:8002)()\n\nNotImplementedError: parents Integer Ring Integer Ring True\nsage: \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T16:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3362#issuecomment-23527",
    "user": "mabshoff"
}
```

Robert, any idea what is going on here? 

This is still broken with "new" coercion:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: Integer(5)._lmul_(Integer(3))
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement._lmul_ (sage/structure/element.c:8032)()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement._lmul_ (sage/structure/element.c:8002)()

NotImplementedError: parents Integer Ring Integer Ring True
sage: 
```


Cheers,

Michael



---

archive/issue_comments_023528.json:
```json
{
    "body": "This should be marked as invalid. _lmul_ and _rmul_ are used for multiplication by an element of the basering, not for multiplication of elements themselves. Throwing an error here is the right thing to do, as it signals that the coercion model an action is not the appropriate thing to do here, but rather that both a and b should be coerced to the same parent and a._mul_(b) should be called. \n\nWriting a*b or b*a preserves the order of operands are fed into _mul_, so non-commutative operations can be supported just fine. \n\n_lmul_, _rmul_, etc. are not made to be called directly anyways in most cases.",
    "created_at": "2008-10-28T17:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3362#issuecomment-23528",
    "user": "robertwb"
}
```

This should be marked as invalid. _lmul_ and _rmul_ are used for multiplication by an element of the basering, not for multiplication of elements themselves. Throwing an error here is the right thing to do, as it signals that the coercion model an action is not the appropriate thing to do here, but rather that both a and b should be coerced to the same parent and a._mul_(b) should be called. 

Writing a*b or b*a preserves the order of operands are fed into _mul_, so non-commutative operations can be supported just fine. 

_lmul_, _rmul_, etc. are not made to be called directly anyways in most cases.



---

archive/issue_comments_023529.json:
```json
{
    "body": "RobertWB's wish is my command -> Invalid. :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T17:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3362#issuecomment-23529",
    "user": "mabshoff"
}
```

RobertWB's wish is my command -> Invalid. :)

Cheers,

Michael



---

archive/issue_comments_023530.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-28T17:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3362#issuecomment-23530",
    "user": "mabshoff"
}
```

Resolution: invalid
