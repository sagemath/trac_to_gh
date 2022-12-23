# Issue 5332: Convert MV polynomial constructors in multi_polynomial_ideal.py, category_object.py, etc

Issue created by migration from https://trac.sagemath.org/ticket/5332

Original creator: mabshoff

Original creation time: 2009-02-21 22:50:25

Assignee: mabshoff

CC:  malb

From http://groups.google.com/group/sage-support/browse_thread/thread/21d861876918e668


```
> While I looked at ideal's docstring I noticed plenty of construct like 
>     sage: R, x = PolynomialRing(ZZ, 'x').objgen() 
> Shouldn't we get those cleaned up to read 
>    sage: R.<x>=ZZ[] 
> or am I missing the point? I have seen too many people use the above 
> old objgen() constuct and I find it rather hideous. 


Yeah, its just old and noone got around cleaning that up. 

Martin 
```


There are some more places, to find them run

```
grep "PolynomialRing" .doctest* | grep objgen
```

in $SAGE_ROOT/tmp
Cheers,

Michael


---

Comment by mmezzarobba created at 2015-04-14 08:19:02

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2015-04-14 08:19:02

Changing priority from minor to trivial.


---

Comment by mmezzarobba created at 2015-04-14 08:19:02

New commits:


---

Comment by mmezzarobba created at 2015-04-14 08:19:02

Changing component from doctest coverage to documentation.


---

Comment by mmezzarobba created at 2015-04-14 08:52:28

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-04-14 09:30:54

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2015-04-14 09:32:19

With the last version of the patch:

```
$ git grep "sage: .*PolynomialRing.*objgen" src/sage/
src/sage/rings/fraction_field_element.pyx:        sage: K, x = FractionField(PolynomialRing(QQ, 'x')).objgen()
src/sage/rings/polynomial/multi_polynomial_element.py:            sage: R, x = PolynomialRing(QQbar, 10, 'x').objgens()
src/sage/rings/polynomial/multi_polynomial_ring.py:    sage: PolynomialRing(GF(5), 3, 'xyz').objgens()
src/sage/rings/polynomial/polynomial_element.pyx:    sage: PolynomialRing(ZZ,'x').objgen()
src/sage/structure/category_object.pyx:            sage: R, x = PolynomialRing(QQ,'x').objgen()
src/sage/structure/category_object.pyx:         sage: R, x = PolynomialRing(QQ,'x',12).objgens()
```



---

Comment by mmezzarobba created at 2015-04-14 09:32:19

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2015-04-14 09:51:39

This is horrible

```
R.<x,y> = QQ[]
```

(but working, I know).

Please use either

```
sage: R = QQ['x,y']
sage: x,y = R.gens()
```

or the shorter

```
sage: R.<x,y> = QQ['x,y']
```


Having something implicit in the right hand side of this declaration is really bad. Don't you think?

Vincent


---

Comment by mmezzarobba created at 2015-04-14 11:10:36

Replying to [comment:10 vdelecroix]:
> Having something implicit in the right hand side of this declaration is really bad. Don't you think?

No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.


---

Comment by vdelecroix created at 2015-04-14 11:16:30

Replying to [comment:11 mmezzarobba]:
> Replying to [comment:10 vdelecroix]:
> > Having something implicit in the right hand side of this declaration is really bad. Don't you think?
> 
> No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.

This is one more thing that induces confusion between Python variables and mathematical variables (not worse than `var(x)` though). It is not a repetition as the semantic are very different.


---

Comment by bruno created at 2015-04-14 11:55:18

Replying to [comment:12 vdelecroix]:
> Replying to [comment:11 mmezzarobba]:
> > Replying to [comment:10 vdelecroix]:
> > > Having something implicit in the right hand side of this declaration is really bad. Don't you think?
> > 
> > No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.
> 
> This is one more thing that induces confusion between Python variables and mathematical variables (not worse than `var(x)` though). It is not a repetition as the semantic are very different.

I agree with Marc, I clearly see `sage: R.<x,y> = QQ['x,y']` as a repetition. And I honestly do not see the problem with `sage: R.<x,y> = QQ[]`: one is simply saying "_I define the polynomial ring over QQ with 2 variables, and I use the Python `x` and `y` to denote its generators. I let Sage choose the way it represents graphically these generators_". And then, of course it is quite nice that the default choice is to use the string `"x"` for `x` and the string `"y"` for `y`. 

