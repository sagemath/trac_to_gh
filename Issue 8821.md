# Issue 8821: Adding a section on coercion to the tutorial (guided tour)

archive/issues_008821.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  robertwb\n\nKeywords: tutorial coercion\n\nSo far, the word \"coercion\" has only been used twice in the tutorial - without explanation or reference. I believe coercion is far too important to not cover it in the tutorial, and moreover some pitfalls may be confusing for mathematicians, while programmers might confuse it with implicit type conversion.\n\nMy patch adds such section.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8821\n\n",
    "created_at": "2010-04-29T09:58:47Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "Adding a section on coercion to the tutorial (guided tour)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8821",
    "user": "SimonKing"
}
```
Assignee: mvngu

CC:  robertwb

Keywords: tutorial coercion

So far, the word "coercion" has only been used twice in the tutorial - without explanation or reference. I believe coercion is far too important to not cover it in the tutorial, and moreover some pitfalls may be confusing for mathematicians, while programmers might confuse it with implicit type conversion.

My patch adds such section.

Issue created by migration from https://trac.sagemath.org/ticket/8821





---

archive/issue_comments_080998.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T10:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-80998",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080999.json:
```json
{
    "body": "Looks good, and is much needed. I haven't finished reading it, but I have some comments: \n\nFirst, I might focus less on the types and isinstance corresponding to mathematical categories, as they can be misleading. For example, univarite polynomials are instances of PrincipalIdealDomainElement, even if they are. Another example, testing for RingElement could be deceptive. At least one of\n\n\n```\nsage: isinstance(matrix(ZZ, 2), RingElement)\nTrue\nsage: isinstance(matrix(ZZ, 2,3), RingElement)\nTrue\n```\n\n\nis False. (I consider the first a bug.)\n\nSecond, we don't want to create the expectation that Python elements are unique, as they usually aren't: \n\n\n```\nsage: a = -15r\nsage: b = -15r\nsage: a is b\nFalse\n```\n\n\nOnly some really common integers are.",
    "created_at": "2010-04-29T10:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-80999",
    "user": "robertwb"
}
```

Looks good, and is much needed. I haven't finished reading it, but I have some comments: 

First, I might focus less on the types and isinstance corresponding to mathematical categories, as they can be misleading. For example, univarite polynomials are instances of PrincipalIdealDomainElement, even if they are. Another example, testing for RingElement could be deceptive. At least one of


```
sage: isinstance(matrix(ZZ, 2), RingElement)
True
sage: isinstance(matrix(ZZ, 2,3), RingElement)
True
```


is False. (I consider the first a bug.)

Second, we don't want to create the expectation that Python elements are unique, as they usually aren't: 


```
sage: a = -15r
sage: b = -15r
sage: a is b
False
```


Only some really common integers are.



---

archive/issue_comments_081000.json:
```json
{
    "body": "Hi Robert,\n\nReplying to [comment:2 robertwb]:\n\n> First, I might focus less on the types and isinstance corresponding to mathematical categories, as they can be misleading.\n\nOK, I wanted to give a first approximation on how classes relate with mathematics. Perhaps I should emphasize that the analogy is not perfect (I already mention that different classes may also relate with different implementations of the same mathematical structure).\n\n> ` sage: isinstance(matrix(ZZ, 2), RingElement) True sage: isinstance(matrix(ZZ, 2,3), RingElement) True ` is False. (I consider the first a bug.)\n\nReally? The first is a square matrix, so, I think the second is wrong.\n\n> Second, we don't want to create the expectation that Python elements are unique, as they usually aren't:\n\nRight, that should be clarified.\n\nThank you!\n\nSimon",
    "created_at": "2010-04-29T10:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81000",
    "user": "SimonKing"
}
```

Hi Robert,

Replying to [comment:2 robertwb]:

> First, I might focus less on the types and isinstance corresponding to mathematical categories, as they can be misleading.

OK, I wanted to give a first approximation on how classes relate with mathematics. Perhaps I should emphasize that the analogy is not perfect (I already mention that different classes may also relate with different implementations of the same mathematical structure).

> ` sage: isinstance(matrix(ZZ, 2), RingElement) True sage: isinstance(matrix(ZZ, 2,3), RingElement) True ` is False. (I consider the first a bug.)

Really? The first is a square matrix, so, I think the second is wrong.

> Second, we don't want to create the expectation that Python elements are unique, as they usually aren't:

Right, that should be clarified.

Thank you!

Simon



---

archive/issue_comments_081001.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> > Second, we don't want to create the expectation that Python elements are unique, as they usually aren't:\n> \n> Right, that should be clarified.\nYes, that's what I suggested in the `sage-devel` thread. ;-)\n(And Robert noted that this is implementation-specific even in plain Python.)\nOne should clarify that in general\n  `a is b` => `a == b`\nbut not necessarily the opposite.\n\nRegarding comparison:\nIt should be stressed that not only `a == b` returns `False` if coercion fails but also `a != b` (silently) returns `False` in that case.\n\nReading on...\n\nBtw (ticket description), I'd still say Sage's coercion *is* (a kind of) implicit type conversion...\n\nIt seems we've reached ultimate confusion in the `sage-devel` thread (\"exact\" and \"inexact\" domains); I unfortunately haven't been able to reply so far...\n\n-Leif",
    "created_at": "2010-04-29T11:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81001",
    "user": "leif"
}
```

