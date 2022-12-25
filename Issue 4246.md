# Issue 4246: bug in coercing symbolic expressions to polynomial rings

archive/issues_004246.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @robertwb\n\nThis was reported by William Stein at #4106:\n\n  I did notice this unfortunate property of the _polynomial_ function that is used\n  to implement this patch, namely it does something dumb when given x+y as input: \n\n  {{{\n  sage: var('x')\n  x\n  sage: var('y')\n  y\n  sage: S = PolynomialRing(Integers(4),1,'x')\n  sage: S(x+y)\n  2*x\n  sage: (x+y)._polynomial_(S)\n  2*x\n  }}}\n\n  I think in this case it should raise a TypeError. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4246\n\n",
    "created_at": "2008-10-05T21:46:40Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "bug in coercing symbolic expressions to polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4246",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

CC:  @robertwb

This was reported by William Stein at #4106:

  I did notice this unfortunate property of the _polynomial_ function that is used
  to implement this patch, namely it does something dumb when given x+y as input: 

  {{{
  sage: var('x')
  x
  sage: var('y')
  y
  sage: S = PolynomialRing(Integers(4),1,'x')
  sage: S(x+y)
  2*x
  sage: (x+y)._polynomial_(S)
  2*x
  }}}

  I think in this case it should raise a TypeError. 


Issue created by migration from https://trac.sagemath.org/ticket/4246





---

archive/issue_comments_030808.json:
```json
{
    "body": "Attachment [trac4246-coerce_symbolic_into_polyrings.patch](tarball://root/attachments/some-uuid/ticket4246/trac4246-coerce_symbolic_into_polyrings.patch) by @aghitza created at 2008-10-05 21:49:01",
    "created_at": "2008-10-05T21:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30808",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac4246-coerce_symbolic_into_polyrings.patch](tarball://root/attachments/some-uuid/ticket4246/trac4246-coerce_symbolic_into_polyrings.patch) by @aghitza created at 2008-10-05 21:49:01



---

archive/issue_comments_030809.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-05T21:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30809",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030810.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-05T23:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30810",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_030811.json:
```json
{
    "body": "This patch breaks two doctests in coerce_maps.pyx:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3$ ./sage -t -long devel/sage/sage/structure/coerce_maps.pyx\nsage -t -long devel/sage/sage/structure/coerce_maps.pyx     \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/coerce_maps.py\", line 110:\n    sage: mor(x^2/4+1)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[4]>\", line 1, in <module>\n        mor(x**Integer(2)/Integer(4)+Integer(1))###line 110:\n    sage: mor(x^2/4+1)\n      File \"map.pyx\", line 133, in sage.categories.map.Map.__call__ (sage/categories/map.c:2755)\n      File \"coerce_maps.pyx\", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3348)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1886, in _polynomial_\n        raise TypeError, \"%s is not a variable of %s\" %(v, R)\n    TypeError: x is not a variable of Univariate Polynomial Ring in t over Rational Field\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/coerce_maps.py\", line 113:\n    sage: mor(x^2/4+1)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[6]>\", line 1, in <module>\n        mor(x**Integer(2)/Integer(4)+Integer(1))###line 113:\n    sage: mor(x^2/4+1)\n      File \"map.pyx\", line 133, in sage.categories.map.Map.__call__ (sage/categories/map.c:2755)\n      File \"coerce_maps.pyx\", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3348)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1886, in _polynomial_\n        raise TypeError, \"%s is not a variable of %s\" %(v, R)\n    TypeError: x is not a variable of Power Series Ring in t over Finite Field of size 7\n**********************************************************************\n```\n\n\nSince this is coercion related I am adding RobertWB to the CC.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T20:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch breaks two doctests in coerce_maps.pyx:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3$ ./sage -t -long devel/sage/sage/structure/coerce_maps.pyx
sage -t -long devel/sage/sage/structure/coerce_maps.pyx     
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/coerce_maps.py", line 110:
    sage: mor(x^2/4+1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        mor(x**Integer(2)/Integer(4)+Integer(1))###line 110:
    sage: mor(x^2/4+1)
      File "map.pyx", line 133, in sage.categories.map.Map.__call__ (sage/categories/map.c:2755)
      File "coerce_maps.pyx", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3348)
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1886, in _polynomial_
        raise TypeError, "%s is not a variable of %s" %(v, R)
    TypeError: x is not a variable of Univariate Polynomial Ring in t over Rational Field
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/coerce_maps.py", line 113:
    sage: mor(x^2/4+1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[6]>", line 1, in <module>
        mor(x**Integer(2)/Integer(4)+Integer(1))###line 113:
    sage: mor(x^2/4+1)
      File "map.pyx", line 133, in sage.categories.map.Map.__call__ (sage/categories/map.c:2755)
      File "coerce_maps.pyx", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3348)
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1886, in _polynomial_
        raise TypeError, "%s is not a variable of %s" %(v, R)
    TypeError: x is not a variable of Power Series Ring in t over Finite Field of size 7
**********************************************************************
```


Since this is coercion related I am adding RobertWB to the CC.

Cheers,

Michael



---

archive/issue_comments_030812.json:
```json
{
    "body": "Attachment [trac4246-coerce_symbolic_into_polyrings_1.patch](tarball://root/attachments/some-uuid/ticket4246/trac4246-coerce_symbolic_into_polyrings_1.patch) by @aghitza created at 2008-11-29 07:27:37",
    "created_at": "2008-11-29T07:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30812",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac4246-coerce_symbolic_into_polyrings_1.patch](tarball://root/attachments/some-uuid/ticket4246/trac4246-coerce_symbolic_into_polyrings_1.patch) by @aghitza created at 2008-11-29 07:27:37



---

archive/issue_comments_030813.json:
```json
{
    "body": "I added a small patch that changes the two failing doctests slightly so that they pass now.  I thought about the behaviour a bit and it seems sensible to me, but Robert should feel free to defend the original doctests if necessary.",
    "created_at": "2008-11-29T07:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30813",
    "user": "https://github.com/aghitza"
}
```

I added a small patch that changes the two failing doctests slightly so that they pass now.  I thought about the behaviour a bit and it seems sensible to me, but Robert should feel free to defend the original doctests if necessary.



---

archive/issue_comments_030814.json:
```json
{
    "body": "I think the new doctests are fine.",
    "created_at": "2008-12-04T11:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30814",
    "user": "https://github.com/mwhansen"
}
```

I think the new doctests are fine.



---

archive/issue_comments_030815.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T14:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.2.alpha0



---

archive/issue_events_004485.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-04T14:55:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4246#event-4485"
}
```



---

archive/issue_comments_030816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T14:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4246#issuecomment-30816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
