# Issue 6904: change ring broken over QQ and GF(2)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-08 20:13:34

Assignee: was


```
sage: matrix(QQ,2,[1,0,0,1]).change_ring(GF(2)) - 1
Traceback (most recent call last):
...
RuntimeError
}}


---

Comment by was created at 2010-02-18 23:45:15

Here's another bug that bit me while doing research today and might be caused by the same problem:

```
sage: a = matrix(QQ,22,[0, 0, 0, -1, 1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 1, 0, 1, 0, 0, 0, -1, 1, 0, -1, 0, 1, 0, 0, -1, 0, -2, 1, -1, -1, 1,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0,
0, -1, 1, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 0,
-1, 1, 0, 1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, -1, 0,
0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0,
0, 1, -1, 0, 1, 0, -1, 0, 1, 1, 0, 2, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0,
1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, 0, 0, 0, 0, 1, -2, 1, 1, 0,
0, 0, 0, 0, 1, -1, -1, 0, -1, 0, -1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1,
0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, -1, 1, 0, 0, 0, 0,
0, 0, 1, -1, -1, 0, 0, -1, -1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1, 0,
-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0,
0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 1, 0, 0,
0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0,
0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, -1, 1, 0, -1, 0, 0, 0, 0, 0,
0, -2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, -1, 1, 0, -1, -1, 1, 0, 0, 0, 0,
-2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, 0, -1,
0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0,
0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0,
1]).change_ring(GF(2))

sage: a^21
Traceback (click to the left of this block for traceback)
...
TypeError: Cannot convert
sage.matrix.matrix_modn_dense.Matrix_modn_dense to
sage.matrix.matrix_mod2_dense.Matrix_mod2_dense

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_79.py", line 9, in <module>
    open("___code___.py","w").write("# -*- coding: utf-8 -*-\n" + _support_.preparse_worksheet_cell(base64.b64decode("diA9IFsoYV5pKS5saXN0KCkgZm9yIGkgaW4gWzEuLjIxXV0="),globals())+"\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpVclvdc/___code___.py", line 3, in <module>
    v = [(a**i).list() for i in (ellipsis_range(_sage_const_1 ,Ellipsis,_sage_const_21 ))]
  File "", line 1, in <module>
    
  File "matrix0.pyx", line 3893, in sage.matrix.matrix0.Matrix.__pow__ (sage/matrix/matrix0.c:21527)
  File "element.pyx", line 1409, in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:11201)
  File "element.pyx", line 3264, in sage.structure.element.generic_power_c (sage/structure/element.c:23714)
  File "element.pyx", line 2134, in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:14292)
  File "matrix_mod2_dense.pyx", line 645, in sage.matrix.matrix_mod2_dense.Matrix_mod2_dense._matrix_times_matrix_ (sage/matrix/matrix_mod2_dense.c:5144)
TypeError: Cannot convert sage.matrix.matrix_modn_dense.Matrix_modn_dense to sage.matrix.matrix_mod2_dense.Matrix_mod2_dense

```



---

Comment by was created at 2010-07-07 06:26:25

Amazingly, this is still broken in Sage-4.5.alpha4!

```

wstein`@`sage:~/build/sage-4.5.alpha4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: matrix(QQ,2,[1,0,0,1]).change_ring(GF(2)) - 1
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |
| Type notebook() for the GUI, and license() for information.        |
/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/<ipython console> in <module>()

/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()

/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6123)()

/mnt/usb1/scratch/wstein/build/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11005)()

RuntimeError: 
sage: 
```



---

Comment by wjp created at 2010-07-07 09:01:28

This is occurring in `Matrix_modn_dense._sub_()`. It gets called with 'right' of type Matrix_mod2_dense, but casts it to Matrix_modn_dense internally. (I haven't looked at all at why this is happening and if it should be happening.)


---

Comment by cpernet created at 2010-07-07 13:09:03

Proposed fix for the bug #6904


---

Comment by cpernet created at 2010-07-07 13:12:16

Changing status from new to needs_review.


---

Attachment

The problem is due to the fact that with p=2, the change_ring() method  should not create a matrix_modn_dense but a matrix_mod2_dense (wrapping m4ri).

I added this special case.

Meanwhile, it revealed a conflict in the declaration of ONE (in libs/pari/gens.pyx, and in m4ri). So I renammed the macros in pari/gens.*.


---

Comment by cpernet created at 2010-07-07 13:13:53

Changing assignee from was to cpernet.


---

Comment by was created at 2010-07-08 12:33:23

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-07-08 12:33:23

Two changes needed:

   * Add the example as a doctest.

   * Change _mod_int_c(self, mod_int p) so it calls _mod_two if p=2.


---

Attachment

corrected version following the remarks by was


---

Comment by cpernet created at 2010-07-08 13:02:54

fix a typo in the docstring


---

Comment by was created at 2010-07-08 13:03:45

Changing status from needs_work to positive_review.


---

Attachment


---

Comment by mpatel created at 2010-07-20 08:19:43

I've filled in the Author(s) and Reviewer(s) fields.  If I'm wrong, please correct them.


---

Comment by mpatel created at 2010-07-20 08:19:43

Resolution: fixed
