# Issue 8344: Factor constant polynomials over QQbar

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2010-02-24 04:15:55

Assignee: AlexGhitza


```
boothby`@`sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f = QQbar['x'](1)
sage: f.roots()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 4.3.2, Release Date: 2010-02-06                       |
| Type notebook() for the GUI, and license() for information.        |
/home/boothby/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:29646)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/complex_roots.pyc in complex_roots(p, skip_squarefree, retval, min_prec)
    339         factors = [(p, 1)]
    340     else:
--> 341         factors = p.squarefree_decomposition()
    342 
    343     prec = 53

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.squarefree_decomposition (sage/rings/polynomial/polynomial_element.c:10808)()

IndexError: list index out of range
sage: 


```


This one should be pretty easy.


---

Comment by dimpase created at 2010-02-24 07:15:31

Changing status from new to needs_work.


---

Comment by dimpase created at 2010-02-24 07:15:31

it's an easy to fix bug in squarefree_decomposition in sage/rings/ 
polynomial/polynomial_element.pyx, line 1142
The case of constant polynomials needs a special treatment.
 
I can fix it if there are no takers...


---

Attachment


---

Comment by dimpase created at 2010-02-26 07:46:18

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-02-26 07:46:18

Replying to [comment:1 dimpase]:
> it's an easy to fix bug in squarefree_decomposition in sage/rings/ 
> polynomial/polynomial_element.pyx, line 1142
> The case of constant polynomials needs a special treatment.
>  
> I can fix it if there are no takers... 

the patch is uploaded (also fixing a similar bug in factors()). Please test etc.


---

Comment by cremona created at 2010-03-08 21:14:08

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-03-08 21:14:08

I don't think this is right.

```
  if self.degree() == 0: 
 	 return Factorization([(self,1)]) 
```

If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.


---

Comment by dimpase created at 2010-03-09 02:04:50

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-03-09 02:04:50

Replying to [comment:3 cremona]:
> I don't think this is right.
> {{{
>   if self.degree() == 0: 
>  	 return Factorization([(self,1)]) 
> }}}
> If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.

I don't understand your remark.
My patch appears to be in accordance with the current design.

sage: f = ZZ['x'](4*x)
sage: f.squarefree_decomposition()
(4) * x
sage: f.factor()
2^2 * x

And it works:

sage: f = ZZ['x'](4)
sage: f.factor()
2^2
sage: f.squarefree_decomposition()
4

sage: f = QQbar['x'](4)
sage: f.factor()
4
sage: f.squarefree_decomposition()
4


---

Comment by dimpase created at 2010-03-09 02:11:22

Replying to [comment:4 dimpase]:

oops, sorry, wrong formatting in my previous comment (look OK in preview...). Fixed here.

> Replying to [comment:3 cremona]:
 > I don't think this is right.
 > {{{
 >   if self.degree() == 0: 
 >  	 return Factorization([(self,1)]) 
 > }}}
 > If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.
 
 I don't understand your remark.
 My patch appears to be in accordance with the current design.

