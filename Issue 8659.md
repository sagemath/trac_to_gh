# Issue 8659: another broken square root simplification

archive/issues_008659.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  kcrisman\n\nReported by Alex Raichev on sage-support:\n\n\n```\nOn Wed, 7 Apr 2010 16:56:01 -0700 (PDT)\nAlex Raichev <tortoise.said@gmail.com> wrote:\n\n> What the?\n> \n> ----------------------------------------------------------------------\n> | Sage Version 4.3.5, Release Date: 2010-03-28                       |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant(); a\n> 8\n> sage: a^(-1/2)\n> ---------------------------------------------------------------------------\n> TypeError                                 Traceback (most recent call\n> last)\n> \n> /Users/arai021/Dropbox/sage_work/<ipython console> in <module>()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/\n> expression.so in sage.symbolic.expression.Expression.__pow__ (sage/\n> symbolic/expression.cpp:11892)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/rings/\n> number_field/number_field_element.so in\n> sage.rings.number_field.number_field_element.NumberFieldElement.__pow__\n> (sage/rings/number_field/number_field_element.cpp:10038)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/\n> power_helper.so in sage.symbolic.power_helper.try_symbolic_power\n> (sage/ symbolic/power_helper.cpp:633)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/\n> power_helper.so in sage.symbolic.power_helper.try_symbolic_power\n> (sage/ symbolic/power_helper.cpp:509)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/\n> expression.so in sage.symbolic.expression.Expression.__pow__ (sage/\n> symbolic/expression.cpp:11892)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/rings/\n> rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/\n> rational.c:15609)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/structure/\n> element.so in sage.structure.element.RingElement.__mul__ (sage/\n> structure/element.c:11337)()\n> \n> /Applications/sage/local/lib/python2.6/site-packages/sage/structure/\n> coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op\n> (sage/structure/coerce.c:6994)()\n> \n> TypeError: unsupported operand parent(s) for '*': 'Rational Field' and\n> '<type 'NoneType'>'\n\n```\n\n\nHere is the thread:\n\nhttp://groups.google.com/group/sage-support/t/3e8ae9f6b7c44e7c\n\nThis looks similar to #8540, though it is a long standing issue, not caused by that ticket:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant(); a\n8\nsage: a^(-1/2)\n<boom>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8659\n\n",
    "created_at": "2010-04-08T10:10:49Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "another broken square root simplification",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8659",
    "user": "burcin"
}
```
Assignee: burcin

CC:  kcrisman

Reported by Alex Raichev on sage-support:


```
On Wed, 7 Apr 2010 16:56:01 -0700 (PDT)
Alex Raichev <tortoise.said@gmail.com> wrote:

> What the?
> 
> ----------------------------------------------------------------------
> | Sage Version 4.3.5, Release Date: 2010-03-28                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant(); a
> 8
> sage: a^(-1/2)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call
> last)
> 
> /Users/arai021/Dropbox/sage_work/<ipython console> in <module>()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> expression.so in sage.symbolic.expression.Expression.__pow__ (sage/
> symbolic/expression.cpp:11892)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/rings/
> number_field/number_field_element.so in
> sage.rings.number_field.number_field_element.NumberFieldElement.__pow__
> (sage/rings/number_field/number_field_element.cpp:10038)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> power_helper.so in sage.symbolic.power_helper.try_symbolic_power
> (sage/ symbolic/power_helper.cpp:633)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> power_helper.so in sage.symbolic.power_helper.try_symbolic_power
> (sage/ symbolic/power_helper.cpp:509)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> expression.so in sage.symbolic.expression.Expression.__pow__ (sage/
> symbolic/expression.cpp:11892)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/rings/
> rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/
> rational.c:15609)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/structure/
> element.so in sage.structure.element.RingElement.__mul__ (sage/
> structure/element.c:11337)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/structure/
> coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op
> (sage/structure/coerce.c:6994)()
> 
> TypeError: unsupported operand parent(s) for '*': 'Rational Field' and
> '<type 'NoneType'>'

