# Issue 2703: make _fast_float_ work on inequality testing

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-28 17:29:54

Assignee: mabshoff

It would be really nice if this worked:


```
sage: var('x y')
sage: f=x^2+y^2<=1
sage: g=f._fast_float_('x','y')
sage: g(1,2)
False
sage: g(0.5,0.5)
True
```


Here is a toy implementation:


```
def ff(func,*args):
    g1 = func.left()._fast_float_(*args)
    g2 = func.right()._fast_float_(*args)
    oper = func.operator()
    def ret(*sub_args):
        return oper(g1(*sub_args), g2(*sub_args))
    return ret
```




---

Comment by mabshoff created at 2008-03-28 18:06:57

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2008-03-28 18:06:57

Changing component from Cygwin to calculus.


---

Comment by jwmerrill created at 2008-09-01 15:22:03

This looks like a near duplicate of #2768, where it was decided that this functionality was a bad idea.  See comment by robertwb.


---

Comment by mabshoff created at 2008-09-02 10:18:02

Resolution: invalid


---

Comment by mabshoff created at 2008-09-02 10:18:02

Thanks Jason,

this is invalid - another ticket gone :)

Cheers,

Michael
