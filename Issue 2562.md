# Issue 2562: [with partial patch] few issues in calculus.py

Issue created by migration from https://trac.sagemath.org/ticket/2562

Original creator: zimmerma

Original creation time: 2008-03-16 22:37:16

Assignee: was

I continue my review of calculus.py (I find it a good way to learn SAGE). There are a few easy
issues I could fix (mostly typos), the other ones are mentioned here, separated by ###...### lines for different issues. The line numbers correspond to 2.10.3.

###############################################################

A definition is missing for is_SymbolicExpression:
-> is_SymbolicExpression? gives no definition.

###############################################################

Line 376:

```
            sage: cmp(SR, SymbolicExpressionRing()) #random
            0
```

-> is that really random?

###############################################################

Line 582:

```
        Here is an inexact element.
            sage: SR(1.9393)
            1.93930000000000
```

-> this is a bad example, since after conversion to binary, the number is an
exact rational:

```
sage: x=1.9393
sage: x.exact_rational()
8733830757359603/4503599627370496
```


###############################################################

Line 656: "The default hashing strategy is to simply hash
        the string representation of an object."
However on a Pentium M I get different hash values:

```
sage: hash(x^2 + 1)
1356423479
sage: hash(repr(x^2+1))
-1487868884
```

Is that normal?

###############################################################

    def __nonzero__(self):
        Return True if this element is definitely not zero.

        EXAMPLES:

```
            sage: k = var('k')
            sage: pol = 1/(k-1) - 1/k - 1/k/(k-1)
            sage: pol.is_zero()
            True
            sage: f = sin(x)^2 + cos(x)^2 - 1
            sage: f.is_zero()
            True
```

the examples are misleading since they demonstrate is_zero and not __nonzero__.

Also "is definitely not zero" should be clearly defined, as the following
example demonstrates:


```
sage: e = sqrt(1002301750441) - 10007*sqrt(10009)
sage: e.is_zero()
False
sage: RealField(200)(e)
0.00000000000000000000000000000000000000000000000000000000000
```

(Remember that deciding zero is undecidable in general.)

###############################################################


```
sage: f = integral(sin(x^2)); f
sage: print f

                                             (sqrt(2)  I + sqrt(2)) x
       sqrt( pi) ((sqrt(2)  I + sqrt(2)) erf(------------------------)
                                                        2
                                                   (sqrt(2)  I - sqrt(2)) x
                      + (sqrt(2)  I - sqrt(2)) erf(------------------------))/8
                                                              2
```

-> it would be nicer to have a blank line between the two output lines,
   since the '2' in the denominator might be confused with some exponent
   of the second line.




---

Attachment


---

Comment by kcrisman created at 2009-09-04 18:51:25

Most of the issues above (as well as the typos in the patch) are no longer in Sage.  Of those that are, the issue about inexactness is fine, because 1.9393 is not in fact in SR, but SR(1.9393) is inexact in that sense.  

It is true that help for is_SymbolicVariable and is_SymbolicExpressionRing is nonexistent, for Python reasons, apparently:

```
sage: is_SymbolicExpressionRing??
Error getting source: could not find class definition
Type: partial
...
partial(func, *args, **keywords) - new function with partial application of the given arguments and keywords.
```

But this can go on a new ticket.

The new patch fixes the rest.


---

Comment by burcin created at 2009-09-10 13:57:54

The use of the word `inexact` in Sage is misleading in general, and there are further problems when talking about elements of the `Symbolic Ring`. AFAIK, Sage regards any element of RR, CC, etc. as inexact. Since `1.9393` is by default in RR, we say that it's inexact. E.g.,


```
sage: t = 1.9393
sage: t.parent()
Real Field with 53 bits of precision
sage: RR
Real Field with 53 bits of precision
sage: t.parent() is RR
True
```


Being `inexact` is a property of a ring, which you test with the `.is_exact()` function. The new `Symbolic Ring` can have arbitrary python objects as elements, so it could in theory have exact members too. However, to cover all cases, it reports that it is inexact:


```
sage: SR.is_exact()
False
```


Maybe in the future we'll move this exactness check to the element level, at least for polynomials, matrices etc. over `SR`, since in many cases it prevents using more efficient algorithms.

