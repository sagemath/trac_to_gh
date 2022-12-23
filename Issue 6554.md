# Issue 6554: [with patch, needs review] plotting sparse matrices converts the matrix to a dense matrix

Issue created by migration from https://trac.sagemath.org/ticket/6554

Original creator: jason

Original creation time: 2009-07-18 14:00:55

Assignee: was

CC:  rbeezer mhansen was wcauchois robertwb

Plotting big sparse matrices doesn't even work since it automatically converts the matrix to a dense matrix, instead of calling the spy() function.


---

Attachment

This took a very long time before, if it was even possible.


```
        sage: A=random_matrix(ZZ,100000,density=.00001,sparse=True)
        sage: matrix_plot(A,marker=',')
```



---

Comment by jason created at 2009-07-21 17:06:18

(To those I'm adding as CC): if you have time, could you review this ticket?  This is a simple change that makes plotting sparse matrices possible.  Currently, it is very, very slow or is not even really possible to plot large sparse matrices because Sage immediately converts the matrix to a dense matrix.


---

Comment by jason created at 2009-07-26 09:02:11

It would be really great if this was reviewed in time for the Monday deadline for 4.1.1.  This is a simple change that makes plotting sparse matrices possible. Currently, it is very, very slow or is not even really possible to plot large sparse matrices because Sage immediately converts the matrix to a dense matrix.


---

Comment by wdj created at 2009-07-26 12:07:55

This installs fine (amd64 ubuntu 9.04, sage 4.1.1.alpha0) and I'm running tests now. However, why is it that


```
sage: B = random_matrix(ZZ, 10, 20, density=.4, sparse=True, x = 10)
sage: matrix_plot(B, cmap='hsv').show(axes=False)
```

returns a ble-and white scatterplot, but


```
sage: C = random_matrix(ZZ, 10, 20, x = 10)
sage: matrix_plot(C, cmap='hsv').show(axes=False)
```

returns a multi-colored plot? The docstring indicates that the colors plotted
indicate the relative difference in sizes between the matrix entries. This seems
to be incorrect, unless I am missing something, in the sparse case. Should a 
comment to this effect be added to the docstring?


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2009-07-27 16:05:44

Good point; the docstring should be updated.  I've attached a small patch that updates the docstring.  Can you review this docstring change?


---

Comment by wdj created at 2009-07-27 18:29:02

Yes, looks good and passes sage -testall (intel macbook, OS 10.4.11) except for


```
        sage -t  "devel/sage/sage/parallel/decorate.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

They seem unrelated. As far as I am concerned, this gets a positive review.


---

Comment by mvngu created at 2009-07-29 12:57:11

Resolution: fixed


---

Comment by mvngu created at 2009-07-29 12:57:11

Merged both patches.
