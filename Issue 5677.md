# Issue 5677: Underscore for repeating output clobbered by symbolic variables

Issue created by migration from https://trac.sagemath.org/ticket/5677

Original creator: rbeezer

Original creation time: 2009-04-03 21:39:51

Assignee: was

Keywords: underscore repeat output

When creating a function with a statement like

`f(x,y) = x<sup>2+y</sup>2`

the preparser creates a command to declare the variables and assigns it to underscore.  This renders the underscore unusable for repeating the previous output.

A workaround is to use  

`del _` 

to restore the functionality.


---

Comment by dsm created at 2012-05-25 22:55:53

Is this still valid?  It looks more like `__tmp__` is used, not `_`, these days:



```
sage: preparse("f(x,y) = x^2+y^2")
'__tmp__=var("x,y"); f = symbolic_expression(x**Integer(2)+y**Integer(2)).function(x,y)'
sage: 5
5
sage: _
5
sage: f(x,y) = x^2+y^2
sage: _
5
sage: 7
7
sage: _
7
```



---

Comment by mhansen created at 2013-07-23 12:56:14

Yep, I think this is invalid now.


---

Comment by mhansen created at 2013-07-23 12:56:14

Resolution: invalid
