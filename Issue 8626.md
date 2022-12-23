# Issue 8626: qqbar quadratic elements

Issue created by migration from https://trac.sagemath.org/ticket/8626

Original creator: jason

Original creation time: 2010-03-29 19:24:06

Assignee: AlexGhitza

CC:  cwitty

It would be nice if roots of quadratics printed using the quadratic formula in QQbar, i.e., 


```
sage: QQbar(sqrt(2))
sqrt(2)
```



---

Comment by jason created at 2010-03-29 19:27:02

This patch almost certainly needs work, but does give some nice results:


```
sage: QQbar(sqrt(5))  
sqrt(20)/2
sage: QQbar(sqrt(2))  
sqrt(8)/2
```


Things are not simplified because I don't want to do any extra work in the printing.


---

Comment by jason created at 2010-03-29 19:29:22

Another example with this patch:


```
sage: m=matrix(2,2,[0,1,1,1]);m
[0 1]
[1 1]
sage: m.eigenvalues()          
[(--1-sqrt(5))/2, (--1+sqrt(5))/2]

```



---

Comment by jason created at 2010-03-29 19:38:24

That last patch corrects the double negative, so I get:


```
sage: m=matrix(2,2,[0,1,1,1]);m
[0 1]
[1 1]
sage: m.eigenvalues()  
[(1-sqrt(5))/2, (1+sqrt(5))/2]

```



---

Attachment


---

Comment by jason created at 2010-04-21 02:47:22

apply on top of previous patch


---

Attachment

I've attached a work-in-progress patch that allows qqbar elements to be converted to symbolics elements in a smart way, i.e., square roots become symbolic square roots, etc.


---

Comment by jason created at 2010-04-21 02:49:04

Changing status from new to needs_work.


---

Comment by jason created at 2010-09-22 03:09:41

Changing priority from minor to major.


---

Comment by jason created at 2010-09-22 03:09:41

Here is another problem that could probably be solved if qqbar elements could be converted to symbolics.  The application for this example was trying to plot a line from the eigenvector of a matrix:


```
sage: A=matrix(QQ,2,2,[2,5,1,2])
sage: EV=A.right_eigenvectors()
sage: EV
[(-0.2360679774997897?, [(1, -0.4472135954999580?)], 1), (4.236067977499789?, [(1, 0.4472135954999580?)], 1)]
sage: evec=EV[0][1][0]
sage: var('t')
t
sage: evec.n()*t # works fine
(t, -0.447213595499958*t)
sage: t*evec
Traceback (most recent call last):
...
NotImplementedError: symbol

```



---

Comment by jason created at 2010-09-22 03:13:44

Changing component from algebra to coercion.


---

Comment by mmezzarobba created at 2013-12-28 17:34:44

Related: #14239


---

Comment by jdemeyer created at 2014-12-13 22:11:03

Duplicate of #14239


---

Comment by jdemeyer created at 2014-12-13 22:11:03

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-12-18 07:39:13

Resolution: duplicate