Otherwise stated, I like in the notation `sage: R.<x,y> = QQ[]` the fact that I simply define the object and not the way it is printed.


---

Comment by vbraun created at 2015-04-14 12:26:35

Its Magma syntax so its going to stay either way.

I also prefer `R.<x,y> = QQ[]`. Technically the variable labels also enter the right hand side, but thats just an implementation detail. We could dig the labels out of the globals dictionary without having the preparser put them into the right hand side of the declaration, so its not truly necessary. Of course the preparser implementation is superior.


---

Comment by kcrisman created at 2015-04-14 13:19:25

> Its Magma syntax so its going to stay either way.
As well as being old and so liable to break others' code if removed.

+1


---

Comment by vdelecroix created at 2015-04-14 13:27:40

All right, let me start again.

1. I agree with all of you on what *I* am doing every day to implement a polynomial ring in Sage. The syntax `R.<x,y> = QQ[]` is compact and useful.

2. My comment was about newcomers for which the concept of a Python variable is not necessarily clear (and the confusion with mathematic variable is automatic). So if you answer, please either be a newcomer or try to be one. Claiming as Bruno in [comment:13 comment:13] that the syntax is very simple is a bit of a lie.

Vincent


---

Comment by mmezzarobba created at 2015-04-14 13:41:45

If the compact syntax is confusing for newcomers (which I agree it may be), I think we should better explain it in tutorials and other documentation targetted at newcomers, not avoid using it in reference documentation. So I don't see what the problem has to do with this ticket.


---

Comment by vdelecroix created at 2015-04-14 13:50:30

Replying to [comment:17 mmezzarobba]:
> If the compact syntax is confusing for newcomers (which I agree it may be), I think we should better explain it in tutorials and other documentation targetted at newcomers, not avoid using it in reference documentation. So I don't see what the problem has to do with this ticket.

True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.


---

Comment by mmezzarobba created at 2015-04-14 13:55:57

Replying to [comment:18 vdelecroix]:
> True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.

Then add a paragraph or two to explain the syntax in well-chosen docstrings...

Do you really see `Polynomial.valuation?` as something people who don't know how to define basic objects are likely to read?


---

Comment by vdelecroix created at 2015-04-14 13:59:43

Replying to [comment:19 mmezzarobba]:
> Replying to [comment:18 vdelecroix]:
> > True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.
> 
> Then add a paragraph or two to explain the syntax in well-chosen docstrings...

Will do.

> Do you really see `Polynomial.valuation?` as something people who don't know how to define basic objects are likely to read?

I don't know. Some researcher in algebraic geometry might.


---

Comment by vdelecroix created at 2015-04-15 17:21:24

Changing status from needs_review to needs_info.


---

Comment by vdelecroix created at 2015-04-15 17:21:24

I will update a commit in a minute. Few questions first:

- what about other parts of the doc? (I have a commit ready for that)
- what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)
- what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?

Vincent


---

Comment by mmezzarobba created at 2015-04-15 17:25:00

Replying to [comment:21 vdelecroix]:
> I will update a commit in a minute. Few questions first:
> 
> - what about other parts of the doc? (I have a commit ready for that)

Which “other parts” are you talking about?

> - what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)
> - what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?

In library code, they are very useful!


---

Comment by vdelecroix created at 2015-04-15 17:35:02

Replying to [comment:22 mmezzarobba]:
> Replying to [comment:21 vdelecroix]:
> > I will update a commit in a minute. Few questions first:
> > 
> > - what about other parts of the doc? (I have a commit ready for that)
> 
> Which “other parts” are you talking about?

Number field

```
sage: K.<a> = NumberField(x^2 - 2)
```

Finite fields

```
sage: K.<a> = GF(3^5)
```

Power series

```
sage: R.<x> = QQ[[]]
```

Dirichlet group

```
sage: G.<e> = DirichletGroup(20)
```

There are more or less a dozen of files (including `sage/schemes` and `sage/modular`).

> > - what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)
> > - what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?
> 
> In library code, they are very useful!

I agree that the method is useful on number fields, polynomial rings, power series. But at the level of category objects or parent?

Vincent

PS: Not speaking about the fact that

```
K = NumberField(x^2 - 2, 'a')
a = K.gen()
```

is faster, less cryptic and more economic in characters than

```
K,a = NumberField(x^2-2,'a').objgen()
```



---