The problem reported on line 582 of the old `calculus.py` has moved to line 403 of `sage/symbolic/ring.pyx`. Paul, do you have any suggestions on how to improve the documentation (especially around the place you mentioned) with regards to this issue?

----

Most of the problems pointed out by this ticket don't exist in the new symbolics code, so I would be ok with addressing the two issues in attachment:trac_2562-minor-symb-docs.patch) and closing this ticket. 

Though, I am still not comfortable with the wording here:


```
       Return True if this symbolic expression does not evaluate to  
       (symbolic) zero.
```


I suggest something like


```
        Return True unless this symbolic expression can be shown to be zero.

        Note that deciding if an expression is zero is undecidable in general.
```


It would be better to write more on how the function tests for zero, and explain that there could be cases where it returns `True` for an expression equal to zero (though I couldn't think of an example right now), but I'm willing to give this a positive review with the minor improvement I suggest above.


---

Comment by zimmerma created at 2009-09-10 14:03:54

> Paul, do you have any suggestions on how to improve the documentation (especially around the place you mentioned) with regards to this issue? 

I believe one could simply avoid the wording "exact" or "inexact" in that context.

Paul


---

Comment by kcrisman created at 2009-09-10 14:31:44

Note that most of the places this definition shows up don't even have this much detail.  More typical is:

```
x.__nonzero__() <==> x != 0
```

Anyway, I agree this should be as clear as possible, so hopefully the latest version is okay.  If you come up with an example please add it.

Perhaps tickets could be opened for general improvement of exact/inexactness and for the missing interactive documentation, if Paul or Burcin feel they are worthy of them (I don't feel competent to judge on either of them).


---

Attachment

I am confused with this exactness issue. Please excuse my ignorance of floating point representation issues. 

I don't understand what it means for an element of `RR` to be an _exact rational_. As far as I understand, the `.exact_rational()` function returns the value stored in floating point representation as a rational number (i.e., `mantissa*2^exp` ).


```
sage: RR(1/3).exact_rational()
6004799503160661/18014398509481984
sage: (1.9393).exact_rational()
8733830757359603/4503599627370496
```


However, these rationals don't represent the given value exactly.


```
sage: 1/3 - RR(1/3).exact_rational()
1/54043195528445952
sage: 19393/10000 - RR(1.9393).exact_rational()
-67/2814749767106560000
```


As opposed to:


```
sage: 37/16 - RR(37/16).exact_rational()
0
```


So in this case, can `1.9393` be called inexact?

I'd appreciate any reference where these issues are explained as well.


---

Comment by kcrisman created at 2009-09-12 23:52:49

I think a new ticket should be opened and/or a question asked on sage-devel on this, since it is clearly not  "minor symbolic doc thing" :)  If the current patch is okay, though, this issue shouldn't stop it from getting a positive review, going in, and improving the documentation on those issues.  As I said above, I don't understand the exact/inexact stuff.


---

Comment by zimmerma created at 2009-09-14 07:18:40

Burcin, with respect to your example:

```
sage: 1/3 - RR(1/3).exact_rational()
1/54043195528445952
```

the problem is that when you type RR(1/3), say a is this object, then Sage does not know it comes from 1/3!
If you consider that you only have a=RR(1/3), but you don't know how it was obtained, then every such a is
an exact rational, because the form mantissa*2**exp is always an exact rational.


---

Comment by burcin created at 2009-09-22 10:15:31

Thank you for the explanation. I see your point now, though I think this problem is more related to the use of the words "exact" and "inexact" in Sage.

I'm going to go ahead and give this a positive review.

Even though the sentence "Here is an inexact element" is confusing, I don't think removing it would improve the situation much. Adding something explaining the use of "exact" and "inexact" in Sage to the documentation would be great, but there is no need to hold this patch up waiting for that.


Only apply attachment:trac_2562-minor-symb-docs.patch.


---

Comment by mvngu created at 2009-09-23 04:06:58

Resolution: fixed


---

Comment by mvngu created at 2009-09-23 04:06:58

Merged `trac_2562-minor-symb-docs.patch`.


---

Comment by mvngu created at 2009-09-27 09:46:47

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
