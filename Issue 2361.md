# Issue 2361: Substitution without specifying variables should raise exception in case of ambiguity

Issue created by migration from https://trac.sagemath.org/ticket/2361

Original creator: parombouts

Original creation time: 2008-03-01 18:14:05

Assignee: was

Keywords: substitution ambiguity

I have just started reading the Sage reference manual (release 2008.02.22) and I noticed an example of substitution in section 4.1 that contradicted the description that preceded it:


----
_If there is no ambiguity of variable names, we don't have to specify them:_

...

_However if there is ambiguity, we must explicitly state what variables we're substituting for:_

```
sage: f = sin(2*pi*x/y)
sage: f(4)
sin(8*pi/y)
```

----

Either the documentation should be changed so that it accurately describes what happens in this example or the implementation should be changed so that an exception is raised in a case like this.

I have a strong preference for the latter solution. I don't find the current substitution behavior in case of ambiguity useful (is it even clearly defined?), and I can think of many examples where this behavior could easily lead to subtle bugs.







---

Comment by parombouts created at 2008-03-01 18:30:52

I am new to Sage so I am not yet able to hack the implementation myself, but it should be fairly straightforward to fix this.

I have noticed that there is a number_of_arguments method, so if the substitution argument doesn't specify a variable, the code should check that self.number_of_arguments()==1 and raise an exception if not.


---

Comment by mhansen created at 2008-03-01 22:21:05

Currently, if you don't specify variables, then the implicit order is the one from f.variables()


```
sage: f = sin(2*pi*x/y)
sage: f.variables()
(x, y)
sage: f(2)
sin(4*pi/y)
sage: f(2,2)
0
sage: f(x,2)
sin(pi*x)
```



---

Comment by gfurnish created at 2008-03-21 16:37:26

This should definately get changed.


---

Comment by burcin created at 2009-04-16 11:02:15

Resolution: fixed


---

Comment by burcin created at 2009-04-16 11:02:15

This was fixed with #5413.

Substitution is symbolic expressions now requires stating the variables explicitly.
