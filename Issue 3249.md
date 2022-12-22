# Issue 3249: a bug in computing the inverse of the matrix

Issue created by migration from Trac.

Original creator: pdenapo

Original creation time: 2008-05-17 22:28:46

Assignee: was

I was doing the following, when testing the jordan_form method...


``` 
sage: A=Matrix(ComplexField(200),[[1,-2],[2,-1]])
sage: jordan=A.jordan_form(transformation=True,subdivide=False)
sage: P=jordan[1]
```


(P is now the transformation matrix, jordan[1] is the jordan canonical
form)


```
sage: det(P)
1.7320508075688772935274463415058723669428052538103806280558*I
```


so clearly the matrix P has non zero determinant, as it should, however...


```
sage: P.inverse()
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/media/hda2/pablo.new_home/sage/sage-2.10.2/<ipython console> in <module>()

/media/hda2/pablo.new_home/sage/sage-2.10.2/matrix2.pyx in sage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19571)()

/media/hda2/pablo.new_home/sage/sage-2.10.2/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:12213)()

<type 'exceptions.ZeroDivisionError'>: self is not invertible
```


The most strange thing is that things depends strongly on the precision used for the
complex field...the same computation using 20 bits of precision gives


```
sage:  A=Matrix(ComplexField(20),[[1,-2],[2,-1]])
sage: jordan=B.jordan_form(transformation=True,subdivide=False)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/media/hda2/pablo.new_home/sage/sage-2.10.2/<ipython console> in <module>()

/media/hda2/pablo.new_home/sage/sage-2.10.2/matrix2.pyx in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:20606)()

<type 'exceptions.AttributeError'>: 'NoneType' object has no attribute 'is_exact'
```






---

Comment by pdenapo created at 2008-05-19 18:32:04

Note that there are two different problems here.

The first one seems to be similar to bugs #1132,#3166


---

Comment by pdenapo created at 2008-05-21 02:12:10

See also  #2256 (same problem)


---

Comment by pdenapo created at 2008-05-27 23:39:01

The second issue reported here is fixed by my patch in #3316


---

Comment by pdenapo created at 2008-05-27 23:39:01

Resolution: duplicate
