# Issue 7797: basic interface to letterplace from singular

Issue created by migration from https://trac.sagemath.org/ticket/7797

Original creator: burcin

Original creation time: 2009-12-30 21:43:47

Assignee: burcin

CC:  polybori saliola malb jhpalmieri sage-combinat oleksandrmotsak

Keywords: singular

Attached patches add a basic interface to the letterplace [1] component of Singular, which allows computation of Groebner bases (up to a degree bound) of (two-sided) ideals of free algebras.

[1] http://www.singular.uni-kl.de/Manual/latest/sing_425.htm#SEC478

These patches depend on #7198.

Since Sage only supports ideals over commutative rings for now, writing a better interface to this would take considerably more work. I suggest we review & merge these patches, and hook it up to the right place when it exists.


---

Comment by burcin created at 2009-12-30 21:46:39

hack to create an MPolynomialRing as a parent for letterplace polynomials


---

Attachment

basic interface to compute groebner bases with letterplace


---

Attachment


---

Comment by burcin created at 2009-12-30 21:47:50

Changing status from new to needs_review.


---

Comment by malb created at 2010-06-03 22:21:04

Doctest failure on sage.math:


```
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage-main/sage/libs/singular/letterplace.py", line 32:
    sage: freegb(l, 10)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/malb/sage-4.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        freegb(l, Integer(10))###line 32:
    sage: freegb(l, 10)
      File "/mnt/usb1/scratch/malb/sage-4.4/local/lib/python/site-packages/sage/libs/singular/letterplace.py", line 70, in freegb
        libsingular_options(bck)
    TypeError: 'sage.libs.singular.option.LibSingularOptions' object is not callable
```


I think we used to allow calling libsingular option objects earlier, however load() replaces it.


---

Comment by malb created at 2010-06-24 14:29:42

Actually, this doesn't make sense to me:


```python
bck = int(libsingular_options)  
#letter place needs these options
libsingular_options['redTail'] = True
libsingular_options['redSB'] = True
libsingular_options(bck)
```


First bck is stored and then options are changed. So far fine. However, then bck is loaded and thus overwrites the options just set.


---

Comment by malb created at 2010-06-24 14:29:42

Changing status from needs_review to needs_work.


---

Comment by PolyBoRi created at 2010-06-30 09:06:53

letter place singular interface


---

Attachment

Hi!

I have corrected that using the new context interface.

Cheers,
Michael


---

Comment by PolyBoRi created at 2010-06-30 09:07:47

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by malb created at 2010-07-14 22:24:34

* While there are doctests, there is no documentation, no explanation what the functions are doing
 * freegb should accept ideals (?)
 * Why are you calling "singular_system"?


---

Comment by malb created at 2010-07-14 22:41:41


```
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage-main/sage/libs/singular/letterplace.py", line 32:

sage: freegb(l, 10)

Expected:

[3*y*x*z^7*y + y*x*z^8, 3*y*x*z^6*y + y*x*z^7, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^5*y + y*x*z^6, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^4*y + y*x*z^5, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*y + y*x*z^4, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*y + y*x*z^3, y*x*z^2*x*z + 3*y^2*x*z^2*x, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, 3*y*x*z*y + y*x*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6, x*z*y^5*x*z - 1296*y*x*z^2*x^5, x*z*y^4*x*z - 216*y*x*z^2*x^4, x*z*y^3*x*z - 36*y*x*z^2*x^3, x*z*y^2*x*z - 6*y*x*z^2*x^2, x*z*y*x*z - y*x*z^2*x, 6*x*z*x - y*x*z, 3*x*y + x*z]

Got
[3*x*y + x*z, 6*x*z*x - y*x*z, 3*y*x*z*y + y*x*z^2, 3*y*x*z^2*y + y*x*z^3, x*z*y*x*z - y*x*z^2*x, 3*y*x*z^3*y + y*x*z^4, y*x*z^2*x*z + 3*y^2*x*z^2*x, x*z*y^2*x*z - 6*y*x*z^2*x^2, 3*y*x*z^4*y + y*x*z^5, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, x*z*y^3*x*z - 36*y*x*z^2*x^3, 3*y*x*z^5*y + y*x*z^6, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, x*z*y^4*x*z - 216*y*x*z^2*x^4, 3*y*x*z^6*y + y*x*z^7, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, x*z*y^5*x*z - 1296*y*x*z^2*x^5, 3*y*x*z^7*y + y*x*z^8, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6]
```

This is with Singular 3-1-1-3 though.


---

Comment by PolyBoRi created at 2010-07-15 08:22:48

Aufruf von System ist offiziell, heißt aber nur, dass es nicht als extra Kommando eingebaut ist.

http://www.singular.uni-kl.de/Manual/latest/sing_433.htm


---

Comment by PolyBoRi created at 2010-07-15 08:25:19

sorry, for the language:
calling system is official. Using singular system was easier for the authors of freegb.

http://www.singular.uni-kl.de/Manual/latest/sing_433.htm


---

Comment by PolyBoRi created at 2010-07-15 08:42:31

the result seem to differ just in order.

What Ideal class is used for free algebras?


---

Attachment

some improvements to plural interface, still not much working


---

Comment by malb created at 2010-07-15 15:27:33

Replying to [comment:11 PolyBoRi]:

> the result seem to differ just in order. What Ideal class is used for free algebras?

Apparently, we don't have one which works yet


```
sage: P.<a,b,c> = FreeAlgebra(QQ,3)
sage: P
Free Algebra on 3 generators (a, b, c) over Rational Field
sage: P.ideal([a*b+c,a+1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/malb/<ipython console> in <module>()

/usr/local/sage-4.3/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.ideal (sage/rings/ring.c:3426)()

/usr/local/sage-4.3/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in Ideal(*args, **kwds)
    187 
    188     if not commutative_ring.is_CommutativeRing(R):
--> 189         raise TypeError, "R must be a commutative ring"
    190 
    191     if len(gens) == 0:

TypeError: R must be a commutative ring
```



---

Comment by SimonKing created at 2010-10-01 19:17:24

Do I understand correctly that in this ticket it is _not_ attempted to replace `FreeAlgebra` by a more efficient implementation based on Singular's Letterplace Algebra? This ticket is only about wrapping free Groebner bases, but not about wrapping the basic arithmetic?

What Sage currently does in free algebras is generic and slow. As pointed out on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ad16f4fbe4ab66f), bot Singular and Gap are faster in basic arithmetic than the current implementation in Sage.

But this should be on a different ticket, right?

Best regards,
Simon


---

Comment by AlexanderDreyer created at 2010-10-01 20:19:41

As I understand, this makes the Singular's letterplace functionality accessible to Sage (in addition to the Plural functionality of #4539).


---

Comment by burcin created at 2010-10-01 20:28:46

This ticket is only about exposing the Groebner basis computation. We didn't think arithmetic was usable since

 * there is a degree bound, and
 * it is a hack in Singular.

If you think the arithmetic should be wrapped as well, that should be on a different ticket. I don't know how much the Plural wrapper (#4539) will help with that.


---

Comment by SimonKing created at 2010-10-02 07:41:50