Comment by mmezzarobba created at 2015-04-15 17:42:39

Replying to [comment:23 vdelecroix]:
> > Which “other parts” are you talking about?
> 
> Number field
[...]
> There are more or less a dozen of files (including `sage/schemes` and `sage/modular`).

Yes, why not. To be honest I made the changes here because I stumbled upon this ticket and thought it would take five minutes and make one years-old open ticket less, but I don't really care about the problem.

> I agree that the method is useful on number fields, polynomial rings, power series. But at the level of category objects or parent?

Okay, I misunderstood, sorry. I don't know.

> PS: Not speaking about the fact that
> {{{
> K = NumberField(x^2 - 2, 'a')
> a = K.gen()
> }}}
> is faster, less cryptic and more economic in characters than
> {{{
> K,a = NumberField(x^2-2,'a').objgen()
> }}}

I actually tend to find the latter more readable, mostly because it only takes one line.


---

Comment by vdelecroix created at 2015-04-15 17:57:42

Rebased on sge-6.7.beta0 with a new commit.
----
New commits:


---

Comment by vdelecroix created at 2015-04-15 17:57:42

Changing status from needs_info to needs_review.


---

Comment by mmezzarobba created at 2015-04-18 10:39:16

* I'm wondering why you made this change:

```
--- a/src/sage/rings/polynomial/polynomial_element.pyx
+++ b/src/sage/rings/polynomial/polynomial_element.pyx
@@ -181,8 +181,12 @@ cdef class Polynomial(CommutativeAlgebraElement):
 
     EXAMPLE::
 
-        sage: R.<y> = QQ['y']
-        sage: S.<x> = R['x']
+        sage: R = QQ['x']['y']
+        sage: R
+        Univariate Polynomial Ring in y over Univariate Polynomial Ring in x
+        over Rational Field
+        sage: y = R.gen()
+        sage: x = R.base_ring().gen()
         sage: f = x*y; f
         y*x
         sage: type(f)
```


* Does this work? How?

```
--- a/src/sage/schemes/generic/algebraic_scheme.py
+++ b/src/sage/schemes/generic/algebraic_scheme.py
@@ -194,7 +194,7 @@ def is_AlgebraicScheme(x):
 
     We create a more complicated closed subscheme::
 
-        sage: A, x = AffineSpace(10, QQ).objgens()
+        sage: A = AffineSpace(10, QQ)
         sage: X = A.subscheme([sum(x)]); X
         Closed subscheme of Affine Space of dimension 10 over Rational Field defined by:
         x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
```


* Shouldn't `>>` be `>` here? Also, I would add a mention of `.<>` without removing that of `objgens()`.

```
 The third argument specifies the printing names of the generators
-of the homogenous coordinate ring. Using objgens() you can obtain
-both the space and the generators as ready to use variables.
+of the homogenous coordinate ring. Using the special syntax with
+``<`` and ``>>`` you can obtain both the space and the generators as ready to
+use variables.
```



---

Comment by mmezzarobba created at 2015-04-18 10:40:06

Changing status from needs_review to needs_work.


---

Comment by mmezzarobba created at 2015-04-18 10:40:06

Changing priority from trivial to minor.


---

Comment by git created at 2015-04-18 11:39:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-04-18 11:40:33

Replying to [comment:26 mmezzarobba]:
> * I'm wondering why you made this change:

Right, it is not really better. Reverted.

> * Does this work? How?

It does not.

> * Shouldn't `>>` be `>` here? Also, I would add a mention of `.<>` without removing that of `objgens()`.

done.


---

Comment by git created at 2015-04-18 17:59:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2015-04-18 18:06:03

I pushed a small fix to your fix (not tested, I'm having trouble with my development build at the moment).

One more comment: exemples like `A, z = R.poly_ring().objgen()` are typical cases where I would have kept the `objgens` version. But I have no problem with your version, do as you prefer.

If you are okay with my commits and assuming all tests pass, please feel free to set the ticket to positive review.


---

Comment by git created at 2015-04-19 06:08:14

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2015-04-19 06:09:32

Changing status from needs_work to needs_review.


---

Comment by mmezzarobba created at 2015-04-19 06:09:32

Turns out the tests didn't pass, but now they should.


---

Comment by vdelecroix created at 2015-04-20 11:06:08

They do!


---

Comment by vdelecroix created at 2015-04-20 11:06:08

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-21 00:10:52

Resolution: fixed
