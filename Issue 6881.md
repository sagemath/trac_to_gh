# Issue 6881: Conics

Issue created by migration from https://trac.sagemath.org/ticket/6881

Original creator: victor

Original creation time: 2009-09-03 22:47:34

Assignee: tbd

CC:  mstreng

Keywords: conic, curve

We should have a class (or classes) for conic curves, and, more specially diagonal conics.  In particular, one of the methods should be John Cremona's algorithms for finding points on solvable conics, both over Q and over fraction fields of polynomial rings.  Other methods might include getting discriminants, primes of bad reduction, producing parametrized solutions, etc.


---

Comment by AlexGhitza created at 2009-11-15 13:13:12

Changing component from algebra to algebraic geometry.


---

Comment by mstreng created at 2010-07-06 11:09:54

See #727
A patch defining a conic class and using Simon's algorithms for finding points over Q is in progress.


---

Comment by mstreng created at 2010-07-20 21:13:37

I changed the description to better fit what is already in #727. Besides things that are already in #727, all that I removed from the original description were the following two requests.

 1. Use John Cremona's algorithms for finding points on conics over QQ.

It seems that Simon's algorithms (in #727) are better, but that doesn't have to stop us from giving Cremona's code as an option. It is inside mwrank, which is part of Sage. If someone wants to do it, then it can be made into a separate ticket.

 2. Getting primes of bad reduction of conics.

This is as good as in #727: make a Conic C. Then do C.determinant().factor()


---

Comment by lackermans created at 2015-08-07 21:15:45

Changing assignee from tbd to lackermans.


---

Comment by git created at 2015-10-03 01:19:55

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-10-28 13:04:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-12-11 16:19:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lackermans created at 2015-12-11 16:31:12

Changing status from new to needs_review.


---

Comment by git created at 2015-12-11 16:56:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mstreng created at 2015-12-14 15:24:18

Changing keywords from "conic, curve" to "conic, curve, function field".


---

Comment by mstreng created at 2015-12-14 15:25:33

Changing priority from minor to major.


---

Comment by mstreng created at 2015-12-15 15:22:42

Not 100% doctest coverage, and there is a doctest that fails.


---

Comment by mstreng created at 2015-12-15 15:22:42

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-12-16 23:46:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lackermans created at 2015-12-16 23:51:23

Replying to [comment:16 mstreng]:
> Not 100% doctest coverage, and there is a doctest that fails.
Should be okay now.


---

Comment by lackermans created at 2015-12-16 23:51:23

Changing status from needs_work to needs_review.


---

Comment by git created at 2015-12-27 16:18:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mstreng created at 2016-01-28 09:06:53

Changing status from needs_review to needs_work.


---

Comment by git created at 2016-02-03 11:12:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lackermans created at 2016-02-03 11:14:07

Changing status from needs_work to needs_review.


---

Comment by git created at 2016-02-04 15:10:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mstreng created at 2016-02-05 12:53:45

Changing status from needs_review to positive_review.


---

Comment by mstreng created at 2016-02-05 12:53:45

All tests pass. Documentation looks good.

The functions do not work perfectly in all cases due to #20003, but after bypassing `squarefree_decomposition`, I get:




```
sage: K.<t> = PolynomialRing(GF(7))
sage: C = Conic([5*t^2+4, t^2+3*t+3, 6*t^2+3*t+2, 5*t^2+5, 4*t+3, 4*t^2+t+5])
sage: C.has_rational_point()
True
```


and


