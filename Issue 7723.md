# Issue 7723: Sparse matrices for double fields

Issue created by migration from https://trac.sagemath.org/ticket/7723

Original creator: dagss

Original creation time: 2009-12-17 13:47:31

Assignee: jkantor

Here's the beginnings of my work on sparse double matrices.

This is based on 4.3.rc0. Note that I have *not* run the entire Sage test suite,
only tests in the matrix package. I'm happy to run the entire suite once I know
the final revision this will be rebased to, but 4.3.rc0 produces a few test
failures in itself (=noise I'm not bothering with for the moment).

There are three patches, which should be applied and reviewed in this order:

 - generic_multiply lets one override matrix multiplication with
   different parents.  This is in a seperate patch because it changes
   structure/element.pxd, causing a big recompile.

 - double_sparse is the main new classes

 - coo_format changes the matrix constructor to accept "coo=..." (see docstring
   in patch)

More comments:

 - I will not introduce seperate classes for real and complex -- there
   will be other subclasses (Hermitian, strictly-diagonal etc.) and I
   don't want to double the size of the hierarchy. There are other
   (and better) ways to get efficient getitem/setitem without a speed
   penalty (such as introducing a seperate ItemAccessor protocol/class
   -- though for sparse matrices an if-test won't matter either).

 - Once this is accepted (and I have a general feel for what I do
   right and wrong) I hope to continue with solvers etc. (as I scratch my itches).




---

Comment by dagss created at 2009-12-17 13:50:07

Changing status from new to needs_review.


---

Comment by dagss created at 2009-12-17 13:50:50

Changing component from numerical to linear algebra.


---

Attachment


---

Attachment


---

Comment by was created at 2009-12-19 20:32:38

Changing status from needs_review to needs_work.


---

Attachment

REFEREE REPORT:

* trac_7723-generic_multiply.patch: 

Looks good, except there is a missing word "have" in this documentation:

```
3485	        The matrices should both the same base ring and either both 
3486	        should be dense or both sparse. 
```

This doesn't cause any doctest failures, and factoring this code out is a good idea. 

* trac_7723-double_sparse.patch

Looks good.


* trac_7723-coo_format.patch 

This causes a bunch of doctest failures:


```
wstein@sage:~/build/referee/sage-4.3.rc0$         sage -t  devel/sage/sage/matrix/matrix_integer_2x2.pyx # 5 doctests failed
sage -t  "devel/sage/sage/matrix/matrix_integer_2x2.pyx"    
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 266:
    sage: m.__iter__()
Expected:
    <listiterator object at ...>
Got:
    <generator object row_iterator at 0x3ddab90>
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 397:
    sage: m.__invert__unit()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[4]>", line 1, in <module>
        m.__invert__unit()###line 397:
    sage: m.__invert__unit()
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 400:
    sage: type(m.__invert__unit())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[5]>", line 1, in <module>
        type(m.__invert__unit())###line 400:
    sage: type(m.__invert__unit())
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 407:
    sage: m.__invert__unit() == m^-1
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[8]>", line 1, in <module>
        m.__invert__unit() == m**-Integer(1)###line 407:
    sage: m.__invert__unit() == m^-1
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
File "/scratch/wstein/build/referee/sage-4.3.rc0/devel/sage/sage/matrix/matrix_integer_2x2.pyx", line 409:
    sage: M([2,0,0,2]).__invert__unit()
Expected:
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Not a unit!
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/referee/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[9]>", line 1, in <module>
        M([Integer(2),Integer(0),Integer(0),Integer(2)]).__invert__unit()###line 409:
    sage: M([2,0,0,2]).__invert__unit()
    AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_de' object has no attribute '__invert__unit'
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_13
   4 of  10 in __main__.example_19
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_matrix_integer_2x2.py
         [1.5 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/matrix/matrix_integer_2x2.pyx"
Total time for all tests: 1.5 seconds
```



I noticed a *massive* performance regression as a result of your patches:

```
OLD SAGE:
sage: s = random_matrix(RDF,100)
sage: time t =s*s
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.15 s


WITH YOUR PATCHES:
sage: s = random_matrix(RDF,100)
sage: time t =s*s
CPU times: user 0.91 s, sys: 0.00 s, total: 0.91 s
Wall time: 0.91 s
```


Ouch.  These are both dense matrices.  There must be something that got seriously messed up with re-factoring?

* Why is there a backslash here in `matrix_double_sparse.pyx`:

```
        either as a single list of length ``nrows\*ncols``, or as a 
```



---

Overall I'm very happy and excited about this patch!!  I'm really, really glad you're working on this, and would like to do anything I can to encourage this.  It is critically valuable to the Sage project to get much better numerical sparse matrix support.


---

Comment by dagss created at 2009-12-21 11:00:07

Changing status from needs_work to needs_review.


---

Comment by dagss created at 2009-12-21 11:00:07

The attached patch should address the above issues (I guess this should have been folded into the original patches? But I hope this is OK, I still have some way to go before getting to terms with using Mercurial/MQ in a patch-review process.)


---

Attachment


---

Comment by was created at 2009-12-21 18:21:53

Replying to [comment:4 dagss]:
> The attached patch should address the above issues (I guess this should have been folded into the original patches? But I hope this is OK, I still have some way to go before getting to terms with using Mercurial/MQ in a patch-review process.)


I'm really glad you *didn't* fold this into the original patch, since it makes it much easier for me to see what you changed.


---

Comment by was created at 2009-12-21 18:28:03

Looks great!


---

Comment by was created at 2009-12-21 18:28:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-04 02:10:55

I get failures applying trac_7723-coo_format.patch


---

Comment by dagss created at 2010-01-04 21:42:59

I can't reproduce this, applying on 4.3.1.alpha0.

Did you apply them in the wrong order? Apparently I messed up the order when uploading, sorry. The patches _must_ be applied in this order:


```
trac_7723-generic_multiply.patch
trac_7723-double_sparse.patch
trac_7723-coo_format.patch
trac_7723-fixround1.patch
```



---

Comment by mhansen created at 2010-01-04 21:49:15

Ahh, thanks.  I was doing it in the wrong order.


---

Comment by rlm created at 2010-01-13 10:47:27

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 10:47:27


```
The following tests failed:

        sage -t -long devel/sage-main/sage/matrix/constructor.py # 1 doctests failed
        sage -t -long devel/sage-main/sage/categories/action.pyx # Segfault
```



---

Comment by dagss created at 2010-02-04 08:01:06

Ouch.

I have not idea when I can get back to this at the moment. Basically what has happened is that I bit the bullet and implemented my own numerical matrix class hierarchy which is usable without Sage (but loosely modeled after it). That ended up giving me the results I needed much faster...

The long-term goal is to perhaps try to merge this back into Sage, however as there's no real benefit for my own work in doing that I don't really know if or when.

(Anyone who finds this ticket because they need this functionality are welcome to send me an email and check the status.)
