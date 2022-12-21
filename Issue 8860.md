# Issue 8860: incoherent types for real numbers

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-05-03 18:10:20

Assignee: AlexGhitza

CC:  leif

This was reported by Francois Maltey:

```
sage: map (type, [float(1.2), N(1.2), N(1.2,digits=50)])

                           [<type 'float'>,
                            <type 'sage.rings.real_mpfr.RealLiteral'>,
                            <type 'sage.rings.real_mpfr.RealNumber'>]
```

Why does the second one return `RealLiteral` and the 3rd one
`RealNumber`?

Side question: how does one test if the type of an object 
corresponds to a real number, like for example:

```
type (345) is Integer, type([1,2,3]) is list, type (2/3) is Rational
```



---

Comment by jason created at 2010-05-03 18:50:46

The docstring for RealLiteral indicates what is going on: "RealLiterals are created in preparsing and provide a way to allow casting into higher precision rings."  So (I think) the digits=50 is casting the RealLiteral 1.2 object into a RealNumber with the desired precision.  RealLiteral just looks like a trivial subclass of RealNumber to just aid in parsing.

side question: when you say type, do you mean the computer science type (i.e., the RealNumber or RealLiteral class)?  Or are you just checking if you have a floating point number (i.e., do you want a python floating point number to also return True?)


---

Comment by zimmerma created at 2010-05-04 07:26:20

Jason,

> The docstring for RealLiteral? indicates...

how do you get this docstring?

```
sage: RealLiteral?
Object `RealLiteral` not found.
```


Anyway, I find it quite disturbing from the user point-of-view to see this "preparsing" side-effect:

```
sage: type(n(1.2,prec=52))
<type 'sage.rings.real_mpfr.RealNumber'>
sage: type(n(1.2,prec=53))
<type 'sage.rings.real_mpfr.RealLiteral'>
sage: type(n(1.2,prec=54))
<type 'sage.rings.real_mpfr.RealNumber'>
```


> side question: ...

I forwarded the question to Francois Maltey. I guess he wants to check for a f-p number, and 
probably a python float should also return True.


---

Comment by jason created at 2010-05-04 14:35:55

Replying to [comment:2 zimmerma]:
> Jason,
> 
> > The docstring for RealLiteral? indicates...
> 
> how do you get this docstring?
> {{{
> sage: RealLiteral?
> Object `RealLiteral` not found.
> }}}


I was browsing the source.  Since RealLiteral is not imported to the global namespace (i.e., it appears to be only a preparser thing), you can't get the docstring just by typing RealLiteral?.  For me, it seems like I can't even get the docstring with the full namespace path.  Can you try `sage.rings.real_mpfr.RealLiteral?`


> 
> Anyway, I find it quite disturbing from the user point-of-view to see this "preparsing" side-effect:
> {{{
> sage: type(n(1.2,prec=52))
> <type 'sage.rings.real_mpfr.RealNumber'>
> sage: type(n(1.2,prec=53))
> <type 'sage.rings.real_mpfr.RealLiteral'>
> sage: type(n(1.2,prec=54))
> <type 'sage.rings.real_mpfr.RealNumber'>
> }}}

I guess the underlying question is: why does the preparser have a special type (i.e., subclass) of RealNumber that it creates, instead of just creating a RealNumber?  That question probably deserves a post to sage-devel, since it's not immediately clear from the documentation.


---

Comment by zimmerma created at 2010-05-04 15:31:19

> Can you try sage.rings.real_mpfr.RealLiteral?

I get:

```
sage: sage.rings.real_mpfr.RealLiteral?
Type:              type
Base Class:     <type 'type'>
String Form:    <type 'sage.rings.real_mpfr.RealLiteral'>
Namespace:      Interactive
File:           /usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so
Docstring:
    x.__init__(...) initializes x; see x.__class__.__doc__ for signature
```

which is not very helpful...


---

Comment by mhansen created at 2010-05-04 20:50:49

