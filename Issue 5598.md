# Issue 5598: allow post-creation (pre-use) declaration of coercions

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-03-24 05:12:18

Assignee: robertwb

CC:  nthiery

One can now do 

a = A()
mor = [morphism from X to A]
a.register_coercion(mor)

This works as long as coercion has not yet been used (otherwise information cached (both here and elsewhere) becomes invalid).


---

Attachment

Depends on #5597.


---

Comment by robertwb created at 2009-03-24 05:21:37

One can now do 


```
sage: A = SomeParent()
sage: mor = [morphism from X to A]
sage: A.register_coercion(mor)
```


This works as long as coercion has not yet been used (otherwise information cached (both here and elsewhere) becomes invalid).


---

Comment by robertwb created at 2009-03-24 10:49:40

Actually, though I wrote it on top of #5597, there's probably not a dependance. Note that I don't have any doctests yet (as it's completely unused functionality at this point).


---

Comment by was created at 2009-04-12 05:04:49

> Note that I don't have any doctests yet (as it's completely unused 
> functionality at this point). 

Hence I'm physically incapable of giving this a positive review.  Sorry.


---

Attachment

I have been using this patch (or actually a plain python version of it; see the sage-combinat patch queue) relatively intensively, and it does its job well. However it's hard to extract any interesting unitary test from those uses, since they all rely on the rest of the category stuff.

I have just attached a stupid test instead ... It just plays with register_coercion, but should be easy to adapt to the others.

Btw: robert: would it be possible to have register_coercion just raise a warning if coercions have readily been used? There are cases where it can be handy to abuse the system a bit from the interpreter.


---

Comment by robertwb created at 2009-04-14 11:09:20

Thanks for the tests. In retrospect, sometimes very simple tests like this are best at showing exactly what's going on. 

As for warnings vs. errors, yes it's possible, but I am strongly against it. If you need to abuse it, you can do so from Cython (or even write a spyx file that allows you to do so from the interpreter). 

There was talk about asserting coercions within contexts, but no one's gotten around to implementing them yet.


---

Comment by nthiery created at 2009-04-14 16:52:46

Hi Robert,

> Thanks for the tests. In retrospect, sometimes very simple tests like this are best at showing exactly what's going on. 

Yep.

The construction of the parents and morphisms in this test are still ugly, though. Both ought to be essentially one-liners. Hopefuly things will be nicer when the category patch will be in.

> As for warnings vs. errors, yes it's possible, but I am strongly against it. If you need to abuse it, you can > do so from Cython (or even write a spyx file that allows you to do so from the interpreter). 

My typical (ab)use case is someone constructing a couple parents in the interpreter, playing with them, and suddenly thinking "oh, but wouldn't all be natural if I added a coercion there?". The user will give it a try if this is trivial to do. Otherwise he won't and that's too bad.

Btw: your patch changes the datastructure of parents to add the cython attribute `_coercions_used`. How does this work with unpickling old pickles? That is, will _coercions_used be set to an appropriate value?

> 
> There was talk about asserting coercions within contexts, but no one's gotten around to implementing them yet.


---

Comment by ncalexan created at 2009-05-06 03:15:39

This is all kinds of awesome, and yet totally useless.  For example, the following fails:


```
x = GF(3)['x'].0
K.<a> = GF(3^2, 'a', modulus=x^2+1)
L.<b> = GF(3^2, 'b', modulus=x^2 + x - 1)

L_into_K = L.hom([a - 2], K, check=False)
K.register_coercion(L_into_K)
```


Why?  Because the `a-2` has used the coercion mechanism for K.  It will be essentially impossible to construct morphisms that are mathematically interesting without using coercion at some point.

