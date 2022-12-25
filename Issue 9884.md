# Issue 9884: slow coercion from integer mod ring to integer ring

archive/issues_009884.json:
```json
{
    "body": "Assignee: tbd\n\nSage 4.5.3, 2.6GHz Opteron, Linux\n\nThis is ok:\n\n\n```\nsage: R = Integers(3^20)\nsage: u = R(2)\nsage: timeit(\"z = u.lift()\")\n625 loops, best of 3: 351 ns per loop\n```\n\n\nThis is not:\n\n```\nsage: timeit(\"z = Integer(u)\")\n625 loops, best of 3: 1.27 \u00b5s per loop\n```\n\n\nWhy is this so much slower? Or how is the user supposed to know which one to use?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9885\n\n",
    "created_at": "2010-09-09T16:05:47Z",
    "labels": [
        "component: performance",
        "bug"
    ],
    "title": "slow coercion from integer mod ring to integer ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9884",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux

This is ok:


```
sage: R = Integers(3^20)
sage: u = R(2)
sage: timeit("z = u.lift()")
625 loops, best of 3: 351 ns per loop
```


This is not:

```
sage: timeit("z = Integer(u)")
625 loops, best of 3: 1.27 µs per loop
```


Why is this so much slower? Or how is the user supposed to know which one to use?


Issue created by migration from https://trac.sagemath.org/ticket/9885





---

archive/issue_comments_097802.json:
```json
{
    "body": "This is somewhat slower because Integer.__init__ has a bunch of case statements.  But the patch at #9887 speeds it up some.  If #9887 is positively reviewed, I would suggest closing this ticket.",
    "created_at": "2010-09-23T11:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97802",
    "user": "https://github.com/roed314"
}
```

This is somewhat slower because Integer.__init__ has a bunch of case statements.  But the patch at #9887 speeds it up some.  If #9887 is positively reviewed, I would suggest closing this ticket.



---

archive/issue_comments_097803.json:
```json
{
    "body": "Thinking about it a bit more, we could move the \n`PyObject_HasAttrString(x, \"_integer_\")` check up in `Integer.__init__`.  It should probably be after Integer and Int, but could move above some of the other ones.",
    "created_at": "2010-10-15T08:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97803",
    "user": "https://github.com/roed314"
}
```

Thinking about it a bit more, we could move the 
`PyObject_HasAttrString(x, "_integer_")` check up in `Integer.__init__`.  It should probably be after Integer and Int, but could move above some of the other ones.



---

archive/issue_comments_097804.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T22:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97804",
    "user": "https://github.com/nbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097805.json:
```json
{
    "body": "This at least helps a bit (dropping from 900ns to 580ns in my tests) by avoiding a double attribute lookup that was already highlighted as undesirable in the code.\n----\nNew commits:",
    "created_at": "2014-03-14T22:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97805",
    "user": "https://github.com/nbruin"
}
```

This at least helps a bit (dropping from 900ns to 580ns in my tests) by avoiding a double attribute lookup that was already highlighted as undesirable in the code.
----
New commits:



---

archive/issue_comments_097806.json:
```json
{
    "body": "Looks like we have been working on the issue at the same time! My go at it is at `u/mmezzarobba/9885-intmod_to_int`. And I get:\n* with `develop`:\n  {{{\n  sage: R = Integers(3^20); u = R(2)\n  sage: %timeit u.lift()\n  10000000 loops, best of 3: 106 ns per loop\n  sage: %timeit Integer(u)\n  1000000 loops, best of 3: 466 ns per loop\n  }}}\n* with your patch:\n  {{{\n  sage: %timeit Integer(u)\n  1000000 loops, best of 3: 327 ns per loop\n  }}}\n* with mine:\n  {{{\n  sage: %timeit Integer(u)\n  1000000 loops, best of 3: 289 ns per loop\n  }}}\nSo apparently my version is slightly faster... at least on this particular example.",
    "created_at": "2014-03-15T12:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97806",
    "user": "https://github.com/mezzarobba"
}
```

Looks like we have been working on the issue at the same time! My go at it is at `u/mmezzarobba/9885-intmod_to_int`. And I get:
* with `develop`:
  {{{
  sage: R = Integers(3^20); u = R(2)
  sage: %timeit u.lift()
  10000000 loops, best of 3: 106 ns per loop
  sage: %timeit Integer(u)
  1000000 loops, best of 3: 466 ns per loop
  }}}
* with your patch:
  {{{
  sage: %timeit Integer(u)
  1000000 loops, best of 3: 327 ns per loop
  }}}
* with mine:
  {{{
  sage: %timeit Integer(u)
  1000000 loops, best of 3: 289 ns per loop
  }}}
So apparently my version is slightly faster... at least on this particular example.



---

archive/issue_comments_097807.json:
```json
{
    "body": "It looks like you changed more branches (for the better, I hope). You use a try/except where I use a getattr. I suspect it's better to go with the getattr for the following reasons:\n- The try/except is now also guarding errors that may arise during the execution of the `_integer_` method, not just the ones that arise in looking up the attribute. That could mask genuine errors and cause this method to execute follow-up code when really there is an `_integer_` method available.\n- While try/except is fast to execute when no error is raised, it does incur a large penalty when the attribute is not found (where `getattr(x,\"_integer_\",None)` should return `None` with little penalty). So I expect your code is slower for branches that come below the `x._integer_` branch.\n\nI'd recommend adopting the `getattr` solution and otherwise sticking with your branch.\n\nI've checked and cython produces an inline function for `getattr` that calls `PyObject_GetAttr` and then catches the exception at a rather low level. So perhaps the difference isn't that big. I'm more surprised that cython doesn't seem to specialize these methods to `PyObject_GetAttrString`, so that it can avoid constructing a python string object for the attribute name.\n\n**EDIT:** I've tested the several `getattr`, `PyObject_GetAttr` and `PyObject_GetAttrString` options separately and `getattr` actually does come out as fastest in all situation (although the differences aren't that big). So as is often the case, the cython people have already done the hard work and one should simply write the most straightforward code. In all cases, failing to find the attribute is MUCH more expensive that finding it (by a factor 18), so testing the attribute should come after most other cheap tests.\n\nAnyway, the possibility for catching extraneous errors with guarding too much with try/except is I think the strongest argument.",
    "created_at": "2014-03-15T18:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97807",
    "user": "https://github.com/nbruin"
}
```

It looks like you changed more branches (for the better, I hope). You use a try/except where I use a getattr. I suspect it's better to go with the getattr for the following reasons:
- The try/except is now also guarding errors that may arise during the execution of the `_integer_` method, not just the ones that arise in looking up the attribute. That could mask genuine errors and cause this method to execute follow-up code when really there is an `_integer_` method available.
- While try/except is fast to execute when no error is raised, it does incur a large penalty when the attribute is not found (where `getattr(x,"_integer_",None)` should return `None` with little penalty). So I expect your code is slower for branches that come below the `x._integer_` branch.

I'd recommend adopting the `getattr` solution and otherwise sticking with your branch.

I've checked and cython produces an inline function for `getattr` that calls `PyObject_GetAttr` and then catches the exception at a rather low level. So perhaps the difference isn't that big. I'm more surprised that cython doesn't seem to specialize these methods to `PyObject_GetAttrString`, so that it can avoid constructing a python string object for the attribute name.

**EDIT:** I've tested the several `getattr`, `PyObject_GetAttr` and `PyObject_GetAttrString` options separately and `getattr` actually does come out as fastest in all situation (although the differences aren't that big). So as is often the case, the cython people have already done the hard work and one should simply write the most straightforward code. In all cases, failing to find the attribute is MUCH more expensive that finding it (by a factor 18), so testing the attribute should come after most other cheap tests.

Anyway, the possibility for catching extraneous errors with guarding too much with try/except is I think the strongest argument.



---

archive/issue_comments_097808.json:
```json
{
    "body": "Replying to [comment:6 nbruin]:\n>  - The try/except is now also guarding errors that may arise during the execution of the `_integer_` method, not just the ones that arise in looking up the attribute. That could mask genuine errors and cause this method to execute follow-up code when really there is an `_integer_` method available.\n\nTrue. But that pattern is so common in sage that I don't worry too much.\n\n>  - While try/except is fast to execute when no error is raised, it does incur a large penalty when the attribute is not found (where `getattr(x,\"_integer_\",None)` should return `None` with little penalty). So I expect your code is slower for branches that come below the `x._integer_` branch.\n\nWell, that's the case of the branch used in my timings!\n\n> I'd recommend adopting the `getattr` solution and otherwise sticking with your branch.\n\nI already tried after seeing your version, and the hybrid solution was the slowest of the three (by a significant amount). I didn't try to understand why.",
    "created_at": "2014-03-15T18:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97808",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:6 nbruin]:
>  - The try/except is now also guarding errors that may arise during the execution of the `_integer_` method, not just the ones that arise in looking up the attribute. That could mask genuine errors and cause this method to execute follow-up code when really there is an `_integer_` method available.

True. But that pattern is so common in sage that I don't worry too much.

>  - While try/except is fast to execute when no error is raised, it does incur a large penalty when the attribute is not found (where `getattr(x,"_integer_",None)` should return `None` with little penalty). So I expect your code is slower for branches that come below the `x._integer_` branch.

Well, that's the case of the branch used in my timings!

> I'd recommend adopting the `getattr` solution and otherwise sticking with your branch.

I already tried after seeing your version, and the hybrid solution was the slowest of the three (by a significant amount). I didn't try to understand why.



---

archive/issue_comments_097809.json:
```json
{
    "body": "Replying to [comment:7 mmezzarobba]:\n> I already tried after seeing your version, and the hybrid solution was the slowest of the three (by a significant amount). I didn't try to understand why.\n\nHm, something must have gone wrong in the hybridization then. With this test code:\n\n```\ndef test1(n,x):\n    cdef long N=n\n    for i in range(N):\n        t1(x)\ndef test2(n,x):\n    cdef long N=n\n    for i in range(N):\n        t2(x)\ndef t1(o):\n    cdef object A=getattr(o,\"_integer_\",None)\n    if A is not None:\n        return A\n    else:\n        return None\ndef t2(o):\n    try:\n        return o._integer_\n    except AttributeError:\n        return None\n```\n\nI get\n\n```\nsage: R=GF(5)\nsage: a=R(1)\nsage: timeit('test1(100000,a)')\n125 loops, best of 3: 6.94 ms per loop\nsage: timeit('test2(100000,a)')\n125 loops, best of 3: 7.49 ms per loop\nsage: timeit('test1(100000,R)')\n5 loops, best of 3: 123 ms per loop\nsage: timeit('test2(100000,R)')\n5 loops, best of 3: 146 ms per loop\n```\n\nyou see that `getattr` is consistently faster in looking up the attribute, and also how expensive it is to fail to find it. Other variants using `PyObject_GetAttr` etc. were a little slower still.",
    "created_at": "2014-03-15T18:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97809",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:7 mmezzarobba]:
> I already tried after seeing your version, and the hybrid solution was the slowest of the three (by a significant amount). I didn't try to understand why.

Hm, something must have gone wrong in the hybridization then. With this test code:

```
def test1(n,x):
    cdef long N=n
    for i in range(N):
        t1(x)
def test2(n,x):
    cdef long N=n
    for i in range(N):
        t2(x)
def t1(o):
    cdef object A=getattr(o,"_integer_",None)
    if A is not None:
        return A
    else:
        return None
def t2(o):
    try:
        return o._integer_
    except AttributeError:
        return None
```

I get

```
sage: R=GF(5)
sage: a=R(1)
sage: timeit('test1(100000,a)')
125 loops, best of 3: 6.94 ms per loop
sage: timeit('test2(100000,a)')
125 loops, best of 3: 7.49 ms per loop
sage: timeit('test1(100000,R)')
5 loops, best of 3: 123 ms per loop
sage: timeit('test2(100000,R)')
5 loops, best of 3: 146 ms per loop
```

you see that `getattr` is consistently faster in looking up the attribute, and also how expensive it is to fail to find it. Other variants using `PyObject_GetAttr` etc. were a little slower still.



---

archive/issue_comments_097810.json:
```json
{
    "body": "OK, with this change made to your patch:\n\n```diff\n--- a/src/sage/rings/integer.pyx\n+++ b/src/sage/rings/integer.pyx\n@@ -693,11 +693,10 @@ cdef class Integer(sage.structure.element.EuclideanDomainE\n \n             else:\n \n-                try:\n-                    set_from_Integer(self, x._integer_(the_integer_ring))\n+                otmp=getattr(x,\"_integer_\",None)\n+                if otmp is not None:\n+                    set_from_Integer(self, otmp(the_integer_ring))\n                     return\n-                except AttributeError:\n-                    pass\n```\n\nI get hardly a difference in timing. Using\n\n```\n%cpaste\ncython(\"\"\"\nfrom sage.rings.integer import Integer\ndef test(a,n):\n  cdef long N=n\n  for i in range(N):\n      v=Integer(a)\n\"\"\")\n--\nR = Integers(3^20)\nu=R(2)\ntimeit(\"test(u,100000)\")\n```\n\nI get 20.3 ms for `getattr` and 20.7ms for the `try/except` variant. So, really a minute difference, but still measurable.I'd go for the getattr option, mainly because of the error checking.",
    "created_at": "2014-03-15T19:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97810",
    "user": "https://github.com/nbruin"
}
```

OK, with this change made to your patch:

```diff
--- a/src/sage/rings/integer.pyx
+++ b/src/sage/rings/integer.pyx
@@ -693,11 +693,10 @@ cdef class Integer(sage.structure.element.EuclideanDomainE
 
             else:
 
-                try:
-                    set_from_Integer(self, x._integer_(the_integer_ring))
+                otmp=getattr(x,"_integer_",None)
+                if otmp is not None:
+                    set_from_Integer(self, otmp(the_integer_ring))
                     return
-                except AttributeError:
-                    pass
```

I get hardly a difference in timing. Using

```
%cpaste
cython("""
from sage.rings.integer import Integer
def test(a,n):
  cdef long N=n
  for i in range(N):
      v=Integer(a)
""")
--
R = Integers(3^20)
u=R(2)
timeit("test(u,100000)")
```

I get 20.3 ms for `getattr` and 20.7ms for the `try/except` variant. So, really a minute difference, but still measurable.I'd go for the getattr option, mainly because of the error checking.



---

archive/issue_comments_097811.json:
```json
{
    "body": "You are of course right. I think the hybrid version I tested was with `PyObject_GetAttrString`.\n----\nNew commits:",
    "created_at": "2014-03-16T09:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97811",
    "user": "https://github.com/mezzarobba"
}
```

You are of course right. I think the hybrid version I tested was with `PyObject_GetAttrString`.
----
New commits:



---

archive/issue_comments_097812.json:
```json
{
    "body": "Nils, any chance you can have a quick look at my second commit and set the ticket to positive review? Thanks!",
    "created_at": "2014-04-11T15:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97812",
    "user": "https://github.com/mezzarobba"
}
```

Nils, any chance you can have a quick look at my second commit and set the ticket to positive review? Thanks!



---

archive/issue_comments_097813.json:
```json
{
    "body": "The docstring of `set_from_pari_gen()` doesn't have the right format, it should be an indented `EXAMPLE[S]::` or `TEST[S]::` block, maybe with a line of explanation.",
    "created_at": "2014-05-05T17:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97813",
    "user": "https://github.com/pjbruin"
}
```

The docstring of `set_from_pari_gen()` doesn't have the right format, it should be an indented `EXAMPLE[S]::` or `TEST[S]::` block, maybe with a line of explanation.



---

archive/issue_comments_097814.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-05T17:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97814",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097815.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-05T18:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97815",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_097816.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-05T18:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97816",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097817.json:
```json
{
    "body": "Replying to [comment:12 pbruin]:\n> The docstring of `set_from_pari_gen()` doesn't have the right format, it should be an indented `EXAMPLE[S]::` or `TEST[S]::` block, maybe with a line of explanation.\n\nThanks, I didn't know this was necessary for docstrings that only contain tests.",
    "created_at": "2014-05-05T18:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97817",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:12 pbruin]:
> The docstring of `set_from_pari_gen()` doesn't have the right format, it should be an indented `EXAMPLE[S]::` or `TEST[S]::` block, maybe with a line of explanation.

Thanks, I didn't know this was necessary for docstrings that only contain tests.



---

archive/issue_comments_097818.json:
```json
{
    "body": "I can confirm the speedup, if doctests pass I'll give this a positive review.",
    "created_at": "2014-05-05T20:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97818",
    "user": "https://github.com/pjbruin"
}
```

I can confirm the speedup, if doctests pass I'll give this a positive review.



---

archive/issue_comments_097819.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-05T21:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97819",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-05-06T22:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9884#issuecomment-97820",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