Replying to [comment:3 jason]:
> I guess the underlying question is: why does the preparser have a special type (i.e., subclass) of RealNumber that it creates, instead of just creating a RealNumber?  That question probably deserves a post to sage-devel, since it's not immediately clear from the documentation.
> 

It is to solve the problem at http://trac.sagemath.org/sage_trac/ticket/4085.


---

Comment by jason created at 2010-05-04 21:00:14

> It is to solve the problem at http://trac.sagemath.org/sage_trac/ticket/4085.

So is it fair to say that RealLiteral is a decimal-based real number (i.e., like the python [Decimal class](http://docs.python.org/library/decimal.html)), where the actual digits are stored, rather than a binary floating point approximation?  (That's what appears to happen in the code, and seems to be the root cause of the problem at #4085).


---

Comment by mhansen created at 2010-05-04 21:06:31

Nope, it just keeps track of the string that was used to create it.


---

Comment by robertwb created at 2010-05-06 08:46:19

Rather than `type(x) is X` one should use `isinstance(x, X)` which handles subclasses gracefully. In general, I consider the exact value of type(x) to be an implementation detail subject to change. (For example, `type(GF(q, 'a'))` and `type(GF(q, 'a'))` depend on the value `q`, and changes over time.)

`RealLiteral` doesn't do anything fancy (e.g. the sum of two `RealLiteral`s is just a `RealNumber`), it's just used so that floating point literals can be cast into higher precision (or exact) rings without being truncated to an intermediate 53 bit representation first. I consider this a feature rather than a bug.


---

Comment by zimmerma created at 2010-05-06 09:04:20

Robert,

> Rather than type(x) is X one should use isinstance(x, X) ...

thus which X should one use to recognize either x=float(1.2) or x=1.2 or x=n(1.2,100)?

Paul


---

Comment by robertwb created at 2010-05-06 09:17:06

Python's float is completely independent of Sage's class hierarchy, so in this case one would have to do

```
isinstance(x, float) or isinstance(x, RealNumber)
```



---

Comment by zimmerma created at 2010-05-06 09:22:21

Sage 4.3.5:

```
sage: isinstance(1.2, RealNumber)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/<ipython console> in <module>()

TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types
```

Same thing with `isinstance(n(1.2,100), RealNumber)`. Should I open a separate ticket for that?


---

Comment by robertwb created at 2010-05-06 09:36:06

Ah, sorry. That is because RealNumber in the global scope is not the actual type, but a function to create RealNumbers. (This is similar in spirit to how PolynomialRing(...) is a function creating polynomial rings, not a type).  Note that `type(x) is RealNumber` would never work for the same reason. 


```
sage: isinstance(1.2, sage.rings.real_mpfr.RealNumber)
True
```



---

Comment by zimmerma created at 2010-05-06 09:43:19

I find `isinstance(1.2, sage.rings.real_mpfr.RealNumber)` not satisfying for three reasons:

(1) it is much too long, compare say `isinstance(17, Integer)`

(2) it explicitly refers to the underlying implementation and the MPFR component: this should be
    hidden from the user

(3) that underlying implementation may change in the future, which will break some code using
    `sage.rings.real_mpfr.RealNumber`

Thus we need a shortcut like "Integer" for real numbers.

Paul


---

Comment by robertwb created at 2010-05-06 09:49:01

I agree. 

We used to have `is_RealNumber` but that was deprecated. I usually just do something like `x in RR`, unless I really need to know I have exactly a real number (e.g. I'm trying to reach inside and grab it's mpfr_t to initialize myself) in which case the implementation matters.


---

Comment by zimmerma created at 2012-05-22 14:04:28

Changing status from new to needs_review.


---

Comment by zimmerma created at 2012-05-22 14:04:28

I propose to close this ticket, since it seems that `x in RR` solves the original question. I thus put it as "needs review".

Paul


---

Comment by mhansen created at 2012-05-28 05:12:36

Changing keywords from "" to "sd40.5".


---

Comment by mhansen created at 2012-05-28 05:12:36

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2012-05-28 05:12:36

Sounds good.


---

Comment by jdemeyer created at 2012-06-02 12:56:18

Resolution: worksforme
