# Issue 5566: Groebner bases of Symmetric Ideals

Issue created by migration from https://trac.sagemath.org/ticket/5566

Original creator: SimonKing

Original creation time: 2009-03-19 15:25:02

Assignee: SimonKing

CC:  mhansen malb

This ticket is related with [#5453], but the patch should apply to a clean `sage-3.4`.

*Symmetric Ideals* were introduced by [Aschenbrenner and Hillar](http://de.arxiv.org/abs/math/0502078/), meaning "ideals in polynomial rings with countably many variables that are set-wise invariant under all variable permutations"; it was shown that they are finitely generated. 

Later on, Aschenbrenner and Hillar also presented a [Buchberger algorithm](http://de.arxiv.org/abs/0801.4439/) for Symmetric Ideals. 

My aim is to implement this into Sage. The patch provides classes for the Symmetric Polynomial Rings, their elements and their ideals. The methods implement basic polynomial arithmetic, the permutation action, the _Symmetric Cancellation Order_ (a notion that is central in the work of Aschenbrenner and Hillar), symmetric reduction, and the computation of Gröbner bases.

Here are some examples showing the main features

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
```


Now, x and y are generators of X, meaning that we have two infinite sequences of variables, one obtained by `x[n]` and the other by `y[m]` for integers m, n.

We can do polynomial arithmetic in X, and we can create ideals in the usual way:

```
sage: I=X*(x[1]^2+y[2]^2,x[1]*x[2]*y[3]+x[1]*y[4])
```


Now, we can compute a Gröbner basis; the default monomial order is lexicographic (see below).

```
sage: J=I.groebner_basis()
sage: J
Ideal (x1^4 + x1^3, x2*x1^2 - x1^3, x2^2 - x1^2, y1*x1^3 + y1*x1^2, y1*x2 + y1*x1^2, y1^2 + x1^2, y2*x1 + y1*x1^2) of Symmetric polynomial ring in x, y over Rational Field
```


We can do ideal membership test by computing normal forms (symmetric reduction):

```
sage: I.reduce(J)
Ideal (0, 0) of Symmetric polynomial ring in x, y over Rational Field
```


Note that J is not point-wise symmetric. E.g., we have

```
sage: G=J.gens()
sage: P=Permutation([1, 4, 3, 2])
sage: G[2]
x2^2 - x1^2
sage: G[2]^P
x4^2 - x1^2
sage: G.__contains__(G[2]^P)
False
```


But it is set-wise symmetric, e.g.:

```
sage: [(p^P).reduce(J) for p in G]
[0, 0, 0, 0, 0, 0, 0]
```


As usual, it is a special feature of Gröbner bases that they produce unique normal forms. I is not a Gröbner basis, and thus ideal membership test wouldn't work:

```
sage: [p.reduce(I) for p in G]

[x1^4 + x1^3,
 x2*x1^2 - x1^3,
 x2^2 - x1^2,
 y1*x1^3 + y1*x1^2,
 y1*x2 + y1*x1^2,
 y1^2 + x1^2,
 y2*x1 + y1*x1^2]
```


Note that various monomial orders are supported: lex (default), deglex, and degrevlex. 

Note that Aschenbrenner and Hillar restrict their attention to the lexicographic order, and it is not entirely clear whether the Buchberger algorithm would terminate in the other orders, too. But here, it does. As usual, the Gröbner basis depends on the ordering:

```
sage: Y.<x,y> = SymmetricPolynomialRing(QQ,order='degrevlex')
sage: I2=Y*(x[1]^2+y[2]^2,x[1]*x[2]*y[3]+x[1]*y[4])
sage: J2=I2.groebner_basis()
sage: J2
Ideal (y3*x1 - y2*x1, x2^2 - x1^2, y1*x2 - y2*x1, y1^2 + x1^2, x2*x1^2 - x1^3, y1*x1^2 + y2*x1, y2*x1^2 + y2*x1, y2*x2*x1 + y2*x1, y2*y1*x1 + x1^3, x1^4 + x1^3) of Symmetric polynomial ring in x, y over Rational Field
```


Note that we assume an automatic (name-preserving) conversion between X and Y. Hence, we can do the following and see that J2 is not a _lexicographic_ Gröbner basis:

```
sage: J.reduce(J2)
Ideal (0, 0, 0, y2*x1 + y1*x1^2, y2*x1 + y1*x1^2, 0, y2*x1 + y1*x1^2) of Symmetric polynomial ring in x, y over Rational Field
```


In any order, we insist to have `X.gen(i)[m]<X.gen(j)[n]` if and only if i<j or (i==j and m<n).

Probably the doc tests should be improved, and I think it would also be nice to overload the `__pow__` and `__mul__` methods for Symmetric Ideals, since the default methods do not give the correct result: We should have `(X*(x[1]))^2 == X*(x[1]^2,x[1]*x[2])`.
Also, it may be that there should be no coercion between X and Y in the above situation.

Therefore I am uncertain whether it is 'needs review' or 'needs work'. I think I leave it as 'with patch'...


---

Comment by SimonKing created at 2009-03-20 19:51:16

Changing keywords from "" to "Symmetric Ideal".


---

Comment by SimonKing created at 2009-03-20 20:02:44

I think that now the patch is ready for review. Please have a look at the ReST formatting of the doc strings, as this is my first exposition to ReST.


---

Comment by SimonKing created at 2009-03-21 07:20:33

Sorry, please disregard the second attachment (SymmetricIdeals2.patch). It was a mistake.


---

Comment by SimonKing created at 2009-03-21 08:44:10

I think that my patch is already useful for computing symmetric Gröbner bases. However, I think I need to work on one corner case: Variable shift zero.

One problem is: The argument of a permutation must be positive. Hence,

```
sage: X.<x> = SymmetricPolynomialRing(QQ)
sage: P=Permutation([2,1])
sage: x[0]^P
Traceback (most recent call last):
...
TypeError: i (= 0) must be between 1 and 2
```


Since I want to have a permutation action, it follows that I must disallow variable shift zero. This is what I tried in the patch SymmetricIdeals2.patch, which yields an error when calling x[0].

However, with the second patch, one still has 

```
sage: X.<x> = SymmetricPolynomialRing(QQ)
sage: R=PolynomialRing(ZZ,['x0'])
sage: X('x0')
x0
sage: X(R('x0'))
x0
```


I see two ways to proceed:
 1. Allow x[0], but make it _inert_ against permutations, i.e., x[0]**P==x[0] for any permutation P. This also means that (x[1]).reduce([x[0]]) is x[1], not 0.
 2. Strictly forbid x[0]. Then the coercion would be slightly slower, due to additional tests.

I prefer option 1, but if you care you may try to convince me of 2.


---

Comment by SimonKing created at 2009-03-27 10:14:17

I think that now my implementation is in a shape that allows for applications. In fact, i already computed a Symmetric Groebner Basis that should provide a topological invariant for knots and links.

As i announced above, i made variables of index zero _inert_ against permutations / permutation group elements. So, we have

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: P = SymmetricGroup(5).random_element()
sage: x[0]^P
x0
```


Compared with my first implementation, reduction is now a lot faster. This is since i now use the usual libsingular-reduction as much as possible. 

Another trick is that i try to find a compromise between the requirement of small parents versus the feature of having a common parent for all underlying finite polynomials: While computing with symmetric ideals, in some cases a common parent is found for the underlying polynomials of all generators of the ideal.

Example: if we start with an ideal 

```
sage: I = X*(x[1]*y[1],x[50]*y[1000])
```

then we will have

```
sage: [p._p.parent() for p in I.gens()] # start with different rings

[Multivariate Polynomial Ring in x1, y1 over Rational Field,
 Multivariate Polynomial Ring in x50, y1000 over Rational Field]
sage: J=I.groebner_basis()
sage: J
Ideal (x1*y1, x50*y1000, x51*y1) of Symmetric polynomial ring in y, x over Rational Field
sage: [p._p.parent() for p in J.gens()] # end with common rings

[Multivariate Polynomial Ring in x51, x50, x1, y1000, y1 over Rational Field,
 Multivariate Polynomial Ring in x51, x50, x1, y1000, y1 over Rational Field,
 Multivariate Polynomial Ring in x51, x50, x1, y1000, y1 over Rational Field]
```


In that way, we make arithmetic fast (<= common ring) and slim at the same time.


---

Comment by SimonKing created at 2009-03-27 16:34:43

Replying to [comment:6 SimonKing]:
> Example: if we start with an ideal 
> {{{
> sage: I = X*(x[1]*y[1],x[50]*y[1000])
> sage: J=I.groebner_basis()
> sage: J
> Ideal (x1*y1, x50*y1000, x51*y1) of Symmetric polynomial ring in y, x over Rational Field
> }}}

ARRGH! This result is complete nonsense. I need to find out what happened. Needs work. Sorry


---

Comment by SimonKing created at 2009-03-27 19:14:33

Replying to [comment:7 SimonKing]:
> Replying to [comment:6 SimonKing]:
> > Example: if we start with an ideal 
> > {{{
> > sage: I = X*(x[1]*y[1],x[50]*y[1000])
> > sage: J=I.groebner_basis()
> > sage: J
> > Ideal (x1*y1, x50*y1000, x51*y1) of Symmetric polynomial ring in y, x over Rational Field
> > }}}
> 
> ARRGH! This result is complete nonsense. I need to find out what happened. Needs work. Sorry

Got it! The new version of ``SymmetricIdeals.patch`` should still apply to sage-3.4 (tell me if I messed it up), and fixes the bug.

Let N be the maximal variable index occuring in the generators of a symmetric ideal I. According to Aschenbrenner, one has to apply all elements of Sym(N) to the generators, form all S-polynomials, interreduce, then apply Sym(N+1), and so on, until it stabilizes.

Sym(N) can be rather huge, so i tried to be clever: Apply the _generators_ of Sym(N) to the generators of J, interreduce, and repeat until it stabilizes; i thought this is the same as applying _all_ elements of Sym(N), but i was mistaken.

Now i proceed more carefully. I introduced a method 'squeezed', that makes the variable indices as small as possible, without to change the ideal. So, the N above is decreased. Next i apply _all_ elements of Sym(N) to the generators of `I.squeezed()`. Compute the S-polynomials and interreduce (which i do using libsingular's groebner method). 

The result takes care of symmetry out to level N. In order to make it symmetric out to N+1, it then suffices to apply coset representatives of Sym(N+1)/Sym(N), namely (1,N+1), (2,N+1), ..., (N,N+1). The rest is, again, computation of S-polynomials and interreduction, and iteration. 

Do you agree that this is a correct improvement of the algorithm of Aschenbrenner and Hillar?

Anyway. 
The critical example from above is now

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: I = X*(x[1]*y[1],x[50]*y[1000])
sage: [p._p.parent() for p in I.gens()] # start with different rings

[Multivariate Polynomial Ring in y1, x1 over Rational Field,
 Multivariate Polynomial Ring in y1000, x50 over Rational Field]
sage: sage: J=I.groebner_basis()
sage: sage: J
Ideal (y1*x1, y1*x2, y2*x1) of Symmetric polynomial ring in x, y over Rational Field
sage: sage: [p._p.parent() for p in J.gens()] # end with common rings

[Multivariate Polynomial Ring in y2, y1, x2, x1 over Rational Field,
 Multivariate Polynomial Ring in y2, y1, x2, x1 over Rational Field,
 Multivariate Polynomial Ring in y2, y1, x2, x1 over Rational Field]
```


And this is indeed the symmetric Groebner basis.


---

Comment by SimonKing created at 2009-03-30 11:45:04

Herewith i try to unify the dense and the sparse approach towards infinite polynomial rings of ticket #5453. Also, when computing symmetric Groebner bases, i strictly do as suggested by Aschenbrenner and Hillar, without the attempt to be clever.

Here i repeat the main examples from above, with the new syntax, and partially with corrected results:

```
sage: X.<x,y> = InfinitePolynomialRing(QQ)
sage: I=X*(x[1]^2+y[2]^2,x[1]*x[2]*y[3]+x[1]*y[4])
sage: J=I.groebner_basis(); J
Symmetric Ideal (x1^4 + x1^3, x2*x1^2 - x1^3, x2^2 - x1^2, y1*x1^3 + y1*x1^2, y1*x2 + y1*x1^2, y1^2 + x1^2, y2*x1 + y1*x1^2) of Infinite polynomial ring in x, y over Rational Field
sage: I.reduce(J)
Symmetric Ideal (0, 0) of Infinite polynomial ring in x, y over Rational Field
```


Note that indeed the result is a symmetric Gröbner basis (which was not the case in the original example that i gave):

```
sage: for P in Permutations(4):
....:     print [(p^P).reduce(J) for p in J.gens()]
....:
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
```


The same example in 'deglex' or 'degrevlex' works, too, but it takes longer.

Note that the implementation is now _dense_:

```
sage: x[7]; X.polynomial_ring()
sage: x[7]; X.polynomial_ring()
x7
Multivariate Polynomial Ring in y7, y6, y5, y4, y3, y2, y1, y0, x7, x6, x5, x4, x3, x2, x1, x0 over Rational Field
```


I just stumbled over another error: When trying to compute this example in the sparse implementation, it fails, since at some place a univariate polynomial occurs, which has no reduce method. 

It really sucks that uni- and multivariate polynomials have a different interface!

Continuing with the examples:
If high variable indices occur, the dense implementation is not good. But the following works in the sparse implementation.

```
sage: X.<x,y> = InfinitePolynomialRing(QQ,implementation='sparse')
sage: P = SymmetricGroup(5).random_element()
sage: x[0]^P
x0
sage: I = X*(x[1]*y[1],x[50]*y[1000])
sage: [p._p.parent() for p in I.gens()]
[Multivariate Polynomial Ring in y1, x1 over Rational Field,
 Multivariate Polynomial Ring in y1000, x50 over Rational Field]
sage: J=I.groebner_basis(); J
Symmetric Ideal (y1*x1, y1*x2, y2*x1) of Infinite polynomial ring in x, y over Rational Field
sage: [p._p.parent() for p in J.gens()]
[Multivariate Polynomial Ring in y1, x1 over Rational Field,
 Multivariate Polynomial Ring in y1, x2 over Rational Field,
 Multivariate Polynomial Ring in y2, x1 over Rational Field]
```


OK. 

Summary: It is a common interface for both implementations, but i need to work on the reduce method.


---

Comment by SimonKing created at 2009-03-30 12:06:50

Replying to [comment:11 SimonKing]:
...
> sage: X.<x,y> = InfinitePolynomialRing(QQ)
> sage: I=X*(x[1]<sup>2+y[2]</sup>2,x[1]*x[2]*y[3]+x[1]*y[4])
> sage: J=I.groebner_basis(); J
> Symmetric Ideal (x1^4 + x1^3, x2*x1^2 - x1^3, x2^2 - x1^2, y1*x1^3 + y1*x1^2, y1*x2 + y1*x1^2, y1^2 + x1^2, y2*x1 + y1*x1^2) of Infinite polynomial ring in x, y over Rational Field
...
> I just stumbled over another error: When trying to compute this example in the sparse implementation, it fails, since at some place a univariate polynomial occurs, which has no reduce method. 

It is fixed in reduce_bugfix.patch. Now, we have in the sparse implementation:

```
sage: X.<x,y> = InfinitePolynomialRing(QQ,implementation='sparse')
sage: I=X*(x[1]^2+y[2]^2,x[1]*x[2]*y[3]+x[1]*y[4])
sage: J=I.groebner_basis(); J
Symmetric Ideal (x1^4 + x1^3, x2*x1^2 - x1^3, x2^2 - x1^2, y1*x1^3 + y1*x1^2, y1*x2 + y1*x1^2, y1^2 + x1^2, y2*x1 + y1*x1^2) of Infinite polynomial ring in x, y over Rational Field
```

which coincides with the result in the dense implementation.

So, hope it is ready for review...


---

Comment by malb created at 2009-04-12 09:45:59

Hi Simon, quick question: Why does `groebner_basis()` return an ideal instead of a `Sequence`? Sage's default is to return a `Sequence`.


---

Comment by SimonKing created at 2009-04-12 14:24:07

Hi Martin,

Replying to [comment:14 malb]:
> Hi Simon, quick question: Why does `groebner_basis()` return an ideal instead of a `Sequence`? Sage's default is to return a `Sequence`.

Very easy answer: I was not aware that it is the default.

In the last two weeks I tried various improvements (performance-wise). Currently I am more or less in vacancy. If I'll be back at work, my plan is to change groebner so that it returns `Sequence`s, to update the doc tests, and to post the most recent version perhaps end of next week. And I will also not forget to create a ticket about `GroebnerStrategy` for libsingular.


---

Comment by SimonKing created at 2009-04-14 22:21:36

I forgot to change the tag for this ticket (needs work). 

Recently I was improving the performance of reduction, by adding some Cython module that provides a Reduction Strategy class for symmetric ideals. In applications, this seems to work very well. After updating the doc tests, I will post the new patch bomb, probably end of this week.


---

Comment by malb created at 2009-04-16 14:39:37

Hi Simon,
 * I've deleted the redundant attachments, (you need special rights to do that)
 * Can you confirm that Mike is happy with the infinite polynomial ring interface?
 * btw. you can simply write (`foo in bar` instead of `bar.__contains__(foo)`.


---

Comment by SimonKing created at 2009-04-16 14:48:31

Replying to [comment:18 malb]:
> Hi Simon,
>  * I've deleted the redundant attachments, (you need special rights to do that)

Why hasn't the owner all rights for his/her tickets?

>  * Can you confirm that Mike is happy with the infinite polynomial ring interface?
I can only hope (I haven't heard of Mike for a long time).

At least I would expect that he likes it, because it is his original terminology ('InfinitePolynomialRing', not 'SymmetricPolynomialRing')... 

Btw., I would insist on the name 'SymmetricIdeal' and 'SymmetricReduction' since this is the terminology of Aschenbrenner and Hillar.

>  * btw. you can simply write (`foo in bar` instead of `bar.__contains__(foo)`.
Ok, but I think I wouldn't rewrite the code for that reason...


---

Comment by SimonKing created at 2009-04-16 15:16:20

Since many things changed, here is an account of what the patch provides:
 * Two implementations of polynomial rings over fields with countably many generators, indexed by natural numbers:
   - A sparse implementation, that allows for working with very high variable indices
   - A dense implementation, that is much faster provided the variable indices are not too big.
 * Elements of these infinite polynomial rings, with usual arithmetic and with a permutation action on the variables.
 * Symmetric Ideals, which are ideals that, in addition, are invariant under variable permutation.
 * Gröbner stuff:
   - A symmetric version of polynomial reduction, based on the Cython class 'SymmetricReductionStrategy' that tries to perform the reduction in an efficient way (idea: keep intermediate results small).
   - Symmetric Interreduction
   - Computation of Symmetric Gröbner bases, which is at least possible for lexicographic term order, according to Aschenbrenner and Hillar.

*__Disclaimer__*

I am afraid that again I tried to be clever in implementing the symmetric Gröbner basis computation. The following is my justification:

The underlying idea of any Gröbner basis computation (symmetric or straight) is:
 * Perform certain operations that may yield new leading monomials.
 * Continue to perform these operations until it stabilizes.

In the case of symmetric ideals, these operations are (according to Aschenbrenner and Hillar):
 1. S-polynomials
 2. The action of Sym(N), the full symmetric group, where N is some number that will increase until it stabilizes.

I replace Sym(N) by the elementary transpositions (i,j) for i,j<=N. I think this works, for the following reason:
 * Let m, n be monomials, m<n, and let P in Sym(N) be a permutation so that `m<sup>P>n</sup>P`.
 * The action of P does not change the polynomial degree. Hence, in all of our term orders (lex, deglex, degrevlex), "`m<n but m<sup>P>n</sup>P`" can only occur if P changes the lexicographic order of m and n.
 * If it changes the lexicographic order then we find indices i, j so that 
   - the exponents of x_k in m and n coincide, for all k<i
   - the exponent of x_i in m is smaller than the exponent of x_j in m
   - P(j)=i.
 * Hence, the elementary transposition (i,j) would change the order of m and n as well.

In other words, if there is a permutation that turns a non-leading monomial into a leading monomial, then there is an elementary transposition that does the job as well.

I am sorry to do mathematics here. With that trick, I can do serious examples (20000 polynomials out to variables index 10), which would be impossible when studying _all_ permutations.


---

Comment by malb created at 2009-04-16 15:59:51

Replying to [comment:19 SimonKing]:
> Why hasn't the owner all rights for his/her tickets?

I don't know, I didn't design trac. I guess our workflow is unusal.
 
> >  * btw. you can simply write (`foo in bar` instead of `bar.__contains__(foo)`.
> Ok, but I think I wouldn't rewrite the code for that reason...

It was only a suggestion.


---

Comment by mabshoff created at 2009-04-16 21:16:58

Replying to [comment:21 malb]:
> Replying to [comment:19 SimonKing]:
> > Why hasn't the owner all rights for his/her tickets?
> 
> I don't know, I didn't design trac. I guess our workflow is unusal.

The permission model does not allow it since it isn't that fine grained.

Cheers,

Michael


---

Comment by malb created at 2009-04-17 12:02:27

*Review*
 * this patch should go in soon, because it is quite big already
 * please document the parameters for {{{InfinitePolynomial.__init__}}
 * note that `__foo__` functions are not included in the docs, so I guess the `__init__` docs should be class level docs.
 * please don't use `__repr__` and friends in doctests but use examples that are natural Python and mark them `#indirect doctest`
 * please fill in the 32-bit hash doctest values
 * why do you ask coercion questions in `_add_` and friends, at this point coercion should be done. What am I missing?
 * most of the code is beautifully documented! Well done.
 * you should add an `AUTHORS` block and add your name to each file
 * the `INPUT` syntax is that each entry starts with a `-` not a `*`
 * at the risk of being obnoxious: the Python convention is to use `add_generator` over `AddGenerator`
 * I cannot vouche for the mathematics but it all seems very sound. 
 * Did you generate and check the docs?


---

Comment by mabshoff created at 2009-04-17 12:31:16

Hi Simon,

the missing 32 bit has values are

```
sage -t -long "devel/sage/sage/rings/polynomial/infinite_polynomial_element.py"
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/polynomial/infinite_polynomial_element.py", line 133:
    sage: hash(a)
                      
Expected nothing
Got:
    233743571
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/polynomial/infinite_polynomial_element.py", line 136:
    sage: hash(a._p)
                      
Expected nothing
Got:
    233743571
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-04-17 12:40:29

One last thing: You used _P in your code and `_[A-Z` are reserved numerical constants on some BSDs as well as Solaris. The way your code is written does not trigger any compilation failures (I tested on Solaris 10), but I would generally discourage the use. One prominent example where this caused endless problems was the PolyBoRi interface where Burcin and I rewrote large parts of the variable names because of it.

Cheers,

Michael


---

Comment by SimonKing created at 2009-04-17 21:30:43

Hi Martin,

Replying to [comment:23 malb]:
>  * please don't use `__repr__` and friends in doctests but use examples that are natural Python and mark them `#indirect doctest`

Could you elaborate? I don't understand what that means.

>  * why do you ask coercion questions in `_add_` and friends, at this point coercion should be done. What am I missing?

You mean `hasattr(self.parent(),'_P')`? This is since I have a dense and a sparse implementation of infinite polynomial rings, but I only have a _single_ class of infinite polynomials, in order to avoid code duplication. So, I have to check whether the parent of an infinite polynomial is dense or sparse.

But now, as you mention it: The dense ring class inherits from the sparse ring class; perhaps there should also be dense and a sparse element class, with separate `_add_`?

>  * most of the code is beautifully documented! Well done.

Thank you!

>  * you should add an `AUTHORS` block and add your name to each file

So, the copyright information is not enough?

Conncerning copyright: Although most of the code is original, I would like to include mhanson in the copyright, because his code was the starting point for me, and his 'dense' approach towards infinite polynomial rings is now the standard implementation (since it is faster). Is it ok to name him, although he did not explicitly state that he agrees with being named?

>  * at the risk of being obnoxious: the Python convention is to use `add_generator` over `AddGenerator`

Ok, will change it. Note, however, that `addGenerator` without underscore  is the name of the corresponding method in polybory's `GroebnerStrategy`.

At this occasion: Would you prefer the method name 'symmetric_cancellation_order' over 'sco'?

>  * Did you generate and check the docs?

I checked the doc tests, but I don't know how to generate the docs.

Best regards,
   Simon


---

Comment by SimonKing created at 2009-04-17 21:37:22

Replying to [comment:25 mabshoff]:
> One last thing: You used _P in your code and `_[A-Z` are reserved numerical constants on some BSDs as well as Solaris. 

O my goodness!

> The way your code is written does not trigger any compilation failures (I tested on Solaris 10), but I would generally discourage the use. 

The `_P` is one detail that I took from Mike's code. But you say _compilation_ failures -- so wouldn't this problem only be relevant for cython, not python?

Anyway. In `symmetric_reduction.pyx` I have `_R` as an attribute name of a cdef'd class. Perhaps I better channge it.

Cheers,
   Simon


---

Comment by SimonKing created at 2009-04-17 21:38:43

Replying to [comment:24 mabshoff]:
> Hi Simon,
> 
> the missing 32 bit has values are
...
>     233743571

Thank you!


---

Comment by malb created at 2009-04-19 13:58:42

Replying to [comment:26 SimonKing]:
> Replying to [comment:23 malb]:
> >  * please don't use `__repr__` and friends in doctests but use examples that are natural Python and mark them `#indirect doctest`
> 
> Could you elaborate? I don't understand what that means.

You have lines like `foo.__repr__()` in your `EXAMPLES`. It should be `str(foo)` instead, i.e. double underscore functions shouldn't be called directly (but indirectly by Python).
 
> >  * why do you ask coercion questions in `_add_` and friends, at this point coercion should be done. What am I missing?
> 
> You mean `hasattr(self.parent(),'_P')`? This is since I have a dense and a sparse implementation of infinite polynomial rings, but I only have a _single_ class of infinite polynomials, in order to avoid code duplication. So, I have to check whether the parent of an infinite polynomial is dense or sparse.
> 
> But now, as you mention it: The dense ring class inherits from the sparse ring class; perhaps there should also be dense and a sparse element class, with separate `_add_`?

It probably would be cleaner and faster.

> >  * you should add an `AUTHORS` block and add your name to each file
> 
> So, the copyright information is not enough?

It is "enough" for legal purposes but someone reading the docs won't see your name which would be a shame.
 
> Conncerning copyright: Although most of the code is original, I would like to include mhanson in the copyright, because his code was the starting point for me, and his 'dense' approach towards infinite polynomial rings is now the standard implementation (since it is faster). Is it ok to name him, although he did not explicitly state that he agrees with being named?

That is probably alright.

> >  * at the risk of being obnoxious: the Python convention is to use `add_generator` over `AddGenerator`
> 
> Ok, will change it. Note, however, that `addGenerator` without underscore  is the name of the corresponding method in polybory's `GroebnerStrategy`.

Note that they changed that in PolyBoRi 0.6 to be consistent with Python's convention.

> At this occasion: Would you prefer the method name 'symmetric_cancellation_order' over 'sco'?

If `sco` is not the word used in papers, I'd prefer `symmetric_cancelation_order`. I have no hard feelings either way though.

> >  * Did you generate and check the docs?
> 
> I checked the doc tests, but I don't know how to generate the docs.

run `sage -docbuild  reference html` and check for warnings + inspect the result.


---

Comment by SimonKing created at 2009-04-21 08:20:15

Hi Martin,

Replying to [comment:29 malb]:
> Replying to [comment:26 SimonKing]:
...
> > But now, as you mention it: The dense ring class inherits from the sparse ring class; perhaps there should also be dense and a sparse element class, with separate `_add_`?
> 
> It probably would be cleaner and faster.

OK, I'll try and do it (which needs more time). I guess, as for the rings, the dense class should inherit from the sparse class, and overload the arithmetic methods.

> > At this occasion: Would you prefer the method name 'symmetric_cancellation_order' over 'sco'?
> 
> If `sco` is not the word used in papers, I'd prefer `symmetric_cancelation_order`. I have no hard feelings either way though.

OK, my impression is that _explicit_ names are preferred.

> > I checked the doc tests, but I don't know how to generate the docs.
> 
> run `sage -docbuild  reference html` and check for warnings + inspect the result.

Thank you. It complains:
 * WARNING: Missing title for sage.rings.polynomial.infinite_polynomial_element
 * reST markup error: /home/king/SAGE/devel/sage-3.2.3/local/lib/python2.5/site-packages/sage/rings/polynomial/symmetric_ideal.py:docstring of sage.rings.polynomial.symmetric_ideal.SymmetricIdeal:4: (SEVERE/4) Unexpected section title.

   THEORY:

   -------

So, how can I add a title? And what's wrong with the section title?


---

Comment by mabshoff created at 2009-04-21 08:22:20

Please keep the review tags in a standard way so the right reports pick up ticket.

Cheers,

Michael


---

Comment by malb created at 2009-04-21 09:11:16

Replying to [comment:30 SimonKing]:
> Thank you. It complains:
>  * WARNING: Missing title for sage.rings.polynomial.infinite_polynomial_element
>  * reST markup error: /home/king/SAGE/devel/sage-3.2.3/local/lib/python2.5/site-packages/sage/rings/polynomial/symmetric_ideal.py:docstring of sage.rings.polynomial.symmetric_ideal.SymmetricIdeal:4: (SEVERE/4) Unexpected section title.

>    THEORY:

>    -------
> 
> So, how can I add a title? And what's wrong with the section title?

You'd add a docstring to the beginning of the file and its first line would be the title.

I think the `Theory` block needs a different underline, these encode section level in ReST IIRC.


---

Comment by SimonKing created at 2009-04-22 15:26:36

The new patch (still self-contained) should apply to sage-3.4.1.rc3

Let me address your comments:

 * I built the documentation, and it looks OK to me.

 * Now, I have separate dense and sparse implementations for `InfinitePolynomial`s.

 * I changed `sco` into `symmetric_cancellation_order` and `AddGenerator` into `add_generator`.

*__New Feature__*
 * I added a `__getattr__` method to `InfinitePolynomial`s that forwards to the underlying finite polynomials. Consequence: Any attribute of the underlying finite polynomial is directly available to the Infinite Polynomial, unless that method is overwritten. In that way, I automatically have latex typeset for the Infinite Polynomials.
 * A propos latex: I also added latex methods for Infinite Polynomial Rings and Symmetric Ideals. 

Latex looks like this:

```
sage: X.<x,y> = InfinitePolynomialRing(QQ)
sage: latex(x)
x_{\ast}
```

I think this makes sense. After all, `x` generates a series of variables, indexed by natural numbers, and in this situation it is common to use a star as index. Similarly:

```
sage: latex(X)
\mathbf{Q}[x_{\ast}, y_{\ast}]
sage: latex(x[2]*y[0]+3*x[4]+1)
y_{0} x_{2} + 3 x_{4} + 1
sage: latex(X*(x[1]*y[2]))
\left(y_{2} x_{1}\right)\mathbf{Q}[x_{\ast}, y_{\ast}][\mathfrak{S}_{\infty}]
```

Perhaps the last line requires some explanation. 
 1. G=S_infinity shall denote the symmetric group over the natural numbers. I hope this is understandable.
 2. R=Q[x_*,y_*] is the infinite polynomial ring.
 3. R[G] is the group ring of G with coefficients in R.
 4. A symmetric ideal is nothing but a R[G] module. Since G acts from the right, we thus have the above notation.

Rather huge patch, sorry...


---

Comment by malb created at 2009-04-22 22:11:05

Simon, IIRC you addressed all the issues I raised, right? I guess, the patch needs some final re-reading by e.g. me and then it should go in ASAP. It is a patch bomb already.


---

Comment by SimonKing created at 2009-04-27 09:18:51

First, some general questions:

 1. Should previous versions of a patch be preserved, or is it better to overwrite the old patch with the new version? 
 2. Should there only be _one_ patch, or should there be one starter patch, and all other patches only define the change with respect to the previous patch (hence, one has to apply a sequence of one big and perhaps 10 small patches)?

Anyway. This time I created a new patch `SymmetricIdeals.2.patch`, that should be applied first (e.g., to sage-3.4.1.rc3). After that, please apply `SymmetricIdealsCorrection.patch`, that corrects some doc tests.

Changes with respect to previous versions:
 - Major improvement of the documentation. I did `sage -docbuild reference html`, and it looks good in the browser.
 - Now any class has a `X==loads(dumps(X))` doc test. In particular, the Cython class `SymmetricReductionStrategy` is provided with pickling.
 - The performance is further improved: With `prune`, I found that a considerable amount of time was spent with `deepcopy`. Since I know that the object to be copied is a dict whose values are lists of integers, it is cheaper to do the copy manually. I am surprised that it makes such a big difference!

After applying `SymmetricIdealsCorrection.patch`, the doc tests of my files pass for me.

One question to the referee: As mentioned in a comment above, I try to be clever, i.e., in `SymmetricIdeal.symmetrisation()` I only apply elementary transpositions rather than the full symmetric group. I believe it works, but it is a difference to what Aschenbrenner and Hillar suggested. Shall I point it out in the documentation?

Best regards,
     Simon


---

Comment by malb created at 2009-04-27 09:54:53

Replying to [comment:35 SimonKing]:
> First, some general questions:
> 
>  1. Should previous versions of a patch be preserved, or is it better to overwrite the old patch with the new version? 

I don't think we established a good practice here yet. But it is certainly easier for the release manager if there is only one patch or a clear description what to apply when.

>  2. Should there only be _one_ patch, or should there be one starter patch, and all other patches only define the change with respect to the previous patch (hence, one has to apply a sequence of one big and perhaps 10 small patches)?

It depends. I would say: This ticket should be closed soon. The patch is way too big already. So in this case new patches (in different tickets) should be created.

> Anyway. This time I created a new patch `SymmetricIdeals.2.patch`, that should be applied first (e.g., to sage-3.4.1.rc3). After that, please apply `SymmetricIdealsCorrection.patch`, that corrects some doc tests.
> 
> Changes with respect to previous versions:
>  - Major improvement of the documentation. I did `sage -docbuild reference html`, and it looks good in the browser.
>  - Now any class has a `X==loads(dumps(X))` doc test. In particular, the Cython class `SymmetricReductionStrategy` is provided with pickling.
>  - The performance is further improved: With `prune`, I found that a considerable amount of time was spent with `deepcopy`. Since I know that the object to be copied is a dict whose values are lists of integers, it is cheaper to do the copy manually. I am surprised that it makes such a big difference!
> 
> After applying `SymmetricIdealsCorrection.patch`, the doc tests of my files pass for me.
> 
> One question to the referee: As mentioned in a comment above, I try to be clever, i.e., in `SymmetricIdeal.symmetrisation()` I only apply elementary transpositions rather than the full symmetric group. I believe it works, but it is a difference to what Aschenbrenner and Hillar suggested. Shall I point it out in the documentation

Yes, that should be pointed out clearly.

Let me know what the 'final' version of your patch is and then I'll review it.


---

Comment by mabshoff created at 2009-04-27 10:00:39

Replying to [comment:36 malb]:
> Replying to [comment:35 SimonKing]:
> > First, some general questions:
> > 
> >  1. Should previous versions of a patch be preserved, or is it better to overwrite the old patch with the new version? 
> 
> I don't think we established a good practice here yet. But it is certainly easier for the release manager if there is only one patch or a clear description what to apply when.

Yes, especially if it is all work by one person (maybe integrating someone else's patch) one patch is best. 

> >  2. Should there only be _one_ patch, or should there be one starter patch, and all other patches only define the change with respect to the previous patch (hence, one has to apply a sequence of one big and perhaps 10 small patches)?
> 
> It depends. I would say: This ticket should be closed soon. The patch is way too big already. So in this case new patches (in different tickets) should be created.

I agree with Martin that this ticket and its patches is already large enough. Followup patches are the way to go. Just imagine someone reading this ticket from top to bottom - I don't think any additional work should be done here.

In the end it is also important to make clear which patches to apply in which order and who gets credit for authorship.

Cheers,

Michael


---

Comment by SimonKing created at 2009-04-27 11:04:16

Final version (currently...) of Infinite Polynomial Rings and Symmetric Gröbner Bases


---

Attachment

Dear Martin and Michael,

Replying to [comment:36 malb]:
> Replying to [comment:35 SimonKing]:
> > First, some general questions:
> > 
> >  1. Should previous versions of a patch be preserved, or is it better to overwrite the old patch with the new version? 
> 
> I don't think we established a good practice here yet. But it is certainly easier for the release manager if there is only one patch or a clear description what to apply when.

OK, so I produced a stand-alone patch `SymmetricIdealsFinal.patch` relative to sage-3.4.1.rc3 that I consider final (see below).


> > One question to the referee: As mentioned in a comment above, I try to be clever, i.e., in `SymmetricIdeal.symmetrisation()` I only apply elementary transpositions rather than the full symmetric group. I believe it works, but it is a difference to what Aschenbrenner and Hillar suggested. Shall I point it out in the documentation
> 
> Yes, that should be pointed out clearly.

OK, I did so in the documentation of `SymmetricIdeal.symmetrisation()` and `SymmetricIdeal.groebner_basis()`: I give no evidence _why_ I believe that my algorithm is correct, but I state in what respect it differs from the work of Aschenbrenner and Hillar.

Moreover, I made it optional to chose the _original_ algorithm of Aschenbrenner and Hillar -- if some users don't trust me.
 
> Let me know what the 'final' version of your patch is and then I'll review it.

I think this version is final, in the following sense:
 - doc tests pass
 - I am already doing serious computations with that version, and it seems to work well
 - I looked intensely at the html documentation, and I found it alright.

Cheers,
    Simon


---

Comment by malb created at 2009-04-27 13:21:02

Doctests fail:


```
from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
ImportError: No module named symmetric_reduction
```


Maybe you didn't add the module to `module_list.py`?


---

Comment by SimonKing created at 2009-04-27 14:28:32

To be applied after SymmetricIdealsFinal.patch


---

Attachment

Replying to [comment:39 malb]:
> Doctests fail:
> 
> {{{
> from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
> ImportError: No module named symmetric_reduction
> }}}
> 
> Maybe you didn't add the module to `module_list.py`?

Yes. So, `SymmetricIdealsFinal.patch` is not the final word. Please also apply `SymmetricIdealsForgotten.patch`.

And I think it worked for me since I had built the extension in a different branch, so, it was somehow present.

Sorry,
    Simon


---

Comment by malb created at 2009-04-27 14:43:01

It seems all my concerns were addressed, doctests pass, positive review


---

Comment by SimonKing created at 2009-04-29 10:06:03

Dear Martin,

I am very sorry, but I found one bug. Since the ticket is not yet closed, I allowed myself to add yet another patch.

The bug was:

```
sage: X.<x,y>=InfinitePolynomialRing(QQ)
sage: p=x[2]-x[1]
sage: q=x[1]-x[2]
sage: p.reduce([q])
0
sage: q.reduce([p])
-x2 + x1
```


Reason: In `SymmetricReductionStrategy.[tail]reduce()`, I compared polynomials rather than leading monomials: I was not aware that `-x<x`. This is now fixed

At this occasion, there also is an enhancement: It is now possible to use fraction fields as base ring. In the previous version, this was impossible, since the duck typing in `_coerce_map_from_` was not appropriate, and since in `_div_` I have to work around the bug that I reported at #5917.

Now, one can do:

```
sage: F = FractionField(PolynomialRing(QQ,['a','b']))
sage: X.<x,y>=InfinitePolynomialRing(F)
sage: I=(F('a')*x[1]*y[2]+F('b')*x[2])*X
sage: G=I.groebner_basis()
sage: G
[y1*x2 + b/a*x1, y2*x1 + b/a*x2]
sage: for p in Permutations(4):
....:     print [(x^p).reduce(G) for x in G]
....:
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
```


*__How to apply the patches__*
 1. `SymmetricIdealsFinal`
 2. `SymmetricIdealsForgotten`
 3. `SymmetricIdealsBugfix`


---

Attachment

I've fixed a few doctest failures in `symmetric_ideal.py` and `infinite_polynomial_ring.py`. Simon, there is still a doctest failure on sage.math with 3.4.2 in `symmetric_ideal.py`. It is the protocol output of the calculation which is somehow different now. Please fix it, then we can merge this big patch.


---

Comment by SimonKing created at 2009-05-15 06:22:26

Replying to [comment:43 malb]:
> I've fixed a few doctest failures in `symmetric_ideal.py` and `infinite_polynomial_ring.py`. Simon, there is still a doctest failure on sage.math with 3.4.2 in `symmetric_ideal.py`. It is the protocol output of the calculation which is somehow different now. Please fix it, then we can merge this big patch.

This is very interesting, because I do not get any doctest failure for `infinite_polynomial_ring.py` with sage-3.4.2 on my computer. I'll try and see what happens on sage.math.


---

Comment by SimonKing created at 2009-05-15 06:52:32

One trivial doc test fix


---

Attachment

Hi Martin, hi Michael,

it turned out that the doc test failure was not in `infinite_polynomial_ring.py` but in `symmetric_ideal.py`. The fix is trivial, it is just insertion of one ':'.

After applying all four patches in order, all doc test for infinite polynomial rings and symmetric ideals pass both on sage.math and at home:

```
SimonKing@sage:~/SAGE/sage-3.4.2/devel/sage-symmdevel/sage/rings/polynomial$ ~/SAGE/sage-3.4.2/sage -t -optional -long symmetric_ideal.py
sage -t -optional -long "devel/sage-symmdevel/sage/rings/polynomial/symmetric_ideal.py"
         [12.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 12.4 seconds
SimonKing@sage:~/SAGE/sage-3.4.2/devel/sage-symmdevel/sage/rings/polynomial$ ~/SAGE/sage-3.4.2/sage -t -optional -long symmetric_reduction.pyx
sage -t -optional -long "devel/sage-symmdevel/sage/rings/polynomial/symmetric_reduction.pyx"
         [4.3 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.3 seconds
SimonKing@sage:~/SAGE/sage-3.4.2/devel/sage-symmdevel/sage/rings/polynomial$ ~/SAGE/sage-3.4.2/sage -t -optional -long infinite_polynomial_element.py
sage -t -optional -long "devel/sage-symmdevel/sage/rings/polynomial/infinite_polynomial_element.py"
         [6.0 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.0 seconds
SimonKing@sage:~/SAGE/sage-3.4.2/devel/sage-symmdevel/sage/rings/polynomial$ ~/SAGE/sage-3.4.2/sage -t -optional -long infinite_polynomial_ring.py
sage -t -optional -long "devel/sage-symmdevel/sage/rings/polynomial/infinite_polynomial_ring.py"
         [2.6 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.6 seconds
```


I tag the ticket as [needs review], but I hope that Martin's comment can be taken as a positive review already...

Cheers,
    Simon


---

Comment by mabshoff created at 2009-05-15 07:35:46

Last patch fixes the problem seen by malb, so by extension positive review.

What is the credit situation? I.e. did Mike Hansen write some of this?

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 07:37:51

Resolution: fixed


---

Comment by mabshoff created at 2009-05-15 07:37:51

Merged all four patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by SimonKing created at 2009-05-15 07:56:28

Replying to [comment:46 mabshoff]:
> What is the credit situation? I.e. did Mike Hansen write some of this?

I credited Mike Hansen both in `infinite_polynomial_ring.py` and in `infinite_polynomial_element.py`, since the _dense_ implementations are based on the code that he posted at #5453.

Recall the history of these patches: 
 * At sage-devel, I sometimes expressed my interest in having Aschenbrenner's and Hillar's algorithms in Sage. 
 * Mike Hanse opened #5453, but his main interest seemed to be working with the polynomials rather than with symmetric ideals. 
 * First, I contributed to #5453 by providing an alternative (sparse) implementation to Mike Hansen's approach. 
 * But when I realised that the purpose of the ticket was different from my own intent, I opened #5566 and implemented Symmetric Gröbner Bases, using Mike Hansen's _dense_ approach as default implementation and my _sparse_ approach as another option for the user. 
 * Unfortunately, since then, I didn't hear a single word of Mike Hansen.

__Conclusion__
 1. Mike Hansen deserves to be credited, since I started with his code.
 2. He is credited
 3. `symmetric_ideal.py` and `symmetric_reduction.pyx` is my own code, hence, only one author.
 4. Merging these patches should also result in closing #5453.

Cheers,
    Simon