Replying to [comment:14 AlexanderDreyer]:
> As I understand, this makes the Singular's letterplace functionality accessible to Sage (in addition to the Plural functionality of #4539).

What is meant by "Letterplace functionality"? Is it "simply" computing Gröbner basis with degree bound in free associative algebras?

Something that irritates me (and I already asked in the Singular forum) is that I could not find a way to _apply_ such Groebner basis, e.g., in order to compute a normal form of an element of the free associative algebra w.r.t. this Gröbner basis. Also I tend to call _basic arithmetic_ a funtionality.

Replying to [comment:15 burcin]:
> This ticket is only about exposing the Groebner basis computation. We didn't think arithmetic was usable since
> 
>  * there is a degree bound, and
>  * it is a hack in Singular.
> 
> If you think the arithmetic should be wrapped as well, that should be on a different ticket. I don't know how much the Plural wrapper (#4539) will help with that.

OK. _If_ I find the time, I'll finish the wrappers that I hacked together yesterday. The new ticket will then provide two alternative implementations of free (associative) algebras. One will be based on Gap, the other on Letterplace. The latter will be a hack as well: While doing arithmetic, the degree bound will be dynamically adapted. Currently I use Expect interfaces, but I guess using the Plural wrapper will improve things further.

Cheers,
Simon


---

Comment by SimonKing created at 2011-03-17 14:32:50

I tried to apply the patches - apparently it is

Apply trac_7797-letterplace_ring_hack.patch trac_7797-letterplace.3.patch plural_functions.patch

Correct?

Unfortunately, plural_functions.patch fails. Can you rebase it, please?


---

Comment by SimonKing created at 2011-03-17 14:32:50

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-03-17 14:36:38

In addition, one doc test has a different result:


```
sage: from sage.libs.singular.letterplace import freegb 
sage: F.<x,y,z> = FreeAlgebra(QQ, 3); F 
Free Algebra on 3 generators (x, y, z) over Rational Field
sage: l=[2*x*z*x+y*x*y, 3*x*y+x*z] 
sage: freegb(l, 10) 
[3*x*y + x*z, 6*x*z*x - y*x*z, 3*y*x*z*y + y*x*z^2, 3*y*x*z^2*y + y*x*z^3, x*z*y*x*z - y*x*z^2*x, 3*y*x*z^3*y + y*x*z^4, y*x*z^2*x*z + 3*y^2*x*z^2*x, x*z*y^2*x*z - 6*y*x*z^2*x^2, 3*y*x*z^4*y + y*x*z^5, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, x*z*y^3*x*z - 36*y*x*z^2*x^3, 3*y*x*z^5*y + y*x*z^6, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, x*z*y^4*x*z - 216*y*x*z^2*x^4, 3*y*x*z^6*y + y*x*z^7, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, x*z*y^5*x*z - 1296*y*x*z^2*x^5, 3*y*x*z^7*y + y*x*z^8, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6]
```


Which one is correct?


---

Comment by SimonKing created at 2011-03-19 08:19:21

FYI: As I mentioned in an earlier post, just having a two-sided Gröbner basis is not enough for my envisioned applications. I also need a competitive arithmetic for free associative algebras, normal form computation, and, if possible, ideals in non-commutative rings, and ring quotients.

So, I implemented something from scratch, _not_ based on the previous patches. I already got an implementation of free associative algebras based on letterplace (with a dynamic degree bound). For example, computing `(x+y)**20` is 84 times faster than with the old implementation of free algebras.

I also have a base class for left, right and twosided ideals: If R is any ring and L a list of elements, then R*L is a left ideal, L*R a right ideal, and R*L*R a twosided ideal.

Using freegb for the computation of a two-sided Gröbner basis will be straight forward. In addition, Grischa Studzinski and Viktor Levandoskyy provided me with some code for computing normal forms in free algebras, that is supposed to be in a future Singular release. My plan is to back-port it.

And then there's documentation to write...


---

Comment by SimonKing created at 2011-03-24 16:21:53

I have attached a new patch that replaces all previous patches and provides a lot more functionality.

Since I learned much from the previous patches, I hesitate to remove Michael and Burcin from the author list. But perhaps you like to be referee? Then you should move your name into the reviewer field.

*__Technical Remarks__*

`singular_function` is very useful! However, it was impossible to simply call the `freegb.lib` library functions of Singular, since they rely on ring attributes -- but ring attributes have not been wrapped in `libSingular`.

Moreover, it is not a good idea to call the `makeLetterplaceRing` function from Singular and then transform the resulting `RingWrap` into a polynomial ring. It _is_ possible -- but the result can not be pickled, since its variable names look like `x(1),y(1),x(2),y(2)` and are thus no valid identifiers.

But it is no problem to create another ring with more sober variable names, and apply the letterplace functions to it. One just needs to work around the attribute tests that these functions do. In fact, these functions do only one thing after the checking, namely a system call. So, I simply did this system calls as well.

In the current release, Singular does provide the Gröbner basis computations in free algebras, but it does _not_ provide normal form computations. Grischa Studzinski has send me some code that is supposed to become part of `freegb.lib` -- again, I can not call it directly, but it was fairly straight forward to implement along the lines of Grischa's code.

*__New Features__*

___Free Algebra constructor as `UniqueFactory`___

Up to now, the `FreeAlgebra` constructor was based on an incomplete way of caching: When you pickle and unpickle a free algebra, you would not get the same object.

```
# old behaviour
sage: F.<a,b,c> = FreeAlgebra(QQ,3)
sage: loads(dumps(F)) is F
False
```


This is now resolved. Moreover, it is not needed to explicitly provide the number of generators, when it is obvious from the list of names:

```
sage: F.<x,y,z> = FreeAlgebra(QQ)
sage: loads(dumps(F)) is F
True
```


I did one change that may be subject to criticism, and I wouldn't oppose to revert it. A free algebra in one generator is a polynomial ring. So, I return a polynomial ring:

```
sage: FreeAlgebra(QQ,'x')
Univariate Polynomial Ring in x over Rational Field
```


The constructor can now also be asked for a different implementation, as in all examples below.

___Free Algebra via Letterplace___

I provide a new implementation of free algebras. It can be constructed as follows:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: F
Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field
```


Due to some shortcomings of Singular's letterplace implementation, unfortunately we need to restrict to homogeneous elements:

```
sage: (x+2*y)^2
x*x + 2*x*y + 2*y*x + 4*y*y
sage: x+0
x
Traceback (most recent call last):
...
ArithmeticError: Can only add elements of the same degree
```

This is why the new implementation can not yet become the default.

However, the arithmetic in the new implementation is much faster than the old:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: F_old.<a,b,c> = FreeAlgebra(QQ)
sage: timeit('t=(x+y)^15')
5 loops, best of 3: 27.7 ms per loop
sage: timeit('t=(a+b)^15')
sage: %time t=(a+b)^15
CPU times: user 4.51 s, sys: 0.09 s, total: 4.60 s
Wall time: 6.46 s
sage: 4510/27.7
162.815884476534
sage: timeit('t=(x+y)^15')
25 loops, best of 3: 19.7 ms per loop
sage: %time t=(a+b)^15
CPU times: user 2.70 s, sys: 0.02 s, total: 2.72 s
Wall time: 2.73 s
sage: 2700/19.7
137.055837563452
```


