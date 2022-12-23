# Issue 5958: [with patch, needs work] MPolynomial_polydict.factor() should accept proof parameter

Issue created by migration from https://trac.sagemath.org/ticket/5958

Original creator: malb

Original creation time: 2009-05-01 15:09:53

Assignee: malb

CC:  john_perry

Keywords: singular, factor

The parameter should be ignored, but for compatibility it is necessary.

E.g. this should work:


```
sage: R.<x,y> = CC[]
sage: I = R.ideal(x^2+y^2-1,x*y-1)
sage: I.variety()
```


but it raises an except in 3.4.1.


---

Comment by malb created at 2009-05-01 15:11:04

The patch fixes the exception, however:


```
sage: sage: R.<x,y> = CC[]
sage: sage: I = R.ideal(x^2+y^2-1,x*y-1)
sage: sage: I.variety()
verbose 0 (1735: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.
[{y: -1.00000000000000}, {y: 0}, {y: 1.00000000000000}]
```


which is certainly the wrong answer (`x` is missing), thus there seems to be another bug.


---

Comment by malb created at 2009-05-01 15:15:44

It seems `toy_variety` does not switch to 'lex' when it should?


---

Attachment


---

Comment by malb created at 2009-05-01 15:30:02

The attached patch switches to lex before calling `toy_variety.triangular_factorization`


---

Comment by AlexGhitza created at 2009-05-02 11:26:17

Two issues:

 * in the first patch, "proofably" should be "provably"
 
 * I'm getting some slight numerical noise in the doctests from the second patch:


```
sage -t  "devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/opt/sage-devel/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py", line 1908:
    sage: for v in I.variety():
       print v
Expected:
    verbose 0 (...: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.
    {y: -0.866025403784439 - 0.500000000000000*I, x: -0.866025403784438 + 0.500000000000000*I}
    {y: -0.866025403784438 + 0.500000000000000*I, x: -0.866025403784438 - 0.499999999999999*I}
    {y: 0.866025403784438 + 0.500000000000001*I, x: 0.866025403784440 - 0.499999999999999*I}
    {y: 0.866025403784439 - 0.500000000000000*I, x: 0.866025403784439 + 0.500000000000000*I}
Got:
    verbose 0 (1735: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.
    {y: -0.866025403784439 - 0.500000000000000*I, x: -0.866025403784439 + 0.500000000000001*I}
    {y: -0.866025403784439 + 0.500000000000000*I, x: -0.866025403784439 - 0.500000000000000*I}
    {y: 0.866025403784438 + 0.500000000000000*I, x: 0.866025403784438 - 0.499999999999999*I}
    {y: 0.866025403784439 - 0.500000000000000*I, x: 0.866025403784438 + 0.500000000000001*I}
**********************************************************************
1 items had failures:
   1 of  36 in __main__.example_34
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-devel/tmp/.doctest_multi_polynomial_ideal.py
	 [12.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py"
Total time for all tests: 12.8 seconds
```



---

Comment by mabshoff created at 2009-05-03 00:18:53

Wrong milestone - better luck in Sage 4.0.

Cheers,

Michael


---

Comment by malb created at 2009-05-07 13:49:16

fix typo


---

Attachment

