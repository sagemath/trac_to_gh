# Issue 2588: [with patch, needs review] documentation and tests for sage.schemes.hyperelliptic_curves.jacobian_morphism

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-18 18:38:29

Assignee: was

CC:  ncalexan

Keywords: jacobian morphism hyperelliptic curve

Before:


```
----------------------------------------------------------------------
sage/schemes/hyperelliptic_curves/jacobian_morphism.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/schemes/hyperelliptic_curves/jacobian_morphism.py: 0% (0 of 15)

Missing documentation:
         * cantor_reduction_simple(a1,b1,f,genus)
         * cantor_reduction(a,b,f,h,genus)
         * cantor_composition_simple(D1,D2,f,genus)
         * cantor_composition(D1,D2,f,h,genus)
         * __init__(self, parent, polys, reduce=True, check=False)
         * __repr__(self)
         * scheme(self)
         * list(self)
         * __add__(self,other)
         * __cmp__(self, other)
         * __nonzero__(self)
         * __sub__(self, other)
         * __neg__(self)
         * __mul__(self, n)
         * _rmul_(self, n)

----------------------------------------------------------------------
```


After:


```
----------------------------------------------------------------------
./jacobian_morphism.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE ./jacobian_morphism.py: 100% (17 of 17)
----------------------------------------------------------------------
```


The final `s == loads(dumps(s))` requires lots of other fixes to happen first, so it could be a while.


---

Attachment

Review:  this looks like an excellent job with a lot of useful explanations and examples.  I successfully applied the patch to 2.10.4.rc0.  Testing all files in sage/schemes/hyperelliptic/ resulted in one error:

```
**********************************************************************
File "jacobian_morphism.py", line 382:
    sage: print latex(Q + Q)
Expected:
    \left(x^{2} + 5x + 1, y + 3\alpha x + 6\alpha + 2\right) # known failure (trac #2586)
Got:
    \left(x^{2} + 5x + 1, y + 3\alphax + 6\alpha + 2\right)
**********************************************************************
```



---

Comment by ncalexan created at 2008-03-18 22:34:21

That example is marked known failure and the relevant trac number (#2586) is beside it.  I am happier with a useful failing doctest than no doctest, or a useless doctest, or a doctest certifying bad output.

Thanks for the prompt review!


---

Comment by mabshoff created at 2008-03-19 12:15:50

Replying to [comment:2 ncalexan]:
> That example is marked known failure and the relevant trac number (#2586) is beside it.  I am happier with a useful failing doctest than no doctest, or a useless doctest, or a doctest certifying bad output.
> 
> Thanks for the prompt review!

I would recommend merging everything but the failing doctest and merge that hunk once #2586 is fixed. Any objections, Nick?

Cheers,

Michael


---

Comment by ncalexan created at 2008-03-19 19:21:31

Sure, that's fine by me.  Maybe it's better to certify the failing output and change it when #2586 is complete.


---

Comment by mabshoff created at 2008-03-20 01:40:44

Nick, I changed the above lines to 

```
+            sage: print latex(Q + Q)
+            \left(x^{2} + 5x + 1, y + 3\alphax + 6\alpha + 2\right) # this is a bug - see trac #2586
```

Once #2586 is fixed the doctest will fail and I am sure the person will fix the doctest.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 01:41:02

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-20 01:41:02

Resolution: fixed


---

Attachment

this patch actually fixes the stupid mistake I introduces in the changed doctest
