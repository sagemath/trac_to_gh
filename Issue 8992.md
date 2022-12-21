# Issue 8992: Coercion of univariate quotient polynomial rings

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-05-19 10:26:01

Assignee: robertwb

Keywords: coercion quotient ring

Consider the following setting:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
```


The gcd of the moduli is `(x<sup>2+1)</sup>2`, and so it should be true that the pushout of Q1 and Q2 is the quotient ring with this gcd as modulus. Currently, the pushout raises an error, but with #8800 one has:

```
sage: from sage.categories.pushout import pushout
sage: Q = pushout(Q1,Q2); Q
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
```


However, there remain two bugs that are not covered in #8800 and that prevent a proper coercion of Q1 and Q2.

First bug:

```
sage: Q.has_coerce_map_from(Q1)
False
sage: Q.has_coerce_map_from(Q2)
False
```


Second bug:

```
sage: Q(Q1.gen())
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/sage-4.3.1/devel/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in __call__(self, x)
    272                 return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)
    273         return PolynomialQuotientRingElement(
--> 274                         self, self.__ring(x) , check=True)
    275
    276     def _is_valid_homomorphism_(self, codomain, im_gens):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    310                 x = x.Polrev()
    311
--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)
    313
    314     def is_integral_domain(self, proof = True):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in __init__(self, parent, x, check, is_gen, construct)
    654
    655         if check:
--> 656             x = [QQ(z) for z in x]
    657
    658         self.__list = list(x)

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)()

TypeError: Unable to coerce xbar (<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>) to Rational
sage: Q.gen()
xbar
```


It could be that the following is an additional bug, but perhaps it is just a special case of the previous:

```
sage: Q(str(Q.gen()))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/sage-4.3.1/devel/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in __call__(self, x)
    272                 return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)
    273         return PolynomialQuotientRingElement(
--> 274                         self, self.__ring(x) , check=True)
    275
    276     def _is_valid_homomorphism_(self, codomain, im_gens):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    297                 R = self.base_ring()
    298                 p = Parser(Integer, R, LookupNameMaker({self.variable_name(): self.gen()}, R))
--> 299                 return self(p.parse(x))
    300             except NameError:
    301                 raise TypeError,"Unable to coerce string"

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse (sage/misc/parser.c:3481)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse (sage/misc/parser.c:3345)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_eqn (sage/misc/parser.c:5136)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_expr (sage/misc/parser.c:5456)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_term (sage/misc/parser.c:5681)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:6044)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_power (sage/misc/parser.c:6158)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_atom (sage/misc/parser.c:6711)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.LookupNameMaker.__call__ (sage/misc/parser.c:7653)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6517)()

TypeError: unable to convert xbar to a rational
```



---

Comment by SimonKing created at 2010-05-19 10:54:44

The quotient rings implement their own call method, instead of implementing _element_constructor_. I guess this is where I should start.


---

Comment by SimonKing created at 2010-05-19 11:10:20

I think I found one source of the problem. The call method (that will become an element_constructor method) says:

```
        if isinstance(x, PolynomialQuotientRingElement):
            P = x.parent()
            if P is self:
                return x
            elif P == self:
                return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)
```


In other words: _Only_ if the parent of x is equal to self, it is attempted to convert x into self via conversion in the polynomial ring. I think this condition should simply be dropped.

Furthermore, after the above code block

```
        return PolynomialQuotientRingElement(self, self.__ring(x) , check=True)
```

Hence, it is again tried to interprete x in the polynomial ring of self. But the problem is that the variable names in self and in `self.__ring` are usually different. So, conversion of strings must fail.


---

Comment by SimonKing created at 2010-05-19 12:15:16

A side remark: I just noticed that univariate quotient rings have no representation in Singular. I guess this will be on a different ticket, though.


---

Attachment

_element_constructor_ and _coerce_map_from_ for polynomial quotient rings; may depend on #8800


---

Comment by SimonKing created at 2010-05-19 14:01:19

OK, I have a ticket. I worked on top of my patches for #8807 and #8800, but _if_ this new patch applies then it should be stand-alone (simply try).

What does it provide?

1. Polynomial quotient rings had a call method instead of an _element_constructor_. My patch provides one.

2. Previously, a coercion between polynomial quotient rings was not used, even though it clearly should exist when the modulus of the codomain divides the modulus of the domain. This is now solved, by adding a _coerce_map_from_ method.

3. The old call method relied on the variable names of the underlying polynomial ring, when processing a string. That's obviously wrong, because the variable names of the _quotient_ ring may be different.

4. String evaluation is possible even when one has a polynomial quotient ring over a polynomial ring (example below). This is possible by using `GenDictWithBasering`, which I had originally introduced for infinite polynomial rings.

*__Examples__*

Conversion between two quotient rings (coercion exists only in one direction):

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2])
sage: Q2(Q1.gen())
xbar
sage: Q1(Q2.gen())
xbar
sage: Q1.has_coerce_map_from(Q2)
False
sage: Q2.has_coerce_map_from(Q1)
True
```


