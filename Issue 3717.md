# Issue 3717: implement _latex_ method for formal derivative function (in symbolic calculus)

Issue created by migration from https://trac.sagemath.org/ticket/3717

Original creator: was

Original creation time: 2008-07-24 10:06:46

Assignee: gfurnish


```
> sage: var('c x y t')
> (c, x, y, t)
> sage: x=function('x',t)
> sage: y=function('y',t)
> sage: f=c*x*y
> sage: diff(f,t)
> c*x(t)*diff(y(t), t, 1) + c*y(t)*diff(x(t), t, 1)
>
> In the above example, x and y are some functions of t while c is
> independent of t. If I take the derivative of f=c*x(t)*y(t), I
> correctly obtain diff(f(t),t)=c*x(t)*diff(y(t), t) + c*y(t)*diff(x(t),
> t), but for the result looks a bit ugly and does not show well in
> latex. Can diff(x(t), t) be expressed in a shorter way, such as x'(t),
> similarly to Mathematica?

Try using "print" for a much nicer "ascii art" view of symbolic expressions:

sage: print diff(f,t)

                           d                    d
                   c x(t) (-- (y(t))) + c y(t) (-- (x(t)))
                           dt                   dt

(Hopefully the "rich text formatting" of this email works for you... or
just try it out.)

> Is there a way of getting derivatives
> translated into latex code?

Yes, this would be easy for us to implement.


> Something similar would apply to integrals.

Yep, same with my comments.

William
```



---

Comment by jhpalmieri created at 2008-10-31 03:19:59

Changing keywords from "" to "latex, calculus".


---

Comment by jhpalmieri created at 2008-10-31 03:19:59

With f as above, if I do `latex(diff(f,t))`, I get

```
{{c x\left(t\right)} {{d}\over{d\,t}}\,y\left(t\right)} + {{c y\left(t\right)} {{d}\over{d\,t}}\,x\left(t\right)}
```

So is there anything to be done here?  I suppose one could quibble about the spacing between the "d" and the "t", but otherwise, it already looks okay to me.


---

Comment by jason created at 2009-01-18 02:05:41

See #4202 for the ticket that enabled the behavior in the comment.  I believe this ticket can be closed because of #4202.


---

Comment by mabshoff created at 2009-01-18 04:12:28

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 04:12:28

With Sage 3.3.alpha0 this now works:

```
sage: k
c*x(t)*diff(y(t), t, 1) + c*y(t)*diff(x(t), t, 1)
sage: print(k)

                            d                    d
                    c x(t) (-- (y(t))) + c y(t) (-- (x(t)))
                            dt                   dt
sage: latex(k)
{{c x\left(t\right)} {{{\it \partial}}\over{{\it \partial}\,t}}\,y\left(t\right)} + 
{{c y\left(t\right)} {{{\it \partial}}\over{{\it \partial}\,t}}\,x\left(t\right)}
```


I am closing this ticket as fixed. 

Cheers,

Michael
