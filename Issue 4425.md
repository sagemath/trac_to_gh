# Issue 4425: sqrt(4) returns a SymbolicComposition instead of the number 2!

Issue created by migration from https://trac.sagemath.org/ticket/4425

Original creator: was

Original creation time: 2008-11-02 17:34:58

Assignee: somebody

In Sage-3.1.4 we have this, which I consider wrong:


```
sage: n = 4
sage: type(sqrt(n))
<class 'sage.calculus.calculus.SymbolicComposition'>
sage: type(n.sqrt())
<type 'sage.rings.integer.Integer'>
```


I think sqrt(foo) should first check if foo has a sqrt method, and
if so call it.    I realize there is a subtle problem here, because
the integer sqrt function calls the symbolic calculus one!  So we
need some sort of architecture to fix this right.   This isn't trivial.


---

Comment by kcrisman created at 2008-11-04 03:41:24

Changing assignee from somebody to kcrisman.


---

Comment by kcrisman created at 2008-11-04 03:41:24

This patch takes care of the problem as stated, passes tests for integer.pyx and rational.pyx; test for calculus.py times out (as it always does on my computer, not just for this patch).  

I am _fairly_ certain it also does not introduce some new endless loops or other weird bugs, but that would be worth checking out by any reviewer.


---

Comment by kcrisman created at 2008-11-04 03:41:48

Based on 3.2.alpha0


---

Attachment

I think that the .sqrt() method in Integer and Rational should call sqrt._do_sqrt instead of creating the SymbolicComposition themselves.  For example, see


```
sage: sqrt._do_sqrt(4)
2
sage: type(_)
<class 'sage.calculus.calculus.SymbolicComposition'>
sage: sqrt._do_sqrt(5)
sqrt(5)
sage: sqrt._do_sqrt(5, all=True)
[sqrt(5), -sqrt(5)]
```



---

Attachment

I've attached a patch which makes the change I suggested.  What are your thoughts?


---

Attachment


---

Comment by kcrisman created at 2008-11-06 14:34:12

This is fine; in the meantime I did get around to implementing this.  However, I also moved the prec evaluation to the _do_sqrt function as well, since it seemed consonant with your review.

After thinking about it, it also makes more sense do that because if for some reason something lands in sqrt with prec which isn't RR, Rational, Integer, etc. then _do_sqrt() should still make the square root be in RR if x is positive; the previous behavior was to automatically put it in CC.  

Does this seem okay?


---

Comment by was created at 2008-11-06 19:48:40

I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. 

The original patch sqrt-nonsymbolic-1.patch and that patch plus the attached followup sqrt-nonsymblic-2.patch together pass all doctests for me in rings and calculus.


---

Attachment

mabshoff -- apply this and sqrt-nonsymbolic-1.patch; don't apply anything else


---

Comment by kcrisman created at 2008-11-06 21:02:35

Replying to [comment:5 was]:
> I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. 

This seems okay; I didn't have time to merge it but the new tests behave correctly.  So this means that the following is the desired behavior for when to extend and when not to extend?

```
sage: sqrt._do_sqrt(Integer(3),extend=False)
sqrt(3)
sage: a=3; type(a)
<type 'sage.rings.integer.Integer'>
sage: a.sqrt(extend=False)
---------------------------------------------------------------------------
ValueError: square root of 3 not an integer
```

If so, then let's finally let the square root of 4 be 2!


---

Comment by mabshoff created at 2008-11-08 07:12:11

Resolution: fixed


---

Comment by mabshoff created at 2008-11-08 07:12:11

Merged sqrt-nonsymbolic-1.patch and sqrt-nonsymbolic-2.patch in Sage 3.2.rc0
