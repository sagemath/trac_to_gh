# Issue 4561: _fast_float_ for sin/cos, etc., in caculus.py is implemented stupidly

Issue created by migration from https://trac.sagemath.org/ticket/4561

Original creator: was

Original creation time: 2008-11-20 01:55:11

Assignee: burcin

See #4557.


```
>
> Why are we using math.sin/math.cos at all? Really, it should use the
> native C sin and cos.
>
> - Robert

You're right Robert, and that definition of _fast_float_ for sin and cos
is totally the wrong approach.  E.g., observe that your _fast_float_ sin
is twice as fast as math.sin:

sage: a = sin._fast_float_()
sage: timeit('a(3.4r)')
625 loops, best of 3: 469 ns per loop
sage: a = sin(x)._fast_float_()
sage: timeit('a(3.4r)')
625 loops, best of 3: 254 ns per loop

Note that the code in calculus.py is *not* just returning math.sin,
actually, but constructing a fast_float object, which is actually
way *WORSE* than math.sin, even:

sage: a = sin._fast_float_()
sage: timeit('a(3.4r)')
625 loops, best of 3: 809 ns per loop
sage: type(a)
<type 'sage.ext.fast_eval.FastDoubleFunc'>


William
```



---

Attachment


---

Comment by mhansen created at 2008-11-21 17:11:38

This is much better than my implementation :-)

Applies to 3.2 and passes tests.


---

Comment by mabshoff created at 2008-11-21 19:13:57

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-21 19:13:57

Resolution: fixed