```
sage: F = FiniteField(7)
sage: P.<t> = F[]                                                               
sage: K = P.fraction_field()
sage: for i in range(50):                                                       
    c = [K.random_element() for j in range(6)]
    C = Conic(c)
    C.has_rational_point(point=True)
....:     
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^8 + 5*t^7 + 6*t^6 + 5*t^5 + 4*t^4 + 5*t^2 + 3*t + 2)/(t^8 + 5*t^7 + 5*t^6
 + 4*t^5 + 3*t^4 + 2*t^3 + t^2 + 5*t + 6) : (t^8 + 2*t^7 + t^5 + t^4 + 2*t^3 + 2
*t^2 + 4*t + 4)/(t^8 + 6*t^7 + t^6 + 4*t^5 + t^4 + 2*t^2 + 5*t + 3) : 1))
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^8 + t^7 + 6*t^6 + 4*t^5 + 6*t^4 + 5*t^2 + 1)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5
 + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : (2*t^8 + 4*t^7 + 5*t^6 + 3*t^5 + t^4 + 5*t + 1
)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5 + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^4 + 2*t^3 + 3*t^2)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : (5*t^7 + 3*t^6 + t
^5 + 5*t^4 + 6*t^3 + 2*t^2 + 4*t)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((t^8 + 5*t^7 + 2*t^6 + 2*t^5 + 3*t^3 + t^2 + 3)/(t^7 + t^6 + 6*t^4 + 5*t^3 + 6
*t^2 + 2*t + 2) : (4*t^5 + 2*t^4 + 5*t^3 + 4*t^2 + 5*t + 2)/(t^4 + 2*t^3 + 5*t^2
 + 4*t + 5) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^11 + 3*t^10 + 6*t^9 + t^8 + 6*t^7 + 4*t^6 + t^5 + 4*t^4 + 2*t^3 + 3*t + 5
)/(t^11 + 5*t^10 + 5*t^9 + t^8 + t^7 + 6*t^6 + 6*t^5 + 4*t^4 + 6*t^3 + 4*t) : (2
*t^9 + 4*t^8 + 4*t^7 + 6*t^6 + 5*t^5 + 5*t^4 + 4*t^3 + t^2 + 6*t + 1)/(t^10 + 5*
t^8 + 4*t^7 + 2*t^6 + 3*t^5 + 5*t^4 + 6*t^2 + 5*t) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
```



---

Comment by jdemeyer created at 2016-02-05 13:18:34

Please rebase to sage-7.1.beta2 (in particular, `sage.rings.arith` has moved to `sage.arith.all`) and use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.

If you have done this, you can set this ticket back to positive review.


---

Comment by jdemeyer created at 2016-02-05 13:18:34

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2016-02-05 13:23:12

You might also want to fix these `pyflakes` warnings:

```
src/sage/schemes/plane_conics/con_rational_function_field.py:25: 'NumberField' imported but unused
src/sage/schemes/plane_conics/con_rational_function_field.py:26: 'identity_matrix' imported but unused
src/sage/schemes/plane_conics/con_rational_function_field.py:32: redefinition of unused 'vector' from line 30
```



---

Comment by git created at 2016-02-07 22:33:14

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:


---

Comment by lackermans created at 2016-02-07 22:35:01

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2016-02-08 07:28:20

Changing status from positive_review to needs_review.


---

Comment by jdemeyer created at 2016-02-08 07:28:20

10 new commits? Sorry, but this needs to be reviewed (not by me).


---

Comment by jdemeyer created at 2016-02-08 07:30:01

This is malformatted:

```
EXAMPLES:
    
    Create a conic::

        sage: K = FractionField(PolynomialRing(QQ, 't'))
```

It should be

```
EXAMPLES:
    
Create a conic::

    sage: K = FractionField(PolynomialRing(QQ, 't'))
```



---

Comment by jdemeyer created at 2016-02-08 07:30:01

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2016-02-08 07:30:53

Please do this:

Replying to [comment:25 jdemeyer]:
> use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.


---

Comment by lackermans created at 2016-02-08 11:22:58

Replying to [comment:29 jdemeyer]:
> 10 new commits? Sorry, but this needs to be reviewed (not by me).
Only the last 3 are new


---

Comment by git created at 2016-02-08 11:25:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lackermans created at 2016-02-08 11:27:02

Changing status from needs_work to needs_review.


---

Comment by lackermans created at 2016-02-08 11:27:02

Replying to [comment:31 jdemeyer]:
> Please do this:
> 
> Replying to [comment:25 jdemeyer]:
> > use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.

Sorry, I misunderstood your last comment. All should be okay now.


---

Comment by mstreng created at 2016-02-11 12:07:47

Thanks Jeroen. I checked the changes and documentation html, and I ran the doctests again.


---

Comment by mstreng created at 2016-02-11 12:07:47

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-02-11 23:26:40

Resolution: fixed