```


Here is the thread:

http://groups.google.com/group/sage-support/t/3e8ae9f6b7c44e7c

This looks similar to #8540, though it is a long standing issue, not caused by that ticket:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant(); a
8
sage: a^(-1/2)
<boom>
```


Issue created by migration from https://trac.sagemath.org/ticket/8659





---

archive/issue_comments_078565.json:
```json
{
    "body": "This problem might not be in symbolics, but in number fields:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();\nsage: a\n8\nsage: type(a.pyobject())\n<type 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>\nsage: b=a.pyobject()\nsage: b\n8\nsage: parent(b)\nNumber Field in I with defining polynomial x^2 + 1\nsage: sqrt(b)\n2*sqrt(2)\nsage: 1/sqrt(b)\n1/4*sqrt(2)\nsage: b^(-1/2)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.3.4, Release Date: 2010-03-19                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/jason/<ipython console> in <module>()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.NumberFieldElement.__pow__ (sage/rings/number_field/number_field_element.cpp:10038)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:633)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:509)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11892)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15609)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()\n\nTypeError: unsupported operand parent(s) for '*': 'Rational Field' and '<type 'NoneType'>'\n```\n",
    "created_at": "2010-04-08T14:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78565",
    "user": "jason"
}
```

This problem might not be in symbolics, but in number fields:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();
sage: a
8
sage: type(a.pyobject())
<type 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>
sage: b=a.pyobject()
sage: b
8
sage: parent(b)
Number Field in I with defining polynomial x^2 + 1
sage: sqrt(b)
2*sqrt(2)
sage: 1/sqrt(b)
1/4*sqrt(2)
sage: b^(-1/2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.4, Release Date: 2010-03-19                       |
| Type notebook() for the GUI, and license() for information.        |
/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.NumberFieldElement.__pow__ (sage/rings/number_field/number_field_element.cpp:10038)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:633)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:509)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11892)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15609)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and '<type 'NoneType'>'
```




---

archive/issue_comments_078566.json:
```json
{
    "body": "Interestingly, these all work (starting from the above example in my post):\n\n\n```\nsage: b^(1/3)\n2\nsage: b^(1/4)\n8^(1/4)\nsage: b^(-1/4)\n1/8*8^(3/4)\n```\n\n\nSo it seems that b^(1/2) is the only problem?",
    "created_at": "2010-04-08T14:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78566",
    "user": "jason"
}
```

Interestingly, these all work (starting from the above example in my post):


```
sage: b^(1/3)
2
sage: b^(1/4)
8^(1/4)
sage: b^(-1/4)
1/8*8^(3/4)
```


So it seems that b^(1/2) is the only problem?



---

archive/issue_comments_078567.json:
```json
{
    "body": "On the other hand, it seems like the problem is in try_symbolic_power.  When I change that function to:\n\n\n```\n    global __pynac_pow\n    print \"entering try_symbolic_power: \", obj, p, \"; __pynac_pow is \", __pynac_pow\n    if __pynac_pow:\n        __pynac_pow = False\n        print \"    set __pynac_pow to False and return None\"\n        return None\n    else:\n        try:\n            __pynac_pow = True\n            print \"    Try SR powers: \", ring.SR(obj), ring.SR(p)\n            return ring.SR(obj)**ring.SR(p)\n        finally:\n            print \"        and then set __pynac_pow to False\"\n            __pynac_pow = False\n```\n\n\nthen I get:\n\n\n```\nsage: b^(1/2)\nentering try_symbolic_power:  8 1/2 ; __pynac_pow is  False\n    Try SR powers:  8 1/2\nentering try_symbolic_power:  2 1/2 ; __pynac_pow is  True\n    set __pynac_pow to False and return None\n        and then set __pynac_pow to False\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/<ipython console> in <module>()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.NumberFieldElement.__pow__ (sage/rings/number_field/number_field_element.cpp:10065)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:755)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:614)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11892)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15609)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()\n\nTypeError: unsupported operand parent(s) for '*': 'Rational Field' and '<type 'NoneType'>'\nsage: b^(1/4)\nentering try_symbolic_power:  8 1/4 ; __pynac_pow is  False\n    Try SR powers:  8 1/4\nentering try_symbolic_power:  8 1/4 ; __pynac_pow is  True\n    set __pynac_pow to False and return None\n        and then set __pynac_pow to False\n8^(1/4)\n\n```\n",
    "created_at": "2010-04-08T15:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78567",
    "user": "jason"
}
```

On the other hand, it seems like the problem is in try_symbolic_power.  When I change that function to:


```
    global __pynac_pow
    print "entering try_symbolic_power: ", obj, p, "; __pynac_pow is ", __pynac_pow
    if __pynac_pow:
        __pynac_pow = False
        print "    set __pynac_pow to False and return None"
        return None
    else:
        try:
            __pynac_pow = True
            print "    Try SR powers: ", ring.SR(obj), ring.SR(p)
            return ring.SR(obj)**ring.SR(p)
        finally:
            print "        and then set __pynac_pow to False"
            __pynac_pow = False
