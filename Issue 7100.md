# Issue 7100: rounding error in QuadraticForm.vectors_by_length()

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-10-03 13:35:57

Assignee: justin

CC:  tornaria

A rounding error causes an issue in `vectors_by_length()`. The square root of a very tiny negative number (which should be rounded to zero) is computed, creating a symbolic imaginary expression which floor can't round to a nearest integer (e.g. `floor(2.0 + 1.49011611938e-08*I)` below).

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Q = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1])
sage: Q.vectors_by_length(2)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1093, 0))
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/tornaria/.sage/temp/sage.math.washington.edu/20501/_home_tornaria__sage_init_sage_0.py in <module>()

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__split_local_covering.py in vectors_by_length(self, bound)
    207             ## 2. Compute bounds
    208             Z = sqrt(T[i] / Q[i][i])
--> 209             L[i] = ZZ(floor(Z - U[i]))  
    210             x[i] = ZZ(ceil(-Z - U[i]) - 0)  
    211 

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)()

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)()

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._integer_ (sage/symbolic/expression.cpp:4136)()

TypeError: unable to convert x (=floor(2.0 + 1.49011611938e-08*I)) to an integer
```



---

Comment by mhansen created at 2009-10-04 03:07:48

I changed it to take the abs of Z, but I don't know if this goes the right way for the bounds.  Someone familiar with the algorithm should check this.  All tests do pass.


---

Comment by tornaria created at 2010-01-14 15:31:38

Replying to [comment:1 mhansen]:
> I changed it to take the abs of Z, but I don't know if this goes the right way for the bounds.  Someone familiar with the algorithm should check this.  All tests do pass.

Actually, this is wrong:

```
Q = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1]) 
sage: map(len, Q.vectors_by_length(2)) 
[1, 12, 11]
```

Because it's missing one of the vectors of norm 2 (namely `[0, -1, 0, -1]`) due to roundoff errors.

The way to fix this is to use a bound for searching which is an epsilon larger than an integer --- enough to cover the roundoff errors. Pari uses `1e-6` for this epsilon.

I'll post a patch in a moment.


---

Comment by tornaria created at 2010-01-14 15:31:38

Changing status from needs_review to needs_work.


---

Comment by tornaria created at 2010-01-14 15:41:27

Changing status from needs_work to needs_review.


---

Comment by tornaria created at 2010-01-14 16:55:42

Use this patch instead of the other one (updated)


---

Attachment

All tests pass with my patch on top of a clean sage-4.3.


---

Comment by mhansen created at 2010-01-14 17:20:06

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-14 17:20:06

Looks good.  Thanks for looking over this!


---

Comment by rlm created at 2010-01-16 02:48:16

Resolution: fixed
