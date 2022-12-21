# Issue 4343: gradient needs to be more careful about the variables

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-10-23 00:28:09

Assignee: burcin


```
The reference manual shows the following example for the gradient()  
function:

sage: x,y = var('x y')
sage: f = x2+y2
sage: f.gradient()
(2*x, 2*y)

However, if instead I enter:

sage: x,y,n = var('x y n')
sage: f = x^n+y^n
sage: f.gradient()
(y^n*log(y) + x^n*log(x), n*x^(n - 1), n*y^(n - 1))

(not what I wanted, but I can understand what happened.)
So I tried:

sage: f(x,y) = x^n+y^n
sage: f.gradient()
((x, y) |--> y^n*log(y) + x^n*log(x), (x, y) |--> n*x^(n - 1), (x, y)  
|--> n*y^(n - 1))
So even if I specify that f is a function of x and y,
gradient() still insists on also differentiating w.r.t. n

How do I tell gradient() that n is a constant?

Thanks in advance for insights.
Jim Clark
```



---

Attachment

Doctests in calculus.py pass.


---

Comment by ddrake created at 2008-10-24 04:26:21

Doctests pass, Jim's original problem is fixed, and the code looks good. Positive review.


---

Comment by mabshoff created at 2008-10-26 04:05:06

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 04:05:06

Resolution: fixed
