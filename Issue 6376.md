# Issue 6376: serious bug in _maxima_init_ method for formal derivatives with new symbolics

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-21 14:13:14

Assignee: burcin

CC:  gmhossain mhansen


```
sage: f(x) = function('f',x)
sage: g = f(-x).diff(x); g
-D[0](f)(-x)
sage: g._maxima_init_()
"(diff('f(x), x, 1))*(-1)"
```


Notice that the `-x` inside f is totally ignored!  This is because of code in the derivative method around line 454 of `sage/symbolic/expression_conversion.py`

Changing the line

```
args = ex.args()
```


to 

```
args = ex.operands()
```


"fixes" the problem, in that a NotImplementedError gets raised, instead of a wrong result returned.  This is *way* better than the current situation, and we better fix this asap.  

A better fix of course is to implement proper conversion. mhansen wrote this code, so maybe it would be easy for him.



---

Comment by burcin created at 2009-08-05 08:20:28

Mike, do you have any time to look at this?

Thanks.

Burcin


---

Comment by robert.marik created at 2009-11-17 14:42:31

fixed with patch at  #7401 which waits for review.


```
sage: f(x) = function('f',x)
sage: g = f(-x).diff(x); g
-D[0](f)(-x)
sage: g._maxima_init_()
"(at(diff('f(dummy_var_der), dummy_var_der,1),dummy_var_der=-x))*(-1)"
```



---

Comment by robert.marik created at 2009-11-17 14:46:32

The patch is attached to #7401

#6376 is not doctested, since I did not know about this issue when finished patch for #7401. It could be easily doctested, but doctests in #7401 are equivalent to #6376.


---

Comment by robert.marik created at 2009-11-17 14:46:32

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-17 16:07:45

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-11-17 16:07:45

Okay, this seems okay.  

To release manager: please close this as fixed once #6376 is merged.


---

Comment by mhansen created at 2009-11-19 17:47:22

Resolution: duplicate
