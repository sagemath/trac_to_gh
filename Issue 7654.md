# Issue 7654: Conversion bug in MPolynomialRing_libsingular

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-12-11 00:25:56

Assignee: malb

Keywords: conversion libsingular

The following happens in sage-4.2.1 and sage-4.3.alpha1:

```
sage: R.<y_6, y_3, y_2, y_1, z_6, z_5, z_4, z_3, z_2, z_1> = QQ[]
sage: R.<y_6, y_3, y_2, y_1, z_6, z_5, z_4, z_3, z_2, z_1> = GF(3)[]
sage: S = GF(3)['y_4', 'y_3', 'y_2', 'y_1', 'z_5', 'z_4', 'z_3', 'z_2', 'z_1']
sage: S(y_1*z_2^2*z_1)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (947, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (952, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/.sage/temp/gauss/12072/_home_king__sage_init_sage_0.py in <module>()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7032)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynomial.MPolynomial._polynomial_ (sage/rings/polynomial/multi_polynomial.c:3259)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7195)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/integer_mod_ring.pyc in __call__(self, x)
    761         """
    762         try:
--> 763             return integer_mod.IntegerMod(self, x)
    764         except (NotImplementedError, PariError):
    765             raise TypeError, "error coercing to finite field"

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2969)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_int.__init__ (sage/rings/integer_mod.c:13984)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4241)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:7009)()

TypeError: unable to coerce <type 'list'> to an integer
```


String conversion is fine.

```
sage: S('y_1*z_2^2*z_1')
y_1*z_2^2*z_1
```


I know that there is no coercion between these two rings. However, here we have _conversion_. Conversion should -- as much as I understand -- try to make a meaning out of the input, even if the parents do not support coercion.

Therefore I consider this a quite serious bug.


---

Comment by SimonKing created at 2011-05-28 09:22:08

I still think that this is a serious bug, and it has  not been addressed in the 18 months since this ticket was opened.


---

Comment by malb created at 2011-06-21 13:49:08

Hi, sorry for taking so long to take a look. The reason for this behaviour is that currently, conversion is simply defined by index:


```python
sage: R.<a,b,c> = GF(3)[]
sage: S = QQ['x','y','z']
sage: S(a)
x
```


So, technically, it is not a bug. However, it might be a good idea to change this behaviour?


---

Comment by malb created at 2011-06-21 14:29:17

I noticed a bug in the code when looking into this issue attachment:trac_7654.patch fixes it.


---

Comment by SimonKing created at 2011-06-21 15:25:17

Replying to [comment:2 malb]:
> Hi, sorry for taking so long to take a look. The reason for this behaviour is that currently, conversion is simply defined by index:

I know.

> So, technically, it is not a bug.

I disagree: There is a bug.

Admittedly it is not a bug with my original example, because it contains `z_1` (index 9 in `R.gens()`), whereas `S` only has 9 variables. So, the attempt to find a generator of index 9 must fail (but please with a less cryptic error message!!).

However, we also have

```
sage: S(y_1*z_2^2*z_4)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1154, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1154, 0))
...
```

even though we have

```

sage: R.gens().index(y_1)
3
sage: R.gens().index(z_2)
8
sage: R.gens().index(z_4)
6
sage: S.gens()[3]
y_1
sage: S.gens()[8]
z_1
sage: S.gens()[6]
z_3
```


So, using indices for conversion, one _should_ have

```
sage: S(y_1*z_2^2*z_4)
y_1*z_1^2*z_3
```

but one gets a traceback.

That is clearly a bug. Is that fixed with your patch?


---

Comment by malb created at 2011-06-21 15:49:25

Okay, but my patch does not fix this. 

So, what behaviour do we want?
a) when the number of variables match
b) when the number of variables do not match?

 * If we leave a) as it is (by index) but allow b) by name, it could be quite confusing?
 * If we change a) to match b) we might break some code?
 * We could also `try` by name first and then do it by index in a)?


---

Comment by SimonKing created at 2011-06-21 18:46:35

