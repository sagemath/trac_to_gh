# Issue 995: Generalize polynomial .roots() method by adding optional ring= parameter for result ring

Issue created by migration from https://trac.sagemath.org/ticket/995

Original creator: cwitty

Original creation time: 2007-10-25 06:21:10

Assignee: cwitty


```
<wstein> Better might be to improve the roots function so that it can take 
 an optional ring as input.
 e.g.,
    f = x^3 + 1 (over QQ say), then
 f.roots(ComplexField(200))
 would give the roots in that field.
 What do you think?
<cwitty> I like it.
 I like it a lot.
 f.roots(RealField(200)), f.roots(AA), f.roots(RealIntervalField(200)) ...
<wstein> Yep.
 And it could be intelligent, but when it doesn't know what to do just 
 return f.change_ring(R).roots(...)
 But in many cases it could use that f is defined over a better ring
 than R, e.g., QQ, to find the roots
 to lots of precision.
```



---

Attachment


---

Comment by cwitty created at 2007-11-04 04:01:57

This adds a ring= argument for the univariate polynomial .roots() method, so that you can find the complex roots of a polynomial given over QQ (along with many other possibilities).  Along with that change, we change the default root-finding algorithm for polynomials over RR and CC to numpy instead of Pari; this is vastly faster, but occasionally slightly less accurate, and does not give exactly the same answers on different architectures.

These patches depend on the patch from #1096; without it, some of the doctests will fail.

These patches pass -testall on my 32-bit and 64-bit x86 Linux boxes, but have not been tested on other platforms; it's possible that the floating-point answers will vary more than allowed by the doctests.


---

Comment by robertwb created at 2007-11-04 04:18:19

It works great in almost all cases, but


```
sage: R.<x> = ZZ[]
sage: f = 2*x-3
sage: f.roots(ZZ)
[(3/2, 1)]
```


Perhaps this is due to the default behavior of roots() over Z, not the new code (which is really nice).


---

Comment by cwitty created at 2007-11-04 04:30:07

The bug Robert found here is now #1100.  (It's not caused by this patch.)


---

Comment by mabshoff created at 2007-11-06 21:44:20

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 21:44:20

Resolution: fixed
