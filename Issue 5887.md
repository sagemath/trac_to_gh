# Issue 5887: major bug in images of homorphisms of R-modules

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-24 05:01:35

Assignee: was

The image method on homomorphisms of R-modules is completely wrong.  Here is a simple example that illustrates this serious bug.  I start with V, which is a submodule of index 2 in `ZZ^2`, and define the identity map from V to V.  The image is `ZZ^2`, which is totally wrong.  I think the problem is that the image is being computed over the fraction field. 

```
sage: V = (ZZ^2).span([[1,2],[3,4]])
sage: phi = V.Hom(V)(identity_matrix(ZZ,2))
sage: phi(V.0) == V.0
True
sage: phi(V.1) == V.1
True
sage: phi.image()
Free module of degree 2 and rank 2 over Integer Ring
Echelon basis matrix:
[1 0]
[0 1]
sage: phi.image() == V
False
```


In fact, the image isn't even contained in the codomain!

```
sage: phi.image() == phi.codomain()
False
sage: phi.image().is_submodule( phi.codomain() )
False
```



---

Comment by was created at 2009-04-24 06:51:30

There is one doctest failure (in the whole tree), so this isn't ready for review yet:

```
wstein`@`sage:~/build/sage-3.4.1$ ./sage -t --long devel/sage/sage/modular/abvar/morphism.py
sage -t --long "devel/sage/sage/modular/abvar/morphism.py"  
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1/devel/sage/sage/modular/abvar/morphism.py", line 433:
    sage: (t2 - 1)(C)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[26]>", line 1, in <module>
        (t2 - Integer(1))(C)###line 433:
    sage: (t2 - 1)(C)
      File "/scratch/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py", line 337, in __sub__
        return self.parent()(self.matrix() - other.matrix())
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'matrix'
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1/devel/sage/sage/modular/abvar/morphism.py", line 148:
    sage: (t-1).cokernel()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        (t-Integer(1)).cokernel()###line 148:
    sage: (t-1).cokernel()
      File "/scratch/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py", line 337, in __sub__
        return self.parent()(self.matrix() - other.matrix())
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'matrix'
**********************************************************************
2 items had failures:
   1 of  31 in __main__.example_10
   1 of   7 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1/tmp/.doctest_morphism.py
	 [3.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --long "devel/sage/sage/modular/abvar/morphism.py"
Total time for all tests: 3.4 seconds
```



---

Attachment

OK, I fixed the patch.


---

Comment by AlexGhitza created at 2009-04-30 09:52:14

Is this supposed to apply cleanly to sage-3.4.2.alpha0?  I can't seem to be able to do that:


```
[aghitza`@`cartan sage]$ hg qpush
applying trac_5887.patch
patching file sage/modules/matrix_morphism.py
Hunk #12 FAILED at 555
Hunk #13 FAILED at 576
2 out of 15 hunks FAILED -- saving rejects to file sage/modules/matrix_morphism.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_5887.patch
```



---

Comment by mabshoff created at 2009-05-01 01:39:33

Replying to [comment:5 AlexGhitza]:
> Is this supposed to apply cleanly to sage-3.4.2.alpha0?  I can't seem to be able to do that:

Well, given that #5882 also touches that file (but this ticket is a requirement) I think that the current situation is somewhat messed up. In the end I would not be surprised if this patch gets folded into the other ticket.

Cheers,

Michael


---

Comment by was created at 2009-05-02 08:39:48

this is rebased against 3.4.2.rc0


---

Attachment

This isn't being folded into #5882, and I do not view the "current situation" as at all messed up. There are three tickets: 
    #5886, #5887, and #5882.  

#5886 is first, then #5887, then finally #5882.   

I just applied #5886 and this rebased #5887 to my 3.4.2.rc0 tree on sage.math, and "sage -t devel/sage/sage" passes all tests.


---

Comment by AlexGhitza created at 2009-05-02 12:05:11

Looks good!  I have only a few minor issues, in `matrix_morphism.py`:

 * In the method `__invert__()`, the second example says "Check that a certain non-invertible morphism isn't invertible", but the error that's thrown says "TypeError: no conversion of this rational to integer".  It would be nicer if the error said something like "This morphism is not invertible" instead.

 * There are a couple of typos in the docstring for `decomposition()`: on the (new) line 383, "invariants" should be "invariant", and on line 385, "fro" should be "for".

 * On line 511, "Verify that trac 5887 is fixed" looks out of place.  Did you want to put it before the previous doctest block?


---

Attachment


---

Comment by mabshoff created at 2009-05-04 16:13:24

Merged  trac_5887-rebased_3.4.2.rc0.2.patch and trac_5887-part2-referee_comments.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 16:13:24

Resolution: fixed
