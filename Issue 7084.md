# Issue 7084: Make assumption comparison work for GenericDeclarations

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-09-30 15:30:46

On Sep 30, 11:07 am, lutusp <lut...`@`gmail.com> wrote:
> I find I cannot make more than one of a certain kind of assume
> statement:
> 
> sage: assume(a,'real')
> sage: assume(b,'real')
> 
> If I do, I get an error message:
> 
> AttributeError: 'GenericDeclaration' object has no attribute
> 'variables'

It's comparing your second assumption with the first one, presumably to make sure it doesn't conflict (?) ... but it is strange that it is talking about an attribute variables, since the attribute _var is being called, and b is real has that.

The problem is in symbolic/expression.pyx, where __nonzero__ tries to find the variable of  "a is real" - but it only has a _var, not variables like "t>0", which is a symbolic expression.

> 
> One such assumption is accepted, but not two. But more typical
> assumptions are accepted:
> 
> sage: forget()
> sage: assume(a > 0)
> sage: assume(b > 0)
> sage: assume(c > 0)
> sage: assumptions()
> 
> [a > 0, b > 0, c > 0]
> 
> Am I using the wrong syntax or is this a bug?


---

Comment by kcrisman created at 2009-09-30 18:15:45

This should fix it.


---

Attachment

Based on 4.1.2.alpha4


---

Comment by timdumol created at 2009-10-01 03:00:43

Tests look good. Doctests run perfectly. Positive review.


---

Comment by mhansen created at 2009-10-15 07:20:33

Resolution: fixed
