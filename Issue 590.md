# Issue 590: document extended_rational_field.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-05 15:37:42

Assignee: roed

The rings/extended_rational_field.py file is terribly documented.  There are no doctests, no copyright notice, no author, etc.   I think David Roe wrote this:

was`@`ubuntu:~/d/sage/sage/rings$ sage -coverage extended_rational_field.py
----------------------------------------------------------------------
extended_rational_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
OVERALL SCORE: 0%  (2 good, 71 bad)

Missing documentation:
         * __init__(self)
         * _repr_(self)
         * _latex_(self)
         * __call__(self, x, base = 0)
         * _coerce_impl(self, x)
         * _is_valid_homomorphism(self, codomain, im_gens)
         * __iter__(self)
         * complex_embedding(self, prec=53)
         * gens(self)
         * gen(self, n=0)
         * is_prime_field(self)
         * ngens(self)
         * numberfield(self, poly_var, nf_var)
         * __init__(self, x = None, base = 0)
         * __cmp__(self, other)
         * copy(self)
         * lcm(self, other)
         * square_root(self)
         * nth_root(self)
         * _add_(self, right)
         * _sub_(self, right)
         * _neg_(self)
         * _mul_(self, right)
         * _div_(self, right)
         * __invert__(self)
         * __pow__(self, n)
         * __abs__(self)
         * floor(self)
         * ceil(self)
         * __lshift__(self, n)
         * __rshift__(self, n)
         * __init__(self)
         * __cmp__(self, other)
         * __repr__(self)
         * _latex_(self)
         * _add_(self, other)
         * _mul_(self, other)
         * _sub_(self, other)
         * _div_(self, other)
         * _neg_(self)
         * __invert__(self)
         * __abs__(self)
         * __pow__(self, right)
         * sqrt(self)
         * square_root(self)
         * nth_root(self, n)
         * floor(self)
         * ceil(self)
         * numerator(self)
         * denominator(self)
         * __init__(self)
         * __cmp__(self, other)
         * _repr_(self)
         * _latex_(self)
         * _add_(self, other)
         * _mul_(self, other)
         * _sub_(self, other)
         * _div_(self, other)
         * _neg_(self)
         * __invert__(self)
         * __abs__(self)
         * __pow__(self, right)
         * sqrt(self)
         * square_root(self)
         * nth_root(self, n)
         * floor(self)
         * ceil(self)
         * numerator(self)
         * denominator(self)


Missing doctests:
         * numerator(self)
         * denominator(self)




---

Comment by mhansen created at 2008-02-29 06:38:50

Changing assignee from roed to mhansen.


---

Comment by mhansen created at 2008-02-29 06:38:50

Changing status from new to assigned.


---

Attachment


---

Comment by dmharvey created at 2008-03-02 16:15:40

I'm mostly happy with this patch; I have a few questions.

 * What is `IntegerWrapper`? That's been added with no explanation at all, and I don't understand its purpose. Is it really necessary? If so, there needs to be some documentation.

 * regarding `coerce_map_from_impl` and `Q_to_ExtendedQ`: I don't understand the coercion framework any more, so I can't vouch for correctness of the implementations. I'd like someone who understands coercion to take a quick look. Mike, if you find someone on IRC who can sign off on these, that's fine. One thing that bothers me slightly is:


```
sage: ExtendedRationalField.coerce_map_from_impl(ExtendedIntegerRing)
[boom]
```


 * docstring for `ExtendedRational.__init__` is a little confusing; "The class of extended rational numbers" is a little confusing, sounds like "The set of extended rational numbers". Perhaps better something like "Constructor for elements of the extended rational field".

 * `_mul_`: I'd like to see examples of multiplying infinity by infinity and minus infinity

I have various other complaints about this module, but it's not in the new code you've written and I don't want to hold up this patch, so I won't go into them now.


---

Comment by gfurnish created at 2008-03-02 17:35:20

I'm happy with coerce_map_from_impl and Q_to_ExtendedQ, but I think _coerce_impl needs to by default check if its in ExtendedZZ then see if it can be coerced into QQ, then error out.  Current code may not work with things that can be in ExtendedQQ but are not typed as integers (3 in RR).


---

Comment by mhansen created at 2008-03-02 23:27:45

I attached a patch addressing the referee's concerns.


---

Comment by dmharvey created at 2008-03-03 19:48:50

Ummm, the doctests for `sage/rings/extended_integer_ring.py` do not pass for me with this patch.


---

Comment by mhansen created at 2008-03-03 22:32:00

Which ones fail?  What version are you applying against?  If it's the cmp ones, it may just be something random due to architecture differences.


---

Comment by dmharvey created at 2008-03-03 22:58:34

It's mac os 10.4.11 intel. Here's the failure:


```
sage -t  devel/sage-590/sage/rings/extended_integer_ring.py **********************************************************************
File "extended_integer_ring.py", line 58:
    sage: cmp(ExtendedIntegerRing, ExtendedRationalField)
Expected:
    1
Got:
    -1
**********************************************************************
```


Why would cmp be architecture-dependent? Is it comparing pointers somewhere or something stupid like that?


---

Comment by mhansen created at 2008-03-03 23:00:55

Yep.  Python like to be able to compare everything.  With the new coercion stuff coming in, things will have more meaningful _cmp_ functions.


---

Attachment

okay, I'm happy now.


---

Comment by mabshoff created at 2008-03-04 03:53:52

Resolution: fixed


---

Comment by mabshoff created at 2008-03-04 03:53:52

Merged both patches in Sage 2.10.3.rc1
