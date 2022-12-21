# Issue 9884: slow coercion from integer mod ring to integer ring

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2010-09-09 16:05:47

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



---

Comment by roed created at 2010-09-23 11:29:09

This is somewhat slower because Integer.__init__ has a bunch of case statements.  But the patch at #9887 speeds it up some.  If #9887 is positively reviewed, I would suggest closing this ticket.


---

Comment by roed created at 2010-10-15 08:46:52

Thinking about it a bit more, we could move the 
`PyObject_HasAttrString(x, "_integer_")` check up in `Integer.__init__`.  It should probably be after Integer and Int, but could move above some of the other ones.


---

Comment by nbruin created at 2014-03-14 22:24:09

Changing status from new to needs_review.


---

Comment by nbruin created at 2014-03-14 22:24:09

This at least helps a bit (dropping from 900ns to 580ns in my tests) by avoiding a double attribute lookup that was already highlighted as undesirable in the code.
----
New commits:


---

Comment by mmezzarobba created at 2014-03-15 12:52:26

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

Comment by nbruin created at 2014-03-15 18:16:41

It looks like you changed more branches (for the better, I hope). You use a try/except where I use a getattr. I suspect it's better to go with the getattr for the following reasons:
 - The try/except is now also guarding errors that may arise during the execution of the `_integer_` method, not just the ones that arise in looking up the attribute. That could mask genuine errors and cause this method to execute follow-up code when really there is an `_integer_` method available.
 - While try/except is fast to execute when no error is raised, it does incur a large penalty when the attribute is not found (where `getattr(x,"_integer_",None)` should return `None` with little penalty). So I expect your code is slower for branches that come below the `x._integer_` branch.

I'd recommend adopting the `getattr` solution and otherwise sticking with your branch.

I've checked and cython produces an inline function for `getattr` that calls `PyObject_GetAttr` and then catches the exception at a rather low level. So perhaps the difference isn't that big. I'm more surprised that cython doesn't seem to specialize these methods to `PyObject_GetAttrString`, so that it can avoid constructing a python string object for the attribute name.

*EDIT:* I've tested the several `getattr`, `PyObject_GetAttr` and `PyObject_GetAttrString` options separately and `getattr` actually does come out as fastest in all situation (although the differences aren't that big). So as is often the case, the cython people have already done the hard work and one should simply write the most straightforward code. In all cases, failing to find the attribute is MUCH more expensive that finding it (by a factor 18), so testing the attribute should come after most other cheap tests.

Anyway, the possibility for catching extraneous errors with guarding too much with try/except is I think the strongest argument.


---

Comment by mmezzarobba created at 2014-03-15 18:32:12

Replying to [comment:6 nbruin]:
>  - The try/except is now also guarding errors that may arise during the execution of the `_integer_` method, not just the ones that arise in looking up the attribute. That could mask genuine errors and cause this method to execute follow-up code when really there is an `_integer_` method available.

True. But that pattern is so common in sage that I don't worry too much.

>  - While try/except is fast to execute when no error is raised, it does incur a large penalty when the attribute is not found (where `getattr(x,"_integer_",None)` should return `None` with little penalty). So I expect your code is slower for branches that come below the `x._integer_` branch.

Well, that's the case of the branch used in my timings!

> I'd recommend adopting the `getattr` solution and otherwise sticking with your branch.

I already tried after seeing your version, and the hybrid solution was the slowest of the three (by a significant amount). I didn't try to understand why.


---

Comment by nbruin created at 2014-03-15 18:52:06

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

Comment by nbruin created at 2014-03-15 19:28:18

OK, with this change made to your patch:

```diff
--- a/src/sage/rings/integer.pyx
+++ b/src/sage/rings/integer.pyx
`@``@` -693,11 +693,10 `@``@` cdef class Integer(sage.structure.element.EuclideanDomainE
 
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

Comment by mmezzarobba created at 2014-03-16 09:03:52

You are of course right. I think the hybrid version I tested was with `PyObject_GetAttrString`.
----
New commits:


---

Comment by mmezzarobba created at 2014-04-11 15:45:28

Nils, any chance you can have a quick look at my second commit and set the ticket to positive review? Thanks!


---

Comment by pbruin created at 2014-05-05 17:19:11

The docstring of `set_from_pari_gen()` doesn't have the right format, it should be an indented `EXAMPLE[S]::` or `TEST[S]::` block, maybe with a line of explanation.


---

Comment by pbruin created at 2014-05-05 17:19:11

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-05-05 18:52:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2014-05-05 18:55:05

Changing status from needs_work to needs_review.


---

Comment by mmezzarobba created at 2014-05-05 18:55:05

Replying to [comment:12 pbruin]:
> The docstring of `set_from_pari_gen()` doesn't have the right format, it should be an indented `EXAMPLE[S]::` or `TEST[S]::` block, maybe with a line of explanation.

Thanks, I didn't know this was necessary for docstrings that only contain tests.


---

Comment by pbruin created at 2014-05-05 20:14:15

I can confirm the speedup, if doctests pass I'll give this a positive review.


---

Comment by pbruin created at 2014-05-05 21:05:01

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-05-06 22:02:49

Resolution: fixed
