# Issue 8860: incoherent types for real numbers

archive/issues_008860.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @nexttime\n\nKeywords: sd40.5\n\nThis was reported by Francois Maltey:\n\n```\nsage: map (type, [float(1.2), N(1.2), N(1.2,digits=50)])\n\n                           [<type 'float'>,\n                            <type 'sage.rings.real_mpfr.RealLiteral'>,\n                            <type 'sage.rings.real_mpfr.RealNumber'>]\n```\nWhy does the second one return `RealLiteral` and the 3rd one\n`RealNumber`?\n\nSide question: how does one test if the type of an object \ncorresponds to a real number, like for example:\n\n```\ntype (345) is Integer, type([1,2,3]) is list, type (2/3) is Rational\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8860\n\n",
    "closed_at": "2012-06-02T12:56:18Z",
    "created_at": "2010-05-03T18:10:20Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "incoherent types for real numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8860",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

CC:  @nexttime

Keywords: sd40.5

This was reported by Francois Maltey:

```
sage: map (type, [float(1.2), N(1.2), N(1.2,digits=50)])

                           [<type 'float'>,
                            <type 'sage.rings.real_mpfr.RealLiteral'>,
                            <type 'sage.rings.real_mpfr.RealNumber'>]
```
Why does the second one return `RealLiteral` and the 3rd one
`RealNumber`?

Side question: how does one test if the type of an object 
corresponds to a real number, like for example:

```
type (345) is Integer, type([1,2,3]) is list, type (2/3) is Rational
```

Issue created by migration from https://trac.sagemath.org/ticket/8860





---

archive/issue_comments_081280.json:
```json
{
    "body": "The docstring for RealLiteral indicates what is going on: \"RealLiterals are created in preparsing and provide a way to allow casting into higher precision rings.\"  So (I think) the digits=50 is casting the RealLiteral 1.2 object into a RealNumber with the desired precision.  RealLiteral just looks like a trivial subclass of RealNumber to just aid in parsing.\n\nside question: when you say type, do you mean the computer science type (i.e., the RealNumber or RealLiteral class)?  Or are you just checking if you have a floating point number (i.e., do you want a python floating point number to also return True?)",
    "created_at": "2010-05-03T18:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81280",
    "user": "https://github.com/jasongrout"
}
```

The docstring for RealLiteral indicates what is going on: "RealLiterals are created in preparsing and provide a way to allow casting into higher precision rings."  So (I think) the digits=50 is casting the RealLiteral 1.2 object into a RealNumber with the desired precision.  RealLiteral just looks like a trivial subclass of RealNumber to just aid in parsing.

side question: when you say type, do you mean the computer science type (i.e., the RealNumber or RealLiteral class)?  Or are you just checking if you have a floating point number (i.e., do you want a python floating point number to also return True?)



---

archive/issue_comments_081281.json:
```json
{
    "body": "Jason,\n\n> The docstring for RealLiteral? indicates...\n\n\nhow do you get this docstring?\n\n```\nsage: RealLiteral?\nObject `RealLiteral` not found.\n```\n\nAnyway, I find it quite disturbing from the user point-of-view to see this \"preparsing\" side-effect:\n\n```\nsage: type(n(1.2,prec=52))\n<type 'sage.rings.real_mpfr.RealNumber'>\nsage: type(n(1.2,prec=53))\n<type 'sage.rings.real_mpfr.RealLiteral'>\nsage: type(n(1.2,prec=54))\n<type 'sage.rings.real_mpfr.RealNumber'>\n```\n\n> side question: ...\n\n\nI forwarded the question to Francois Maltey. I guess he wants to check for a f-p number, and \nprobably a python float should also return True.",
    "created_at": "2010-05-04T07:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81281",
    "user": "https://github.com/zimmermann6"
}
```

Jason,

> The docstring for RealLiteral? indicates...


how do you get this docstring?

```
sage: RealLiteral?
Object `RealLiteral` not found.
```

Anyway, I find it quite disturbing from the user point-of-view to see this "preparsing" side-effect:

```
sage: type(n(1.2,prec=52))
<type 'sage.rings.real_mpfr.RealNumber'>
sage: type(n(1.2,prec=53))
<type 'sage.rings.real_mpfr.RealLiteral'>
sage: type(n(1.2,prec=54))
<type 'sage.rings.real_mpfr.RealNumber'>
```

> side question: ...


I forwarded the question to Francois Maltey. I guess he wants to check for a f-p number, and 
probably a python float should also return True.



---

archive/issue_comments_081282.json:
```json
{
    "body": "Replying to [comment:2 zimmerma]:\n> Jason,\n> \n> > The docstring for RealLiteral? indicates...\n\n> \n> how do you get this docstring?\n> \n> ```\n> sage: RealLiteral?\n> Object `RealLiteral` not found.\n> ```\n\n\n\nI was browsing the source.  Since RealLiteral is not imported to the global namespace (i.e., it appears to be only a preparser thing), you can't get the docstring just by typing RealLiteral?.  For me, it seems like I can't even get the docstring with the full namespace path.  Can you try `sage.rings.real_mpfr.RealLiteral?`\n\n\n> \n> Anyway, I find it quite disturbing from the user point-of-view to see this \"preparsing\" side-effect:\n> \n> ```\n> sage: type(n(1.2,prec=52))\n> <type 'sage.rings.real_mpfr.RealNumber'>\n> sage: type(n(1.2,prec=53))\n> <type 'sage.rings.real_mpfr.RealLiteral'>\n> sage: type(n(1.2,prec=54))\n> <type 'sage.rings.real_mpfr.RealNumber'>\n> ```\n\n\nI guess the underlying question is: why does the preparser have a special type (i.e., subclass) of RealNumber that it creates, instead of just creating a RealNumber?  That question probably deserves a post to sage-devel, since it's not immediately clear from the documentation.",
    "created_at": "2010-05-04T14:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81282",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 zimmerma]:
