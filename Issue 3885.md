# Issue 3885: [with patch, needs review and discussion] Bug in free module __call__ method

Issue created by migration from https://trac.sagemath.org/ticket/3885

Original creator: craigcitro

Original creation time: 2008-08-17 21:58:14

Assignee: craigcitro

Salman Butt ran into the following bug:


```
sage: V = QQ**2
sage: W = V.subspace([[1,2]])
sage: W([2,1])
(2, 1)
```


Fix is attached, but the fact that you can still do the following is possibly worrisome:


```
sage: V = QQ**2
sage: W = V.subspace([[1,2]])
sage: W([2,1], check=False) in W
True
```


I just started a sage-devel thread to see if we should also stop this, i.e. not let users shoot themselves in the foot so easily.


---

Attachment


---

Comment by craigcitro created at 2008-08-17 22:07:57

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-08-17 22:07:57

Credit for this patch goes to Martin Albrecht and myself for the fix. (Sorry I didn't mention that above, Martin. :) )


---

Comment by mhansen created at 2008-08-29 01:20:22

Looks good to me.


---

Comment by mabshoff created at 2008-08-29 02:09:56

With the patch applied I am seeing the following doctest failure:

```
sage -t -long devel/sage/sage/modular/modsym/ambient.py     **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/tmp/ambient.py", line 1027:
    sage: M.factorization()                    # long time (about 8 seconds)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[6]>", line 1, in <module>
        M.factorization()                    # long time (about 8 seconds)###line 1027:
    sage: M.factorization()                    # long time (about 8 seconds)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 1143, in factorization
        for E in self.eisenstein_submodule().decomposition(anemic=True):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 582, in decomposition
        X = t.decomposition_of_subspace(U[i], is_diagonalizable=is_diagonalizable)
      File "matrix2.pyx", line 2169, in sage.matrix.matrix2.Matrix.decomposition_of_subspace (sage/matrix/matrix2.c:13376)
      File "matrix2.pyx", line 2255, in sage.matrix.matrix2.Matrix.restrict (sage/matrix/matrix2.c:14068)
      File "element.pyx", line 1899, in sage.structure.element.Vector.__mul__ (sage/structure/element.c:11232)
      File "coerce.pyx", line 634, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6030)
      File "action.pyx", line 195, in sage.categories.action.PrecomposedAction._call_ (sage/categories/action.c:3506)
      File "morphism.pyx", line 88, in sage.categories.morphism.CallMorphism._call_ (sage/categories/morphism.c:2309)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/modules/free_module.py", line 684, in __call__
        raise ValueError, "element (= %s) is not in free module"%(x,)
    ValueError: element (= [0, 1, 0, -1, -zeta3 + 1, 1/2*zeta3 + 1, zeta3 + 1/2]) is not in free module
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_20
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/tmp/.doctest_ambient.py
         [10.9 s]
exit code: 1024
```


Cheers,

Michael


---

Comment by craigcitro created at 2008-09-02 06:40:48

Yep, thank god for doctests. This was really hard to track down: elements of `CyclotomicField(3)` were getting created whose print representation was the same, but whose internal representation was different. (Even harder was finding out that was the problem.) The attached patch corrects the problem. I don't have a current alpha tree to test this against, so let me know if anything still breaks.


---

Attachment

With Craig's second patch all doctests pass. Somebody more knowledgeable in this area of the code please check that this is the correct fix.

Cheers,

Michael


---

Comment by robertwb created at 2008-09-02 17:28:48

That looks good to me.


---

Comment by mabshoff created at 2008-09-03 00:09:49

Merged both patches in Sage 3.1.2.rc0. Nice work Craig :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-03 00:09:49

Resolution: fixed
