# Issue 6954: [with patch, needs review] latex output for dictionaries

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-09-18 08:41:21

Assignee: was

Keywords: latex

The attached patch implements latex output for dictionaries:


```
sage: var('x,y')
sage: latex({x: y^2, y: 1/2})
\left\{y\rightarrow \frac{1}{2}, x\rightarrow y^{2}\right\}
```



---

Comment by jhpalmieri created at 2009-09-18 17:03:33

Two comments: first, this doesn't pass doctests, due to ordering issues in dictionaries:

```
**********************************************************************
File "/Applications/sage/devel/sage/sage/misc/latex.py", line 257:
    sage: latex(d)
Expected:
    \left\{2\rightarrow x + \sin\left(y^{2}\right), z\rightarrow \left[1, 2, x^{2}\right], y\rightarrow 2, x\rightarrow \frac{1}{2} \, y\right\}
Got:
    \left\{2\rightarrow x + \sin\left(y^{2}\right), x\rightarrow \frac{1}{2} \, y, y\rightarrow 2, z\rightarrow \left[1, 2, x^{2}\right]\right\}
```

This is on a Mac, OS X 10.5, 32-bit.  Doctests pass on 64-bit OS X.  Maybe there should be different doctests depending on 32-bit vs. 64-bit, as in the `__hash__` method in `sage/rings/padics/padic_capped_relative_element.pyx`.  (Or maybe it's not a 32/64-bit issue; maybe the doctest should just be modified so order doesn't matter.)

Second, I think I would prefer a colon rather than an arrow: I think the typeset version should mimic the string representation, just as we do for lists and tuples.  (I don't feel that strongly about this.)


---

Comment by jason created at 2009-09-19 03:07:23

Replying to [comment:1 jhpalmieri]:

> Second, I think I would prefer a colon rather than an arrow: I think the typeset version should mimic the string representation, just as we do for lists and tuples.  (I don't feel that strongly about this.)

I agree; we should have a colon, since there isn't a completely standard latex notation for dictionaries, and a colon will be less likely to confuse the user who is used to seeing it as text.


---

Comment by jason created at 2009-09-19 03:07:58

If we insist on having an arrow, it seems to make more sense to do a \mapsto arrow, or a knuth-style \leftarrow.


---

Attachment


---

Comment by whuss created at 2009-09-23 08:00:54

I changed the patch to use a colon, and added a seperate doctest for 64bit.
Unfortunately I don't have access to a machine with OS X, so I cannot test
this myself.


---

Comment by jhpalmieri created at 2009-09-23 17:26:01

I like the colon better; thanks.  I'm having problems with the same doctest, though, and I don't think it's a 32/64-bit issue; I get one answer with a 32-bit build on a mac, a different answer with a 64-bit build on a mac, and still a different answer on sage.math.  So maybe the doctest should be modified so order doesn't matter, say a dictionary with a single entry like

```
sage: d = {(1,2,3): [y/2, sin(z^2)]}
sage: latex(d)
...
```

I'm attaching a patch which makes this change.  I'll give the main patch (trac_6954-latex_dict.patch) a positive review, and if my change is okay, the whole ticket should get a positive review.


---

Comment by jhpalmieri created at 2009-09-23 17:26:32

apply on top of the other patch


---

Attachment

Looks good to me.  Apply both patches.


---

Comment by mvngu created at 2009-09-26 08:15:18

Resolution: fixed


---

Comment by mvngu created at 2009-09-26 08:15:18

Merged both patches.


---

Comment by mvngu created at 2009-09-27 10:53:26

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