``` 
 sage: f = ZZ['x'](4*x)
 sage: f.squarefree_decomposition()
 (4) * x
 sage: f.factor()
 2^2 * x
}}} 
And it works:
{{{ 
 sage: f = ZZ['x'](4)
 sage: f.factor()
 2^2
 sage: f.squarefree_decomposition()
 4
 
 sage: f = QQbar['x'](4)
 sage: f.factor()
 4
 sage: f.squarefree_decomposition()
 4
}}}


---

Comment by cremona created at 2010-03-09 09:23:43

Sorry if I misunderstood -- I thought that was in the factor() function not the square-free decomposition.  Objection withdrawn (but no proper review yet, sorry).


---

Comment by zimmerma created at 2010-03-14 16:28:32

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-03-14 16:28:32

I tried to review that one, but I have some questions (maybe unrelated to that ticket):

```
sage: R = QQbar['x']
sage: f = R(x)
...
NotImplementedError: symbol
```

This works this way:

```
sage: R.<x> = PolynomialRing(QQbar)
sage: f = R(x)
```

but then:

```
sage: f = R(x^2)
sage: f.factor()
...
NotImplementedError: 
```

What is the point of being able to factor only constant polynomials over QQbar?


---

Comment by cremona created at 2010-03-14 17:13:47

Good point, Paul;  I had forgotten that no-one had done this yet, which is silly since it only takes one line:

```
sage: x = polygen(QQbar)
sage: f = 3*x^2-2
sage: Factorization([(x-r,e) for r,e in f.roots()],unit=f.leading_coefficient())
(3) * (x - 0.8164965809277260?) * (x + 0.8164965809277260?)
```

But doing this for QQbar would also mean doing it for AAbar, which is a little more complicated, which is probably why no-one has done it yet.

```
sage: f = x^4-2
sage: x = polygen(AA)
sage: f = x^4-2      
sage: fr = f.roots(QQbar)
sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())
sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if f.image()>0])
sage: f1*f2
(x - 1.189207115002722?) * (x + 1.189207115002722?) * (x^2 + 1.414213562373095?)
```


It is very tempting to add this as a second patch to the ticket.  Can you see anything wrong in my worked examples here?


---

Comment by zimmerma created at 2010-03-14 17:46:13

Dear John,

your method seems ok to me, however I can't reproduce your first example in Sage 4.3.3:

```
sage: x = polygen(QQbar)
sage: f = 3*x^2-2
sage: lc = f.leading_coefficient()
sage: Factorization([(x-r,e) for r,e in f.roots()])
(x - 0.8164965809277260?) * (x + 0.8164965809277260?)
sage: Factorization([(x-r,e) for r,e in f.roots()],unit=1)
(x - 0.8164965809277260?) * (x + 0.8164965809277260?)
sage: Factorization([(x-r,e) for r,e in f.roots()],unit=lc)
...
TypeError: Illegal initializer for algebraic number
sage: type(lc), parent(lc)
(<class 'sage.rings.qqbar.AlgebraicNumber'>, Algebraic Field)
```

Does it depend on another ticket?


---

Comment by cremona created at 2010-03-14 18:07:37

Replying to [comment:9 zimmerma]:
> Dear John,
> 
> your method seems ok to me, however I can't reproduce your first example in Sage 4.3.3:

> Does it depend on another ticket?

#7984 I think, which was merged in 4.3.4.alpha0.  I was using 4.3.4.alpha1.  Keep up!


---

Comment by dimpase created at 2010-03-15 02:27:41

Replying to [comment:8 cremona]:
> Good point, Paul;  I had forgotten that no-one had done this yet, which is silly since it only takes one line:
> {{{
> sage: x = polygen(QQbar)
> sage: f = 3*x^2-2
> sage: Factorization([(x-r,e) for r,e in f.roots()],unit=f.leading_coefficient())
> (3) * (x - 0.8164965809277260?) * (x + 0.8164965809277260?)
> }}}
> But doing this for QQbar would also mean doing it for AAbar, which is a little more complicated, which is probably why no-one has done it yet.
> {{{
> sage: f = x^4-2
> sage: x = polygen(AA)
> sage: f = x^4-2      
> sage: fr = f.roots(QQbar)
> sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())
> sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if f.image()>0])
> sage: f1*f2
> (x - 1.189207115002722?) * (x + 1.189207115002722?) * (x^2 + 1.414213562373095?)
> }}}
> 
> It is very tempting to add this as a second patch to the ticket.  Can you see anything wrong in my worked examples here?


Shouldn't these roots be exact? (i.e. they should come with intervals isolating them, otherwise one can potentially get
wrong results, mixing numerical noise with true multiplicities --- or is it built-in f.roots() already?)

(same applies to QQbar---although I do not know anything
about isolating complex roots, excuse my ignorance...)


>


---

Comment by cremona created at 2010-03-15 09:30:33

QQbar elements have infinite precision, in effect:  the ? in the output is normal for elements of RIF.  The QQbar implementation automatically increases the precision as necessary.  Each element also comes with a polynomial (over QQ) of which it is a root.

I suggest that you read some of the documentation of QQbar, which is an amazing piece of code!


---

Comment by zimmerma created at 2010-03-15 10:28:16

John,

after applying #7984 on vanilla 4.3.3, your first example works, but the second one still fails:

```
sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())
...
AttributeError: 'Polynomial_generic_dense_field' object has no attribute 'imag'
```

Any other ticket to apply? (Sorry I have no time to install an alpha version.)


---

Comment by cremona created at 2010-03-15 10:41:52

Very sorry, it was a cut-and-paste error.  The lines defining f1 and f2 should read

```
sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if r.imag().is_zero()],unit=f.leading_coefficient())
sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if r.imag()>0])
```

(there was a typo in the second one too).

The trick of testing r.imag()>0 was just a way of picking exactly one conjugate of each pair of non-real conjugate roots.  I think that is quite cheap.  But a better way would be, for each element of AA or QQbar to have a function returning its minpoly over RR (currently the minpoly() function returns its minpoly over QQ).  And we have the norm of an element of QQbar which is the product of it with its CC/RR-conjugate (and not its norm down to QQ), but we do not have a trace:  another function I would like to add!


---

Comment by zimmerma created at 2010-03-15 12:39:38

John, now I can reproduce your two examples. Just waiting for a patch to review, if you still believe we should add that to that ticket...

Paul


---

Comment by zimmerma created at 2010-03-15 12:39:38

Changing status from needs_info to needs_work.


---

Comment by cremona created at 2010-03-15 20:41:56

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-03-15 20:41:56

I think we should use a different ticket for the general factorization of polynomials over QQbar (and AA).  So I will give this a positive review, and open a new ticket which refers to the discussion at this one.


---

Comment by cremona created at 2010-03-15 20:42:07

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-03-15 20:45:56

See #8644 for factoring general polynomials over QQbar and AA.


---

Comment by jhpalmieri created at 2010-04-15 20:10:28

Merged trac-8344.patch in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:10:28

Resolution: fixed


---

Comment by cremona created at 2010-05-26 20:03:40

Replying to [comment:19 cremona]:
> See #8644 for factoring general polynomials over QQbar and AA.

That should read #8544.  A patch is now there.