___One- and Twosided Ideals of Noncommutative Rings___

I implemented it in a fairly general way, ideals can be created for any ring:

```
sage: A = SteenrodAlgebra(2)
sage: IL = A*[A.1+A.2,A.1^2]; IL
Left Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra
sage: IR = [A.1+A.2,A.1^2]*A; IR
Right Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra
sage: IT = A*[A.1+A.2,A.1^2]*A; IT
Twosided Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra
```


Note some nastyness: The parent of an ideal still is the "monoid of ideals of a ring". But we actually have no multiplication in the non-commutative setting:

```
sage: IL*IR
Traceback (most recent call last):
...
NotImplementedError: Can not multiply non-commutative ideals.
```


Of course, in general, we have no way to solve the ideal containment problem. But in free algebras, we have letterplace:

```
sage: I.groebner_basis(degbound=3)
Twosided Ideal (y*y*y - y*y*z + y*z*y - y*z*z, y*y*x + y*y*z + y*z*x + y*z*z, x*y + y*z, x*x - y*x - y*y - y*z) of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field
sage: (x*y*z*y*x).normal_form(I)
y*z*z*y*z + y*z*z*z*x + y*z*z*z*z
sage: x*y*z*y*x - (x*y*z*y*x).normal_form(I) in I
True
sage: x*I.0-I.1*y+I.0*y in I
True
sage: 1 in I
False
```


___Quotient Rings___

Previously, quotient rings have only been available for rings that inherit from the base class of commutative rings. My patch makes them available for all rings, and actually it should work to some extent even for objects that belong to the category `Rings()` but do not inherit from `sage.rings.ring.Ring`.

The requirement is that we mod by an ideal `I` that is _twosided_ and that has a method `I.reduce(x)` that returns a normal form of an element `x` with respect to `I`. That requirement holds for ideals of polynomial rings, and also for homogeneous ideals of free associative algebras. In particular:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: I = F*[x*y+y*z,x^2+x*y-y*x-y^2]*F
sage: Q.<a,b,c> = F.quo(I); Q
Quotient of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field by the ideal (x*y + y*z, x*x + x*y - y*x - y*y)
sage: a*b
-b*c
sage: a^3
-b*c*a - b*c*b - b*c*c
sage: J = Q*[a^3-b^3]*Q
sage: R.<i,j,k> = Q.quo(J); R
Quotient of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field by the ideal (-y*y*z - y*z*x - 2*y*z*z, x*y + y*z, x*x + x*y - y*x - y*y)
sage: i^3
-j*k*i - j*k*j - j*k*k
sage: j^3
-j*k*i - j*k*j - j*k*k
```


One can also test if the quotient is commutative:

```
sage: Q.is_commutative()
False
sage: J = F*[x*y-y*x,x*z-z*x,y*z-z*y,x^3-y^3]*F
sage: R = F.quo(J)
sage: R.is_commutative()
True
```


*__Miscellaneous__*

I inserted the documentation of the new modules into the reference manual - I think it looks nice, but I guess a referee should double check.

Doc tests pass for me. Thus: Ready for review!!


---

Comment by SimonKing created at 2011-03-24 16:22:08

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-03-24 16:26:07

I forgot one technical detail:

Not all rings inherit from the base class of rings. Examples are matrix algebras. In order to support non-commutative ideals for such rings, I provide the relevant methods as `ParentMethods` in the category of `Rings()`. Perhaps this duplication of code is considered a code smell.

At least, it enables the following:

```
sage: MS = MatrixSpace(QQ,2,2)
sage: MS*[MS.1,2]
Left Ideal 
(
  [0 1]
  [0 0],

  [2 0]
  [0 2]
)
 of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
```



---

Comment by SimonKing created at 2011-03-24 16:28:56

Apparently the patchbot does not read the ticket description.

Apply trac7797-full_letterplace_wrapper.patch


---

Comment by SimonKing created at 2011-03-24 16:38:04

I realise that I made at least two copy-and-paste errors in the examples above: One of the "timeit" commands should be removed, and the ideals `I` always is the same, namely `I = F*[x*y+y*z,x<sup>2+x*y-y*x-y</sup>2]*F`.

Sorry, Simon


---

Comment by SimonKing created at 2011-03-25 18:17:56

Anne Schilling reported a problem on sage-combinat-devel: The patch did apply, but "sage -br" did not work. I think I found the reason: The patch did not contain the empty `__init__.py` file in `sage/algebras/letterplace/`. Simply I forgot to add it.

I updated the patch, and now I hope it works. By the way, is the patchbot not working? I miss the coloured stamp on the ticket!

Apply trac7797-full_letterplace_wrapper.patch


---

Comment by SimonKing created at 2011-03-27 06:33:47

Currently, the Letterplace Gröbner bases can only be computed if the ring of coefficients is a field. I don't know whether this condition can be lifted and whether the Singular team is working on it.

That restriction _was_ mentioned in the doc, but not very clearly, and the error message was obscure (namely, it came from the failing call to a Singular system function). There is now additional documentation of that restriction, and the error message is nicer.

Apply trac7797-full_letterplace_wrapper.patch


---

Comment by nthiery created at 2011-03-27 07:55:52

Version rebased on top of #10961 available from:

http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch


---

Comment by SimonKing created at 2011-03-27 07:59:41

Replying to [comment:30 nthiery]:
> Version rebased on top of #10961 available from:
> 
> http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch

Thank you!

What is the procedure? Shall I replace my patch with the rebased one and state the dependency (to the patchbot), or shall the rebased version remain on the combinat patch server?

Best regards,
Simon


---

Comment by aschilling created at 2011-03-27 08:10:27

This patch provides an interface to Singular, which gives a faster implementation of free algebras and adds new features such as for example quotients of free algebras (for terms of homogeneous degree). I have tested the quotient algebra features extensively and they seem to work great!

I do not feel qualified to do a technical review, but I am happy to give a positive review for the new features added.

Anne


---

Comment by aschilling created at 2011-03-27 08:12:55

Replying to [comment:31 SimonKing]:
> Replying to [comment:30 nthiery]:
> > Version rebased on top of #10961 available from:
> > 
> > http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch
> 
> Thank you!
> 
> What is the procedure? Shall I replace my patch with the rebased one and state the dependency (to the patchbot), or shall the rebased version remain on the combinat patch server?
> 
> Best regards,
> Simon

Since #10961 hopefully gets merged soon, you should probably upload the rebased version on trac and add `Dependencies: #10961' to the description. Then patchbot should in principle know!


---

Comment by SimonKing created at 2011-03-27 08:28:03

For the patchbot:

Apply trac7797-full_letterplace_wrapper.patch
Depends on #10961


---

Comment by SimonKing created at 2011-03-27 08:34:03

Replying to [comment:32 aschilling]:
> This patch provides an interface to Singular, which gives a faster implementation of free algebras and adds new features such as for example quotients of free algebras (for terms of homogeneous degree). I have tested the quotient algebra features extensively and they seem to work great!

Good! I'll give that feedback to the Singular team as well.

> I do not feel qualified to do a technical review, but I am happy to give a positive review for the new features added.

