# Issue 3732: calculus -- some examples of sage integration failing

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-28 04:11:23

Assignee: gfurnish

These should be integrated into the doctest framework for sage's calculus. See attached.  This is by Elliot Brossard.


---

Attachment


---

Comment by aginiewicz created at 2008-09-01 23:32:18

There's another example (that's with 3.1.2.alpha2), here it shouldn't need assumption on a:


```
sage: var('a')
a
sage: integrate((x-a)^2*exp(-(x-a)^2), x, -Infinity, +Infinity)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/giniu/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    252     """
    253     try:
--> 254         return f.integral(*args, **kwds)
    255     except ValueError, err:
    256         raise err

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in integral(self, v, a, b)
   2532                     raise ValueError, "Integral is divergent."
   2533                 else:
-> 2534                     raise TypeError, error
   2535                     
   2536 

TypeError: Computation failed since Maxima requested additional constraints (use assume):
Is  a  positive or negative?

```



---

Comment by gnprice created at 2008-10-24 10:25:20

another failing integral


---

Attachment

I added a testcase for another integral, namely `integral( s^2 * exp(- (a + b) * s^2 ), s)`, that fails to integrate.  This is reproduced on Sage 3.1.1.


---

Comment by kcrisman created at 2009-01-29 16:45:24

Added clearer summary.  The second attachment is not relevant to this ticket, though certainly we should be able to integrate arbitrary functions!

What is the purpose of this ticket long-term?  These could be added, complete with their error messages, to calculus.py examples - but we already have several of those.  Or one could say this is just a reminder of what we would eventually like Sage to be able to use Maxima to do, and put them in but not test them.  

Otherwise this is in some sense related to solving #780 (among several others), which is a thornier problem.


---

Comment by kcrisman created at 2009-09-24 00:43:52

With the latest Maxima upgrade and Pynac conversion, the last two integrals are correct - the penultimate one is, of course, 

```
1/2*sqrt(pi)
```

and the last one is 

```
1/2*(a+b)^(3/2)*s^3*gamma_incomplete(-3/2,(a+b)/s^2)/(s^2)^(3/2)
```



---

Comment by kcrisman created at 2009-10-02 16:37:46

Here is the current state of this ticket.  Of the examples in the first attached file, the following are legitimate bugs of this type.

The first example has unnecessary questions.

```
sage: integrate(1/sqrt(x-q), x, 1, 2)
2 sqrt(2 - q) - 2 sqrt(1 - q) # should be this always
```


The third example is definitely a case for this, as of Maxima 5.19.1:

```
(%i19) integrate(log(q-x), x, a, b);
Is  b - a  positive, negative, or zero?

positive;
(%o19)          (b - q) log(q - b) - (a - q) log(q - a) - b + a
(%i20) integrate(log(q-x), x, a, b);
Is  b - a  positive, negative, or zero?

negative;
(%o20)          (b - q) log(q - b) - (a - q) log(q - a) - b + a
(%i21) integrate(log(q-x), x, a, b);
Is  b - a  positive, negative, or zero?

zero;
(%o21)          (b - q) log(q - b) - (a - q) log(q - a) - b + a
```


The fifth example has MANY questions to ask, always the same answer:

```
(%i36) integrate(1/sqrt(q^2-x^2),x, a, b);
Is  b - a  positive, negative, or zero?

negative;
Is  q - a  positive, negative, or zero?

zero;
Is  q + a  positive, negative, or zero?

zero;
Is  q + b  positive, negative, or zero?

positive;
                                 b              a
(%o36)                    asin(------) - asin(------)
                               abs(q)         abs(q)

```


++++++++++++++++++++++++++++++++

The following should not be considered bugs, at least not for the reason given.

The second example is okay:

```
sage: integrate(1/(x-q),x,1,2)
```

Maxima adds pi*I and/or switches q-2 to 2-q as appropriate.  If we don't like those differences, that should be on a different ticket.

The fourth example is:

```
sage: integrate(1/(q-x^2), x)
```

The answers given are a constant away from each other, but look very different.  This probably should be considered a bug (Maxima can't connect between logs and arctan/h stuff), but is likely to not be resolved soon, or by questions. 

The last example is definitely not a bug, as for q=-1 you should get a different answer!


---

Comment by kcrisman created at 2009-12-22 17:02:41

Update: these (the three remaining ones above) are still in Maxima 5.20.1.


---

Comment by @DaveWitteMorris created at 2021-01-27 18:57:21

Here is a particularly easy one (that sympy and giac can do, of course):

```
sage: var("a");
sage: integrate(cos(x), x, 0, a)
    <snip>
ValueError: ...
Is a positive, negative or zero?

sage: integrate(cos(x), x, 0, a, algorithm="sympy")
sin(a)

sage: integrate(cos(x), x, 0, a, algorithm="giac")
sin(a)
```