What is to be done?  I have no great ideas.  Personally I would be happy with a flag to `register_coercion` that "broke the links" of the coercion graph, or even tried to `reset_cache()` on the coercion_model.  Notice that I tried this, but it doesn't work, because `reset_cache` doesn't twiddle the flag on each parent.  (That's a bug, in my opinion.)


---

Comment by ncalexan created at 2009-05-06 06:10:57

Apply both `5598-` patches.  My fixes make actions work (they're still broken pretty hard in parent_old, but they work here) and test this code in a non-combinat tree.  In order to make this work I include an ugly hack.

robertwb, this badly needs documentation; it really can't be accepted without *something*.


---

Comment by robertwb created at 2009-05-06 06:14:50

Yes, I just haven't had time to work on any coercion-related stuff for a while. I'll be attacking issues like this during Sage days.


---

Attachment


---

Comment by ncalexan created at 2009-05-08 23:05:15

Updated `fixes` patch includes a few line of documentation.  robertwb, this is ready for you to review.


---

Comment by robertwb created at 2009-05-14 23:00:39

5598-ncalexan-fixes-and-tests.patch seems malformed, could you try recreating this patch?


---

Attachment


---

Attachment

Ah, the mystery of the malformed patches.  hg export -o *DOESN'T* overwrite an existing file, it appends!  I think this is totally wrong, but I can work around it.  This has been biting me for weeks, I now realize.  Anyway, only tests.3.patch should be applied.


---

Attachment

I made a patch out of test-coercion. Apply, in order

 * 5598-coerce-declare.patch
 * 5598-ncalexan-fixes-and-tests.3.patch
 * 5598-test-coercion.patch (1.9 KB)

I give the tests/documentation a positive review, if someone is willing to give a +1 on the original patch we can get this ticket in.


---

Comment by ncalexan created at 2009-05-23 06:54:39

It's not perfect but it's better than what was there before -- and doctested more than it was before!


---

Comment by nthiery created at 2009-05-23 07:12:16

Just a note: the added test adds a dependency on #5967. The later has a positive review, but Michael asked for a confirmation from a non sage-combinat person. Robert told me he would do this shortly.


---

Comment by mhansen created at 2009-06-01 00:47:13

I merged 


```
5598-coerce-declare.patch
5598-ncalexan-fixes-and-tests.3.patch
5598-test-coercion.patch
```


and got the following failures:


```
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 863:
    sage: K.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[5]>", line 1, in <module>
        K.unset_coercions_used()###line 863:
    sage: K.unset_coercions_used()
    AttributeError: 'PolynomialRing_integral_domain' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 864:
    sage: K.register_coercion(L_into_K)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[6]>", line 1, in <module>
        K.register_coercion(L_into_K)###line 864:
    sage: K.register_coercion(L_into_K)
      File "parent.pyx", line 853, in sage.structure.parent.Parent.register_coercion (sage/structure/parent.c:7450)
        cpdef register_coercion(self, mor):
      File "parent.pyx", line 878, in sage.structure.parent.Parent.register_coercion (sage/structure/parent.c:7239)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 866:
    sage: K(0) + b
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[7]>", line 1, in <module>
        K(Integer(0)) + b###line 866:
    sage: K(0) + b
      File "element.pyx", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in a over Integer Ring' and 'Univariate Polynomial Ring in b over Integer Ring'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 868:
    sage: a + b
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[8]>", line 1, in <module>
        a + b###line 868:
    sage: a + b
      File "element.pyx", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in a over Integer Ring' and 'Univariate Polynomial Ring in b over Integer Ring'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 870:
    sage: K(b) # check that convert calls coerce first; normally this is just a
Expected:
    -a
Got:
    a
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 873:
    sage: L(0) + a in K # this goes through the coercion mechanism of K
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[10]>", line 1, in <module>
        L(Integer(0)) + a in K # this goes through the coercion mechanism of K###line 873:
    sage: L(0) + a in K # this goes through the coercion mechanism of K
      File "element.pyx", line 729, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6533)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6589)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in b over Integer Ring' and 'Univariate Polynomial Ring in a over Integer Ring'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 931:
    sage: R.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[12]>", line 1, in <module>
        R.unset_coercions_used()###line 931:
    sage: R.unset_coercions_used()
    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 945:
    sage: R.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[16]>", line 1, in <module>
        R.unset_coercions_used()###line 945:
    sage: R.unset_coercions_used()
    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 975:
    sage: K.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[5]>", line 1, in <module>
        K.unset_coercions_used()###line 975:
    sage: K.unset_coercions_used()
    AttributeError: 'PolynomialRing_integral_domain' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 976:
    sage: K.register_conversion(M_into_K)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[6]>", line 1, in <module>
        K.register_conversion(M_into_K)###line 976:
    sage: K.register_conversion(M_into_K)
      File "parent.pyx", line 965, in sage.structure.parent.Parent.register_conversion (sage/structure/parent.c:8015)
        cpdef register_conversion(self, mor):
      File "parent.pyx", line 985, in sage.structure.parent.Parent.register_conversion (sage/structure/parent.c:7825)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1016:
    sage: K.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[7]>", line 1, in <module>
        K.unset_coercions_used()###line 1016:
    sage: K.unset_coercions_used()
    AttributeError: 'NumberField_quadratic' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1017:
    sage: K.register_embedding(K_into_MS)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[8]>", line 1, in <module>
        K.register_embedding(K_into_MS)###line 1017:
    sage: K.register_embedding(K_into_MS)
      File "parent.pyx", line 1000, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8246)
        cpdef register_embedding(self, embedding):
      File "parent.pyx", line 1039, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8084)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1022:
    sage: L.unset_coercions_used()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[12]>", line 1, in <module>
        L.unset_coercions_used()###line 1022:
    sage: L.unset_coercions_used()
    AttributeError: 'NumberField_quadratic' object has no attribute 'unset_coercions_used'
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1023:
    sage: L.register_embedding(L_into_MS)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[13]>", line 1, in <module>
        L.register_embedding(L_into_MS)###line 1023:
    sage: L.register_embedding(L_into_MS)
      File "parent.pyx", line 1000, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8246)
        cpdef register_embedding(self, embedding):
      File "parent.pyx", line 1039, in sage.structure.parent.Parent.register_embedding (sage/structure/parent.c:8084)
        assert not self._coercions_used, "coercions must all be registered up before use"
    AssertionError: coercions must all be registered up before use
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1025:
    sage: K.coerce_embedding()(a)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[14]>", line 1, in <module>
        K.coerce_embedding()(a)###line 1025:
    sage: K.coerce_embedding()(a)
    TypeError: 'NoneType' object is not callable
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1028:
    sage: L.coerce_embedding()(b)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[15]>", line 1, in <module>
        L.coerce_embedding()(b)###line 1028:
    sage: L.coerce_embedding()(b)
    TypeError: 'NoneType' object is not callable
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1032:
    sage: a.matrix() * b
Expected:
    [-272118       0]
    [      0    -462]
Got:
    [           0      b521155]
    [-462*b521155            0]
**********************************************************************
File "/scratch/mhansen/release/4.0.1/alpha0/sage-4.0.1.alpha0/devel/sage-main/sage/structure/parent.pyx", line 1035:
    sage: a * b.matrix()
Expected:
    [-272118       0]
    [      0    -462]
Got:
    [              0         a161099]
    [-272118*a161099               0]
**********************************************************************
4 items had failures:
   6 of  12 in __main__.example_21
   2 of  19 in __main__.example_22
   2 of   9 in __main__.example_23
   8 of  18 in __main__.example_24
***Test Failed*** 18 failures.
```



---

Attachment

I've attached trac_5598.patch which folds the above three together and is rebased for 4.2.  I believe this should pass all tests.


---

Comment by mhansen created at 2009-10-19 13:22:04

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-10-19 13:22:15

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-19 13:22:15

The faliures above were just because in the tests "unset_coercions_used" should have been "_unset_coercions_used".

All tests pass with trac_5598.patch.


---

Comment by mhansen created at 2009-10-19 13:23:22

Resolution: fixed