Thank you! There is at least one point that should probably be raised on sage-algebra: Is it acceptable that (with my patch) the `FreeAlgebra` constructor returns a polynomial ring when asked for a free algebra with only one generator? 

Mathematically it is correct, but I wonder if that is acceptable in a CAS.

Simon


---

Comment by SimonKing created at 2011-03-27 09:32:21

The new patch differs from the old one only in the comments.

Again for the patchbot:

Apply trac7797-full_letterplace_wrapper.patch

Depends on #10961


---

Attachment

A full wrapper for Singular's letterplace functionality, plus non-commutative ideals and ring quotients; rebased on top of 10961


---

Comment by SimonKing created at 2011-03-27 13:53:16

I added an `__iter__` method for `FreeAlgebraElement_letterplace`, returning the list of pairs "exponent tuple, coefficient", and a method of `FreeAlgebra_letterplace` that returns an element, such that `F(dict(p))==p` for any element p of F. That has been requested by Nicolas.

For the patchbot:

Apply trac7797-full_letterplace_wrapper.patch

Depends on #10961


---

Comment by SimonKing created at 2011-03-27 14:04:55

Replying to [comment:37 SimonKing]:
> ...such that `F(dict(p))==p` for any element p of F.

Sorry, I meant to write `p == F._from_dict_(dict(p))`.


---

Comment by SimonKing created at 2011-03-28 07:46:03

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-03-28 07:46:03

It was suggested to split this ticket, and also it was suggested that the `FreeAlgebra` constructor always returns a free algebra, not a polynomial ring.


---

Comment by SimonKing created at 2011-03-28 14:01:45

I managed to split my patch. The part concerning "basic implementation of ideals in non-commutative rings" is now at #11068. The new patch is based on top of that.

*__TODO__*

Let the `FreeAlgebra` constructor always return a free algebra, not a polynomial ring.

*__New Feature__*

In addition to what was described in previous comments, my letterplace wrapper can compute _complete_ twosided Gröbnerbases by an adaptive algorithm. The idea is simple: If the Gröbner basis is known out to degree `2*d-1`, but the highest degree of its generators is `d`, then the Gröbner basis is complete.

Example:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: I = F*[x*y-y*x,x*z-z*x,y*z-z*y,x^2*y-z^3,x*y^2+z*x^2]*F
sage: I.groebner_basis(Infinity)
Twosided Ideal (z*z*z*y*y + z*z*z*z*x, z*x*x*x + z*z*z*y, y*z - z*y, y*y*x + z*x*x, y*x*x - z*z*z, x*z - z*x, x*y - y*x) of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field
```


Since the commutators are contained in the ideal, we can verify that result with a commutative Gröbner basis, as follows:

```
sage: P.<c,b,a> = PolynomialRing(QQ,order='neglex')
sage: J = P*[a^2*b-c^3,a*b^2+c*a^2]
sage: J.groebner_basis()
[b*a^2 - c^3, b^2*a + c*a^2, c*a^3 + c^3*b, c^3*b^2 + c^4*a]
```


So, that's a good consistency test.

Apply trac7797-full_letterplace_wrapper_rel11068.patch

Depends on #11068


---

Comment by SimonKing created at 2011-04-01 06:57:20

I don't know why, but even though mercurial claims that it tracks `sage/algebras/letterplace/__init__.py`, it kept forgetting to include it into the patch. So, I decided to fill `__init__.py` with some comment. Now it should work.

Of course, you may play with the patch, but it still needs work. First of all, there is the issue that the free algebra constructor should never return a polynomial ring (in the univariate case). And then, my plan is to refactor things, such that there will also be dependencies with #9138 and #9944.

Depends on #11068 

Apply trac7797-full_letterplace_wrapper_rel11068.patch


---

Comment by SimonKing created at 2011-04-27 10:42:11

I updated the patch.

Apply trac7797-full_letterplace_wrapper_rel11068.patch

Depends on #11068

Actually I am not sure about all dependencies. #11068 should be enough on top of sage-4.7.alpha5. However, here is a full account of the patches that I had applied to sage-4.7.alpha5 before creating the patch here: #10296, #9944, #9138, #9976, #11115, #11068.

In particular, I think the refactoring of rings, quotient rings and non-commutative ideals is successfully solved in #9138 and #11068. Concerning unigenerated free algebras, it seems better to stay in the world of free algebras, rather than returning a polynomial ring. So, we have

```
sage: F.<x> = FreeAlgebra(QQ)
sage: F
Free Algebra on 1 generators (x,) over Rational Field
sage: F.is_commutative()
True
sage: F.<x> = FreeAlgebra(QQ, implementation='letterplace')
sage: F
Free Associative Unital Algebra on 1 generators (x,) over Rational Field
sage: F.is_commutative()
True
```


In principle, it could be reviewed now. But the patch chain in front of it is rather large, and not everything has a positive review, yet.

My next plan: Allow positive integer degree weights on the generators, extending the scope of the letterplace wrapper from homogeneous to weighted homogeneous elements, and allow degree-wise computation of weighted homogeneous Gröbner bases. Note that this goes beyond what is currently implemented in Singular, but it should work using a little hack (slack variables).


---

Comment by SimonKing created at 2011-04-27 10:42:11

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-27 12:21:13

Sorry, I needed to update the patch due to some outdated doc tests that I forgot to correct.

Apply trac7797-full_letterplace_wrapper_rel11068.patch

Depends on #11068


---

Comment by SimonKing created at 2011-04-28 11:34:52

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-28 11:34:52

I just found that the documentation (at least with #9976 applied) is not good. Some stuff is included that certainly does not belong there.


---

Comment by SimonKing created at 2011-04-28 12:52:06

Replying to [comment:44 SimonKing]:
> I just found that the documentation (at least with #9976 applied) is not good. Some stuff is included that certainly does not belong there.

Actually, on second thought, it belongs there: I am talking about the two singular_function instances included in the module. The main problem was that singular_function includes the documentation provided by Singular without taking care of formatting -- resulting in numerous errors (e.g., back ticks are misinterpreted as the beginning of Latex expressions, the indentation is handled differently, and so on).

In #11268, I suggest to take care if it by turning the Singular documentation into a verbose code block. With that change, the documentation looks a lot better. I therefore make it a new dependency.

Depends on #11068 #11268


---

Comment by SimonKing created at 2011-04-28 12:52:06

Changing status from needs_work to needs_review.


---

Attachment

Positive integral degree weights for letterplace. UniqueFactory for free algebras.


---

Comment by SimonKing created at 2011-05-26 09:31:57

Changing keywords from "singular" to "singular, free algebra, letterplace".


---

Comment by SimonKing created at 2011-05-26 09:31:57

Meanwhile I implemented two other features:

*Uniqueness of parents*

We had

```
sage: F.<x,y,z> = FreeAlgebra(QQ, 3)
sage: loads(dumps(F)) is F
False
```


I rewrote the `FreeAlgebra` constructor using `UniqueFactory`, so that the answer above becomes `True`.

*Degree weights*

The letterplace implementation in Singular is restricted to homogeneous ideals, and each generator can only have degree 1. With a little hack, I introduced positive integral degree weights for generators, so that we can now do:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace', degrees=[1,2,3])
sage: I = F*[x*y+z-y*x,x*y*z-x^6+y^3]*F
sage: I.groebner_basis(Infinity)
Twosided Ideal (x*z*z - y*x*x*z - y*x*y*y + y*x*z*x + y*y*y*x + z*x*z + z*y*y - z*z*x, x*y - y*x + z, x*x*x*x*z*y*y + x*x*x*z*y*y*x - x*x*x*z*y*z - x*x*z*y*x*z + x*x*z*y*y*x*x + x*x*z*y*y*y - x*x*z*y*z*x - x*z*y*x*x*z - x*z*y*x*z*x + x*z*y*y*x*x*x + 2*x*z*y*y*y*x - 2*x*z*y*y*z - x*z*y*z*x*x - x*z*y*z*y + y*x*z*x*x*x*x*x - 4*y*x*z*x*x*z - 4*y*x*z*x*z*x + 4*y*x*z*y*x*x*x + 3*y*x*z*y*y*x - 4*y*x*z*y*z + y*y*x*x*x*x*z + y*y*x*x*x*z*x - 3*y*y*x*x*z*x*x - y*y*x*x*z*y + 5*y*y*x*z*x*x*x + 4*y*y*x*z*y*x - 4*y*y*y*x*x*z + 4*y*y*y*x*z*x + 3*y*y*y*y*z + 4*y*y*y*z*x*x + 6*y*y*y*z*y + y*y*z*x*x*x*x + y*y*z*x*z + 7*y*y*z*y*x*x + 7*y*y*z*y*y - 7*y*y*z*z*x - y*z*x*x*x*z - y*z*x*x*z*x + 3*y*z*x*z*x*x + y*z*x*z*y + y*z*y*x*x*x*x - 3*y*z*y*x*z + 7*y*z*y*y*x*x + 3*y*z*y*y*y - 3*y*z*y*z*x - 5*y*z*z*x*x*x - 4*y*z*z*y*x + 4*y*z*z*z - z*y*x*x*x*z - z*y*x*x*z*x - z*y*x*z*x*x - z*y*x*z*y + z*y*y*x*x*x*x - 3*z*y*y*x*z + 3*z*y*y*y*x*x + z*y*y*y*y - 3*z*y*y*z*x - z*y*z*x*x*x - 2*z*y*z*y*x + 2*z*y*z*z - z*z*x*x*x*x*x + 4*z*z*x*x*z + 4*z*z*x*z*x - 4*z*z*y*x*x*x - 3*z*z*y*y*x + 4*z*z*y*z + 4*z*z*z*x*x + 2*z*z*z*y, x*x*x*x*x*z + x*x*x*x*z*x + x*x*x*z*x*x + x*x*z*x*x*x + x*z*x*x*x*x + y*x*z*y - y*y*x*z + y*z*z + z*x*x*x*x*x - z*z*y, x*x*x*x*x*x - y*x*z - y*y*y + z*z) of Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field
```

