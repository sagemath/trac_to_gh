# Issue 9263: airy_ai yields wrong results in arbitrary precision

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-06-18 11:33:59

Assignee: AlexGhitza

CC:  eviatarbach


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n(airy_ai(1),digits=100)
0.1352924163128813861423083153567858971655368804931640625000000000000000000000000000000000000000000000
```

Clearly the last digits are wrong. It looks like Sage only knows how
to compute Ai(x) in double precision, and then extended the double
precision result to 100 digits.
| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
This is a *defect*: an error should be raised if the target precision cannot be attained (or Sage should be able to compute
Ai(x) to arbitrary precision).

I guess this problem concerns other functions than Ai.


---

Comment by ylchapuy created at 2010-06-18 23:54:38

one solution would be to use mpmath:

```
sage: import mpmath
sage: mpmath.mp.dps = 100
sage: mpmath.airyai(1)
mpf('0.1352924163128814155241474235154663061749441429883307060091020547576335348022657236634871099087486832138')
```



---

Comment by eviatarbach created at 2013-06-14 08:23:07

There appear to be two different problems related to numerical evaluation with Maxima. First, that some functions are locked to float precision. In Maxima:


```
(%i15) airy_ai(bfloat(%pi)),fpprec:20;
(%o15)                 airy_ai(3.1415926535897932385b0)
```


I think it's returning unevaluated because `airy_ai` doesn't know how to operate on `bigfloat`s.

Other functions do know how to operate on `bigfloat`s:


```
(%i18) bfloat(spherical_bessel_j(4, bfloat(%pi))),fpprec:200;
(%o18) 6.471630031847746208103870635408583211756194941699504852294921875b-2
```


But, the interface is losing precision:


```
sage: spherical_bessel_J(4, pi.n(digits=1000)).n(digits=100)
0.06471630031847745712081376723290304653346538543701171875000000000000000000000000000000000000000000000
```


This is because Maxima truncates to float precision:



```
(%i20) 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825,fpprec:200;
(%o20)                         3.141592653589793
```


One way of avoiding this is converting to an exact rational and passing it to `bfloat`, which may not be worth the overhead. Maybe something like the patch in #11643?


---

Comment by kcrisman created at 2013-06-14 12:13:39

I believe the "correct" solution (for Sage) for now is to use #12455 and mpmath for (at least default) evaluation.  I've cc:ed you on that ticket.


---

Comment by eviatarbach created at 2013-06-14 18:24:56

Oh, thank you. I guess there's not much use working on the Maxima problems when mpmath works well. I'll change this ticket to apply to all Maxima-evaluated functions.


---

Comment by eviatarbach created at 2013-06-14 18:32:46

Changing component from basic arithmetic to numerical.


---

Comment by eviatarbach created at 2013-06-14 18:32:46

Changing assignee from AlexGhitza to jason, jkantor.


---

Comment by kcrisman created at 2013-06-14 18:40:29

That is a good change.  However, we don't have that many of those left, and so probably it will have to wait until we reliably have a keyword for evaluation algorithm.


---

Comment by kcrisman created at 2013-06-14 18:41:36

Maybe there is a way to sense whether we are passing in something other than regular precision and then ask Maxima to use a bfloat.


---

Comment by eviatarbach created at 2013-06-14 19:09:39

Do you mean #12289? What would be the problem with changing the backend before that's implemented though?

Actually, this ticket applies to many more functions than I thought initially. I added them to the description.

I also changed it again to apply to all special functions that don't work with arbitrary precision.


---

Comment by kcrisman created at 2013-06-14 19:22:03

> Do you mean #12289? What would be the problem with changing the backend before that's implemented though?
No problem at all, I just meant that it would make more sense to switch them to mpmath first, and then worry about getting Maxima to have the right precision after that ticket.  Though I guess even spherical Bessel hasn't been implemented in mpmath yet...


---

Comment by zimmerma created at 2013-08-24 12:55:03

about `hypergeometric_U`, the documentation (in Sage 5.11) says that Pari is the default, contrary to what is said in the description of this ticket. Which one is correct?

Paul


---

Comment by zimmerma created at 2013-08-24 12:58:17

`bessel_K` and `bessel_Y` are fixed in Sage 5.11 thanks to #4102, thus I update the description:

```
sage: n(bessel_K(1,2), prec=100)
0.13986588181652242728459880704
sage: n(bessel_Y(1,2), prec=100)
-0.10703243154093754688837077228
```

Paul


---

Comment by jdemeyer created at 2015-05-06 09:54:48

Works for me.


---

Comment by jdemeyer created at 2015-05-06 09:54:48

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-05-06 09:54:55

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2015-05-06 10:00:34

`hypergeometric_U` is strange, since the answer is always 53 bits:

```
sage: hypergeometric_U(1,2,3)
0.333333333333333
sage: R = RealField(1000)
sage: hypergeometric_U(R(1), R(2), R(3))
0.333333333333333
sage: hypergeometric_U(R(1), R(2), R(3)).n(100)
...
TypeError: cannot approximate to a precision of 100 bits, use at most 53 bits
```


The others work properly.


---

Comment by jdemeyer created at 2015-05-06 10:06:14

And the issue with `hypergeometric_U` is #14896.


---

Comment by zimmerma created at 2015-05-06 11:49:03

with Sage 6.0 I get:

```
sage: R = RealField(1000)
sage: hypergeometric_U(R(1), R(2), R(3)).n(100)
0.33333333333333331482961625625
sage: hypergeometric_U(1,2,3).n(100)
0.33333333333333331482961625625
```

Maybe a regression?


---

Comment by zimmerma created at 2015-05-06 11:53:54

is the issue with `airy_ai` fixed? I still get with Sage 6.0:

```
sage: n(airy_ai(1),digits=75)
0.135292416312881413897883930985699407756328582763671875000000000000000000000
```



---

Comment by jdemeyer created at 2015-05-06 12:14:04

Well, Sage 6.0 is ancient.

With 6.7.beta4:

```
sage: n(airy_ai(1),digits=75)
0.135292416312881415524147423515466306174944142988330706009102054757633534802
```

and

```
sage: hypergeometric_U(1,2,3).n(100)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-7c7c457a86be> in <module>()
----> 1 hypergeometric_U(Integer(1),Integer(2),Integer(3)).n(Integer(100))

/usr/local/src/sage-config/src/sage/structure/element.pyx in sage.structure.element.Element.numerical_approx (build/cythonized/sage/structure/element.c:7437)()
    744         """
    745         from sage.misc.functional import numerical_approx
--> 746         return numerical_approx(self, prec=prec, digits=digits,
    747                                 algorithm=algorithm)
    748     n = numerical_approx

/usr/local/src/sage-config/local/lib/python2.7/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits, algorithm)
   1329 
   1330     if prec > inprec:
-> 1331         raise TypeError("cannot approximate to a precision of %s bits, use at most %s bits" % (prec, inprec))
   1332 
   1333     # The issue is not precision, try conversion instead

TypeError: cannot approximate to a precision of 100 bits, use at most 53 bits
```



---

Comment by kcrisman created at 2015-05-06 15:20:27

Note that Maxima functions we didn't usually have a good precision interface with, if that is what is going on with the hgu.


---

Comment by vbraun created at 2015-05-19 06:43:17

Resolution: worksforme
