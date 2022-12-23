# Issue 3144: bug in calculus var command

Issue created by migration from https://trac.sagemath.org/ticket/3144

Original creator: was

Original creation time: 2008-05-09 15:16:51

Assignee: was

Note that the output of var('x,y') below the second time is *totally broken* - it returns a string:


```
sage: x,y=var("x,y")
sage: f(x,y)=sin(x)+cos(y)
sage: grads=[diff(f,var) for var in (x,y)]
sage: var('x,y')
'x,y'
```



---

Comment by was created at 2008-05-09 16:37:00


```


On Fri, May 9, 2008 at 9:28 AM, Marshall Hampton <hamptonio@gmail.com> wrote:
>
> I'm not sure I agree that this is a bug.  After using the name "var"
> in the loop, the value of var is y.  y is a symbolic variable, and
> when evaluated at the string "x,y" it returns "x,y"; this seems like
> desirable behavior (to have string-valued functions seems OK to me).
>
> Or another way to put it: if the above behavior is a bug, then I think
> the following would be as well:
> sage: x,y = var("x,y")
> sage: y(2)
> 2
>
> Or perhaps I am missing something.
> -M. Hampton

There is an issue with the design, though it is arguable what it is.
Notice that var('x') acts as the identity function irregardless of the input,
where as var('x')^2 coerces its input to the SymbolicRing. 

sage: x = var('x')
sage: x('hello world')
'hello world'
sage: type(x('hello world'))
<type 'str'>
sage: (x^2)('hello world')
hello^2*world^2
sage: type((x^2)('hello world'))
<class 'sage.calculus.calculus.SymbolicArithmetic'>
sage: x,y=var("x,y")

I thus think the right fix would be for var('x') to also coerce its input
to the symbolic ring.  So, in the original question var('x,y') would
give an error since:

 sage: SR('x,y')
Traceback (most recent call last):
...
TypeError: Malformed expression: x, !!! y

By the way, what's up with the !!! in the error message?  That looks very weird. 

What do you think.

 -- william
```



---

Comment by was created at 2009-01-22 02:30:33

Resolution: invalid


---

Comment by was created at 2009-01-22 02:30:33

stupid mistake by me, since var is defined in the list...
