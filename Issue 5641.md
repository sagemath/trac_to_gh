# Issue 5641: plotting of matrices with 0 rows or columns is broken in multiple ways

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-30 03:18:23

Assignee: was


```
sage: matrix(QQ,0).plot()
Traceback (most recent call last):
...
IndexError: index out of bounds

sage: matrix(QQ,0,5).plot()
Traceback (most recent call last):
...
IndexError: index out of bounds

sage: matrix(QQ,5,0).plot()
Traceback (most recent call last):
...
ValueError: zero-size array to ufunc.reduce without identity
```



---

Comment by kcrisman created at 2012-06-01 18:31:15

Still broken, though now all three have the latter error message.  I'm not sure I like this even being possible:

```
sage: A = matrix(QQ,5,0)
sage: A.rows()
[(), (), (), (), ()]
```

Does this have meaning?

Anyway, the error is raised while trying to acquire a colormap in matplotlib in imshow, and then Numpy doesn't like one of the inputs.  Having a Numpy or matplotlib-native version of this would be helpful - maybe the problem is upstream?  Or maybe we're just using it wrong and should have a special thing for plotting empty matrices... ??
