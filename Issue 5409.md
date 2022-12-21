# Issue 5409: rewrite quaternion algebras -- the current implementation isn't sufficiently good

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-01 06:57:40

Assignee: tbd

CC:  bober




---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2009-03-02 18:09:55

Some issues doctesting against my 3.4.rc0 merge tree

```
	sage -t  devel/sage/sage/quadratic_forms/special_values.py # 4 doctests failed
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__siegel_product.py # 8 doctests failed
	sage -t  devel/sage/sage/rings/ring.pyx # 1 doctests failed
	sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t  devel/sage/sage/modular/dirichlet.py # 4 doctests failed
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py # 2 doctests failed
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py # 1 doctests failed
	sage -t  devel/sage/sage/interfaces/magma.py # 1 doctests failed
```


Cheers,

Michael


---

Comment by tornaria created at 2009-03-02 18:23:33

Replying to [comment:2 mabshoff]:
I can fix all the doctest failures except

```
 	sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
```

which I don't know how to deal with.

The fix is two one-liners on top of part6

```
diff -r 311c05f56282 sage/rings/arith.py
--- a/sage/rings/arith.py       Mon Mar 02 04:52:16 2009 -0500
+++ b/sage/rings/arith.py       Mon Mar 02 10:20:29 2009 -0800
`@``@` -3964,6 +3964,7 `@``@`
     1, mod 4, and such that, at most, the only square dividing it is
     4.
     """
+    from sage.rings.all import Integer
     D = Integer(D)
     D = D.squarefree_part()
     if D%4 == 1:
diff -r 311c05f56282 sage/rings/ring.pyx
--- a/sage/rings/ring.pyx       Mon Mar 02 04:52:16 2009 -0500
+++ b/sage/rings/ring.pyx       Mon Mar 02 10:20:29 2009 -0800
`@``@` -735,7 +735,7 `@``@`
             sage: ZpCA(7).is_commutative()
             True
             sage: A = QuaternionAlgebra(QQ, -1, -3, names=('i','j','k')); A
-            Quaternion algebra with generators (i, j, k) over Rational Field
+            Quaternion Algebra (-1, -3) with base ring Rational Field
             sage: A.is_commutative()
             False
         """
```



---

Attachment

review patch -- fix doctests except for pickle jar


---

Comment by tornaria created at 2009-03-02 19:00:08

Caching of quaternion algebras seems to be broken:

```
sage: QuaternionAlgebra(GF(5)(2),GF(5)(3))
Quaternion Algebra (2, 3) with base ring Finite Field of size 5
sage: QuaternionAlgebra(2,3)
Quaternion Algebra (2, 3) with base ring Finite Field of size 5
```


The second time we should have constructed

```
Quaternion Algebra (2, 3) with base ring Rational Field
```



---

Attachment

fix caching


---

Comment by tornaria created at 2009-03-02 20:01:06

Found a couple of issues with vector_space():
 a. I didn't find a way to map vectors between the quaternion algebra and the vector space
 b. neither the norm or the inner_product in the vector space seem to match the norm in the quaternion algebra

```
sage: Q1 = QuaternionAlgebra(2,3)
(reverse-i-search)`V1': V1
KeyboardInterrupt
sage: V1 = Q1.vector_space()
sage: q = Q1([1,2,3,4])
sage: v = V1(q)
...
TypeError: can't initialize vector from nonzero non-list
sage: v = V1([1,2,3,4])
sage: Q1(v)
...
TypeError: Unable to coerce (1, 2, 3, 4) (<type 'sage.modules.vector_rational_dense.Vector_rational_dense'>) to Rational
sage: q.norm()
62
sage: v.norm()
sqrt(30)
sage: v.inner_product(v)
124
```



---

Attachment

We didn't do quat alg from discriminants for number fields yet.   I'm going to also get rid of "norm" and "trace" and just have "reduced_norm" and "reduced_trace" since even Gonzalo clearly got confused by having both and an alias.


---

Comment by was created at 2009-03-04 07:17:46

get rid of "norm" and "trace" -- this confused gonzalo; now have only reduced norm and trace!


---

Attachment


---

Comment by jvoight created at 2009-03-04 19:55:46

Bug fixes and doctests


---

Attachment

I got it to patch correctly against 3.4.rc0.  I found some bugs and added a few doctests.  Partial positive review.  JV


---

Comment by was created at 2009-03-04 20:35:34

I found a few issues with jvoight's referee patch, which I'm noting here:

* In inner_product_matrix the docs say: "The standard basis 1, i, j, k is orthogonal, so this matrix is just the diagonal matrix with diagonal entries 1, a, b, a*b."  In the code, though, it's 2,2*a,2*b,2*a*b.  

* Line 475 is:

"and j*i=-i*j.  K is a field not of characteristic and a,b are nonzero elements of K"

but it should say "and j*i=-i*j.  K is a field not of characteristic 2 and a,b are nonzero elements of K"  (the missing 2).

Otherwise the referee patch from jvoight looks very very good!


---

Comment by jvoight created at 2009-03-05 00:17:13

Great, so then this gets a positive review from me, too.  I tried a few things out and the multiplication, and this last doctest might be useful (to test cpdef RingElement _mul_), but maybe there's enough already.


```
            sage: K.<x> = QQ[]
            sage: Q_ab = QuaternionAlgebra(Frac(K), 17, -3)
            sage: Q = QuaternionAlgebra(17, -3)
            sage: for t in xrange(100):
            sage:     v1 = [ZZ.random_element() for i in range(4)]
            sage:     v2 = [ZZ.random_element() for i in range(4)]
            sage:     if list(Q(v1)*Q(v2)) <> list(Q_ab(v1)*Q_ab(v2)):
            sage:         print "Multiplication is inconsistent", v1, v2
