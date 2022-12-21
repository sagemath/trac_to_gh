# Issue 8624: integral of abs(cos(x))*sin(x) gives false results

Issue created by migration from Trac.

Original creator: jeroen

Original creation time: 2010-03-29 16:04:59

Assignee: AlexGhitza

CC:  kcrisman

The integral of abs(cos(x))*sin(x) returns the result as if abs() is ignored:

```
sage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))
-1/2
```

while

```
sage: numerical_integral(abs(cos(x))*sin(x),pi/2,pi)
(0.49999999999999994, 5.5511151231257819e-15)
```




---

Comment by jason created at 2010-03-29 17:31:41

This might be related to this bug, which should be somewhere on trac:


```
sage: integrate(sqrt(cos(x)^2+sin(x)^2), x,0,2*pi)       
pi
```



---

Comment by jason created at 2010-04-20 16:53:52

#8729 may point to a solution


---

Comment by jason created at 2010-04-20 16:54:08

Changing assignee from AlexGhitza to burcin.


---

Comment by jason created at 2010-04-20 16:54:08

Changing component from algebra to calculus.


---

Comment by jason created at 2010-04-20 20:12:30

This patch fixes the problem, but introduces some other doctest errors that should be fixed.


---

Comment by jason created at 2010-04-20 20:12:30

Changing status from new to needs_work.


---

Comment by kcrisman created at 2010-04-20 20:40:06

Make sure it doesn't introduce any errors - sometimes loading extra Maxima packages causes trouble. Also note that elsewhere there are complaints about Maxima start time, which this would contribute to.


---

Comment by jason created at 2010-05-13 04:40:31

Replying to [comment:5 kcrisman]:
> Also note that elsewhere there are complaints about Maxima start time, which this would contribute to.


Sure, but it was *wrong* before, and correctness trumps maxima startup time.  Unless we can detect what kind of integrals need this package loaded and load it dynamically, I think the best thing is to load it up front.


---

Attachment


---

Comment by jason created at 2010-05-13 06:49:34

I think I caught the failing doctests...


---

Comment by jason created at 2010-05-13 06:49:34

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-05-13 12:52:00

I don't like replacing the z85 etc. with z... stuff.  The output is not random, it just changes whenever we change those doctests.  Until we find a way to have Sage parse that and replace it with our own variables (if we even want to do that, which I'm not convinced of), it seems reasonable to just change them.


---

Comment by burcin created at 2010-05-22 10:27:45

It's exciting to see that we can handle one more of the Wester tests. Thanks for the patch Jason.


I get the following errors after applying attachment:trac-8624-abs-integration.patch to 4.4.2:


```
**********************************************************************
File ".../devel/sage-t/sage/functions/piecewise.py", line 780:
    sage: f.integral()
Expected:
    Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)
Got:
    Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)
**********************************************************************
```

Maple simply gives 2 for this one:

```
> integrate(exp(-abs(x)), x=-infinity..infinity);
memory used=3.8MB, alloc=3.1MB, time=0.15
                                       2
```


----

```
**********************************************************************
File ".../devel/sage-t/sage/misc/functional.py", line 705:
    sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h
Expected:
    integrate(sin(x)/x^2, x, 1, 1/2*pi)
Got:
    1/2*gamma(-1, -1/2*I*pi) + 1/2*gamma(-1, 1/2*I*pi) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I)
**********************************************************************
File ".../devel/sage-t/sage/misc/functional.py", line 707:
    sage: h.n()
Expected:
    0.339447940978915...
Got:
    0.339447940978884
**********************************************************************
```


Here's the Maple output:

```
> integrate(sin(x)/x^2, x=1..1/2*Pi);
memory used=7.6MB, alloc=5.1MB, time=0.33
                                               Pi
                    sin(1) Pi - Ci(1) Pi + Ci(----) Pi - 2
                                               2
                    --------------------------------------
                                      Pi
```


It would be interesting to see how this is transformed to the expression with the incomplete gamma function above.

----

```
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 429:
    sage: A = integral(1/ ((x-4) * (x^3+2*x+1)), x); A
Expected:
    1/73*log(x - 4) - 1/73*integrate((x^2 + 4*x + 18)/(x^3 + 2*x + 1), x)
Got:
    1/73*log(x - 4) - 1/73*integrate(x^2/(x^3 + 2*x + 1), x) - 4/73*integrate(x/(x^3 + 2*x + 1), x) - 18/73*integrate(1/(x^3 + 2*x + 1), x)
```


This just distributes the integral to the polynomial in the numerator. It's interesting to see that maxima cannot handle results with algebraic numbers.

----

```
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 464:
    sage: integrate(sin(x)*cos(10*x)*log(x), x)
Expected:
    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
Got:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
```

Here is the result from Maple:

```
> integrate(sin(x)*cos(10*x)*log(x), x);
1/18 ln(x) cos(9 x) - 1/22 ln(x) cos(11 x) - 1/18 Ci(9 x) - 1/198 I Pi

     + 1/198 I Pi csgn(x) + 1/22 Ci(11 x)
```

This looks OK to me.

----

