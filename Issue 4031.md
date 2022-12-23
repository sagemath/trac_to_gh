# Issue 4031: Callable symbolic expressions should allow keyword args

Issue created by migration from https://trac.sagemath.org/ticket/4031

Original creator: jwmerrill

Original creation time: 2008-09-01 06:25:55

Assignee: tbd

For consistency with symbolic expressions, callable symbolic expressions should accept keyword arguments.


```
sage: x, y = var('x,y')
sage: f = x^2 + y^2
sage: type(f)
<class 'sage.calculus.calculus.SymbolicArithmetic'>
sage: f(3,2)
13
sage: f(x=3,y=2)
13

The desired behavior is

sage: f(x,y) = x^2 + y^2
sage: type(f)
<class 'sage.calculus.calculus.CallableSymbolicExpression'>
sage: f(3,2)
13
sage: f(x=3, y=2)
13

But the current behavior is

sage: f(x=3, y=2)
Traceback (most recent call last):
...
TypeError: __call__() got an unexpected keyword argument 'y'
```




---

Attachment


---

Comment by jwmerrill created at 2008-09-01 06:28:56

Changing type from defect to enhancement.


---

Comment by jwmerrill created at 2008-09-01 06:28:56

The attached patch implements keyword args for callable symbolic expressions, along with doctests.


---

Comment by jwmerrill created at 2008-09-01 06:28:56

Changing component from algebra to calculus.


---

Comment by jwmerrill created at 2008-09-01 06:28:56

Changing assignee from tbd to jwmerrill.


---

Comment by mabshoff created at 2008-09-01 12:25:31

Opps :)


---

Attachment


---

Comment by mhansen created at 2008-09-01 22:39:29

Hello,

I agree with patch, but I tweaked the implementation a bit.  Do you agree with the change jwmerrill?

--Mike


---

Comment by mhansen created at 2008-09-01 22:47:25

Also, I forgot to mention that this patch fixes the issue at #4030.


---

Comment by jwmerrill created at 2008-09-01 22:48:36

mhansen, I think your implementation is better.  Only trac_4031.patch should be applied.


---

Comment by jwmerrill created at 2008-09-01 23:14:40


```
mhansen: Nope, if you think my patch is good and it works, give the ticket a positive review.
```


with mhansen's patch, all tests pass.


---

Comment by mabshoff created at 2008-09-02 10:13:23

Resolution: fixed


---

Comment by mabshoff created at 2008-09-02 10:13:23

Merged trac_4031.patch in Sage 3.1.2.alpha4