```



---

Comment by mabshoff created at 2009-03-10 16:57:38

If I read this correctly the last two suggestions by William still need to be fixed in John's patch. 

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 18:01:14

Besides the known pickle issue John's patch breaks two more doctests:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
sage -t -long devel/sage/sage/algebras/quaternion_algebra.py # 8 doctests failed
sage -t -long devel/sage/sage/algebras/quaternion_algebra_element.pyx # 1 doctests failed
```

In detail:

```
sage -t -long "devel/sage/sage/algebras/quaternion_algebra_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.rc2/devel/sage/sage/algebras/quaternion_algebra_element.pyx", line 322:
    sage: 1/Q(0)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[6]>", line 1, in <module>
        Integer(1)/Q(Integer(0))###line 322:
    sage: 1/Q(0)
      File "element.pyx", line 1238, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9116)
      File "coerce.pyx", line 712, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5438)
      File "element.pyx", line 1236, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)
      File "quaternion_algebra_element.pyx", line 362, in sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract._div_ (sage/algebras/quaternion_algebra_element.cpp:5726)
      File "quaternion_algebra_element.pyx", line 346, in sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract.__invert__ (sage/algebras/quaternion_algebra_element.cpp:5660)
      File "rational.pyx", line 1445, in sage.rings.rational.Rational.__invert__ (sage/rings/rational.c:10565)
    ZeroDivisionError: rational division by zero
**********************************************************************
```

and

```
sage -t -long "devel/sage/sage/algebras/quaternion_algebra.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.rc2/devel/sage/sage/algebras/quaternion_algebra.py", line 89:
    sage: QuaternionAlgebra(0,0)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[7]>", line 1, in <module>
        QuaternionAlgebra(Integer(0),Integer(0))###line 89:
    sage: QuaternionAlgebra(0,0)
      File "/scratch/mabshoff/sage-3.4.rc2/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py", line 175, in QuaternionAlgebra
        raise ValueError, "a and b must be nonzero"
    ValueError: a and b must be nonzero
**********************************************************************
<SNIP>
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 18:52:25

Ok, this fixes the first problem:

```
diff -r c0c80b6d1261 sage/algebras/quaternion_algebra_element.pyx
--- a/sage/algebras/quaternion_algebra_element.pyx      Wed Mar 04 11:54:38 2009 -0800
+++ b/sage/algebras/quaternion_algebra_element.pyx      Tue Mar 10 11:51:54 2009 -0700
`@``@` -320,6 +320,7 `@``@`
             sage: type(theta)
             <type 'sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
             sage: 1/Q(0)
+            Traceback (most recent call last):
             ...
             ZeroDivisionError: rational division by zero
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 19:14:56

trac_5409-part12-reviewer.patch makes the doctest pass again. It is only a diff since I did not want to commit anything to that tree. Most of the changes are trivial. Mike Hansen also pointed out some of the fixes :)

I am somehow under the impression John's patch was not the final one or somehow incomplete.

Cheers,

Michael


---

Comment by was created at 2009-03-10 19:41:14

positive review (I fixed the other two small mistakes from John Voight's patch in Mabshoff's tree).


---

Attachment


---

Comment by mabshoff created at 2009-03-10 19:52:49

Merged 12 patches in Sage 3.4.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 19:52:49

Resolution: fixed
