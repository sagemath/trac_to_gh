# Issue 9633: binomial does not accept float

Issue created by migration from https://trac.sagemath.org/ticket/9633

Original creator: Henryk.Trappmann

Original creation time: 2010-07-29 07:23:07

Assignee: AlexGhitza

CC:  kcrisman


```
sage: binomial(0.5r,5)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call
last)

/home/bo198214/projects/<ipython console> in <module>()

/opt/sage-4.5-linux-32bit-ubuntu_10.04_lts-i686-Linux/local/lib/
python2.6/site-packages/sage/rings/arith.pyc in binomial(x, m)
   2887     if isinstance(x, (float, sage.rings.real_mpfr.RealNumber,
   2888                       sage.rings.real_mpfr.RealLiteral)):
-> 2889         P = x.parent()
   2890         if m < 0:
   2891             return P(0)

AttributeError: 'float' object has no attribute 'parent' 
```




---

Comment by johanbosman created at 2011-04-11 20:22:19

Changing status from new to needs_review.


---

Comment by dsm created at 2011-04-12 06:52:56

Two points: (1) I think "P = parent(x)" is simpler, if I'm reading sage.structure.parent correctly.  (2) Doctest? `:^)`


---

Attachment


---

Comment by johanbosman created at 2011-04-12 09:09:29

Good points. :).


---

Comment by kcrisman created at 2011-04-25 15:58:31

Certainly looks good!   Interesting that we didn't catch that when we put it in, even though it explicitly has 'float' in the previous version :( 

Currently running tests in case there was something subtle about `x.parent()` that was different from `parent(x)`, though I can't see what that would be ...


---

Comment by kcrisman created at 2011-04-25 16:41:26

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-04-25 16:41:26

Pass :)  Good catch.


---

Comment by jdemeyer created at 2011-05-03 12:28:45

Resolution: fixed