```


then I get:


```
sage: b^(1/2)
entering try_symbolic_power:  8 1/2 ; __pynac_pow is  False
    Try SR powers:  8 1/2
entering try_symbolic_power:  2 1/2 ; __pynac_pow is  True
    set __pynac_pow to False and return None
        and then set __pynac_pow to False
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.NumberFieldElement.__pow__ (sage/rings/number_field/number_field_element.cpp:10065)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:755)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:614)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11892)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15609)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and '<type 'NoneType'>'
sage: b^(1/4)
entering try_symbolic_power:  8 1/4 ; __pynac_pow is  False
    Try SR powers:  8 1/4
entering try_symbolic_power:  8 1/4 ; __pynac_pow is  True
    set __pynac_pow to False and return None
        and then set __pynac_pow to False
8^(1/4)

```




---

archive/issue_comments_078568.json:
```json
{
    "body": "Unsurprisingly, I get the same error traceback if I do `(b*b)^(1/4)`",
    "created_at": "2010-04-08T16:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78568",
    "user": "jason"
}
```

Unsurprisingly, I get the same error traceback if I do `(b*b)^(1/4)`



---

archive/issue_comments_078569.json:
```json
{
    "body": "Now that we have the `hold()` function for symbolic expressions (#9879), we don't need `sage.symbolic.power_helper`. attachment:trac_8659-hold_powers.patch removes this module, and fixes the problem described.\n\nThis ticket depends on #9879.",
    "created_at": "2010-09-25T23:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78569",
    "user": "burcin"
}
```

Now that we have the `hold()` function for symbolic expressions (#9879), we don't need `sage.symbolic.power_helper`. attachment:trac_8659-hold_powers.patch removes this module, and fixes the problem described.

This ticket depends on #9879.



---

archive/issue_comments_078570.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-25T23:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78570",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078571.json:
```json
{
    "body": "Attachment [trac_8659-hold_powers.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.patch) by kcrisman created at 2011-04-25 17:02:33\n\nAt first I thought I minded this discrepancy, but I think that maybe that's okay, given they really do live in different places.  At the same time, in theory then we should be holding anything that might ever be multivalued.  Like a square root.\n\n```\nsage: 8^(1/2)\n2*sqrt(2)\nsage: I.pyobject().parent()\nNumber Field in I with defining polynomial x^2 + 1\nsage: I.pyobject().parent()(8)^(1/2)\nsqrt(8)\n```\n\nIn particular, what do we want here?\n\n```\nsage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();\nsage: b = a.pyobject()\nsage: b^(-1/2); a^(-1/2)\n1/sqrt(8)\n1/8*sqrt(8)\n```\n",
    "created_at": "2011-04-25T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78571",
    "user": "kcrisman"
}
```

Attachment [trac_8659-hold_powers.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.patch) by kcrisman created at 2011-04-25 17:02:33

At first I thought I minded this discrepancy, but I think that maybe that's okay, given they really do live in different places.  At the same time, in theory then we should be holding anything that might ever be multivalued.  Like a square root.

```
sage: 8^(1/2)
2*sqrt(2)
sage: I.pyobject().parent()
Number Field in I with defining polynomial x^2 + 1
sage: I.pyobject().parent()(8)^(1/2)
sqrt(8)
```

In particular, what do we want here?

```
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();
sage: b = a.pyobject()
sage: b^(-1/2); a^(-1/2)
1/sqrt(8)
1/8*sqrt(8)
```




---

archive/issue_comments_078572.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-04-25T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78572",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_078573.json:
```json
{
    "body": "Also, is \n\n```\nsage: (t^2)^(1/4) \n64^(1/4) \n```\n\nintended to test\n\n```\nreturn SR(nbase).power(nexp*exp, hold=True)\n```\n\nBut the powers weren't multiplied, because `SR(base)` already is just 64.  \n\nSimilarly, \n\n```\nsage: 8^(-1/5) \n```\n\ncan't be to test the change in that file, because 8 isn't rational.  \n\nOr am I missing something?   Sorry if I've misinterpreted something; otherwise this is a good fix, it seems.",
    "created_at": "2011-04-25T19:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78573",
    "user": "kcrisman"
}
```

Also, is 

```
sage: (t^2)^(1/4) 
64^(1/4) 
```

intended to test

```
return SR(nbase).power(nexp*exp, hold=True)
```

But the powers weren't multiplied, because `SR(base)` already is just 64.  

Similarly, 

```
sage: 8^(-1/5) 
```

can't be to test the change in that file, because 8 isn't rational.  

Or am I missing something?   Sorry if I've misinterpreted something; otherwise this is a good fix, it seems.



---

archive/issue_comments_078574.json:
```json
{
    "body": "Attachment [trac_8659-hold_powers.take2.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.take2.patch) by burcin created at 2011-05-30 22:28:01",
    "created_at": "2011-05-30T22:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78574",
    "user": "burcin"
}
```

Attachment [trac_8659-hold_powers.take2.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.take2.patch) by burcin created at 2011-05-30 22:28:01



---

archive/issue_comments_078575.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-05-30T22:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78575",
    "user": "burcin"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_078576.json:
```json
{
    "body": "attachment:trac_8659-hold_powers.take2.patch should address the issues in comment:7 at the cost of magically changing the type of the coefficients to rational.\n\nThe test\n\n```\nsage: 8^(-1/5)\n```\n\ndoes test the `__pow__` method of rationals, since the `__pow__` method of `Integer` casts the base to a rational and calls pow again.",
    "created_at": "2011-05-30T22:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78576",
    "user": "burcin"
}
```

attachment:trac_8659-hold_powers.take2.patch should address the issues in comment:7 at the cost of magically changing the type of the coefficients to rational.

The test

```
sage: 8^(-1/5)
```

does test the `__pow__` method of rationals, since the `__pow__` method of `Integer` casts the base to a rational and calls pow again.



---

archive/issue_comments_078577.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-16T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78577",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078578.json:
```json
{
    "body": "I uploaded a new patch which should finally fix this. Please review.",
    "created_at": "2012-02-15T15:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78578",
    "user": "burcin"
}
```

I uploaded a new patch which should finally fix this. Please review.



---

archive/issue_comments_078579.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-15T15:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78579",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078580.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-15T15:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78580",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078581.json:
```json
{
    "body": "[[[\ninfite loops\n}}}",
    "created_at": "2012-02-15T15:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78581",
    "user": "kcrisman"
}
```

[[[
infite loops
}}}



---

archive/issue_comments_078582.json:
```json
{
    "body": "Hmm, that didn't format right.  I meant to say, there are two occurrences of \n\n```\ninfite loops\n```\n\n\nI think it would be helpful to have a doctest or two for each branch of the number field code.  Some are no doubt already in there, but all?  For instance, I would have thought that `(t<sup>2)</sup>(1/4)` is testing `return nbase.power(pexp * exp, hold=True) `, but it doesn't give `8^(1/2)` like I would have thought from that (so it must be from the `if not SR` branch); so it would be good to have one for that branch.\n\nAlso, can you think of a place where putting the rational power in the denominator could cause something to break?    Is that standard practice in this kind of computer algebra?  For instance, Maxima does not do this.\n\n```\n(%i3) 2^(-1/2);\n(%o3) 1/sqrt(2)\n```\n\n\nSorry if these are dumb questions.",
    "created_at": "2012-02-15T16:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78582",
    "user": "kcrisman"
}
```

Hmm, that didn't format right.  I meant to say, there are two occurrences of 

```
infite loops
```


I think it would be helpful to have a doctest or two for each branch of the number field code.  Some are no doubt already in there, but all?  For instance, I would have thought that `(t<sup>2)</sup>(1/4)` is testing `return nbase.power(pexp * exp, hold=True) `, but it doesn't give `8^(1/2)` like I would have thought from that (so it must be from the `if not SR` branch); so it would be good to have one for that branch.

Also, can you think of a place where putting the rational power in the denominator could cause something to break?    Is that standard practice in this kind of computer algebra?  For instance, Maxima does not do this.

```
(%i3) 2^(-1/2);
(%o3) 1/sqrt(2)
```


Sorry if these are dumb questions.



---

archive/issue_comments_078583.json:
```json
{
    "body": "Attachment [trac_8659-hold_powers.take3.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.take3.patch) by burcin created at 2012-02-15 16:59:30",
    "created_at": "2012-02-15T16:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78583",
    "user": "burcin"
}
```

Attachment [trac_8659-hold_powers.take3.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.take3.patch) by burcin created at 2012-02-15 16:59:30



---

archive/issue_comments_078584.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-15T17:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78584",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078585.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Hmm, that didn't format right.  I meant to say, there are two occurrences of \n> {{{\n> infite loops\n> }}}\n\nI updated the patch to fix the typos.\n\n> I think it would be helpful to have a doctest or two for each branch of the number field code.  Some are no doubt already in there, but all?  For instance, I would have thought that `(t<sup>2)</sup>(1/4)` is testing `return nbase.power(pexp * exp, hold=True) `, but it doesn't give `8^(1/2)` like I would have thought from that (so it must be from the `if not SR` branch); so it would be good to have one for that branch.\n\nThat branch is tested by these:\n\n\n```\n            sage: sqrt2^(1/5)\n            2^(1/10)\n            sage: sqrt2^sqrt2\n            2^(1/2*sqrt(2))\n```\n\n\n> Also, can you think of a place where putting the rational power in the denominator could cause something to break?    Is that standard practice in this kind of computer algebra?  For instance, Maxima does not do this.\n> {{{\n> (%i3) 2^(-1/2);\n> (%o3) 1/sqrt(2)\n> }}}\n\nAFAICT, GiNaC assumes this normal form.\n\n\nOn another note... IMHO, a simple typo in comments within source code, or not documenting which doctest corresponds to which branch in the code is justification to switch a ticket to `needs_work`. You might not be satisfied with the work, but it is possible that someone else will give a positive review, especially since this is a `critical` ticket.",
    "created_at": "2012-02-15T17:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78585",
    "user": "burcin"
}
```

