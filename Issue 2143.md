# Issue 2143: [with patch, needs review] wrap scipy optimization routines and cvxopt linear programming, add gradient/hessian to calculus

Issue created by migration from https://trac.sagemath.org/ticket/2143

Original creator: jkantor

Original creation time: 2008-02-12 05:33:27

Assignee: jkantor

CC:  dfdeshom

http://sage.math.washington.edu/home/jkantor/optimize.patch




---

Comment by was created at 2008-02-12 05:36:43

Clicking the link gives:

```
Forbidden

You don't have permission to access /home/jkantor/optimize.patch on this server.
```


Of course, I could fix that since I'm root on that machine... but I'm too busy at the moment.


---

Attachment

Attaching the patch on trac for convenience...


---

Comment by dfdeshom created at 2008-03-05 05:57:10

Review: 

Doctests were failing due to either missing imports or unsuppressed output. I'm attaching a patch where all doctests pass...


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-03-15 23:09:39

I fixed some typos and formatting issues. Both 2143.patch and 2143-2.patch should be applied.


---

Comment by mabshoff created at 2008-03-16 02:57:15

Merged 2143.patch and 2143-2.patch in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-16 02:57:15

Resolution: fixed


---

Comment by edrex created at 2008-03-16 03:38:09


```
sage: f(x,y)=x^2+y^2
sage: f.gradient()
<type 'exceptions.NotImplementedError'>:
sage: f.parent()
Callable function ring with arguments (x, y)
sage: var('x,y')
sage: g=x^2+y^2
sage: g.gradient()
sage: g.parent()
Symbolic Ring
(2*x, 2*y)
```


I guess this isn't a bug, just not implemented yet? I thought f(x)=x^2 was equivalent to var('x');f=x^2 but evidently they are different?


---

Comment by mhansen created at 2008-03-16 03:40:44

These are actually different things.


```
sage: preparse('f(x)=x^2')
'_=var("x");f=symbolic_expression(x**Integer(2)).function(x)'
sage: preparse("var('x');f=x^2")
"var('x');f=x**Integer(2)"
```



---

Comment by edrex created at 2008-03-16 16:48:38

Ah... I like the f(x,y)=x<sup>2+y</sup>2 syntax/construction better, since it makes the mapping explicit for expressions which may not contain all variables. Filed as #2547
