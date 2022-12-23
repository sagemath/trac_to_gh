# Issue 9429: Undesirable behaviour when deriving from QuotientRingElement

archive/issues_009429.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  novoselt robertwb\n\nAll arithmetic operations on `QuotientRingElement` return a new `QuotientRingElement`, which is not the desired result for derived classes. Instead one should use `self.__class__` to return an instance of the actual type:\n\n```\nsage: from sage.rings.quotient_ring_element import QuotientRingElement\nsage: class Q(QuotientRingElement):\n...    pass\n...\nsage: P.<x,y> = PolynomialRing(QQ, 'x, y')\nsage: Pquo = P.quo(x^3)\nsage: q = Q(Pquo, x)\nsage: type(q)\n<class '__main__.Q'>\nsage: type(q^2)\n<class 'sage.rings.quotient_ring_element.QuotientRingElement'>\n```\n\n\nExpected behaviour: `q^2` should have the same (derived) type as `q`.\n\nI am running into this issue because I want to express cohomology classes on toric varieties as derived classes of `QuotientRingElement`, see #9326. I'll write the obvious patch and attach it later today.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9429\n\n",
    "created_at": "2010-07-05T10:44:05Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Undesirable behaviour when deriving from QuotientRingElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9429",
    "user": "vbraun"
}
```
Assignee: AlexGhitza

CC:  novoselt robertwb

All arithmetic operations on `QuotientRingElement` return a new `QuotientRingElement`, which is not the desired result for derived classes. Instead one should use `self.__class__` to return an instance of the actual type:

```
sage: from sage.rings.quotient_ring_element import QuotientRingElement
sage: class Q(QuotientRingElement):
...    pass
...
sage: P.<x,y> = PolynomialRing(QQ, 'x, y')
sage: Pquo = P.quo(x^3)
sage: q = Q(Pquo, x)
sage: type(q)
<class '__main__.Q'>
sage: type(q^2)
<class 'sage.rings.quotient_ring_element.QuotientRingElement'>
```


Expected behaviour: `q^2` should have the same (derived) type as `q`.

I am running into this issue because I want to express cohomology classes on toric varieties as derived classes of `QuotientRingElement`, see #9326. I'll write the obvious patch and attach it later today.

Issue created by migration from https://trac.sagemath.org/ticket/9429





---

archive/issue_comments_090005.json:
```json
{
    "body": "Attachment\n\nmissed one occurrence",
    "created_at": "2010-07-05T11:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90005",
    "user": "vbraun"
}
```

Attachment

missed one occurrence



---

archive/issue_comments_090006.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-05T12:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90006",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090007.json:
```json
{
    "body": "I think\n\n```\nP = self.parent()\nreturn P._element_constructor_(...)\n```\n\nis the way to go here according to http://wiki.sagemath.org/coercion (if it does not work, that this is a bug that should be fixed ;-))",
    "created_at": "2010-07-05T13:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90007",
    "user": "novoselt"
}
```

I think

```
P = self.parent()
return P._element_constructor_(...)
```

is the way to go here according to http://wiki.sagemath.org/coercion (if it does not work, that this is a bug that should be fixed ;-))



---

archive/issue_comments_090008.json:
```json
{
    "body": "Actually, I should have probably written\n\n```\nP = self.parent()\nreturn P(...)\n```\n\nto eliminate the use of private methods completely.",
    "created_at": "2010-07-06T15:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90008",
    "user": "novoselt"
}
```

Actually, I should have probably written

```
P = self.parent()
return P(...)
```

to eliminate the use of private methods completely.



---

archive/issue_comments_090009.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-06T16:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90009",
    "user": "novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090010.json:
```json
{
    "body": "I have added a couple of printing lines into the quotient ring and got the following:\n\n```\nsage: FF = FiniteField(7)\nsage: P.<x> = PolynomialRing(FF)\n_coerce_map_from_(Finite Field of size 7, <type 'int'>)\n_coerce_map_from_(Finite Field of size 7, Integer Ring)\n_element_constructor_(Finite Field of size 7, 0)\nsage: x + 1\n_element_constructor_(Finite Field of size 7, 1)\n...\nTypeError: unsupported operand parent(s) for '+':\n'Univariate Polynomial Ring in x over Finite Field of size 7'\nand 'Integer Ring'\nsage: isinstance(FF, sage.rings.quotient_ring.QuotientRing_generic)\nTrue\n```\n",
    "created_at": "2010-07-06T16:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90010",
    "user": "novoselt"
}
```

I have added a couple of printing lines into the quotient ring and got the following:

```
sage: FF = FiniteField(7)
sage: P.<x> = PolynomialRing(FF)
_coerce_map_from_(Finite Field of size 7, <type 'int'>)
_coerce_map_from_(Finite Field of size 7, Integer Ring)
_element_constructor_(Finite Field of size 7, 0)
sage: x + 1
_element_constructor_(Finite Field of size 7, 1)
...
TypeError: unsupported operand parent(s) for '+':
'Univariate Polynomial Ring in x over Finite Field of size 7'
and 'Integer Ring'
sage: isinstance(FF, sage.rings.quotient_ring.QuotientRing_generic)
True
```




---

archive/issue_comments_090011.json:
```json
{
    "body": "Attachment\n\nVolker Braun's patch (with two print statements)",
    "created_at": "2010-07-06T16:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90011",
    "user": "novoselt"
}
```

Attachment

Volker Braun's patch (with two print statements)



---

archive/issue_comments_090012.json:
```json
{
    "body": "Hi Volker,\n\nI think I need to clarify my position a bit. I think that the coercion system is great and we should try to use it and comply with it as much as possible, especially in new classes. However it is not yet implemented everywhere and \"fixing\" existing files sometimes leads to a lot of problems, which may have a simple solution, but it is not necessarily obvious. I have tried today to switch divisor groups to the new framework and discovered that all modules in Sage are still inherited from old-style parents and trying to change it gives tons of errors. So if you are up to determine the exact cause of the problems above and fix them - it would be great (looks like the issue here is with `int` type, which should be treated like `ZZ`), but at the same time I don't think it should be mandatory.\n\nMeanwhile, I am attaching a version of your first patch with `return self.parent()(...)` statements. Naturally, `q^2` in your example will be of type `QuotientRingElement` since this is what the parent of `q` constructs as its elements. However, if you derive a class from `QuotientRing` which will construct its elements as some other type, these operations should return that other type. Please check if it actually works for your patches (I checked that at least it does not break anything so far). If it works, then perhaps we can add an example in the module docstring with derived classes for both ring and element and then mark it as ready for inclusion.\n\nThank you,\nAndrey",
    "created_at": "2010-07-07T06:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90012",
    "user": "novoselt"
}
```

Hi Volker,

I think I need to clarify my position a bit. I think that the coercion system is great and we should try to use it and comply with it as much as possible, especially in new classes. However it is not yet implemented everywhere and "fixing" existing files sometimes leads to a lot of problems, which may have a simple solution, but it is not necessarily obvious. I have tried today to switch divisor groups to the new framework and discovered that all modules in Sage are still inherited from old-style parents and trying to change it gives tons of errors. So if you are up to determine the exact cause of the problems above and fix them - it would be great (looks like the issue here is with `int` type, which should be treated like `ZZ`), but at the same time I don't think it should be mandatory.

Meanwhile, I am attaching a version of your first patch with `return self.parent()(...)` statements. Naturally, `q^2` in your example will be of type `QuotientRingElement` since this is what the parent of `q` constructs as its elements. However, if you derive a class from `QuotientRing` which will construct its elements as some other type, these operations should return that other type. Please check if it actually works for your patches (I checked that at least it does not break anything so far). If it works, then perhaps we can add an example in the module docstring with derived classes for both ring and element and then mark it as ready for inclusion.

Thank you,
Andrey



---

archive/issue_comments_090013.json:
```json
{
    "body": "`return self.parent()(...)` version",
    "created_at": "2010-07-07T06:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90013",
    "user": "novoselt"
}
```

`return self.parent()(...)` version



---

archive/issue_comments_090014.json:
```json
{
    "body": "Attachment\n\nI agree that your self.parent() version, of course. If we can't improve `QuotientRing` then we should go with the current version. I asked on sage-devel for help, maybe somebody can tell us more about the issue:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/efe93107ce004d3b",
    "created_at": "2010-07-07T18:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90014",
    "user": "vbraun"
}
```

Attachment

I agree that your self.parent() version, of course. If we can't improve `QuotientRing` then we should go with the current version. I asked on sage-devel for help, maybe somebody can tell us more about the issue:

http://groups.google.com/group/sage-devel/browse_thread/thread/efe93107ce004d3b



---

archive/issue_comments_090015.json:
```json
{
    "body": "The reason why `first_attempt.patch` breaks so many things is because the classes `QuotientRing_generic` -> `IntegerModRing_generic` -> `FiniteField_prime_modn` do not work within the new coercion model. \n\nRobert wrote on sage-devel:\n> What should have happened is that QuotientRing should be an abstract class, and with subclasses QuotientRingGeneric and FiniteField/IntegerModRing/etc. as the latter end up \n ignoring/subverting the implementation of the former. This would make things like this much easier to change\n\nWe should eventually port this to the new coercion model, but it seems to be a bigger effort. I don't want to wait with the current toric varieties code until this is done. So I'd like to go ahead with the \"wrong\" coercion in #9326, and leave this ticket for later.",
    "created_at": "2010-07-15T17:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90015",
    "user": "vbraun"
}
```

The reason why `first_attempt.patch` breaks so many things is because the classes `QuotientRing_generic` -> `IntegerModRing_generic` -> `FiniteField_prime_modn` do not work within the new coercion model. 

Robert wrote on sage-devel:
> What should have happened is that QuotientRing should be an abstract class, and with subclasses QuotientRingGeneric and FiniteField/IntegerModRing/etc. as the latter end up 
 ignoring/subverting the implementation of the former. This would make things like this much easier to change

We should eventually port this to the new coercion model, but it seems to be a bigger effort. I don't want to wait with the current toric varieties code until this is done. So I'd like to go ahead with the "wrong" coercion in #9326, and leave this ticket for later.



---

archive/issue_comments_090016.json:
```json
{
    "body": "What about merging only `trac_9429_fix_derived_classes.2.patch` for now? Forgetting coercion, it still would be nice if cohomology classes were represented by a new class rather than just an element of a quotient polynomial ring, since it will allow us to add methods to these classes.",
    "created_at": "2010-07-15T17:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90016",
    "user": "novoselt"
}
```

What about merging only `trac_9429_fix_derived_classes.2.patch` for now? Forgetting coercion, it still would be nice if cohomology classes were represented by a new class rather than just an element of a quotient polynomial ring, since it will allow us to add methods to these classes.



---

archive/issue_comments_090017.json:
```json
{
    "body": "I am right now moving your 'trac_9429_fix_derived_classes.patch' to #9326. Then you will hopefully review that ticket positively, allowing it to get merged :-)",
    "created_at": "2010-07-15T17:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90017",
    "user": "vbraun"
}
```

I am right now moving your 'trac_9429_fix_derived_classes.patch' to #9326. Then you will hopefully review that ticket positively, allowing it to get merged :-)



---

archive/issue_comments_090018.json:
```json
{
    "body": "I meant to write: I'm moving your `trac_9429_fix_derived_classes.2.patch`...",
    "created_at": "2010-07-15T17:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90018",
    "user": "vbraun"
}
```

I meant to write: I'm moving your `trac_9429_fix_derived_classes.2.patch`...



---

archive/issue_comments_090019.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd59\".",
    "created_at": "2014-06-22T06:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90019",
    "user": "tscrim"
}
```

Changing keywords from "" to "sd59".



---

archive/issue_comments_090020.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-22T06:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90020",
    "user": "tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090021.json:
```json
{
    "body": "I've \"reverted\" back to using the `self.__class__(self.parent(), x)` since this (as I remember) is the \"correct\" way to do things as it does not go through the coercion model. So can someone double-check to make sure doctests pass?\n----\nNew commits:",
    "created_at": "2014-06-22T06:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90021",
    "user": "tscrim"
}
```

I've "reverted" back to using the `self.__class__(self.parent(), x)` since this (as I remember) is the "correct" way to do things as it does not go through the coercion model. So can someone double-check to make sure doctests pass?
----
New commits:



---

archive/issue_comments_090022.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-05T10:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90022",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-02-17T19:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9429#issuecomment-90023",
    "user": "vbraun"
}
```

Resolution: fixed