> Jason,
> 
> > The docstring for RealLiteral? indicates...

> 
> how do you get this docstring?
> 
> ```
> sage: RealLiteral?
> Object `RealLiteral` not found.
> ```



I was browsing the source.  Since RealLiteral is not imported to the global namespace (i.e., it appears to be only a preparser thing), you can't get the docstring just by typing RealLiteral?.  For me, it seems like I can't even get the docstring with the full namespace path.  Can you try `sage.rings.real_mpfr.RealLiteral?`


> 
> Anyway, I find it quite disturbing from the user point-of-view to see this "preparsing" side-effect:
> 
> ```
> sage: type(n(1.2,prec=52))
> <type 'sage.rings.real_mpfr.RealNumber'>
> sage: type(n(1.2,prec=53))
> <type 'sage.rings.real_mpfr.RealLiteral'>
> sage: type(n(1.2,prec=54))
> <type 'sage.rings.real_mpfr.RealNumber'>
> ```


I guess the underlying question is: why does the preparser have a special type (i.e., subclass) of RealNumber that it creates, instead of just creating a RealNumber?  That question probably deserves a post to sage-devel, since it's not immediately clear from the documentation.



---

archive/issue_comments_081283.json:
```json
{
    "body": "> Can you try sage.rings.real_mpfr.RealLiteral?\n\n\nI get:\n\n```\nsage: sage.rings.real_mpfr.RealLiteral?\nType:              type\nBase Class:     <type 'type'>\nString Form:    <type 'sage.rings.real_mpfr.RealLiteral'>\nNamespace:      Interactive\nFile:           /usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so\nDocstring:\n    x.__init__(...) initializes x; see x.__class__.__doc__ for signature\n```\nwhich is not very helpful...",
    "created_at": "2010-05-04T15:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81283",
    "user": "https://github.com/zimmermann6"
}
```

> Can you try sage.rings.real_mpfr.RealLiteral?


I get:

```
sage: sage.rings.real_mpfr.RealLiteral?
Type:              type
Base Class:     <type 'type'>
String Form:    <type 'sage.rings.real_mpfr.RealLiteral'>
Namespace:      Interactive
File:           /usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so
Docstring:
    x.__init__(...) initializes x; see x.__class__.__doc__ for signature
```
which is not very helpful...



---

archive/issue_comments_081284.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> I guess the underlying question is: why does the preparser have a special type (i.e., subclass) of RealNumber that it creates, instead of just creating a RealNumber?  That question probably deserves a post to sage-devel, since it's not immediately clear from the documentation.\n> \n\n\nIt is to solve the problem at http://trac.sagemath.org/sage_trac/ticket/4085.",
    "created_at": "2010-05-04T20:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81284",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:3 jason]:
> I guess the underlying question is: why does the preparser have a special type (i.e., subclass) of RealNumber that it creates, instead of just creating a RealNumber?  That question probably deserves a post to sage-devel, since it's not immediately clear from the documentation.
> 


It is to solve the problem at http://trac.sagemath.org/sage_trac/ticket/4085.



---

archive/issue_comments_081285.json:
```json
{
    "body": "> It is to solve the problem at http://trac.sagemath.org/sage_trac/ticket/4085.\n\n\nSo is it fair to say that RealLiteral is a decimal-based real number (i.e., like the python [Decimal class](http://docs.python.org/library/decimal.html)), where the actual digits are stored, rather than a binary floating point approximation?  (That's what appears to happen in the code, and seems to be the root cause of the problem at #4085).",
    "created_at": "2010-05-04T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81285",
    "user": "https://github.com/jasongrout"
}
```

> It is to solve the problem at http://trac.sagemath.org/sage_trac/ticket/4085.


So is it fair to say that RealLiteral is a decimal-based real number (i.e., like the python [Decimal class](http://docs.python.org/library/decimal.html)), where the actual digits are stored, rather than a binary floating point approximation?  (That's what appears to happen in the code, and seems to be the root cause of the problem at #4085).



---

archive/issue_comments_081286.json:
```json
{
    "body": "Nope, it just keeps track of the string that was used to create it.",
    "created_at": "2010-05-04T21:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81286",
    "user": "https://github.com/mwhansen"
}
```

Nope, it just keeps track of the string that was used to create it.



---

archive/issue_comments_081287.json:
```json
{
    "body": "Rather than `type(x) is X` one should use `isinstance(x, X)` which handles subclasses gracefully. In general, I consider the exact value of type(x) to be an implementation detail subject to change. (For example, `type(GF(q, 'a'))` and `type(GF(q, 'a'))` depend on the value `q`, and changes over time.)\n\n`RealLiteral` doesn't do anything fancy (e.g. the sum of two `RealLiteral`s is just a `RealNumber`), it's just used so that floating point literals can be cast into higher precision (or exact) rings without being truncated to an intermediate 53 bit representation first. I consider this a feature rather than a bug.",
    "created_at": "2010-05-06T08:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81287",
    "user": "https://github.com/robertwb"
}
```

Rather than `type(x) is X` one should use `isinstance(x, X)` which handles subclasses gracefully. In general, I consider the exact value of type(x) to be an implementation detail subject to change. (For example, `type(GF(q, 'a'))` and `type(GF(q, 'a'))` depend on the value `q`, and changes over time.)

`RealLiteral` doesn't do anything fancy (e.g. the sum of two `RealLiteral`s is just a `RealNumber`), it's just used so that floating point literals can be cast into higher precision (or exact) rings without being truncated to an intermediate 53 bit representation first. I consider this a feature rather than a bug.



---

archive/issue_comments_081288.json:
```json
{
    "body": "Robert,\n\n> Rather than type(x) is X one should use isinstance(x, X) ...\n\n\nthus which X should one use to recognize either x=float(1.2) or x=1.2 or x=n(1.2,100)?\n\nPaul",
    "created_at": "2010-05-06T09:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81288",
    "user": "https://github.com/zimmermann6"
}
```

Robert,

> Rather than type(x) is X one should use isinstance(x, X) ...


thus which X should one use to recognize either x=float(1.2) or x=1.2 or x=n(1.2,100)?

Paul



---

archive/issue_comments_081289.json:
```json
{
    "body": "Python's float is completely independent of Sage's class hierarchy, so in this case one would have to do\n\n```\nisinstance(x, float) or isinstance(x, RealNumber)\n```",
    "created_at": "2010-05-06T09:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81289",
    "user": "https://github.com/robertwb"
}
```

Python's float is completely independent of Sage's class hierarchy, so in this case one would have to do

```
isinstance(x, float) or isinstance(x, RealNumber)
```



---

archive/issue_comments_081290.json:
```json
{
    "body": "Sage 4.3.5:\n\n```\nsage: isinstance(1.2, RealNumber)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/users/caramel/zimmerma/<ipython console> in <module>()\n\nTypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types\n```\nSame thing with `isinstance(n(1.2,100), RealNumber)`. Should I open a separate ticket for that?",
    "created_at": "2010-05-06T09:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81290",
    "user": "https://github.com/zimmermann6"
}
```

Sage 4.3.5:

```
sage: isinstance(1.2, RealNumber)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/<ipython console> in <module>()

TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types
```
Same thing with `isinstance(n(1.2,100), RealNumber)`. Should I open a separate ticket for that?



---

archive/issue_comments_081291.json:
```json
{
    "body": "Ah, sorry. That is because RealNumber in the global scope is not the actual type, but a function to create RealNumbers. (This is similar in spirit to how PolynomialRing(...) is a function creating polynomial rings, not a type).  Note that `type(x) is RealNumber` would never work for the same reason. \n\n```\nsage: isinstance(1.2, sage.rings.real_mpfr.RealNumber)\nTrue\n```",
    "created_at": "2010-05-06T09:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81291",
    "user": "https://github.com/robertwb"
}
```

Ah, sorry. That is because RealNumber in the global scope is not the actual type, but a function to create RealNumbers. (This is similar in spirit to how PolynomialRing(...) is a function creating polynomial rings, not a type).  Note that `type(x) is RealNumber` would never work for the same reason. 

```
sage: isinstance(1.2, sage.rings.real_mpfr.RealNumber)
True
```



---

archive/issue_comments_081292.json:
```json
{
    "body": "I find `isinstance(1.2, sage.rings.real_mpfr.RealNumber)` not satisfying for three reasons:\n\n(1) it is much too long, compare say `isinstance(17, Integer)`\n\n(2) it explicitly refers to the underlying implementation and the MPFR component: this should be\n    hidden from the user\n\n(3) that underlying implementation may change in the future, which will break some code using\n    `sage.rings.real_mpfr.RealNumber`\n\nThus we need a shortcut like \"Integer\" for real numbers.\n\nPaul",
    "created_at": "2010-05-06T09:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81292",
    "user": "https://github.com/zimmermann6"
}
```

I find `isinstance(1.2, sage.rings.real_mpfr.RealNumber)` not satisfying for three reasons:

(1) it is much too long, compare say `isinstance(17, Integer)`

(2) it explicitly refers to the underlying implementation and the MPFR component: this should be
    hidden from the user

(3) that underlying implementation may change in the future, which will break some code using
    `sage.rings.real_mpfr.RealNumber`

Thus we need a shortcut like "Integer" for real numbers.

Paul



---

archive/issue_comments_081293.json:
```json
{
    "body": "I agree. \n\nWe used to have `is_RealNumber` but that was deprecated. I usually just do something like `x in RR`, unless I really need to know I have exactly a real number (e.g. I'm trying to reach inside and grab it's mpfr_t to initialize myself) in which case the implementation matters.",
    "created_at": "2010-05-06T09:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81293",
    "user": "https://github.com/robertwb"
}
```

I agree. 

We used to have `is_RealNumber` but that was deprecated. I usually just do something like `x in RR`, unless I really need to know I have exactly a real number (e.g. I'm trying to reach inside and grab it's mpfr_t to initialize myself) in which case the implementation matters.



---

archive/issue_comments_081294.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-22T14:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81294",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081295.json:
```json
{
    "body": "I propose to close this ticket, since it seems that `x in RR` solves the original question. I thus put it as \"needs review\".\n\nPaul",
    "created_at": "2012-05-22T14:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81295",
    "user": "https://github.com/zimmermann6"
}
```

I propose to close this ticket, since it seems that `x in RR` solves the original question. I thus put it as "needs review".

Paul



---

archive/issue_comments_081296.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T05:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81296",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_081297.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-28T05:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81297",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081298.json:
```json
{
    "body": "Sounds good.",
    "created_at": "2012-05-28T05:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81298",
    "user": "https://github.com/mwhansen"
}
```

Sounds good.



---

archive/issue_events_021621.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2012-05-28T05:12:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8860#event-21621"
}
```



---

archive/issue_events_021622.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-02T12:56:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8860#event-21622"
}
```



---

archive/issue_comments_081299.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-06-02T12:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8860#issuecomment-81299",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
