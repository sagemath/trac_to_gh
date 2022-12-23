# Issue 4306: bug in supersingular module

Issue created by migration from https://trac.sagemath.org/ticket/4306

Original creator: was

Original creation time: 2008-10-16 09:17:19

Assignee: craigcitro

CC:  davidloeffler


```
sage: X = SupersingularModule(389)
sage: X
Module of supersingular points on X_0(1)/F_389 over Integer Ring
sage: X.basis()
Traceback (most recent call last):
...
AttributeError: 'SupersingularModule' object has no attribute 'free_module'
```



---

Comment by was created at 2010-01-19 13:08:54

Changing status from new to needs_review.


---

Comment by was created at 2010-01-19 13:08:54

The attached patch doesn't implement elements of supersingular modules -- that isn't implemented yet at all!  But it implements a free_module() method so that now the above input results in a NotImplementedError, which is the right behavior when something isn't implemented.


---

Attachment


---

Comment by AlexGhitza created at 2010-01-23 02:02:41

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2010-01-23 02:02:41

With the patch applied, I'm getting


```
sage -t -long "modular/ssmod/ssmod.py"                      
**********************************************************************
File "/opt/sage-4.3.1/devel/sage-main/sage/modular/ssmod/ssmod.py", line 38:
    sage: t = X.T(2).matrix()            # long time (but still less than a minute!)
Exception raised:
    Traceback (most recent call last):
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        t = X.T(Integer(2)).matrix()            # long time (but still less than a minute!)###line 38:
    sage: t = X.T(2).matrix()            # long time (but still less than a minute!)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 1343, in T
        return self.hecke_operator(n)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 1330, in hecke_operator
        return self.hecke_algebra().hecke_operator(n)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 325, in hecke_algebra
        self.__hecke_algebra = algebra.HeckeAlgebra(self)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/algebra.py", line 136, in HeckeAlgebra
        k = (M, M.basis_matrix())
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 828, in basis_matrix
        return self.free_module().basis_matrix()
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modules/free_module.py", line 2087, in basis_matrix
        A = MAT.identity_matrix()
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py", line 944, in identity_matrix
        A = self(0)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py", line 395, in __call__
        return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py", line 1087, in matrix
        return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)
      File "matrix_rational_dense.pyx", line 149, in sage.matrix.matrix_rational_dense.Matrix_rational_dense.__cinit__ (sage/matrix/matrix_rational_dense.c:4931)
    MemoryError: out of memory allocating a matrix
**********************************************************************
File "/opt/sage-4.3.1/devel/sage-main/sage/modular/ssmod/ssmod.py", line 39:
    sage: t.nrows()                      # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        t.nrows()                      # long time###line 39:
    sage: t.nrows()                      # long time
    NameError: name 't' is not defined
**********************************************************************
1 items had failures:
   2 of  18 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_ssmod.py
	 [21.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "modular/ssmod/ssmod.py"
Total time for all tests: 21.4 seconds
```



---

Comment by AlexGhitza created at 2013-07-22 17:26:15

OK, it seems like the underlying issue in the last comment has disappeared.  With sage-5.10:


```
sage: X = SupersingularModule(389)
sage: X.basis()                   
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-2-30f7d3cb5e51> in <module>()
----> 1 X.basis()

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/modular/hecke/module.pyc in basis(self)
    865             return self.__basis
    866         except AttributeError:
--> 867             self.__basis = self.gens()
    868         return self.__basis
    869 

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:3292)()

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/modular/hecke/module.pyc in gen(self, n)
   1342             (1,17)
   1343         """
-> 1344         return self(self.free_module().gen(n))
   1345 
   1346     def hecke_matrix(self, n):

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7916)()

NotImplementedError: 
```


I am adding a reviewer patch that doctests this.


---

Attachment


---

Comment by AlexGhitza created at 2013-07-22 17:29:13

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2013-07-22 17:29:13

Changing keywords from "" to "sd51, beginner".


---

Comment by davidloeffler created at 2013-07-25 11:06:56

Alex's patch with a better commit message


---

Attachment

I edited Alex's patch to add a better commit message. Other than that I think this is fine.


---

Comment by davidloeffler created at 2013-07-25 11:08:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-19 06:45:33

Resolution: fixed
