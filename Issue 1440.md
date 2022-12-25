# Issue 1440: Inconsistency in subs and substitute for univariate polynomials

archive/issues_001440.json:
```json
{
    "body": "Assignee: somebody\n\nI very much agree that the problem below is a bug, which we should resolve. \n\n```\nsubs and substitute are not equivalent for single variable\npolynomials,\nthough they are in the field of fractions or for polynomials in more\nthan\none variable:\n\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.15, Release Date: 2007-12-03                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R.<x> = QQ[]\nsage: f = x^3 + x - 3\nsage: f.subs(x = 5)\n127\nsage: f.substitute(x = 5)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call\nlast)\n\n/Users/mafwc/<ipython console> in <module>()\n\n/Users/mafwc/element.pyx in\nsage.structure.element.Element.substitute()\n\n/Users/mafwc/polynomial_element.pyx in\nsage.rings.polynomial.polynomial_element.Polynomial.subs()\n\n/Users/mafwc/polynomial_element.pyx in\nsage.rings.polynomial.polynomial_element.Polynomial.__call__()\n\n<type 'exceptions.ValueError'>: must not specify both a keyword and\npositional argument\n\n\nsage: g = f/(x - 1)\nsage: [g.subs(x = 5), g.substitute(x = 5)]\n[127/4, 127/4]\n\n\nsage: R2.<y, z> = PolynomialRing(QQ, 2)\nsage: h = y^3*z + 4*y*z^2 + y + 3*z - 7\nsage: [h.subs(y = 5), h.substitute(y = 5)]\n[20*z^2 + 128*z - 2, 20*z^2 + 128*z - 2]\n\n\n[Mac OS X 10.4.11, 2 GHz Intel Core 2 Duo, 1 GB].\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1440\n\n",
    "created_at": "2007-12-09T21:09:35Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "Inconsistency in subs and substitute for univariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1440",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

I very much agree that the problem below is a bug, which we should resolve. 

```
subs and substitute are not equivalent for single variable
polynomials,
though they are in the field of fractions or for polynomials in more
than
one variable:


----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.15, Release Date: 2007-12-03                      |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<x> = QQ[]
sage: f = x^3 + x - 3
sage: f.subs(x = 5)
127
sage: f.substitute(x = 5)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call
last)

/Users/mafwc/<ipython console> in <module>()

/Users/mafwc/element.pyx in
sage.structure.element.Element.substitute()

/Users/mafwc/polynomial_element.pyx in
sage.rings.polynomial.polynomial_element.Polynomial.subs()

/Users/mafwc/polynomial_element.pyx in
sage.rings.polynomial.polynomial_element.Polynomial.__call__()

<type 'exceptions.ValueError'>: must not specify both a keyword and
positional argument


sage: g = f/(x - 1)
sage: [g.subs(x = 5), g.substitute(x = 5)]
[127/4, 127/4]


sage: R2.<y, z> = PolynomialRing(QQ, 2)
sage: h = y^3*z + 4*y*z^2 + y + 3*z - 7
sage: [h.subs(y = 5), h.substitute(y = 5)]
[20*z^2 + 128*z - 2, 20*z^2 + 128*z - 2]


[Mac OS X 10.4.11, 2 GHz Intel Core 2 Duo, 1 GB].
```

Issue created by migration from https://trac.sagemath.org/ticket/1440





---