Replying to [comment:3 SimonKing]:
> > Second, we don't want to create the expectation that Python elements are unique, as they usually aren't:
> 
> Right, that should be clarified.
Yes, that's what I suggested in the `sage-devel` thread. ;-)
(And Robert noted that this is implementation-specific even in plain Python.)
One should clarify that in general
  `a is b` => `a == b`
but not necessarily the opposite.

Regarding comparison:
It should be stressed that not only `a == b` returns `False` if coercion fails but also `a != b` (silently) returns `False` in that case.

Reading on...

Btw (ticket description), I'd still say Sage's coercion *is* (a kind of) implicit type conversion...

It seems we've reached ultimate confusion in the `sage-devel` thread ("exact" and "inexact" domains); I unfortunately haven't been able to reply so far...

-Leif



---

archive/issue_comments_081002.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> Btw (ticket description), I'd still say Sage's coercion *is* (a kind of) implicit type conversion...\nOk, one might clarify that an implicit conversion (coercion) in Sage can be performed even if the objects' types appear to be the same; but this is not really different to other object-oriented languages (cf. virtual functions).",
    "created_at": "2010-04-29T11:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81002",
    "user": "leif"
}
```

Replying to [comment:4 leif]:
> Btw (ticket description), I'd still say Sage's coercion *is* (a kind of) implicit type conversion...
Ok, one might clarify that an implicit conversion (coercion) in Sage can be performed even if the objects' types appear to be the same; but this is not really different to other object-oriented languages (cf. virtual functions).



---

archive/issue_comments_081003.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> Regarding comparison:\n> It should be stressed that not only `a == b` returns `False` if coercion fails but also `a != b` (silently) returns `False` in that case.\n\nNo, it doesn't:\n\n\n```\nsage: GF(5)(1) == GF(2)(1)\nFalse\nsage: GF(5)(1) != GF(2)(1)\nTrue\nsage: R.<x,a,b> = QQ[]\nsage: S.<x,c,d> = QQ[]\nsage: x == R('x')\nFalse\nsage: x != R('x')\nTrue\n```\n",
    "created_at": "2010-04-29T12:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81003",
    "user": "SimonKing"
}
```

Replying to [comment:4 leif]:
> Regarding comparison:
> It should be stressed that not only `a == b` returns `False` if coercion fails but also `a != b` (silently) returns `False` in that case.

No, it doesn't:


```
sage: GF(5)(1) == GF(2)(1)
False
sage: GF(5)(1) != GF(2)(1)
True
sage: R.<x,a,b> = QQ[]
sage: S.<x,c,d> = QQ[]
sage: x == R('x')
False
sage: x != R('x')
True
```




---

archive/issue_comments_081004.json:
```json
{
    "body": "To be applied after the first patch",
    "created_at": "2010-04-29T12:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81004",
    "user": "SimonKing"
}
```

To be applied after the first patch



---

archive/issue_comments_081005.json:
```json
{
    "body": "Attachment\n\nI added another patch (on top of the first patch), taking into account some of your remarks. In particular, I try to clarify that \"class <-> category\" is nothing more than a weak analogy.",
    "created_at": "2010-04-29T12:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81005",
    "user": "SimonKing"
}
```

Attachment

I added another patch (on top of the first patch), taking into account some of your remarks. In particular, I try to clarify that "class <-> category" is nothing more than a weak analogy.



---

archive/issue_comments_081006.json:
```json
{
    "body": "Replying to [comment:6 SimonKing]:\n> No, it doesn't:\n> sage: GF(5)(1) != GF(2)(1)\n> True\nThen document the opposite (of what **I** stated) ;-)\n\n(I thought this was said in some Sage documentation, but it seems I took this assumption from Robert's statement:\n\n  \"In Python, the convention is that == and != never raise an error, so  \n  False is returned if coercion fails (the two domains are incompatible).\"\n\nin http://groups.google.com/group/sage-devel/msg/3ec75b62fcb3f295 and my reply: http://groups.google.com/group/sage-devel/msg/2f2e69bfb8623a4a)",
    "created_at": "2010-04-29T13:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81006",
    "user": "leif"
}
```

Replying to [comment:6 SimonKing]:
> No, it doesn't:
> sage: GF(5)(1) != GF(2)(1)
> True
Then document the opposite (of what **I** stated) ;-)