Replying to [comment:5 malb]:
> Okay, but my patch does not fix this. 
> 
> So, what behaviour do we want?
> a) when the number of variables match
> b) when the number of variables do not match?

Time for a little advertisement: At #8821 and #11490, I suggest to add a section in the guided tour resp. a thematic tutorial explaining coercion in Sage (both needs review). At least in #11490, I try to explain the rationale behind the conversion of polynomials in Sage.

I think we should have the following rules:

Let P and Q be polynomial rings, over the same base ring (for simplicity).

If the set of variable names of P is a subset of the set of variable names of Q then the conversion from P to Q is name preserving, and it is used as a coercion. That is how it currently works.

```
sage: P.<a,b,c> = QQ[]
sage: Q = QQ['c','b','d','a']
sage: f = Q.coerce_map_from(P)
sage: f(a),f(b),f(c)
(a, b, c)
```


Otherwise, we should have a position preserving conversion - regardless whether the number of variables matches or not. If the number of variables of P is bigger than of Q, then the conversion is only defined on a sub-ring of P. In any case, that conversion must not be used as a coercion.

Note that at the moment we only have that behaviour if the number of variables matches:

1. Q has more variables than P:

```
sage: P.<a,b,c> = GF(2)[]
sage: Q = GF(2)['c','b','d','e']
sage: f = Q.convert_map_from(P)
sage: f(a)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1154, 0))
...
```

I suggest that one should have

```
sage: f(a), f(b), f(c) # not implemented
(c, b, d)
```


2. Q has as many variables as P:

```
sage: P.<a,b,c> = GF(2)[]
sage: Q = GF(2)['c','b','d']
sage: f = Q.convert_map_from(P)
sage: f(a),f(b),f(c)
(c, b, d)
```

I think that's fine.

3. Q has less variables than P:

```
sage: P.<a,b,c> = GF(2)[]
sage: Q = GF(2)['c','d']
sage: f = Q.convert_map_from(P)
sage: f(a)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1154, 0))
...
```

I suggest that one should have

```
sage: f(a), f(b) # not implemented
(c, d)
sage: f(c)
Traceback (most recent call last):
...
TypeError: That polynomial ring only has 2 variables
```



---

Comment by malb created at 2011-06-22 12:10:46

The attached patch deals with 1) and 2). However, for 3) it currently just raises an error. I'm not sure allowing more variables in the input ring + matching by index is such a good idea. Let me know what you think.


---

Comment by SimonKing created at 2011-06-22 13:27:35

Replying to [comment:7 malb]:
> The attached patch deals with 1) and 2). 

Good!

> However, for 3) it currently just raises an error. I'm not sure allowing more variables in the input ring + matching by index is such a good idea. Let me know what you think.

I have an argument pro and an argument contra:

I think we agree that the solution for situation 1) and 2) makes sense: It is "tradition" in Sage to use a position preserving conversion in 2), and you extended it to 1).

So, why not extending it to 3) as well? Would that be confusing to the user? Well, if a user is not confused by 2) (which already works in Sage) then s/he will not be confused by 1) or 3) either.
The argument "pro" is that we have greatest generality, being consistent with the existing solution 2).

On the other hand, consider the following scenario:

```
sage: R.<x,y> = QQ[]
sage: S = QQ['z','y','x']
sage: S(x),S(y)
(x, y)
sage: R(S(x))
x
sage: R(S(y))
y
```


That is the current behaviour. But 3) would imply that the conversion from S to R should be position preserving, and thus R(S(x)) would raise an error. So, having 3) would mean to change existing behaviour that actually seems quite natural. That is a strong argument "contra".

Allow me to modify my suggestion as follows:

 If the set of variable names of S is a subset of the variable names of R then we have a name-preserving conversion in _both_ directions, and the conversion from S to R is a coercion. Otherwise, we have a position-preserving conversion in both directions, which is not a coercion.