Replying to [comment:13 kcrisman]:
> Hmm, that didn't format right.  I meant to say, there are two occurrences of 
> {{{
> infite loops
> }}}

I updated the patch to fix the typos.

> I think it would be helpful to have a doctest or two for each branch of the number field code.  Some are no doubt already in there, but all?  For instance, I would have thought that `(t<sup>2)</sup>(1/4)` is testing `return nbase.power(pexp * exp, hold=True) `, but it doesn't give `8^(1/2)` like I would have thought from that (so it must be from the `if not SR` branch); so it would be good to have one for that branch.

That branch is tested by these:


```
            sage: sqrt2^(1/5)
            2^(1/10)
            sage: sqrt2^sqrt2
            2^(1/2*sqrt(2))
```


> Also, can you think of a place where putting the rational power in the denominator could cause something to break?    Is that standard practice in this kind of computer algebra?  For instance, Maxima does not do this.
> {{{
> (%i3) 2^(-1/2);
> (%o3) 1/sqrt(2)
> }}}

AFAICT, GiNaC assumes this normal form.


On another note... IMHO, a simple typo in comments within source code, or not documenting which doctest corresponds to which branch in the code is justification to switch a ticket to `needs_work`. You might not be satisfied with the work, but it is possible that someone else will give a positive review, especially since this is a `critical` ticket.