(I thought this was said in some Sage documentation, but it seems I took this assumption from Robert's statement:

  "In Python, the convention is that == and != never raise an error, so  
  False is returned if coercion fails (the two domains are incompatible)."

in http://groups.google.com/group/sage-devel/msg/3ec75b62fcb3f295 and my reply: http://groups.google.com/group/sage-devel/msg/2f2e69bfb8623a4a)



---

archive/issue_comments_081007.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Replying to [comment:6 SimonKing]:\n> > No, it doesn't:\n> > sage: GF(5)(1) != GF(2)(1)\n> > True\n> Then document the opposite (of what **I** stated) ;-)\n\nThis is already part of the patch that I provided a few minutes ago.\n\nCheers,\n\nSimon",
    "created_at": "2010-04-29T13:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81007",
    "user": "SimonKing"
}
```

Replying to [comment:8 leif]:
> Replying to [comment:6 SimonKing]:
> > No, it doesn't:
> > sage: GF(5)(1) != GF(2)(1)
> > True
> Then document the opposite (of what **I** stated) ;-)

This is already part of the patch that I provided a few minutes ago.

Cheers,

Simon



---

archive/issue_comments_081008.json:
```json
{
    "body": "What I should have said is that two incomparable elements are considered inequal (hence == returns False and != returns True). \n\nPerhaps a better way to describe the class <-> category relationship is to mention that the type system is not sufficiently expressive to capture the rich possibilities of mathematical relations (short of hackery like lots and lots of dynamic types), and that the *parent* of an object has to do with its place in the mathematical hierarchy, while the *type* of an object has to do with its underlying implementation.",
    "created_at": "2010-04-29T17:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81008",
    "user": "robertwb"
}
```

What I should have said is that two incomparable elements are considered inequal (hence == returns False and != returns True). 

Perhaps a better way to describe the class <-> category relationship is to mention that the type system is not sufficiently expressive to capture the rich possibilities of mathematical relations (short of hackery like lots and lots of dynamic types), and that the *parent* of an object has to do with its place in the mathematical hierarchy, while the *type* of an object has to do with its underlying implementation.



---

archive/issue_comments_081009.json:
```json
{
    "body": "`programming.rst` (only patched in the first changeset) still contains \"comparing objects of `different types` in Sage\"; here \"different parents\" or \"different Sage meta-types/structures\" or something like that would be more appropriate (perhaps just a footnote on \"types\"?).",
    "created_at": "2010-04-29T20:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81009",
    "user": "leif"
}
```

`programming.rst` (only patched in the first changeset) still contains "comparing objects of `different types` in Sage"; here "different parents" or "different Sage meta-types/structures" or something like that would be more appropriate (perhaps just a footnote on "types"?).



---

archive/issue_comments_081010.json:
```json
{
    "body": "I think this looks good.  [Leif's comment 11](http://trac.sagemath.org/sage_trac/ticket/8821#comment:11) might be worth addressing.  Also, in the new coercion section, perhaps in `X.__add__(Y), X.__sub__, X.__mul__`, every term should have `(Y)`?\n\nOtherwise, I think this should get a positive review.",
    "created_at": "2010-06-21T18:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81010",
    "user": "jhpalmieri"
}
```

I think this looks good.  [Leif's comment 11](http://trac.sagemath.org/sage_trac/ticket/8821#comment:11) might be worth addressing.  Also, in the new coercion section, perhaps in `X.__add__(Y), X.__sub__, X.__mul__`, every term should have `(Y)`?

Otherwise, I think this should get a positive review.



---

archive/issue_comments_081011.json:
```json
{
    "body": "There's a typo (missing space) in one headline (\"Parents,types and categories\"[sic]).\n\n----\n\nI've actually given up thinking about Sage's \"coercion model\", because IMHO still different people seem to have different ideas of what it is and how it does or should work (including different interpretations of terms).\n\nIf you want to have fun, compare this description to that in [William's and Burcin's recent paper](http://wstein.org/papers/icms/icms_2010.pdf) (page 12)... ;-)\n\n(Reading that, one would think *every* coercion in Sage is a type \n**promotion**. \"only from exact to inexact\" suggests the opposite, type **demotion**, and does, e.g., not include `QQ.has_coerce_map_from(ZZ)`, where I'd consider `ZZ` the [more] \"inexact\" domain.)\n\n----\n\nI'd write that Sage implements its own *type system*, which must not be confused with **Python's** (as opposed to \"... type conversion and type coercion known from, e.g., the C programming language\").\n\nThe explanation that there can only be a finite number of classes in Python is somewhat wrong; in fact, classes can be created dynamically (regarding finite memory, there can only be finitely many instances of a class, too).",
    "created_at": "2010-06-21T21:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81011",
    "user": "leif"
}
```

There's a typo (missing space) in one headline ("Parents,types and categories"[sic]).

----

I've actually given up thinking about Sage's "coercion model", because IMHO still different people seem to have different ideas of what it is and how it does or should work (including different interpretations of terms).

If you want to have fun, compare this description to that in [William's and Burcin's recent paper](http://wstein.org/papers/icms/icms_2010.pdf) (page 12)... ;-)

(Reading that, one would think *every* coercion in Sage is a type 
**promotion**. "only from exact to inexact" suggests the opposite, type **demotion**, and does, e.g., not include `QQ.has_coerce_map_from(ZZ)`, where I'd consider `ZZ` the [more] "inexact" domain.)

----

I'd write that Sage implements its own *type system*, which must not be confused with **Python's** (as opposed to "... type conversion and type coercion known from, e.g., the C programming language").

The explanation that there can only be a finite number of classes in Python is somewhat wrong; in fact, classes can be created dynamically (regarding finite memory, there can only be finitely many instances of a class, too).



---

archive/issue_comments_081012.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n\n> If you want to have fun, compare this description to that in [William's and Burcin's recent paper](http://wstein.org/papers/icms/icms_2010.pdf) (page 12)... ;-)\n> \n> (Reading that, one would think *every* coercion in Sage is a type \n> **promotion**. \"only from exact to inexact\" suggests the opposite, type **demotion**, and does, e.g., not include `QQ.has_coerce_map_from(ZZ)`, where I'd consider `ZZ` the [more] \"inexact\" domain.)\n\nZZ and QQ are equally exact: any element of them can be represented exactly on a computer.  Because of the presence of some transcendental numbers with no exact representation, RR is inherently inexact: when you work in RR, you're only working up to some level of precision.\n\nReading p. 12 of the Stein-Erocal paper, I would think that every coercion comes from an embedding, but this is not true.  Every coercion should come from a mathematically canonical map (like mapping Z to any ring, or the inclusion of Q into R).  Thinking about it mathematically makes sense to me, and I think this is the whole point.\n\nAlso, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other \"consumers\" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.",
    "created_at": "2010-06-21T21:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81012",
    "user": "jhpalmieri"
}
```

