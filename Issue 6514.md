# Issue 6514: Boolean function for cryptography

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-07-11 18:09:13

Assignee: somebody

CC:  malb mvngu

This module provides a class to study properties such as nonlinearity, resiliency, correlation immunity, algebraic immunity and other cryptographic properties of Boolean functions.

Some of these are still missing, but I think it is a good start.


---

Comment by ylchapuy created at 2009-07-11 18:12:38

Changing keywords from "" to "boolean function, cryptography".


---

Comment by malb created at 2009-07-15 14:29:46

*Review*

 * typo: "This module allow" -> allows
 * it would be nice to have docs for `walsh`, `yellow_code`, `reed_muller`
 * maybe replace "BooleanPolynomial" with ":class:`sage.rings.polynomial.pbori.BooleanPolynomial`" which adds a link in the reference manual
 * `if isinstance(x, list)` could be changed to `if isinstance(x, (list,tuple,GeneratorType)` to be less dependent on the type, you'll need to `from types import GeneratorType`
 * is it wanted that these don't have a type? `cdef _walsh_transform, _nvariables, _big_endian, _nonlinearity`
 * typo: "table truth" -> "truth table"
 * cmp doesn't have a proper doctest
 * Maybe put the world "True" in  "``True``" ?
 * Should() popcount() really return a Python int instead of a Sage integer?

 * Patch applies without error but with some fuzz against 4.1 (this isn't an issue)
 * Doctests pass.
 * Reference manual builds without warning.
 * Reference manual looks good.


---

Comment by malb created at 2009-08-25 22:57:04

Is there any movement on this patch, it shouldn't go wasted?


---

Comment by ylchapuy created at 2009-08-26 07:52:20

I've been quite busy, but I'll send a new patch in the very next few days...


---

Attachment

based on 4.1.1


---

Comment by ylchapuy created at 2009-08-28 14:00:06

Hi,
here is an updated patch. I addressed most of Martin's remarks.
popcount now returns an int, because it's what nbits does.

If someone wants to try some Boolean functions, he can have a look at http://www.ii.uib.no/~mohamedaa/odbf/search.html and compare the results.


---

Comment by malb created at 2009-09-01 10:35:30

Hi, even I don't get some of my earlier comments. Sorry, I was in a rush.

 * it would be nice to have docs for walsh, yellow_code, reed_muller
 * wouldn't it be more appropriate if `cdef _walsh_transform` was a tuple instead of a list?
 * the patch applies cleanly
 * doctests pass
 * you could consider breaking lines at 80 or 120 characters in the docstrings maybe


---

Comment by ylchapuy created at 2009-09-01 19:15:38

Hi,

the last patch

 - adds docs to walsh, yellow_code, reed_muller 
 - uses tuples instead of lists
 - cuts some long lines

Yann


---

Attachment


---

Comment by malb created at 2009-09-01 19:18:34

Great! Positive review.


---

Attachment

full log of doctest failures


---

Comment by mvngu created at 2009-09-02 08:02:06

Merged patches in this order:

 1. `trac_6514_BooleanFunction.patch`
 1. `trac_6514_review.patch`
 
Running the test suite gave me some doctest failures:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py # 3 doctests failed
sage -t -long devel/sage-main/sage/server/notebook/notebook.py # 1 doctests failed
```

A full log is attached. These doctest failures have nothing to do with the above patches; they have been reported before in Sage 4.1.1.


---

Comment by mvngu created at 2009-09-02 08:02:06

Resolution: fixed