---

archive/issue_comments_078586.json:
```json
{
    "body": "> On another note... IMHO, a simple typo in comments within source code, or not documenting which doctest corresponds to which branch in the code is justification to switch a ticket to `needs_work`. You might not be satisfied with the work, but it is \n\nFair enough!  Though I do think typos are 'needs work', often I can update them on a refresh.  The doctest thing was just wanting to check that we *did* check all branches.  Maybe 'needs info' is better?  The point is that I want to make sure the comment gets seen; a lot of times I see questions on 'needs review' that are then never actually addressed.  I don't really care what the status itself is.\n\n> possible that someone else will give a positive review, especially since this is a `critical` ticket.\n\nWell, it's apparently been `critical` for nearly two years, so perhaps that is less convincing of an argument on this ticket than others.  But point taken in general!",
    "created_at": "2012-02-15T17:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78586",
    "user": "kcrisman"
}
```

> On another note... IMHO, a simple typo in comments within source code, or not documenting which doctest corresponds to which branch in the code is justification to switch a ticket to `needs_work`. You might not be satisfied with the work, but it is 

Fair enough!  Though I do think typos are 'needs work', often I can update them on a refresh.  The doctest thing was just wanting to check that we *did* check all branches.  Maybe 'needs info' is better?  The point is that I want to make sure the comment gets seen; a lot of times I see questions on 'needs review' that are then never actually addressed.  I don't really care what the status itself is.

