# Issue 9768: Coercon problems to symbolic ring

Issue created by migration from https://trac.sagemath.org/ticket/9769

Original creator: maldun

Original creation time: 2010-08-19 23:47:28

Assignee: burcin

There seems to be some problems with the coercion of some datatypes to the symbolic ring:

sage: cos(MatrixSpace(ZZ, 2)([1, 2, -4, 7]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
.......
TypeError: cannot coerce arguments: no canonical coercion from Full MatrixSpace of 2 by 2 dense matrices over Integer Ring to Symbolic Ring

sage: import numpy
sage: vec = numpy.array([1,2])
sage: sin(vec)
array([ 0.84147098,  0.90929743])
sage: sin(vec[0])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
....
TypeError: cannot coerce arguments: no canonical coercion from <type 'numpy.int64'> to Symbolic Ring
----

sage: x = PolynomialRing(QQ, 'x').gen()
sage: sin(x)
sin(x)
sage: x = PolynomialRing(RR, 'x').gen()
sage: sin(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
.....
TypeError: cannot coerce arguments: __call__() takes exactly 1 positional argument (0 given)
sage: x = PolynomialRing(CC, 'x').gen()
sage: sin(x)
sin(x)


---

Comment by burcin created at 2011-05-10 17:58:29

Note that there is no coercion when you call

```
sage: import numpy
sage: vec = numpy.array([1,2])
sage: sin(vec)
array([ 0.84147098,  0.90929743])
```


The `__call__()` function for `sin` checks if the argument is a numpy array and calls the right numpy function on this input. See line 349 of `sage/symbolic/function.pyx`. We can handle other numpy types there.

We cannot work with matrices as numeric objects in symbolics. I suppose you expect the sin() function to be applied to each entry of the matrix. The `apply_map()` method should be used for this purpose:


```
sage: t = Matrix(ZZ, 2,2)
sage: t.randomize()
sage: t.apply_map(lambda x: sin(x))
[      0 -sin(1)]
[ sin(4)       0]
```


-----


```
sage: x = PolynomialRing(RR, 'x').gen()
sage: sin(x)
<boom>
```


The problem here is really coercion, but it should be copied to another ticket (in the basic_arithmetic component):

The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:


```
sage: R.<x> = RR[]
sage: (x^2+1)(x=5)
11
```



---

Comment by rws created at 2014-04-22 16:47:53

Replying to [comment:2 burcin]:
> {{{
> sage: x = PolynomialRing(RR, 'x').gen()
> sage: sin(x)
> <boom>
> }}}
> 
> The problem here is really coercion, but it should be copied to another ticket (in the basic_arithmetic component):
Incidentally the same with power series is part of #16197.

> The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:
> 
> {{{
> sage: R.<x> = RR[]
> sage: (x^2+1)(x=5)
> 11
> }}}

Edit: confused poly with series, sorry


---

Comment by rws created at 2014-11-10 10:01:50

Replying to [comment:2 burcin]:
> The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:
> 
> {{{
> sage: R.<x> = RR[]
> sage: (x^2+1)(x=5)
> 11
> }}}
This is now #17311


---

Comment by vdelecroix created at 2015-03-28 12:03:51

Hello,

I propose to close this ticket as duplicate because of #18076. With the branch applied

```
sage: import numpy
sage: cos(numpy.int32('12'))
cos(12)
sage: cos(numpy.float32('1.1'))
0.453596100177538
```



---

Comment by vdelecroix created at 2015-03-28 12:03:51

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-04-23 10:10:38

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-23 14:51:46

Resolution: duplicate