Here the underlying polynomial ring has a basering that by itself is a polynomial ring:

```
sage: R.<y> = P[]
sage: Q3 = R.quo([(y^2+1)]); Q3
Univariate Quotient Polynomial Ring in ybar over Univariate Polynomial Ring in x over Rational Field with modulus y^2 + 1
sage: Q3(Q1.gen())  # this uses the lift into the underlying polynomial ring
x
```


String evaluation works (if you think about it, this is non-trivial, since it involves generator names of both Q3 and R):

```
sage: Q3('x*ybar^2')
-x
```


Now, back to the example from the ticket description. If #8807 and #8800 are used as well, one obtains:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: Q1.gen()^2*Q2.gen()^2 + 2*Q1.gen()^2 + 1
0
sage: (Q1.gen()^2*Q2.gen()^2 + 2*Q1.gen()^2 + 1).parent()
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
```


I just realise that I forgot to provide a doc test for _coerce_map_from_. I will post it in a few minutes, and then it's ready for review!


---

Attachment

Additional doc test; to be applied after the previous patch


---

Comment by SimonKing created at 2010-05-19 14:08:58

OK, the doc test is added (testing coercion from a polynomial ring to a quotient ring and between two quotient rings). Ready for review!


---

Comment by SimonKing created at 2010-05-19 14:08:58

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2012-03-11 19:32:49

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-11 19:32:49

Afraid this one has bitrotted -- it needs a rebase.


---

Comment by SimonKing created at 2012-03-11 21:47:56

Apparently, all but the last problem mentioned in the ticket description have already been fixed in other tickets. Namely, with vanilla sage-5.0.beta7, one has

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: from sage.categories.pushout import pushout
sage: Q = pushout(Q1,Q2); Q
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
sage: Q.has_coerce_map_from(Q1)
True
sage: Q.has_coerce_map_from(Q2)
True
sage: Q(Q1.gen())
xbar
sage: Q(str(Q.gen()))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2068, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2068, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2068, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...

TypeError: unable to convert xbar to a rational
```


Also, the `__call__` method of quotient rings has already been replaced by an `_element_constructor_`, as it should.

So, I wouldn't say that the patch needs to be rebased: It has to be rewritten,  or better, it needs to be reduced to those parts that are responsible for making a quotient ring understand the string representation of its generators.


---

Comment by SimonKing created at 2012-03-12 09:55:33

Currently, I can not produce patch that would cover all examples from this ticket. The reason is another bug:

```
sage: P.<y> = QQ['x'][]
sage: y.divides(y)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/simon/SAGE/sage-5.0.beta7/<ipython console> in <module>()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:14887)()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__mod__ (sage/rings/polynomial/polynomial_element.c:15562)()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2919)()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:3302)()

AttributeError: 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense' object has no attribute 'quo_rem'
```


That bug also exists in sage-4.6.2, but apparently it has not been present when I wrote the old patch.

Anyway, I think that bug could be fixed here, I see no need to open yet another ticket.


---

Comment by SimonKing created at 2012-03-12 10:55:55