That would be consistent with the current solution for 2), would coincide with what your patch does in 1), is consistent with the current behaviour of R(S(x)) in the example above, and we would _always_ have a conversion.

What do you think...

Cheers,

Simon


---

Comment by SimonKing created at 2011-06-22 16:41:21

Replying to [comment:8 SimonKing]:
> That would be consistent with the current solution for 2), would coincide with what your patch does in 1), is consistent with the current behaviour of R(S(x)) in the example above, and we would _always_ have a conversion.

_Always_ in the sense of "defined on a subring".


---

Comment by malb created at 2011-06-23 11:56:49

If I understood correctly, I still find this confusing, for the following reason:


```python]
sage: P.<a,x,y> = QQ[]
sage: S = QQ['x','y','b']
sage: S(a) # conversion by index
x
sage: S(x) # conversion by name
x
```


so we get collisions which I don't like.


---

Comment by SimonKing created at 2011-06-23 15:25:51

Replying to [comment:10 malb]:
> If I understood correctly, I still find this confusing, for the following reason:
> ...
> so we get collisions which I don't like.

In your example, the set of variable names of P is not a subset of the set of variable names of S. Hence, I believe that in your example one should have conversion by position _only_. Thus:

```
sage: S(a)
x
sage: S(x)
y
```



---

Comment by malb created at 2011-06-23 15:28:46

Okay, I understood: the variables in the polynomial instead of in the ring. If we take the variables of the ring, everything is fine.

Note, however, that this implies that your original example will fail (?)


```python
sage: R.<y_6, y_3, y_2, y_1, z_6, z_5, z_4, z_3, z_2, z_1> = GF(3)[]
sage: S = GF(3)['y_4', 'y_3', 'y_2', 'y_1', 'z_5', 'z_4', 'z_3', 'z_2', 'z_1']
sage: S(y_1*z_2^2*z_1)
```



---

Comment by SimonKing created at 2011-06-23 15:36:03

Replying to [comment:12 malb]:
> Note, however, that this implies that your original example will fail (?)

I think I can live with it...


---

Comment by malb created at 2011-06-25 14:52:45

Changing status from new to needs_review.


---

Comment by malb created at 2011-06-25 14:52:45

The updated patch _should_ do the trick.


---

Comment by SimonKing created at 2011-08-17 12:51:18

Oops, I completely forgot about that ticket!


---

Comment by SimonKing created at 2011-08-18 12:02:00

First things first: My original example still fails, but I think we agreed that it _should_ fail. And the error message is definitely nicer than before:

```
sage: R.<y_6, y_3, y_2, y_1, z_6, z_5, z_4, z_3, z_2, z_1> = GF(3)[]
sage: S = GF(3)['y_4', 'y_3', 'y_2', 'y_1', 'z_5', 'z_4', 'z_3', 'z_2', 'z_1']
sage: S(y_1*z_2^2*z_1)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (6675, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/mnt/local/king/SAGE/sage-4.7.1.rc1/devel/sage-main/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7805)()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynomial.MPolynomial._polynomial_ (sage/rings/polynomial/multi_polynomial.c:3271)()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:8103)()

TypeError: Could not find a mapping of the passed element to this ring.
```


I went through the examples that we had discussed, and I find that they work as it was proposed. And the logic behind the conversions is explained in the docs.

I am now running all long tests, and if that works then it'll be a positive review.


---

Comment by SimonKing created at 2011-08-18 13:36:18

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-08-18 13:36:18