archive/issue_comments_009262.json:
```json
{
    "body": "This is somewhat tangential to this issue, but subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class.  I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded.  Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug.\n\nNote that because of the issues I mention in the first paragraph I highly suspect that this bug is not unique to univ-variate polys.",
    "created_at": "2007-12-26T14:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9262",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

This is somewhat tangential to this issue, but subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class.  I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded.  Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug.

Note that because of the issues I mention in the first paragraph I highly suspect that this bug is not unique to univ-variate polys.



---

archive/issue_comments_009263.json:
```json
{
    "body": "Changing assignee from somebody to broune.",
    "created_at": "2008-05-10T22:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9263",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing assignee from somebody to broune.



---

archive/issue_comments_009264.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-10T22:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9264",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009265.json:
```json
{
    "body": "Attachment [redef_substi.changeset](tarball://root/attachments/some-uuid/ticket1440/redef_substi.changeset) by @JohnCremona created at 2008-05-13 21:56:50\n\nReview and questions:\n\nIf this is just an alias would it not be simpler to just put\n\n```\n    substitute = subs\n```\nin the class definition instead of defining a second function which calls the first?\n\nSecondly, for some reason the patch posted does not display in the normal way, but I don't know why.\n\nI don't really know enough about the issues raised by  jbmohler  to judge this solution;  but if this does solve the problem then the simple assignment I suggested would also!",
    "created_at": "2008-05-13T21:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9265",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [redef_substi.changeset](tarball://root/attachments/some-uuid/ticket1440/redef_substi.changeset) by @JohnCremona created at 2008-05-13 21:56:50

Review and questions:

If this is just an alias would it not be simpler to just put

```
    substitute = subs
```
in the class definition instead of defining a second function which calls the first?

Secondly, for some reason the patch posted does not display in the normal way, but I don't know why.

I don't really know enough about the issues raised by  jbmohler  to judge this solution;  but if this does solve the problem then the simple assignment I suggested would also!



---

archive/issue_comments_009266.json:
```json
{
    "body": "Is it possible to attach a docstring if the function is written using an assignment? Otherwise you would get no docstring, or possibly the docstring for subs, upon calling help on subtitute.",
    "created_at": "2008-05-13T22:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9266",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Is it possible to attach a docstring if the function is written using an assignment? Otherwise you would get no docstring, or possibly the docstring for subs, upon calling help on subtitute.



---

archive/issue_comments_009267.json:
```json
{
    "body": "Replying to [comment:5 broune]:\n> Is it possible to attach a docstring if the function is written using an assignment? Otherwise you would get no docstring, or possibly the docstring for subs, upon calling help on subtitute.\n\n\nNot literally,  but after the assignment they are the __same__ function so the docstring for one is displayed for both.  For example, `prime_factors` is a synonym for `prime_divisors`, and look:\n\n```\nsage: n=123\nsage: n.prime_factors?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in method prime_divisors of sage.rings.integer.Integer object at 0xa124980>\nNamespace:      Interactive\nDocstring:\n\n            The prime divisors of self, sorted in increasing order.  If n\n            is negative, we do *not* include -1 among the prime divisors, since -1 is\n            not a prime number.\n\n            EXAMPLES:\n                sage: a = 1; a.prime_divisors()\n                []\n                sage: a = 100; a.prime_divisors()\n                [2, 5]\n                sage: a = -100; a.prime_divisors()\n                [2, 5]\n                sage: a = 2004; a.prime_divisors()\n                [2, 3, 167]\n```\nAlthough that looks slightly strange, I think it is ok, especially if the docstring mentions the synonym (which in this case it does not, which is my fault since I inserted the synonym while no-one was looking).",
    "created_at": "2008-05-14T08:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9267",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 broune]:
> Is it possible to attach a docstring if the function is written using an assignment? Otherwise you would get no docstring, or possibly the docstring for subs, upon calling help on subtitute.


Not literally,  but after the assignment they are the __same__ function so the docstring for one is displayed for both.  For example, `prime_factors` is a synonym for `prime_divisors`, and look:

```
sage: n=123
sage: n.prime_factors?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in method prime_divisors of sage.rings.integer.Integer object at 0xa124980>
Namespace:      Interactive
Docstring:

            The prime divisors of self, sorted in increasing order.  If n
            is negative, we do *not* include -1 among the prime divisors, since -1 is
            not a prime number.

            EXAMPLES:
                sage: a = 1; a.prime_divisors()
                []
                sage: a = 100; a.prime_divisors()
                [2, 5]
                sage: a = -100; a.prime_divisors()
                [2, 5]
                sage: a = 2004; a.prime_divisors()
                [2, 3, 167]
```
Although that looks slightly strange, I think it is ok, especially if the docstring mentions the synonym (which in this case it does not, which is my fault since I inserted the synonym while no-one was looking).



---

archive/issue_comments_009268.json:
```json
{
    "body": "Attachment [redef_substi2.patch](tarball://root/attachments/some-uuid/ticket1440/redef_substi2.patch) by broune created at 2008-05-14 14:10:52\n\nReplacement for previous patch",
    "created_at": "2008-05-14T14:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9268",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Attachment [redef_substi2.patch](tarball://root/attachments/some-uuid/ticket1440/redef_substi2.patch) by broune created at 2008-05-14 14:10:52

Replacement for previous patch



---

archive/issue_comments_009269.json:
```json
{
    "body": "The new patch uses = to redefine substitute. I would add a doctest, but I don't know where it would go. It does make the code in the ticket work. Either version is fine by me.",
    "created_at": "2008-05-14T14:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9269",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

The new patch uses = to redefine substitute. I would add a doctest, but I don't know where it would go. It does make the code in the ticket work. Either version is fine by me.



---

archive/issue_comments_009270.json:
```json
{
    "body": "I can see no reason not to apply this one-liner (redef_substi2.patch), even if there are other related issues which the patch does not resolve.",
    "created_at": "2008-05-14T21:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9270",
    "user": "https://github.com/JohnCremona"
}
```

I can see no reason not to apply this one-liner (redef_substi2.patch), even if there are other related issues which the patch does not resolve.



---

archive/issue_comments_009271.json:
```json
{
    "body": "I second that, please apply. I'll open a new ticket for:\n\n```\nThis is somewhat tangential to this issue, but subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class. I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded. Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug.\n```",
    "created_at": "2008-06-04T20:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9271",
    "user": "https://github.com/malb"
}
```

I second that, please apply. I'll open a new ticket for:

```
This is somewhat tangential to this issue, but subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class. I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded. Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug.
```



---

archive/issue_comments_009272.json:
```json
{
    "body": "Merged redef_substi2.patch in Sage 3.0.3.alpha1",
    "created_at": "2008-06-04T20:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9272",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged redef_substi2.patch in Sage 3.0.3.alpha1



---

archive/issue_events_003690.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-04T20:55:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1440#event-3690"
}
```



---

archive/issue_comments_009273.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-04T20:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1440#issuecomment-9273",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
