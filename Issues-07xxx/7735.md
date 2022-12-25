# Issue 7735: incorrect sage exponentiation in interreduced_basis '^' vs '**'

archive/issues_007735.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: interreduced_basis\n\nThere is a bug in the code of interreduced_basis in\n\nsage/rings/polynomial/multi_polynomial_ideal.py\n\n```\nsage: R=QQ['t'].fraction_field()['x,y']                                                                              \nsage: R.inject_variables()                                                                                       \nDefining x, y                                                                                                    \nsage: I=x*R                                                                                                      \nsage: I.interreduced_basis()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/luisfe/<ipython console> in <module>()\n\n/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in wrapper(*args, **kwds)\n    362         \"\"\"\n    363         with RedSBContext():\n--> 364             return func(*args, **kwds)\n    365\n    366     from sage.misc.sageinspect import sage_getsource\n\n/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in interreduced_basis(self)\n   1542                 for f in self._singular_().interred():\n   1543                     f = R(f)\n-> 1544                     ret.append(f.lc()^(-1)*f) # lead coeffs are not reduced by interred\n   1545                 s.option(\"set\",o)\n   1546             except TypeError:\n\n/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__xor__ (sage/structure/element.c:4469)()\n\nRuntimeError: Use ** for exponentiation, not '^', which means xor\nin Python, and has the wrong precedence.\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7735\n\n",
    "closed_at": "2009-12-19T20:27:54Z",
    "created_at": "2009-12-18T13:42:36Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "incorrect sage exponentiation in interreduced_basis '^' vs '**'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7735",
    "user": "https://github.com/lftabera"
}
```
Assignee: @aghitza

Keywords: interreduced_basis

There is a bug in the code of interreduced_basis in

sage/rings/polynomial/multi_polynomial_ideal.py

```
sage: R=QQ['t'].fraction_field()['x,y']                                                                              
sage: R.inject_variables()                                                                                       
Defining x, y                                                                                                    
sage: I=x*R                                                                                                      
sage: I.interreduced_basis()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/luisfe/<ipython console> in <module>()

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in wrapper(*args, **kwds)
    362         """
    363         with RedSBContext():
--> 364             return func(*args, **kwds)
    365
    366     from sage.misc.sageinspect import sage_getsource

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in interreduced_basis(self)
   1542                 for f in self._singular_().interred():
   1543                     f = R(f)
-> 1544                     ret.append(f.lc()^(-1)*f) # lead coeffs are not reduced by interred
   1545                 s.option("set",o)
   1546             except TypeError:

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__xor__ (sage/structure/element.c:4469)()

RuntimeError: Use ** for exponentiation, not '^', which means xor
in Python, and has the wrong precedence.

```

Issue created by migration from https://trac.sagemath.org/ticket/7735





---

archive/issue_comments_066349.json:
```json
{
    "body": "Patch to correct the problem and a test case",
    "created_at": "2009-12-18T13:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66349",
    "user": "https://github.com/lftabera"
}
```

Patch to correct the problem and a test case



---

archive/issue_comments_066350.json:
```json
{
    "body": "Attachment [interreduced.patch](tarball://root/attachments/some-uuid/ticket7735/interreduced.patch) by @lftabera created at 2009-12-18 13:44:09",
    "created_at": "2009-12-18T13:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66350",
    "user": "https://github.com/lftabera"
}
```

Attachment [interreduced.patch](tarball://root/attachments/some-uuid/ticket7735/interreduced.patch) by @lftabera created at 2009-12-18 13:44:09



---

archive/issue_comments_066351.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-18T13:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66351",
    "user": "https://github.com/lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066352.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T16:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66352",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066353.json:
```json
{
    "body": "Changing keywords from \"interreduced_basis, python\" to \"interreduced_basis\".",
    "created_at": "2009-12-18T16:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66353",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "interreduced_basis, python" to "interreduced_basis".



---

archive/issue_comments_066354.json:
```json
{
    "body": "Looks good, applies to 4.3.rc0, tests pass and it has a relevant doctest.",
    "created_at": "2009-12-18T16:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66354",
    "user": "https://github.com/JohnCremona"
}
```

Looks good, applies to 4.3.rc0, tests pass and it has a relevant doctest.



---

archive/issue_events_018494.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-19T20:27:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7735#event-18494"
}
```



---

archive/issue_comments_066355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T20:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7735#issuecomment-66355",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