This and the possibility to compute a complete Gröbner basis (provided a finite complete Gröbner basis exists) go beyond what is currently in Singular.

The underlying idea of the degree weights is: Introduce a homogenizing variable. By default, it is called `x`, but a different name is chosen if there is a name conflict. Here, it is renamed to `x_`. And then, we represent a generator `z` of degree `d` internally as `z*x_^(d-1)` (of course with non-commutative multiplication).

Hence, the underlying truncated letterplace ring becomes a bit bigger, and in the bigger ring all generators are of degree one. Of course, the additional variable is omitted in the string representation. We have for example

```
sage: z
z
sage: z.degree()
3
sage: z.letterplace_polynomial()
z*x__1*x__2
```


As much as I know, with that approach, Gröbner bases are correctly computed: If in all polynomials each occurrence of `z` is followed by `x_^(d-1)` then all S-polynomials and reductions (computed in the ring with additional generator `x_` and with all generators in degree 1) will have the same property.

I know this is a hack, but I guess it may be useful. It certainly will be usefull for my current project, because I _need_ degree weights.

Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch

Depends on #11068, #11268


---

Comment by SimonKing created at 2011-05-26 10:07:47

I noticed that I forgot one detail: Latex!

With the latest patch, we also get

```
sage: K.<z> = GF(25)
sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace', degrees=[1,2,3])
sage: -(a*b*(z+1)-c)^2
(2*z + 1)*a*b*a*b + (z + 1)*a*b*c + (z + 1)*c*a*b - c*c
sage: latex(-(a*b*(z+1)-c)^2)
\left(2 z + 1\right) a b a b + \left(z + 1\right) a b c + \left(z + 1\right) c a b - c c
```

Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch

Depends on #11068, #11268


---

Comment by SimonKing created at 2011-05-26 10:09:14

... or also

```
sage: F.<bla,alpha,z> = FreeAlgebra(QQ, implementation='letterplace', degrees=[1,2,3])
sage: latex(-3*alpha*bla-z)
-3 \alpha \mbox{bla} - z
```



---

Comment by SimonKing created at 2011-05-26 10:49:00

Odd. The documentation for letterplace used to build fine. But now, it does not build _at all_! The output are three empty html pages (empty except for the title and the navigation) - the doc strings do not appear.

Any idea where that might come from?


---

Comment by SimonKing created at 2011-05-26 13:04:59

I don't know where it came from. But after deleting doc/output/html/en/reference and doc/output/doctrees/, building the documentation finally succeeded.

So, problem vanished.


---

Comment by SimonKing created at 2011-05-27 06:39:50

Apparently I had changed the milestone by accident...


---

Comment by SimonKing created at 2011-07-27 15:43:52

In my application, I also need conversion from graded sub-algebras. Hence, I implemented it in the new patch.

To be precise: If we have free graded algebras A and B in letterplace implementation, then there is a coercion from A to B if and only if there is a coercion from the base ring of A to the base ring of B, and the set of generator names of A is a subset of the generator names of B, and the degrees of equally named generators of A and B are equal.

The coercion is always name and degree preserving.

Example:

```
sage: F.<t,y,z> = FreeAlgebra(ZZ, implementation='letterplace', degrees=[4,2,3])
sage: G = FreeAlgebra(GF(5), implementation='letterplace', names=['x','y','z','t'], degrees=[1,2,3,4])
sage: t*G.0       # indirect doctest
t*x
sage: (t*G.0 + G.1*G.2)*y
y*z*y + t*x*y
```


Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch trac7797-letterplace_coercion.patch


---

Attachment

A full wrapper for Singular's letterplace functionality, plus complete Groebner bases; based on top of 11068


---

Attachment

Implement latex for letterplace polynomials and letterplace algebras


---

Comment by SimonKing created at 2011-08-01 16:47:10

Implementing coercion for letterplace algebras


---

Attachment

I had to rebase three of the four patches. Still needing review...

Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch trac7797-letterplace_coercion.patch


---

Comment by fbissey created at 2011-08-01 21:54:05

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2011-08-01 21:54:05

In [attachment:trac7797-full_letterplace_wrapper_rel11068.patch] please do not use SAGE_ROOT + local/include in module_list.py use SAGE_INC instead. I spent sometime cleaning all that up for 4.7.1 and would like to see it stay clean for a little while longer.


