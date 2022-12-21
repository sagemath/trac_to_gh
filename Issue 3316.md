# Issue 3316: Fix a bug and improve documentation in jordan_form

Issue created by migration from Trac.

Original creator: pdenapo

Original creation time: 2008-05-27 23:36:32

Assignee: was


I submit a patch that fixes a bug in jordan_form method in /matrix/matrix2.pyx


```
sage: A=Matrix(CDF,[[1,-2],[2,-1]])
sage: A.jordan_form(transformation=True)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/media/hda2/pablo.new_home/sage/sage-3.0.2/<ipython console> in <module>()

/media/hda2/pablo.new_home/sage/sage-3.0.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20606)()

AttributeError: 'NoneType' object has no attribute 'is_exact'

}}} 

(second issue in ticket #3249)

After this fix, the behavior will be:

{{{

sage: A.jordan_form(transformation=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/media/hda2/pablo.new_home/sage/sage-3.0.2/<ipython console> in <module>()

/media/hda2/pablo.new_home/sage/sage-3.0.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20625)()

ValueError: cannot compute the transformation matrix due to lack of precision

}}}

that it is what it is intendend in the code.

(The bug was that base_ring.is_exact() was used, instead of self.base_ring().is_exact().

Besides that, this patch improves the documentation of this method, by adding
"Transformation" to the list of INPUT parameters


---

Comment by pdenapo created at 2008-05-27 23:37:30

patch for fixing a bug and improving the documentation in jordan_form


---

Attachment


---

Comment by mabshoff created at 2008-06-11 04:36:08

There are some small doctest issues with the patch applied:

```
sage -t -long devel/sage/sage/matrix/matrix2.pyx            
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/matrix2.py", line 3640:
    sage: jf, p = b.jordan_form(RealField(15), transformation=True)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: cannot compute the transformation matrix due to lack of precision
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_71[12]>", line 1, in <module>
        jf, p = b.jordan_form(RealField(Integer(15)), transformation=True)###line 3640:
    sage: jf, p = b.jordan_form(RealField(15), transformation=True)
      File "matrix2.pyx", line 3714, in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20649)
    ValueError: cannot compute the basis of the Jordan block of size 1 with eigenvalue -1.348
**********************************************************************
1 items had failures:
   1 of  23 in __main__.example_71
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/.doctest_matrix2.py
	 [7.8 s]
exit code: 1024
```


Cheers,

Michael


---

Attachment

a new patch (this time correct, I hope)


---

Comment by pdenapo created at 2008-06-12 02:15:50

My previous patch was wrong (in the logic). I'm submitting a new version that is correct (I hope). I've checked it passes the doctest in matrix2.pyx


---

Comment by mabshoff created at 2008-09-26 04:47:40

Merged jordan_form_fixes_correction.patch in Sage 3.1.3.alpha2. 

Pablo: please make sure to post patches and not diffs in the future.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 04:47:40

Resolution: fixed