I fixed the "proofable" vs. "provable" typo. However, I am a bit clueless how to deal with the numerical noise. The `...` works for most of it but not for `0.49999999999` vs. {{{0.500000000}}. Ideas?


---

Comment by john_perry created at 2009-08-21 17:44:03

Martin,

Sorry for the late reply, but according to Lazard's paper, the algorithm I used ("Triangular") does NOT need a lexicographic term ordering. On p. 124, beginning of Section 6:

_These algorithms do not depend explicitly on the ordering; however, they are mainly designed for degree orderings for which the base is more easily obtained; they work also for lexicographic ordering, but, for them, we dispose of a structure theorem which permit us to provide a better algorithm (section 8)._

The algorithm I implemented was Triangular (line 6). So the switch the lexicographic is unnecessary.

I don't know how to fix the problem with complex coefficients, though.


---

Comment by john_perry created at 2009-08-21 17:45:33

Incidentally, I'll look at the problem with the missing x as soon as I finish downloading & compiling the latest Sage. (4.1.1?)


---

Comment by john_perry created at 2009-08-21 21:02:25

I have found two bugs. One of them is not solvable from my end, and possibly not at all (others who know more should comment).

The first one: elim_pol is not always computing the correct polynomial. After removing the switch to lexicographic order, change line 358 (?) of toy_variety.py from

```
  for each in xrange(len(coeffs)-1):
```

to

```
  for each in xrange(len(coeffs)):
```


I have no idea why I had it count until the next-to-last element of coeffs; all of them are necessary. I can submit a patch if you like.

However: even after this fix, a problem remains: line 292 (?) triangular_factorization tries to compute a Groebner basis of an ideal whose generators *should* have a common solution. This is the source of the 1.0 appearing in the triangular variety. Unfortunately, the computed basis is 1.0, suggesting that the ideal has no common solution! I have an idea why this is happening, but I can't yet say for sure.


---

Comment by john_perry created at 2009-08-21 22:41:19

To follow up, the problem occurs when computing the Groebner basis over CC.

I'll use the example given:

The Groebner basis computed is [y^3 + x - y, x^2 + y^2 - 1.00000000000000, x*y - 1.00000000000000].

The result p from elim_pol is y^4 - y^2 + 1.0. (This reflects the bugfix I identified above; it used to return y<sup>4-y</sup>2.)

The first factor q of p is y - 0.866025403784439 - 0.500000000000000*I.

The reduction of B modulo q gives us

[x - 0.866025403784438 + 0.500000000000001*I,
 x^2 - 0.499999999999999 + 0.866025403784439*I,
 (0.866025403784439 + 0.500000000000000*I)*x - 1.00000000000000]

*This should be a consistent system:* the first polynomial is a factor of the second, and the solution to the third is _nearly_ the same as the solution to the first: 0.866025403784438 - 0.500000000000001*I vs. 0.866025403784438 - 0.500000000000000*I. This appears to be a roundoff/floating point error.

The system above should produce a Groebner basis with one polynomial, but it returns [1.00000000000000] instead. This is why nothing is coming back for x. Anyone know how to fix it?


---

Comment by john_perry created at 2009-08-21 22:43:57

Sorry for the repost, but I had some superscript typos in the previou.

To follow up, the problem occurs when computing the Groebner basis over CC.

I'll use the example given:

The Groebner basis computed is [y**3 + x - y, x**2 + y**2 - 1.00000000000000, x*y - 1.00000000000000].

The result p from elim_pol is y**4 - y**2 + 1.0. (This reflects the bugfix I identified above; it used to return y**4-y**2.)

The first factor q of p is y - 0.866025403784439 - 0.500000000000000*I.

The reduction of B modulo q gives us

[x - 0.866025403784438 + 0.500000000000001*I,
 x**2 - 0.499999999999999 + 0.866025403784439*I,
 (0.866025403784439 + 0.500000000000000*I)*x - 1.00000000000000]

*This should be a consistent system:* the first polynomial is a factor of the second, and the solution to the third is _nearly_ the same as the solution to the first: 0.866025403784438 - 0.500000000000001*I vs. 0.866025403784438 - 0.500000000000000*I. This appears to be a roundoff/floating point error.

The system above should produce a Groebner basis with one polynomial, but it returns [1.00000000000000] instead. This is why nothing is coming back for x. Anyone know how to fix it?


---

Comment by malb created at 2009-08-24 11:54:44

Well, we should probably just disallow computing a GB over CC anyway, it doesn't really make sense because CC is not realy a field.


---

Comment by john_perry created at 2009-08-24 17:49:11

You mean CC as implemented, not CC in theory?

I could insert a test for whether the field is CC, and if so raise an exception. That said, the roots we're looking for are algebraic, and so can be described symbolically; i.e., without floating point. So if the polynomial starts from QQ, one could in theory construct the roots. Should the exception just reject the user's input, advise the user to try an extension field, or try to construct one itself?

Is this something I should ask about on sage-devel?


---

Comment by malb created at 2009-08-24 17:55:40

Yes, I mean fixed precision floating point numbers. We could just print a warning? Even if the solutions are algebraic the rounding errors can cause a zero to look like a one.


---

Attachment


---

Comment by john_perry created at 2009-08-26 17:33:18

The uploaded patch should incorporate Martin's changes _and_ should also provide a warning if the field is CC. I'd still like to find a way to make it work in CC, though.


---

Comment by malb created at 2009-08-26 17:57:49

The patch looks good, applies cleanly against 4.1.1 and doctests pass on 64-bit Linux (sage.math). There might be a numerical noise issue (see above) which needs to be addressed.


---

Comment by malb created at 2009-08-26 18:04:45

Ah, the doctest needs a `::` prepended otherwise, it won't be run.


---

Comment by john_perry created at 2009-08-26 18:48:03

which doctest? are you talking about line 1848 of multi_polynomial_ideal.py?


---

Comment by malb created at 2009-08-26 19:15:31

Yes, the doctest starting at 1851.


---

Comment by john_perry created at 2009-08-26 20:48:18

apply over variety_CC.patch


---

Attachment

Okay, double colons on that file. They aren't prepended to the example, though; they appear at the end of line 1849 in the same way as at the end of 1831.

PLEASE tell me this is okay now. Fixing this drove me crazy with hg...


---

Comment by malb created at 2009-08-26 21:06:00

Yes, thats correct this way. However, I expect the doctest will now fail on 32-bit systems (it wasn't run before).


---

Comment by john_perry created at 2009-08-26 22:51:56

I believe that my system is running as a 32-bit system. I know that Linux is running as 32-bit; does sage run differently?


---

Comment by malb created at 2009-08-26 23:37:02

No, if your Linux is 32-bit then your Sage is 32-bit :)


---

Comment by john_perry created at 2009-08-27 00:28:42

still no positive review then? :-( what's still needed?


---

Comment by malb created at 2009-08-27 09:33:17

Sorry, here we go.


---

Comment by mvngu created at 2009-08-30 10:40:06

Which patches should be applied and in what order? The patch `variety_CC.patch` contains all changes made in `mpoly_factor_proof.patch`. Does that mean `mpoly_factor_proof.patch` can be left out?


---

Comment by malb created at 2009-08-30 11:43:26

Indeed, only `variety_CC.patch` and `variety_CC2.patch` should be applied.


---

Comment by mvngu created at 2009-08-30 12:09:06

John -- Please remember to put a sensible commit message in your patch. It's recommended that you reference the ticket number in the commit message. Merged patches in this order:

 1. `variety_CC.patch`
 1. `variety_CC2.patch`


---

Comment by mvngu created at 2009-08-30 12:09:06

Resolution: fixed