---

Comment by SimonKing created at 2011-08-01 23:35:36

Replying to [comment:55 fbissey]:
> In [attachment:trac7797-full_letterplace_wrapper_rel11068.patch] please do not use SAGE_ROOT + local/include in module_list.py use SAGE_INC instead. 

I didn't know that SAGE_INC exists. It is certainly a good idea to use such variables whenever possible.


---

Comment by SimonKing created at 2011-08-01 23:58:51

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-08-01 23:58:51

I'm now using SAGE_INC, and I used the occasion to create a combined patch.
 
Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by SimonKing created at 2011-08-15 09:34:26

I had to rebase my patch: Some trivial changes in the doc tests were needed, since block orders are now displayed differently.

Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by AlexanderDreyer created at 2011-09-26 20:50:15

sage-4.7.2alpha3-prerelease with the following patches applies:

```
trac11815_format_must_preserve_embedding.patch
trac11115-cached_cython.patch
trac11115_cached_function_pickling.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac7797-full_letterplace_wrapper_combined.patch
```

compiles/installs and runs `sage -testall` successfully  on a SuSE Enterprise 11.1.
This is close to a positive review, but I'll check out another platform before and have a look at the patch.


---

Comment by AlexanderDreyer created at 2011-09-26 20:50:15

Remove assignee burcin.


---

Comment by AlexanderDreyer created at 2011-09-26 20:51:30

Set assignee to burcin.


---

Comment by AlexanderDreyer created at 2011-09-27 20:23:18

Also compiles/installs and runs `sage -testall` successfully on Mac OSX ppc (32bit). So I can give a positive review for the technical part. Somebody needs to look for the Maths.


---

Comment by SimonKing created at 2011-10-26 18:59:04

I think it makes sense to use #4539 (which already has a positive review, but is pending because of #9138) as a dependency. I have updated the patch accordingly. The doc tests pass (at least on my machine).


---

Comment by SimonKing created at 2011-10-26 18:59:42

I forgot to notify the patch bot:

Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by davidloeffler created at 2012-03-29 11:55:25

The patch fails to apply to 5.0.beta11 -- see patchbot logs. I suspect #12461 is the cause.


---

Comment by davidloeffler created at 2012-03-29 11:55:25

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-03-30 09:40:12

Yes, #12641 was to blame. The reason was that apparently #12641 did remove four blank spaces. So, the change is trivial.

By the way: At the recent annual meeting of the German Science Foundation Priority Programme on computer algebra, I was talking to Viktor Levandovskii, who is responsible for Letterplace in Singular. He confirmed that my hacks for implementing degree weights and for computing complete Gröbner bases are correct.

Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by SimonKing created at 2012-03-30 09:40:12

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-04-15 11:24:01

It needs to be rebased wrt. #12749: This ticket adds doctests, but one hunk for sage/algebras/free_algebra.py adds some doctest as well...


---

Comment by SimonKing created at 2012-04-15 11:24:01

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-04-15 11:30:41

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-04-15 11:30:41

Done. And please please find someone for a review!

Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by SimonKing created at 2012-08-13 13:17:01

It is now 4 months ago that I last asked if someone could review the patch, so that we would have Gröbner bases of two-sided homogeneous ideals in free associative algebras. Which other CAS has those? So: BUMP!


---

Comment by SimonKing created at 2012-08-14 12:39:34

I had to modify one doctest, due to a new test in the category of rings - see #12988.

Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by AlexanderDreyer created at 2012-08-14 22:38:46

