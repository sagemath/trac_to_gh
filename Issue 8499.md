# Issue 8499: partial_fraction_decomposition does not work over algebraic extensions

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-03-11 16:55:05

Assignee: burcin

How can one compute a partial fraction decomposition over the
complex numbers? Consider the following:

```
sage: x = PolynomialRing(RationalField(), 'x').gen()
sage: r = 1 /(x^4 + 1)
sage: r.partial_fraction_decomposition()
(0, [1/(x^4 + 1)])
```

This is ok since we explicitely work over QQ. Now compare with:

```
sage: P.<y> = PolynomialRing(RationalField())
sage: Qbar.<y> = QuotientRing(P, y^2+1)
sage: x = PolynomialRing(Qbar, 'x').gen()
sage: r = 1 /(x^4 + 1)
sage: r.partial_fraction_decomposition()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
```



---

Comment by zimmerma created at 2013-08-24 08:41:21

I found out the solution by myself. If one wants say a decomposition over Q[sqrt(2)] or Q[I], then simply use `QQ[sqrt(2)]` or `QQ[sqrt(-1)]`:

```
sage: R.<x> = QQ[sqrt(2)][]
sage: r=1/(x^4+1)
sage: r.partial_fraction_decomposition()
(0,
 [(-1/4*sqrt2*x + 1/2)/(x^2 - sqrt2*x + 1),
  (1/4*sqrt2*x + 1/2)/(x^2 + sqrt2*x + 1)])
```

or:

```
sage: R.<x> = QQ[sqrt(-1)][]            
sage: r=1/(x^4+1)                       
sage: r.partial_fraction_decomposition()
(0, [(-1/2*I)/(x^2 - I), 1/2*I/(x^2 + I)])
```

Now if you want Sage to automatically find the extension where the denominator fully factors, use
`QQbar`:

```
sage: R.<x> = QQbar[]                   
sage: r=1/(x^4+1)                       
sage: r.partial_fraction_decomposition()
(0,
 [([-0.17677669529663690 .. -0.17677669529663686] - [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [-0.70710678118654758 .. -0.70710678118654746] - [0.70710678118654746 .. 0.70710678118654758]*I),
  ([-0.17677669529663690 .. -0.17677669529663686] + [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [-0.70710678118654758 .. -0.70710678118654746] + [0.70710678118654746 .. 0.70710678118654758]*I),
  ([0.17677669529663686 .. 0.17677669529663690] - [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [0.70710678118654746 .. 0.70710678118654758] - [0.70710678118654746 .. 0.70710678118654758]*I),
  ([0.17677669529663686 .. 0.17677669529663690] + [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [0.70710678118654746 .. 0.70710678118654758] + [0.70710678118654746 .. 0.70710678118654758]*I)])
```

I'll add some examples to the documentation and then we can close this ticket.

Paul


---

Attachment


---

Comment by zimmerma created at 2013-08-24 11:59:17

Changing status from new to needs_review.


---

Comment by zimmerma created at 2013-08-24 11:59:17

I've changed the ticket summary, and attached a patch (against Sage 5.9) which improves the documentation of `partial_fraction_decomposition`.

Paul


---

Comment by zimmerma created at 2013-08-24 12:00:08

Changing type from defect to enhancement.


---

Comment by lftabera created at 2013-12-21 12:35:17

Looks good, but I have a question. How is computing the rational fraction decomposition over QQbar gives you the extension where the denominator splits? It just returns the full decomposition over QQbar no more no less. The extension would be in any case the splitting field of the denominator, isn't it?

I would expect something like "Now if you want Sage to compute an extension where the denominator fully factors, use QQbar: "


---

Comment by lftabera created at 2013-12-21 12:35:17

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2013-12-21 12:51:14

thank you for your feedback. You have two questions in fact:

> How is computing the rational fraction decomposition over QQbar gives you the extension where the denominator splits?

this is given in the denominators of the output.

> The extension would be in any case the splitting field of the denominator, isn't it? 

yes.

Feel free to propose a reviewer patch!

Paul


---

Comment by lftabera created at 2014-01-31 16:02:42

My complain is that using QQbar does not give you the splitting field of the denominator in an obvious way. I have changed the documentation accordingly. Paul, could you take a look at my changes and check if you agree with them?

Luis


---

Comment by lftabera created at 2014-01-31 16:02:42

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2014-01-31 16:20:01

I get an error when I try this example:

```
sage: R.<x> = QQ[]
sage: r = 1/(x^4+2)
sage: N = r.denominator().splitting_field('a')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-9-c9d534f911a3> in <module>()
----> 1 N = r.denominator().splitting_field('a')

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:3873)()

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/structure/misc.so in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1696)()

AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint' object has no attribute 'splitting_field'
```



---

Comment by lftabera created at 2014-01-31 16:23:47

Sorry for not telling, you need sage 6.1 released today...


---

Comment by zimmerma created at 2014-02-04 20:59:45

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2014-02-04 20:59:45

I tried the added examples with Sage 6.1 and they work, thus positive review for me.


---

Comment by vbraun created at 2014-02-07 00:50:02

Resolution: fixed
