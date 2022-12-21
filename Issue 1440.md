# Issue 1440: Inconsistency in subs and substitute for univariate polynomials

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-09 21:09:35

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



---

Comment by jbmohler created at 2007-12-26 14:48:19

This is somewhat tangential to this issue, but subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class.  I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded.  Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug.

Note that because of the issues I mention in the first paragraph I highly suspect that this bug is not unique to univ-variate polys.


---

Comment by broune created at 2008-05-10 22:59:43

Changing assignee from somebody to broune.


---

Comment by broune created at 2008-05-10 22:59:49

Changing status from new to assigned.


---

Attachment

Review and questions:

If this is just an alias would it not be simpler to just put

```
    substitute = subs
```

in the class definition instead of defining a second function which calls the first?

Secondly, for some reason the patch posted does not display in the normal way, but I don't know why.

I don't really know enough about the issues raised by  jbmohler  to judge this solution;  but if this does solve the problem then the simple assignment I suggested would also!


---

Comment by broune created at 2008-05-13 22:33:10

Is it possible to attach a docstring if the function is written using an assignment? Otherwise you would get no docstring, or possibly the docstring for subs, upon calling help on subtitute.


---

Comment by cremona created at 2008-05-14 08:14:52

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

Attachment

Replacement for previous patch


---

Comment by broune created at 2008-05-14 14:13:49

The new patch uses = to redefine substitute. I would add a doctest, but I don't know where it would go. It does make the code in the ticket work. Either version is fine by me.


---

Comment by cremona created at 2008-05-14 21:39:16

I can see no reason not to apply this one-liner (redef_substi2.patch), even if there are other related issues which the patch does not resolve.


---

Comment by malb created at 2008-06-04 20:38:04

I second that, please apply. I'll open a new ticket for:

```
This is somewhat tangential to this issue, but subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class. I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded. Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug.
```



---

Comment by mabshoff created at 2008-06-04 20:55:50

Merged redef_substi2.patch in Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-06-04 20:55:50

Resolution: fixed