The patch looks good to me, just use  the `:trac:`7791`` statement to refer to this ticket here. Provided, that the tests succeeds (I'm currently building a recent sage), I'd say, that we are close to positive.


---

Comment by SimonKing created at 2012-08-15 06:18:23

Replying to [comment:70 AlexanderDreyer]:
> The patch looks good to me, just use  the `:trac:`7791`` statement to refer to this ticket here. Provided, that the tests succeeds (I'm currently building a recent sage), I'd say, that we are close to positive.

Yep, I think I wrote the patch before the `:trac:` directive has been introduced. The patchbot complains about trailing white space - so, I'll take care of that as well.


---

Comment by SimonKing created at 2012-08-15 06:18:23

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-08-15 06:56:29

Now it should be fine, regarding whitespace and regarding `:trac:` directive.

Apply trac7797-full_letterplace_wrapper_combined.patch


---

Comment by SimonKing created at 2012-08-15 06:56:29

Changing status from needs_work to needs_review.


---

Comment by AlexanderDreyer created at 2012-08-15 07:13:43

The patch applies nicely to sage-5.3 beta1 and the rebuild of the sage library was successful. So let' s wait for `make ptestlong` to finish.


---

Comment by AlexanderDreyer created at 2012-08-15 11:30:38

Ok, `ptestlong` succeeded, so we ave a positive review!


---

Comment by AlexanderDreyer created at 2012-08-15 11:30:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-23 12:46:23

Resolution: fixed


---

Comment by jdemeyer created at 2012-08-24 20:24:40

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2012-08-24 20:24:40

This leads to lots of failures on Solaris SPARC:

```

        sage -t  --long -force_lib devel/sage/sage/algebras/free_algebra.py # 3 doctests failed
        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/free_algebra_element_letterplace.pyx # 13 doctests failed
        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx # 6 doctests failed
        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/letterplace_ideal.pyx # 14 doctests failed
        sage -t  --long -force_lib devel/sage/sage/rings/quotient_ring.py # 11 doctests failed
        sage -t  --long -force_lib devel/sage/sage/rings/quotient_ring_element.py # 1 doctests failed
```

See [http://build.sagemath.org/sage/builders/Skynet%20mark%20%28SunOS%205.10-32%29/builds/207/steps/shell_7/logs/stdio](http://build.sagemath.org/sage/builders/Skynet%20mark%20%28SunOS%205.10-32%29/builds/207/steps/shell_7/logs/stdio).


---

Comment by jdemeyer created at 2012-08-24 20:24:40

Changing status from closed to new.


---

Comment by jdemeyer created at 2012-08-24 20:24:53

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-08-24 20:25:00

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-08-24 22:41:03

I see that most (or all?) the errors reported in the log file occur while calling a singular_function. Is it perhaps the case that singular_function is generally problematic on Solaris SPARC? 

Does Letterplace works on Solaris SPARC in Singular? I think I was told that Singular's system function could be a problem -- but Letterplace relies on it, both in Singular and here.

I.e., is the problem on the side of Singular, or of the wrapper?


---

Comment by jdemeyer created at 2012-08-27 11:21:30

Replying to [comment:79 SimonKing]:
> I.e., is the problem on the side of Singular, or of the wrapper?
How can I check?  What commands should I run in Singular to check?

Also, I added #13237 (Upgrade to Singular-3-1-5) as dependency just in case it matters.  My tests on Solaris SPARC were done with the new Singular from #13237.


---

Comment by SimonKing created at 2012-08-28 16:18:23

Replying to [comment:80 jdemeyer]:
> Replying to [comment:79 SimonKing]:
> > I.e., is the problem on the side of Singular, or of the wrapper?
> How can I check?  What commands should I run in Singular to check?
> 
> Also, I added #13237 (Upgrade to Singular-3-1-5) as dependency just in case it matters.  My tests on Solaris SPARC were done with the new Singular from #13237.

Hans Schönemann has tested it. He used Singular-3-1-5, or in more detail:

```
Singular for SunOS-5 version 3-1-5 (3150)  Aug 27 2012 19:23:52
with
        factory(@(#) factoryVersion = 3.1.5),libfac(3.1.5,July 2012),
        GMP(4.2),NTL(5.5.2),64bit,static readline,Plural,DBM,
        dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1346170574
        CC= gcc -m64 -mptr64 -mcpu=ultrasparc3 -O2 -w -fomit-frame-pointer -pipe -DNDEBUG -DOM_NDEBUG -DSunOS_5 -DHAVE_CONFIG_H,
        CXX= g++ -m64 -mptr64 -mcpu=ultrasparc3 -O2 -w -fomit-frame-pointer -I.. -I/users/cip/alggeom/hannes/galois64 -pipe -DNDEBUG -DOM_NDEBUG -DSunOS_5 -DHAVE_CONFIG_H (3.3.2)
```


The example worked fine, which indicates that it is a problem with my wrapper. If you want to test it for yourself:

```
LIB "freegb.lib";
ring r = 0,(x,y,z),dp;
int d =4; // degree bound
def R = makeLetterplaceRing(d);
setring R;
ideal I = x(1)*y(2) + y(1)*z(2), x(1)*x(2) + x(1)*y(2) - y(1)*x(2) - y(1)*y(2);
option(redSB); option(redTail);
ideal J = letplaceGBasis(I);
J;
```

The expected result is

```
==> J[1]=x(1)*y(2)+y(1)*z(2)
==> J[2]=x(1)*x(2)-y(1)*x(2)-y(1)*y(2)-y(1)*z(2)
==> J[3]=y(1)*y(2)*y(3)-y(1)*y(2)*z(3)+y(1)*z(2)*y(3)-y(1)*z(2)*z(3)
==> J[4]=y(1)*y(2)*x(3)+y(1)*y(2)*z(3)+y(1)*z(2)*x(3)+y(1)*z(2)*z(3)
==> J[5]=y(1)*z(2)*y(3)*y(4)-y(1)*z(2)*y(3)*z(4)+y(1)*z(2)*z(3)*y(4)-y(1)*z(2\
   )*z(3)*z(4)
==> J[6]=y(1)*z(2)*y(3)*x(4)+y(1)*z(2)*y(3)*z(4)+y(1)*z(2)*z(3)*x(4)+y(1)*z(2\
   )*z(3)*z(4)
==> J[7]=y(1)*y(2)*z(3)*y(4)-y(1)*y(2)*z(3)*z(4)+y(1)*z(2)*z(3)*y(4)-y(1)*z(2\
   )*z(3)*z(4)
==> J[8]=y(1)*y(2)*z(3)*x(4)+y(1)*y(2)*z(3)*z(4)+y(1)*z(2)*z(3)*x(4)+y(1)*z(2\
   )*z(3)*z(4)
```

I will see whether `letplaceGBasis` does anything new - perhaps I can learn from it?


---

Comment by SimonKing created at 2012-08-28 16:26:01

Replying to [comment:81 SimonKing]:
> I will see whether `letplaceGBasis` does anything new - perhaps I can learn from it?

No, the essential part is the same. Namely:

```
  ideal J = system("freegb",I,uptodeg,lV);
```

If I am not mistaken, it is the analogue of this command that fails in my code.

The question that I'd like to be answered is: Are calls to Singular's "system" function possible in Sage on Solaris SPARC? Could you please test the following in Sage on Solaris SPARC?

```
sage: from sage.libs.singular.function import singular_function
sage: sing_system = singular_function("system")
sage: R.<x,y> = QQ[]
sage: sing_system("uname", ring=R)
'x86_64-Linux'  # ok, the answer will be different on Solaris SPARC...
```



---

Comment by jdemeyer created at 2012-08-28 17:11:25

Solaris SPARC, Sage 5.2 (i.e. Singular-3-1-3-3):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage.libs.singular.function.singular_function("system")("uname", ring=PolynomialRing(QQ,2,'x'))
// ** s_internalDelete: cannot delete type sqrfree(493)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 5.2, Release Date: 2012-07-25                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
/home/jdemeyer/mark/sage-5.2/<ipython console> in <module>()

/home/jdemeyer/mark/sage-5.2/local/lib/python2.7/site-packages/sage/libs/singular/function.so in sage.libs.singular.function.SingularFunction.__call__ (sage/libs/singular/function.cpp:11875)()

/home/jdemeyer/mark/sage-5.2/local/lib/python2.7/site-packages/sage/libs/singular/function.so in sage.libs.singular.function.call_function (sage/libs/singular/function.cpp:13425)()

RuntimeError: Error in Singular function call 'system':
 system(`sqrfree`) failed
```



---

Comment by SimonKing created at 2012-08-28 17:52:11

Thank you, Jeroen!

So, the bug is not in my wrapper, but in singular_function. And that error looks rather strange. I'll ask Hans, tomorrow.

Martin, do you have an idea where that error might come from?


---

Comment by SimonKing created at 2012-08-29 08:48:03

Here is the code for `system("uname")` (to be found in Singular/extra.cc):

```C
/*==================== uname ==================================*/
    if(strcmp(sys_cmd,"uname")==0)
    {
      res->rtyp=STRING_CMD;
      res->data = omStrDup(S_UNAME);
      return FALSE;
    }
```


About `// ** s_internalDelete: cannot delete type sqrfree(493)`: According to Hans, 493 is the token for the command `sqrfree`, which is _not_ a type but a command. Therefore deleting an object with 493's type is impossible. He doesn't understand how that happens here.

`res->data` is a C string, and `STRING_CMD` is the token 495, which stands for the type of a string (`char *`). Could Solares SPARC mistake 495 for 493??


---

Comment by AlexanderDreyer created at 2012-08-29 09:00:04

Replying to [comment:85 SimonKing]:
> `res->data` is a C string, and `STRING_CMD` is the token 495, which stands for the type of a string (`char *`). Could Solares SPARC mistake 495 for 493??
There probably an outdated Singular/tok.h around. Tokens like INTMOD_CMD were added recently, so this would explain the shift in the enum.


---

Comment by jdemeyer created at 2012-08-30 20:06:14

Okay, with a build from scratch:

```
sage: sage.libs.singular.function.singular_function("system")("uname", ring=PolynomialRing(QQ,2,'x'))
'SunOS-5'
```


So I probably messed up something last time (e.g. forget `sage -b`).


---

Comment by jdemeyer created at 2012-08-30 20:06:14

Changing assignee from burcin to jdemeyer.


---

Comment by jdemeyer created at 2012-08-30 20:35:39

Strange.  I applied the patch of this ticket again and get only one doctest failure now in `sage/algebras`:

```
sage -t  "devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx"
**********************************************************************
File "/home/jdemeyer/mark/sage-5.4.beta0/devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx", line 684:
    sage: G = F._reductor_(I.gens(),3); G
Expected:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3 over Rational Field
Got:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field
**********************************************************************
```


This calls for some further investigation...


---

Comment by SimonKing created at 2012-08-30 20:45:26

Replying to [comment:88 jdemeyer]:
> {{{
> sage -t  "devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx"
> **********************************************************************
> File "/home/jdemeyer/mark/sage-5.4.beta0/devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx", line 684:
>     sage: G = F._reductor_(I.gens(),3); G
> Expected:
>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3 over Rational Field
> Got:
>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field
> **********************************************************************
> }}}
> 
> This calls for some further investigation...

That test is about an internally used method (note the underscores), and the output depends on a polynomial ring that is used to simulate computations in free associative algebras out to a certain degree. As you can see, the ideal we expect and the ideal we got are alike - only the polynomial rings differ.

The point is that the underlying polynomial ring can change during computations, and the free associative algebras are unique parents. Hence, if tests are executed in different order then it may very well be that the polynomial ring used behind the scenes is different. Only the final result (i.e., interpreted in the free associative algebra) is unique.

I suggest to modify that test (and perhaps others as well) as follows:

```
>     sage: G = F._reductor_(I.gens(),3); G
> Expected:
>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field
```

The variables before the `...` are guaranteed to occur, and we don't know (and don't care) whether more variables appear behind the scenes.

Would you accept that solution?


---

Comment by AlexanderDreyer created at 2012-08-30 23:27:20

Replying to [comment:89 SimonKing]:
> I suggest to modify that test (and perhaps others as well) as follows:
> {{{
> >     sage: G = F._reductor_(I.gens(),3); G
> > Expected:
> >     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field
> }}}
> The variables before the `...` are guaranteed to occur, and we don't know (and don't care) whether more variables appear behind the scenes.
> 
> Would you accept that solution?
Sounds reasonable to me. So I'd reestablished the positive review, if Jeroen likes is, too.


---

Comment by jdemeyer created at 2012-08-31 14:33:49

Good for me.


---

Comment by SimonKing created at 2012-08-31 14:45:09

Replying to [comment:91 jdemeyer]:
> Good for me.

OK, then I'll prepare a patch. Probably not before Sunday, though...


---

Comment by SimonKing created at 2012-09-02 07:03:45

I have updated the patch, using an ellipse (...) in the failing test.

Apply  trac7797-full_letterplace_wrapper_combined.patch


---

Comment by SimonKing created at 2012-09-02 07:04:39

Changing status from needs_work to needs_review.


---

Comment by AlexanderDreyer created at 2012-09-07 19:44:36

Hi, I can positively review for Linux. I don't get Sage 5.* compiled on Solaris. Are there any precompiled recent binaries around, maybe at *.washington.edu?


---

Comment by jhpalmieri created at 2012-09-07 20:21:22

Passes tests for me (I just tested the modified files, not the whole Sage library) on Mac OS X 10.7 and OpenSolaris. I'm working on Solaris, but the only Solaris machines I have access to are really slow.

By the way, can you explain the role of the new line 821 in `sage/structure/parent.pyx`?


---

Comment by SimonKing created at 2012-09-07 20:34:52

Replying to [comment:96 jhpalmieri]:
> By the way, can you explain the role of the new line 821 in `sage/structure/parent.pyx`?

I guess the plan was to add a doc test, then I changed my mind and deleted the doctest incompletely. I guess that line can be removed (by a reviewer patch?).


---

Attachment


---

Comment by jhpalmieri created at 2012-10-24 15:01:33

Tests pass on skynet machine mark.


---

Comment by jhpalmieri created at 2012-10-24 15:01:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-10-30 15:52:24

I'm getting (in a trial sage-5.5.beta1, so it includes many other tickets)

```
sage -t  -force_lib devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx
**********************************************************************
File "/release/merger/sage-5.5.beta1/devel/sage-main/sage/algebras/letterplace/free_algebra_letterplace.pyx", line 684:
    sage: G = F._reductor_(I.gens(),3); G
Expected:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3... over Rational Field
Got:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field
**********************************************************************
```



---

Comment by jdemeyer created at 2012-10-30 15:57:17

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2012-10-30 16:00:41

I think we have already discussed that the order of doctests may influence the size of the polynomial ring used to represent the letterplace elements.

So, the fix should be to have `Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field`. I'll do so (hopefully) soonish.


---

Comment by jdemeyer created at 2012-10-30 16:31:32

Doctest error confirmed with (unreleased but essentially ready) sage-5.5.beta0, but not with sage-5.4.rc2.


---

Comment by SimonKing created at 2012-11-09 10:16:51

A full wrapper for Singular's letterplace functionality, plus positive integral degree weights, plus complete Groebner bases of weighted homogeneous two-sided ideals, plus coercion. Rel #12988


---

Comment by SimonKing created at 2012-11-09 10:20:36

Changing status from needs_work to positive_review.


---

Attachment

I am sorry that I took so long to fix it.

I have changed the "big" patch. The diff of the two patch versions is:

```diff
--- trac7797-full_letterplace_wrapper_combined.patch    2012-11-09 11:15:19.355793326 +0100
+++ trac7797-full_letterplace_wrapper_combined.patch        2012-09-02 09:00:20.000000000 +0200
@@ -2176,7 +2176,7 @@
 +            sage: p.reduce(I)
 +            y*y*y - y*y*z + y*z*y - y*z*z
 +            sage: G = F._reductor_(I.gens(),3); G
-+            Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field
++            Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3... over Rational Field
 +
 +        We do not use the usual reduction method for polynomials in
 +        Sage, since it does the reductions in a different order
```


I hope it is ok to restore the positive review, since I assume doctests will be run anyway before releasing.

Apply trac7797-full_letterplace_wrapper_combined.patch trac_7797-ref.patch


---

Comment by AlexanderDreyer created at 2012-11-09 11:49:57

Just realized, that I'm the reviewer: I'm fine with reestablishing to positive review.


---

Comment by jdemeyer created at 2012-11-16 21:25:01

Resolution: fixed


---

Comment by kcrisman created at 2012-12-05 19:37:59

See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I _have_ to add `SAGE_INC + 'factory'`.


---

Comment by AlexanderDreyer created at 2012-12-05 21:51:21

Replying to [comment:108 kcrisman]:
> See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I _have_ to add `SAGE_INC + 'factory'`.
Indeed, looking at the other singular-based modules it makes sense. I don't expect problems doing so.


---

Comment by kcrisman created at 2012-12-05 22:08:26

> > See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I _have_ to add `SAGE_INC + 'factory'`.
> Indeed, looking at the other singular-based modules it makes sense. I don't expect problems doing so.
Great, can you give some feedback on the patch at #13802 then?  Thanks!


---

Comment by AlexanderDreyer created at 2012-12-06 08:38:18

Replying to [comment:110 kcrisman]:
> Great, can you give some feedback on the patch at #13802 then?  Thanks!
Very well, I was able to positively review that patch.


---

Comment by kcrisman created at 2012-12-06 15:15:02

> > Great, can you give some feedback on the patch at #13802 then?  Thanks!
> Very well, I was able to positively review that patch.
Very helpful, thank you.
