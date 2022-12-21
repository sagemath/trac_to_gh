# Issue 3469: Something funny with free modules

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-06-19 07:29:53

Assignee: was

CC:  jason


```
sage: W = (ZZ^2).span([(1/2,1/2), (0,1)]); W
Free module of degree 2 and rank 2 over Integer Ring
Echelon basis matrix:
[1/2 1/2]
[  0   1]
sage: V = (ZZ^2).span([(1/2,1/2), (0,2)]); V
Free module of degree 2 and rank 2 over Integer Ring
Echelon basis matrix:
[1/2 1/2]
[  0   2]
sage: W(V.gen(0))
Traceback (most recent call last):
...
TypeError: no coercion of this rational to integer
```



---

Comment by robertwb created at 2008-06-19 07:38:05

Also

```
sage: type(V.gen())
<type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
sage: type(V([1,2]))
<type 'sage.modules.vector_integer_dense.Vector_integer_dense'>
```



---

Comment by robertwb created at 2008-06-19 07:39:24

This seems to be the real issue: 

```
sage: V([1/2,1/2])
Traceback (most recent call last):
...
TypeError: no coercion of this rational to integer
```



---

Comment by boothby created at 2010-01-18 05:00:30

Seems to work now.


---

Comment by boothby created at 2010-01-18 05:00:30

Resolution: worksforme