We got two failures (interestingly in two modules I'm quite familiar with):

```
sage -t -long "devel/sage-main/sage/categories/pushout.py"  
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored
**********************************************************************
File "/mnt/local/king/SAGE/sage-4.7.1.rc1/devel/sage-main/sage/categories/pushout.py", line 2182:
    sage: F(QQ['y','z'])
Expected:
    Traceback (most recent call last):
    ...
    TypeError: not a constant polynomial
Got:
    Traceback (most recent call last):
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[8]>", line 1, in <module>
        F(QQ['y','z'])###line 2182:
    sage: F(QQ['y','z'])
      File "functor.pyx", line 362, in sage.categories.functor.Functor.__call__ (sage/categories/functor.c:1597)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/categories/pushout.py", line 2265, in _apply_functor
        I = [R(1)*t for t in I.gens()]*R
      File "ring.pyx", line 416, in sage.rings.ring.Ring.__mul__ (sage/rings/ring.c:4581)
      File "multi_polynomial_libsingular.pyx", line 973, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.ideal (sage/rings/polynomial/multi_polynomial_libsingular.cpp:8886)
      File "multi_polynomial_libsingular.pyx", line 851, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7805)
      File "multi_polynomial.pyx", line 175, in sage.rings.polynomial.multi_polynomial.MPolynomial._polynomial_ (sage/rings/polynomial/multi_polynomial.c:3243)
      File "multi_polynomial_libsingular.pyx", line 869, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:8103)
    TypeError: Could not find a mapping of the passed element to this ring.
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_79
***Test Failed*** 1 failures.
For whitespace errors, see the file /mnt/local/king/.sage/tmp/.doctest_pushout.py
	 [11.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/categories/pushout.py"
Total time for all tests: 11.0 seconds
```

and

```
sage -t -long "devel/sage-main/sage/rings/polynomial/infinite_polynomial_element.py"
**********************************************************************
File "/mnt/local/king/SAGE/sage-4.7.1.rc1/devel/sage-main/sage/rings/polynomial/infinite_polynomial_element.py", line 139:
    sage: InfinitePolynomial(X, (alpha_1+alpha_2)^2)
Expected:
    Traceback (most recent call last):
    ...
    TypeError
Got:
    Traceback (most recent call last):
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        InfinitePolynomial(X, (alpha_1+alpha_2)**Integer(2))###line 139:
    sage: InfinitePolynomial(X, (alpha_1+alpha_2)^2)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/rings/polynomial/infinite_polynomial_element.py", line 195, in InfinitePolynomial
        f = PP.hom([x if x in SV else 0 for x in PP.variable_names()], A._P)
      File "parent_gens.pyx", line 471, in sage.structure.parent_gens.ParentWithGens.hom (sage/structure/parent_gens.c:3949)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/rings/homset.py", line 97, in __call__
        return morphism.RingHomomorphism_im_gens(self, im_gens, check=check)
      File "morphism.pyx", line 950, in sage.rings.morphism.RingHomomorphism_im_gens.__init__ (sage/rings/morphism.c:5141)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/structure/sequence.py", line 298, in Sequence
        return Sequence_generic(x, universe, check, immutable, cr, cr_str, use_sage_types)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/structure/sequence.py", line 504, in __init__
        x = [universe(t) for t in x]
      File "multi_polynomial_libsingular.pyx", line 820, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7336)
    TypeError: Could not find a mapping of the passed element to this ring.
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /mnt/local/king/.sage/tmp/.doctest_infinite_polynomial_element.py
	 [3.1 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/rings/polynomial/infinite_polynomial_element.py"
Total time for all tests: 3.1 seconds
```

So, you just need to change two error messages.

I am not sure, but it seems to me that the doc tests of the elliptic curves code became slower. Testing it now.


---

Attachment

Replying to [comment:18 SimonKing]:
> We got two failures (interestingly in two modules I'm quite familiar with):
> So, you just need to change two error messages.

The updated patch does just that.
 
> I am not sure, but it seems to me that the doc tests of the elliptic curves code became slower. Testing it now.

Okay, good. Let me know what the verdict is and I'll take a look at performance if needed.


---

Comment by SimonKing created at 2011-08-18 15:02:40

Concerning timings, I was mistaken (had remembered wrong figures): It is 920 versus 922 seconds for all long tests on elliptic curves. So, no significant difference.

With the new patch, all non-long tests pass, and with the old version all but two long tests passed. Hence, it is a positive review.


---

Comment by SimonKing created at 2011-08-18 15:02:40

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-08-22 17:33:40

Resolution: fixed
