# Issue 6569: sparse integer matrix doesn't raise an error on non-integer index

Issue created by migration from https://trac.sagemath.org/ticket/6569

Original creator: jason

Original creation time: 2009-07-20 13:53:42

Assignee: was

CC:  rbeezer mjo


```
{{{
sage: a=matrix(4,range(1,17),sparse=True)
sage: a[[2.3],[2.1]]                     
[0]
}}}

as compared to

{{{
sage: a=matrix(4,range(1,17))            
sage: a[[2.3],[2.1]]         
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/tiny/8143/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:4999)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix1.so in sage.matrix.matrix1.Matrix.matrix_from_rows_and_columns (sage/matrix/matrix1.c:8613)()

TypeError: 'sage.rings.real_mpfr.RealLiteral' object cannot be interpreted as an index
}}}



---

Comment by mjo created at 2012-01-22 19:36:07

Catch invalid indices in Matrix.__getitem__ and add doctests.


---

Comment by mjo created at 2012-01-22 19:38:14

Changing status from new to needs_review.


---

Attachment

Some invalid indices weren't being caught in the general matrix[foo] accessor; the fact that non-sparse matrices failed with an error was an implementation detail.

I think I've fixed them all, and doctested that sparse/dense behave the same way now.


---

Comment by was created at 2012-01-24 19:21:47

Changing status from needs_review to positive_review.


---

Comment by was created at 2012-01-24 19:21:47

1.  I just looked at this and I'm shocked that `ind` is of type int.  This will work fine on 32-bit, but will be totally broken/buggy in subtle and surprising ways on 64-bit machines.  The type of ind should be `Py_ssize_t`, just like the type of `i`.  
I realize that your patch does not introduce ind.  It was introduced in #4973...

Nobody will notice this now, because there is some sort of massive weird inefficiency in the creation of sparse matrices (maybe the parent space has its basis constructed or something idiotic like that), which makes it impossible to make a large sparse matrix, even though this should be trivial, instant, fast, and take no memory:

```
sage: time a = matrix(QQ, 2^25, sparse=True)
Time: CPU 5.88 s, Wall: 8.46 s
sage: get_memory_usage()   # what ?
3908.29296875
```


I've made the ind and memory issue trac #12348.


2. That said, everything in this particular patch looks great to me.  Positive review!   

I hope you can address #12348 though next.  At least the trivial change of ind to `Py_ssize_t`.


---

Comment by jdemeyer created at 2012-02-02 12:52:32

Resolution: fixed