> possible that someone else will give a positive review, especially since this is a `critical` ticket.

Well, it's apparently been `critical` for nearly two years, so perhaps that is less convincing of an argument on this ticket than others.  But point taken in general!



---

archive/issue_comments_078587.json:
```json
{
    "body": "Okay, I now get all the branches, and it makes sense.  Thanks for hanging in there with me!  Also, good catch and test on the powers less than -1.\n\nI'm not putting 'needs work' :) but also not yet positive review.   In comment:7, we see the equivalent of this inconsistency: \n\n```\nsage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();\nsage: a; type(a)\n8\n<type 'sage.symbolic.expression.Expression'>\nsage: b = SR(8)\nsage: type(b)\n<type 'sage.symbolic.expression.Expression'>\nsage: a.operands(); a.operator()\n[]\nsage: b.operands(); b.operator()\n[]\nsage: b^(-1/2)\n1/4*sqrt(2)\nsage: a^(-1/2)\n1/8*sqrt(8)\nsage: a^(1/2)\nsqrt(8)\nsage: b^(1/2)\n2*sqrt(2)\n```\n\n\nI thought that maybe this was because (for reasons unclear to me) we had entered \n\n```\n\n        if not PY_TYPE_CHECK(self, Rational):\n```\n\nbut \n\n```\nsage: isinstance(b,Rational)\nFalse\nsage: isinstance(a,Rational)\nFalse\n```\n\nso I must be missing something obvious.  Anyway, I can't see why these should return different things, and we still have the switch to rational that should take care of this:\n\n```\n                res = QQ(base)**exp \n```\n\n\n\n\nAlso, the documentation in rational.pyx still says\n\n```\n\n    def __pow__(self, n, dummy):\n        \"\"\"\n        Raise self to the integer power n.\n        \n```\n\nthough I think this code has been used for non-integer powers for quite a while.\n\nBut perhaps another reviewer will see what is going on in these cases, my apologies if I'm wasting time.",
    "created_at": "2012-02-15T20:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78587",
    "user": "kcrisman"
}
```

Okay, I now get all the branches, and it makes sense.  Thanks for hanging in there with me!  Also, good catch and test on the powers less than -1.

I'm not putting 'needs work' :) but also not yet positive review.   In comment:7, we see the equivalent of this inconsistency: 

```
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();
sage: a; type(a)
8
<type 'sage.symbolic.expression.Expression'>
sage: b = SR(8)
sage: type(b)
<type 'sage.symbolic.expression.Expression'>
sage: a.operands(); a.operator()
[]
sage: b.operands(); b.operator()
[]
sage: b^(-1/2)
1/4*sqrt(2)
sage: a^(-1/2)
1/8*sqrt(8)
sage: a^(1/2)
sqrt(8)
sage: b^(1/2)
2*sqrt(2)
```


I thought that maybe this was because (for reasons unclear to me) we had entered 

```

        if not PY_TYPE_CHECK(self, Rational):
