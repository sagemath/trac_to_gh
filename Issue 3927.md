# Issue 3927: Factorization class has no division implemented

Issue created by migration from https://trac.sagemath.org/ticket/3927

Original creator: cremona

Original creation time: 2008-08-22 12:33:08

Assignee: somebody

Keywords: factorization

This works:

```
sage: factor(10)*factor(15)^(-1)             
2 * 3^-1
```

and so does this:

```
sage: factor(10/15)        
2 * 3^-1
```

but not this:

```
sage: factor(10)/factor(15)     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/john/sage-3.1.test/spkg/build/python-2.5.2.p3/tmp/<ipython console> in <module>()

TypeError: unsupported operand type(s) for /: 'Factorization' and 'Factorization'
```


So: Factorizations can be multiplied and inverted but not divided, which is a bit silly.  I suggest adding a `__div___()` method.


---

Attachment


---

Attachment

Two patches:  the first implements division, the second implements gcd() and lcm() for Factorizations.  The first also fixes a small gap discovered while testing those, namely that for FreeAlgebras, the element 1 could not be inverted.  Now, in any ring, for an element a for which a.is_unit() is true, a.__invert__() returns self.  (For many rings, 1 is the only element for which .is_unit() does not return a NotImplementedError).

Theses patches are essentially orthogonal to the other one #2460 concerning factorization.py.
They are based on 3.1.1.


John


---

Attachment

The third patch deals with the issues left from trac #2460.  Each Factorization now has a universe (cached as attribute `self.__universe`) computed using the Sequence idea proposed in trac #2460.  The base_ring() function has been changed to universe() and returns the universe.  If no universe is found it just sets it to None (for example, this is the case for Factorizations of modular symbol spaces).

I also added a new function is_integral and changed the docstrings to reflect the fact that the exponents needs not be positive (for example, factor(2/3) has always worked and returned a prime factorization with a negative exponent).

Since Factorization is used in a lot of different places I did -testall before posting this, and dealt with a few minor things which arose (no-one minded base_ring() being renamed universe(), but in 2 or 3 places unit_part() was changed to unit()).

All three patches should be applied in order;  based on 3.1.1.

I think the __add__ and __sub__ methods are totally pointless but have left them in for now.


---

Comment by cwitty created at 2008-08-23 23:31:19

I fixed a few issues with gcd and lcm, but everything else looks good.

Positive review.  (Apply all four patches.)


---

Attachment


---

Comment by cremona created at 2008-08-24 08:54:39

Last patch is fine -- thanks.


---

Comment by mabshoff created at 2008-08-25 02:59:58

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 02:59:58

Merged sage-trac3927.patch, sage-trac3927a.patch, sage-trac3927b.patch and trac3927-fix-gcd-lcm.patch in Sage 3.1.2.alpha1