```
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 186:
    sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h
Expected:
    integrate(sin(x)/x^2, x, 1, 2)
Got:
    1/2*gamma(-1, -2*I) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I) + 1/2*gamma(-1, 2*I)
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 188:
    sage: h.n() # indirect doctest
Expected:
    0.4723991772689525...
Got:
    0.472399177268906
**********************************************************************
```

We saw this in `sage/misc/functional.py` already.


---

Comment by burcin created at 2010-05-22 10:27:45

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-05-25 16:19:47

> ----
> {{{
> **********************************************************************
> File ".../devel/sage-t/sage/misc/functional.py", line 705:
>     sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h
> Expected:
>     integrate(sin(x)/x^2, x, 1, 1/2*pi)
> Got:
>     1/2*gamma(-1, -1/2*I*pi) + 1/2*gamma(-1, 1/2*I*pi) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I)
> **********************************************************************
> File ".../devel/sage-t/sage/misc/functional.py", line 707:
>     sage: h.n()
> Expected:
>     0.339447940978915...
> Got:
>     0.339447940978884
> **********************************************************************
> }}}

Hmm, did you have the new Maxima package at #8731 already installed?  This is dealt with there.

> 
> Here's the Maple output:
> {{{
> > integrate(sin(x)/x^2, x=1..1/2*Pi);
> memory used=7.6MB, alloc=5.1MB, time=0.33
>                                                Pi
>                     sin(1) Pi - Ci(1) Pi + Ci(----) Pi - 2
>                                                2
>                     --------------------------------------
>                                       Pi
> }}}
> 
> It would be interesting to see how this is transformed to the expression with the incomplete gamma function above.
> 

Apparently via Gamma(-1,x)=Ei(-x)+e^(-x)/x+1/2 (log(-1/x)-log(-x))+log(x) and the connection between Ei and Ci.  But it does check out!


---

Comment by kcrisman created at 2010-05-25 16:45:34

> {{{
> **********************************************************************
> File ".../devel/sage-t/sage/functions/piecewise.py", line 780:
>     sage: f.integral()
> Expected:
>     Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)
> Got:
>     Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)
> **********************************************************************
> }}}

This is actually ok, because it is supposed to return an antiderivative, not a definite integral.  It is fantastically more complicated than it has to be, but it would simplify to

```
x>0: x --> -e^(-x)
x<0: x --> e^x
```

which is indeed the correct antiderivative.

> Maple simply gives 2 for this one:

Which is clearly correct, and indeed given by the previous line in the file:

```
            sage: f.integral(definite=True)
            2
```


So if this really is all the errors (I will check this with the new Maxima package momentarily), then I would say positive review once the z... are reverted to actual numbers.  I thought of another reason for this - the user reading documentation might be confused about that if they didn't see the actual output.


---

Comment by kcrisman created at 2010-05-25 17:11:06

One more thing; this patch will have a failure in doctest due to the semicolon in line 334 of calculus/calculus.py, which suppresses the output in Sage, of course.  Otherwise I think that (with #8731) this will be a good improvement.


---

Comment by mvngu created at 2010-12-06 12:11:44

Resolution: fixed


---

Comment by mvngu created at 2010-12-06 12:11:44

This is fixed at ticket #10187 by upgrading Maxima to version 5.22.1:


```
[mvngu`@`sage sage-4.6.1.alpha3]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))
1/2
sage: numerical_integral(abs(cos(x))*sin(x),pi/2,pi)
(0.49999999999999994, 5.5511151231257819e-15)
sage: integrate(sqrt(cos(x)^2+sin(x)^2), x,0,2*pi)
2*pi
```

| Sage Version 4.6.1.alpha3, Release Date: 2010-12-05                |
| Type notebook() for the GUI, and license() for information.        |
Mathematica 6.0 also agrees:


```
Mathematica 6.0 for Linux x86 (64-bit)
Copyright 1988-2007 Wolfram Research, Inc.

In[1]:= Integrate[Abs[Cos[x]] * Sin[x], {x,Pi/2,Pi}]

        1
Out[1]= -
        2

In[2]:= Integrate[Sqrt[Cos[x]^2 + Sin[x]^2], {x,0,2*Pi}]

Out[2]= 2 Pi
```


So I'm closing this ticket as fixed.


---

Comment by kcrisman created at 2010-12-06 13:15:54

Is that doctested in the patches for #10187?


---

Comment by jason created at 2010-12-06 13:24:33

What about the other integrals that the patch adds to the doctests?  Do those integrals work now too?  If not, we should reopen this ticket or make a new one for those integrals.


---

Comment by mvngu created at 2010-12-06 13:41:42

Replying to [comment:15 jason]:
> What about the other integrals that the patch adds to the doctests?  Do those integrals work now too?  If not, we should reopen this ticket or make a new one for those integrals.

No. But it shouldn't be difficult to write a documentation patch with doctests in the current ticket. The Sage 4.6.1 release cycle is now in feature freeze, but I think documentation patches are OK for merging in the upcoming release candidates. See #10434 for a follow-up documentation ticket.


---

Comment by kcrisman created at 2010-12-10 20:15:43

So... how's 'bout reopenin' this ticket with a changed title as suggested at #10434?  I don't want to get in trouble with someone, but I might do it myself...


---

Comment by kcrisman created at 2011-06-14 18:14:46

See #11483, since reopening is now not allowed for non-release managers :)