```

but 

```
sage: isinstance(b,Rational)
False
sage: isinstance(a,Rational)
False
```

so I must be missing something obvious.  Anyway, I can't see why these should return different things, and we still have the switch to rational that should take care of this:

```
                res = QQ(base)**exp 
```




Also, the documentation in rational.pyx still says

```

    def __pow__(self, n, dummy):
        """
        Raise self to the integer power n.
        
```

though I think this code has been used for non-integer powers for quite a while.

But perhaps another reviewer will see what is going on in these cases, my apologies if I'm wasting time.



---

archive/issue_comments_078588.json:
```json
{
    "body": "Apply trac_8659-hold_powers.take3.patch\n\n(for the patchbot, which is trying to apply all three patches simultaneously)",
    "created_at": "2012-03-10T10:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78588",
    "user": "davidloeffler"
}
```

Apply trac_8659-hold_powers.take3.patch

(for the patchbot, which is trying to apply all three patches simultaneously)



---

archive/issue_comments_078589.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-11T14:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78589",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078590.json:
```json
{
    "body": "Patch does not apply (either to 5.0.beta7, or to 4.8 with #12511 installed).",
    "created_at": "2012-03-11T14:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78590",
    "user": "davidloeffler"
}
```

Patch does not apply (either to 5.0.beta7, or to 4.8 with #12511 installed).



---

archive/issue_comments_078591.json:
```json
{
    "body": "Attachment [trac_8659-hold_powers.take4.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.take4.patch) by burcin created at 2012-05-24 09:49:41",
    "created_at": "2012-05-24T09:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78591",
    "user": "burcin"
}
```

Attachment [trac_8659-hold_powers.take4.patch](tarball://root/attachments/some-uuid/ticket8659/trac_8659-hold_powers.take4.patch) by burcin created at 2012-05-24 09:49:41



---

archive/issue_comments_078592.json:
```json
{
    "body": "I rebased the patch to 5.0. Apply only attachment:trac_8659-hold_powers.take4.patch.",
    "created_at": "2012-05-24T09:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78592",
    "user": "burcin"
}
```

I rebased the patch to 5.0. Apply only attachment:trac_8659-hold_powers.take4.patch.



---

archive/issue_comments_078593.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-24T09:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78593",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078594.json:
```json
{
    "body": "For the patchbot, apply trac_8659-hold_powers.take4.patch",
    "created_at": "2012-05-28T20:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78594",
    "user": "mhansen"
}
```

For the patchbot, apply trac_8659-hold_powers.take4.patch



---

archive/issue_comments_078595.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-28T21:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78595",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078596.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T21:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78596",
    "user": "mhansen"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_078597.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2012-05-28T21:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78597",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_078598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-18T10:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8659#issuecomment-78598",
    "user": "jdemeyer"
}
```

Resolution: fixed
