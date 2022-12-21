# Issue 7537: list(SR('c').iterator()) is empty

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-11-26 17:41:35

Assignee: burcin

CC:  burcin

This looks like a bug to me:


```
sage: list(SR('c+1').iterator())
[c, 1]
sage: list(SR('c').iterator())
[]
```



---

Comment by burcin created at 2010-02-25 13:16:17

I don't think this is a bug. :)

It doesn't make sense to iterate over variables, constants or numeric coefficients. Iterators are only available over `add`, `mul`, and `pow` objects, which correspond to the obvious mathematical operations.

AFAICT, this is also the case in MMA:


```
Mathematica 7.0 for Linux x86 (32-bit)
Copyright 1988-2008 Wolfram Research, Inc.

In[1]:= T=x+1
Out[1]= 1 + x
In[2]:= T
Out[2]= 1 + x
In[3]:= T[This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro)
Out[3]= 1
In[4]:= X
Out[4]= X
In[5]:= X[This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro)
Part::partd: Part specification X[This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro) is longer than depth of object.
Out[5]= X[This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro)
```


We can raise a `ValueError` if the expression corresponds to a `symbol`, `constant` or `numeric` object. The docstring should also be enhanced to point to the data structure for symbolic expressions here:

http://www.ginac.de/tutorial/Internal-representation-of-products-and-sums.html

Comments?


---

Comment by malb created at 2010-02-25 13:31:08

I see your point but why not return `self` in that case?


---

Comment by burcin created at 2010-02-25 14:03:44

Do you mean return an iterable which returns `self` when `.next()` is called? 

If you're traversing a symbolic expression, and working with iterators, I can't think of any case where symbols, constants and numeric coefficients don't form a special case which will be treated separately. The usual way to write code to traverse the expression tree should check if `.operator()` returns `None`.

I admit that I don't use this interface often enough to decide on the design though. The recent thread on sage-devel about indexing parts of expressions also shows that this needs work.

Do you have a use case we can work from? How did you run into this?


---

Comment by malb created at 2010-02-25 14:11:49

I am converting boolean polynomials to Integer Programming problems, for this I convert them to symbolic expressions first and then to MIP. Probably not the most natural application.


---

Comment by malb created at 2010-07-14 13:38:18

So let's close this bug then?


---

Comment by burcin created at 2010-09-26 14:36:46

Changing status from new to needs_review.


---

Comment by burcin created at 2010-09-26 14:36:46

With attachment:trac_7537-iterator.patch we get an error when trying to iterate over symbols, constants or numeric objects:


```
sage: x.iterator()
Traceback (most recent call last):
...
ValueError: cannot iterate over numeric, constant or symbol
sage: pi.iterator()
Traceback (most recent call last):
...
ValueError: cannot iterate over numeric, constant or symbol
sage: SR(5).iterator()
Traceback (most recent call last):
...
ValueError: cannot iterate over numeric, constant or symbol
```


This patch depends on #9989 (not in terms of functionality, but it will fail to apply since the patch there touches the same part of `sage/symbolic/expression.pyx`).


---

Attachment


---

Comment by burcin created at 2011-03-23 12:10:15

I updated the patch with a new error message recommended in #9989.


---

Comment by malb created at 2011-03-24 14:17:04

Patch looks good, applies cleanly against 4.7.alpha2 and doctests pass.


---

Comment by malb created at 2011-03-24 14:17:04

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-28 07:18:08

Resolution: fixed
