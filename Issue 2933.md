# Issue 2933: calculus -- substitution of a dict for SymbolicFunctionEvaluation is broken (but **kwds works)

Issue created by migration from https://trac.sagemath.org/ticket/2933

Original creator: was

Original creation time: 2008-04-15 15:02:46

Assignee: was

Substitution with a dictionary as input is broken.  Notice below in the
third input that the dictionary is ignored?!


```
sage: function('f',x)
f(x)
sage: (f(x)).substitute(f=log)
log(x)
sage: (f(x)).substitute({f:log})
f(x)
sage: type(f(x))
<class 'sage.calculus.calculus.SymbolicFunctionEvaluation'>
sage: (x^3 + 1).substitute(x=5)
126
sage: (x^3 + 1).substitute({x:5})
126
```



---

Comment by mhansen created at 2008-04-15 17:40:47

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-04-15 17:40:47

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2008-04-17 05:17:39

I find the business with isinstance(str) strange, but it looks right and the doctests assert the correct behaviour.


---

Comment by mabshoff created at 2008-04-17 06:11:01

Resolution: fixed


---

Comment by mabshoff created at 2008-04-17 06:11:01

Merged in Sage 3.0.alpha6