Replying to [comment:13 leif]:

> If you want to have fun, compare this description to that in [William's and Burcin's recent paper](http://wstein.org/papers/icms/icms_2010.pdf) (page 12)... ;-)
> 
> (Reading that, one would think *every* coercion in Sage is a type 
> **promotion**. "only from exact to inexact" suggests the opposite, type **demotion**, and does, e.g., not include `QQ.has_coerce_map_from(ZZ)`, where I'd consider `ZZ` the [more] "inexact" domain.)

ZZ and QQ are equally exact: any element of them can be represented exactly on a computer.  Because of the presence of some transcendental numbers with no exact representation, RR is inherently inexact: when you work in RR, you're only working up to some level of precision.

Reading p. 12 of the Stein-Erocal paper, I would think that every coercion comes from an embedding, but this is not true.  Every coercion should come from a mathematically canonical map (like mapping Z to any ring, or the inclusion of Q into R).  Thinking about it mathematically makes sense to me, and I think this is the whole point.

Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other "consumers" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.



---

archive/issue_comments_081013.json:
```json
{
    "body": "See also #9300.",
    "created_at": "2010-06-21T22:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81013",
    "user": "jhpalmieri"
}
```

See also #9300.



---

archive/issue_comments_081014.json:
```json
{
    "body": "Replying to [comment:14 jhpalmieri]:\n> [...] ZZ and QQ are equally exact: any element of them can be represented exactly on a computer.  Because of the presence of some transcendental numbers with no exact representation, RR is inherently inexact: when you work in RR, you're only working up to some level of precision.\nWell, irrational numbers and limited precision are different aspects; in principle, \"the\" real field should contain QQ. And at least some irrational numbers (I personally don't consider them numbers ;-) , or at least not \"real\" in the sense of existence) *can* be represented - in general as (symbolic) constants or as limits.\n\n(On the other hand, `NaN in RR`, but `infinity` is not, `RR.pi` is a method, `RR.pi() == pi` - where `parent(pi)` is `Symbolic Ring` - evaluates to `True`...)\n\n> Reading p. 12 of the Stein-Erocal paper, I would think that every coercion comes from an embedding, but this is not true.  Every coercion should come from a mathematically canonical map (like mapping Z to any ring, or the inclusion of Q into R).  Thinking about it mathematically makes sense to me, and I think this is the whole point.\nIf it's clear to everyone what is meant by \"exact\" and \"inexact\"...\n\nMapping Q into R is not the same as mapping `QQ` into `RR`; in fact, Sage supports the direction that is sound in the mathematical domains, i.e. that is valid for Q and R, though the implementation (the actual domains considered mathematically; floating-point numbers in the case of `RR`) would suggest the opposite, because every element of `RR` (except some symbolic constants) can be represented in `QQ`. IMHO coercions (as opposed to conversions) should be injective; the natural embedding of Q in R does *not* hold for \"Sage's\" Q and R, `QQ` and `RR`.\n\n> Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other \"consumers\" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.\nI'm not sure what that refers to; nevertheless the reader will (or should) be familiar with Python, including the concept of its types and classes, and will be confronted with the differences between Python types (including classes) and Sage's types, namely \"parents\".",
    "created_at": "2010-06-21T23:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81014",
    "user": "leif"
}
```

Replying to [comment:14 jhpalmieri]:
> [...] ZZ and QQ are equally exact: any element of them can be represented exactly on a computer.  Because of the presence of some transcendental numbers with no exact representation, RR is inherently inexact: when you work in RR, you're only working up to some level of precision.
Well, irrational numbers and limited precision are different aspects; in principle, "the" real field should contain QQ. And at least some irrational numbers (I personally don't consider them numbers ;-) , or at least not "real" in the sense of existence) *can* be represented - in general as (symbolic) constants or as limits.

(On the other hand, `NaN in RR`, but `infinity` is not, `RR.pi` is a method, `RR.pi() == pi` - where `parent(pi)` is `Symbolic Ring` - evaluates to `True`...)

> Reading p. 12 of the Stein-Erocal paper, I would think that every coercion comes from an embedding, but this is not true.  Every coercion should come from a mathematically canonical map (like mapping Z to any ring, or the inclusion of Q into R).  Thinking about it mathematically makes sense to me, and I think this is the whole point.
If it's clear to everyone what is meant by "exact" and "inexact"...

Mapping Q into R is not the same as mapping `QQ` into `RR`; in fact, Sage supports the direction that is sound in the mathematical domains, i.e. that is valid for Q and R, though the implementation (the actual domains considered mathematically; floating-point numbers in the case of `RR`) would suggest the opposite, because every element of `RR` (except some symbolic constants) can be represented in `QQ`. IMHO coercions (as opposed to conversions) should be injective; the natural embedding of Q in R does *not* hold for "Sage's" Q and R, `QQ` and `RR`.

> Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other "consumers" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.
I'm not sure what that refers to; nevertheless the reader will (or should) be familiar with Python, including the concept of its types and classes, and will be confronted with the differences between Python types (including classes) and Sage's types, namely "parents".



---

archive/issue_comments_081015.json:
```json
{
    "body": "Coercions in Sage are supposed to model the underlying mathematics.  So a coercion from QQ to RR is defined, as it should be.\n\nReplying to [comment:16 leif]:\n> And at least some irrational numbers *can* be represented - in general as (symbolic) constants or as limits.\n\nThat's why I used the qualifier \"some\" in \"the presence of some transcendental numbers\".  And of course every real number can be represented as a limit of rationals...\n\n> IMHO coercions (as opposed to conversions) should be injective.\n\nNo.  The natural map from ZZ to ZZ/nZZ should be a coercion, as indeed should be the natural map from ZZ to any ring.  The same for the standard map from an object (ring, group, module, ...) to any of its quotients.  These are typically not injective, but they are also completely canonical.  Any canonical map should be a coercion.\n\n> the natural embedding of Q in R does *not* hold for \"Sage's\" Q and R, `QQ` and `RR`.\n\nI'm willing to believe this, but can you provide evidence?\n\n> > Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other \"consumers\" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.\n> I'm not sure what that refers to; nevertheless the reader will (or should) be familiar with Python, including the concept of its types and classes, and will be confronted with the differences between Python types (including classes) and Sage's types, namely \"parents\".\n\nIt refers to, for example, your statement \"I'd write that Sage implements its own type system ...\".  I think this sort of statement puts more of a programming-type focus than a mathematical one.",
    "created_at": "2010-06-22T03:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81015",
    "user": "jhpalmieri"
}
```

Coercions in Sage are supposed to model the underlying mathematics.  So a coercion from QQ to RR is defined, as it should be.

Replying to [comment:16 leif]:
> And at least some irrational numbers *can* be represented - in general as (symbolic) constants or as limits.

That's why I used the qualifier "some" in "the presence of some transcendental numbers".  And of course every real number can be represented as a limit of rationals...

> IMHO coercions (as opposed to conversions) should be injective.

No.  The natural map from ZZ to ZZ/nZZ should be a coercion, as indeed should be the natural map from ZZ to any ring.  The same for the standard map from an object (ring, group, module, ...) to any of its quotients.  These are typically not injective, but they are also completely canonical.  Any canonical map should be a coercion.

> the natural embedding of Q in R does *not* hold for "Sage's" Q and R, `QQ` and `RR`.

I'm willing to believe this, but can you provide evidence?

> > Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other "consumers" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.
> I'm not sure what that refers to; nevertheless the reader will (or should) be familiar with Python, including the concept of its types and classes, and will be confronted with the differences between Python types (including classes) and Sage's types, namely "parents".

It refers to, for example, your statement "I'd write that Sage implements its own type system ...".  I think this sort of statement puts more of a programming-type focus than a mathematical one.



---

archive/issue_comments_081016.json:
```json
{
    "body": "Dear John, dear Leif,\n\nthank you for not forgetting this ticket (I almost did). Currently I am hardly able to work on it, since I am at some conference, and the internet access in my hotel is a bit restricted.\n\nCheers, Simon",
    "created_at": "2010-06-22T16:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81016",
    "user": "SimonKing"
}
```

Dear John, dear Leif,

thank you for not forgetting this ticket (I almost did). Currently I am hardly able to work on it, since I am at some conference, and the internet access in my hotel is a bit restricted.

Cheers, Simon



---

archive/issue_comments_081017.json:
```json
{
    "body": "I just noticed that this very ancient ticket is still unresolved.\n\nI still think that a text on coercion should be added to the guided tour. I think, after a break of 12 months, one should have a fresh look at the texts.\n\nIn addition, I think that there should also be a thematic tutorial (i.e., not just a chapter in the guided tour) covering coercion and categories. I therefore opened #11490.",
    "created_at": "2011-06-15T07:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81017",
    "user": "SimonKing"
}
```

I just noticed that this very ancient ticket is still unresolved.

I still think that a text on coercion should be added to the guided tour. I think, after a break of 12 months, one should have a fresh look at the texts.

In addition, I think that there should also be a thematic tutorial (i.e., not just a chapter in the guided tour) covering coercion and categories. I therefore opened #11490.



---

archive/issue_comments_081018.json:
```json
{
    "body": "Attachment\n\nONLY APPLY THIS PATCH: Insert a section on coercion into the guided tour.",
    "created_at": "2011-06-16T07:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81018",
    "user": "SimonKing"
}
```

Attachment

ONLY APPLY THIS PATCH: Insert a section on coercion into the guided tour.



---

archive/issue_comments_081019.json:
```json
{
    "body": "I have combined the two patches, so that only trac_8821-tutorial-coercion.patch is relevant now. I re-structured the text slightly, and I also refer to my worksheet on coercion that is attached to #11490.\n\nNote that the text we are considering here is not about implementing coercion. The implementation aspect is addressed in #11490.\n\nFor the patchbot:\n\nApply trac_8821-tutorial-coercion.patch",
    "created_at": "2011-06-16T07:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81019",
    "user": "SimonKing"
}
```

I have combined the two patches, so that only trac_8821-tutorial-coercion.patch is relevant now. I re-structured the text slightly, and I also refer to my worksheet on coercion that is attached to #11490.

Note that the text we are considering here is not about implementing coercion. The implementation aspect is addressed in #11490.

For the patchbot:

Apply trac_8821-tutorial-coercion.patch



---

archive/issue_comments_081020.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-07-22T23:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81020",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081021.json:
```json
{
    "body": "Here's a referee's patch.  Positive review.",
    "created_at": "2011-07-22T23:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81021",
    "user": "jhpalmieri"
}
```

Here's a referee's patch.  Positive review.



---

archive/issue_comments_081022.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-07-22T23:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81022",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_081023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-08-02T19:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8821#issuecomment-81023",
    "user": "jdemeyer"
}
```

Resolution: fixed
