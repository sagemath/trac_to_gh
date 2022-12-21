# Issue 9747: assigment to 1x1 submatrices specified by slices fails

Issue created by migration from Trac.

Original creator: phil

Original creation time: 2010-08-14 15:11:51

Assignee: jason, was

CC:  jason

Keywords: matrix assignment slicing __setitem__

Assigment to 1x1 submatrices specified by slices fails:

## Example

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A=matrix([[1,2],[3,4]])
sage: B=matrix([[1,3],[5,7]])
sage: A[1:2,1:2]=B[1:2,1:2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/phil/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5926)()

/Applications/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:7044)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6807)()

TypeError: unable to coerce <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'> to an integer

```

The problem seems to be that the method !__setitem!__ treats 1x1 submatices as elements of the rings over which the matrix is defined, while the method !__getitem!__ treats 1x1 submatices as 1x1 matrices.

Below I will attach a patch which changes the method !__setitem!__ to treat 1x1 submatices specified by slices as 1x1 matrices.


---

Comment by phil created at 2010-08-14 15:38:51

Changing status from new to needs_review.


---

Attachment


---

Comment by jason created at 2010-08-14 16:09:47

Can you add your example as a doctest?


---

Attachment

Ok. Did I do it right? (this is my fist sage patch)


---

Comment by phil created at 2010-08-14 20:23:04

Fix bug in another case


---

Attachment

I added another patch (including a doctest) which fixes the bug in the case that only the second index is a slice. The following example works only after the second patch is applied:

## Example


```
sage: A=matrix([[1,2],[3,4]]); B=matrix([[1,3],[5,7]])
sage: A[1,0:1]=B[1,1:2]
sage: A
[1 2]
[7 4]

```



---

Comment by davidloeffler created at 2010-12-16 12:19:56

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-12-16 12:19:56

Excellent -- positive review. Apply all three patches.


---

Comment by jdemeyer created at 2011-01-12 06:33:03

Resolution: fixed