The reason for my complaint about `y.divides(y)` is that the following example from a comment above would not work with the patch that I am now preparing:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: R.<y> = P[]
sage: Q3 = R.quo([(y^2+1)]); Q3
Univariate Quotient Polynomial Ring in ybar over Univariate Polynomial Ring in x over Rational Field with modulus y^2 + 1
sage: Q3(Q1.gen())  # uses the lift from Q1 to P, which is the base ring of Q3
x
```


The problem is that the coercion framework is not able to find out whether `Q3` has a coerce map from `Q1`.

So, I guess I should add a "try-except" clause in `Q3._coerce_map_from_`, so that an error in division is caught and results in the answer "no, there is no coerce map".


---

Comment by SimonKing created at 2012-03-12 19:41:52

I have produced a new patch.

Recall that most problems mentioned in the ticket description have already been solved in sage-5.0.beta7. The only remaining was conversion from strings.

Here, I suggest to use a tool that I have introduced in my code for infinite polynomial rings: It is a generalisation of the gens_dict of polynomial rings. In contrast to gens_dict, it not only considers the generator names of the ring, but it also considers (recursively) the generator names of the base ring. This recursive version of gens_dict is then passed to sage_eval.

Hence, if Q has generator 'xbar' and is the quotient ring of some polynomial ring P with generator 'x', then `Q('x*xbar')` will be correctly evaluated as `P.gen()*Q.gen()`, which in turn evaluates as `Q(P.gen())*Q.gen()`.

Concerning the problem with `y.divides(...)`: The problem can arise, if Q1 and Q2 are two polynomial quotient rings and one asks `Q1.has_coerce_map_from(Q2)`. It will try to divide the moduli of Q1 and Q2. My suggestion is: If that division fails with an error, then there is no coerce map.

After these changes, the tests in sage/rings/polynomial/polynomial_quotient_ring.py and .../polynomial_quotient_ring_element.py pass.

Let's see if the patchbot finds a reason to complain...

Apply trac8992_conversion_polynomial_quotient_ring.patch


---

Comment by SimonKing created at 2012-03-12 19:41:52

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-03-12 20:15:03

Sorry, I should have mentioned that the patch is for 5.0.beta7, not for 4.8.


---

Comment by SimonKing created at 2012-03-12 20:22:54

Findings of the patchbot: It does apply to 5.0.beta7, the tests pass (except for one test that seems unrelated with my patch).

Nevertheless, I had to modify my patch, because it has added trailing white space. It should be fixed now.

Apply trac8992_conversion_polynomial_quotient_ring.patch


---

Comment by davidloeffler created at 2012-03-12 21:01:51

There are a few typos in your patch: "are no unique", "my lift an", "in principal".


---

Comment by SimonKing created at 2012-03-13 06:21:35

Typos corrected, I hope!

Apply trac8992_conversion_polynomial_quotient_ring.patch


---

Comment by mhansen created at 2012-05-28 22:03:06

This looks pretty good to me.  The one things I worry about is that the result of sage_eval may not actually belong to the correct parent.  I would put a check to make sure that it actually does.  Then, I think we can mark this as positive review.


---

Comment by mhansen created at 2012-05-28 22:04:13

Changing keywords from "coercion quotient ring" to "coercion quotient ring sd40.5".


---

Comment by SimonKing created at 2012-05-31 08:11:56

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-05-31 08:11:56

Replying to [comment:15 mhansen]:
> This looks pretty good to me.  The one things I worry about is that the result of sage_eval may not actually belong to the correct parent.  I would put a check to make sure that it actually does.  Then, I think we can mark this as positive review.

At the moment, we have some problem with converting a string that defines an element of the base ring:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: from sage.categories.pushout import pushout
sage: Q = pushout(Q1,Q2); Q
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
sage: Q(Q1.gen())
xbar
sage: sage: Q(str(Q.gen()))
xbar
sage: Q1(x)
xbar
sage: Q1('x')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2061, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (818, 0))

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/simon/SAGE/sage-5.0/devel/sage-main/<ipython console> in <module>()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7941)()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3345)()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3248)()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in _element_constructor_(self, x)
    419         # Interpretation in self has priority over interpretation in self.__ring
    420         try:
--> 421             return sage_eval(x, GenDictWithBasering(self,self.gens_dict()))
    422         except TypeError, NameError:
    423             pass

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/misc/sage_eval.pyc in sage_eval(source, locals, cmds, preparse)
    197         return locals['_sage_eval_returnval_']
    198     else:
--> 199         return eval(source, sage.all.__dict__, locals)
    200     
    201         

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/all.pyc in <module>()

NameError: name 'x' is not defined
```


I'd like to make that work as well, and then add a test for the correct parent.


---

Comment by SimonKing created at 2012-05-31 08:17:53

Replying to [comment:17 SimonKing]:
> At the moment, we have some problem with converting a string that defines an element of the base ring

Sorry, I meant "cover ring".


---

Comment by SimonKing created at 2012-05-31 08:26:36

Funny. The code was an attempt to convert into the cover ring. But it says

```
        try: 
            return sage_eval(x, GenDictWithBasering(self,self.gens_dict())) 
        except TypeError, NameError: 
            pass 
        try: 
            return PolynomialQuotientRingElement(self, self.__ring(x), check=False) 
        except TypeError: 
            raise TypeError, "unable to convert %s into an element of %s"%(x,repr(self))
```

In the third line, the `NameError` raised by sage_eval is not caught, because I forgot brackets. Arrgh.


---

Comment by SimonKing created at 2012-05-31 08:28:59

Mike, you are right, the wrong parent _can_ occur:

```
sage: Q1('1')
1
sage: _.parent()
Integer Ring
```



---

Attachment

New patch, replacing the old patches


---

Comment by SimonKing created at 2012-05-31 08:40:24

OK, the two issues discussed in the previous posts are fixed and became doc tests. Needs review.

Apply trac8992_conversion_polynomial_quotient_ring.patch


---

Comment by SimonKing created at 2012-05-31 08:40:24

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2012-11-18 20:02:50

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2012-11-18 20:02:50

Looks good to me.


---

Comment by jdemeyer created at 2012-12-17 12:58:03

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-12-19 15:46:23

Resolution: fixed
