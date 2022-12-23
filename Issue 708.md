# Issue 708: performance issue -- Magma is way faster at testing some polynomials for irreducibility

Issue created by migration from https://trac.sagemath.org/ticket/708

Original creator: was

Original creation time: 2007-09-20 17:40:44

Assignee: somebody

CC:  burcin


```
sage: R = QQ['x']
sage: f = R.random_element(1000)
sage: time f.is_irreducible()
CPU times: user 31.45 s, sys: 0.10 s, total: 31.54 s
Wall time: 31.79
True
sage: g = magma(f)
sage: time g.IsIrreducible()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 2.57
true
```



---

Comment by mabshoff created at 2008-08-27 01:29:09

This is still the case:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.alpha0, Release Date: 2008-08-22                |
| Type notebook() for the GUI, and license() for information.        |
sage: R = QQ['x']
sage: f = R.random_element(1000)
sage: time f.is_irreducible()
CPU times: user 57.86 s, sys: 0.13 s, total: 57.99 s
Wall time: 58.02 s
True
sage: g = magma(f)
sage: time g.IsIrreducible()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 4.22 s
true
sage: 
Exiting SAGE (CPU time 0m58.11s, Wall time 3m26.33s).
Exiting spawned Magma process.
```

Is anyone working in that area?

Cheers,

Michael


---

Attachment

There is a simple way of getting within range of Magma's speed: by Gauss' lemma, we can clear the denominators to get a polynomial over the integers, then test it for irreducibility using the significantly faster code over ZZ.

See the attached patch.  I'm getting a speedup factor of about 10, but I can't compare to Magma since I don't have it.


---

Comment by malb created at 2008-08-30 00:31:13

Speed report:


```
sage: R = QQ['x']
sage: f = R.random_element(1000)
sage: time f.is_irreducible()
CPU times: user 2.06 s, sys: 0.00 s, total: 2.06 s
Wall time: 2.06 s
True
sage: g = magma(f)
sage: t = magma.cputime()
sage: sage: time g.IsIrreducible()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 5.24 s
true
sage: magma.cputime(t)
5.2400000000000002
```


The new code seems to compare favorably to Magma. IIRC Bill Hart suggested to do pretty much everything with Flint w.r.t. to QQ[x]. Maybe that could be another ticket/task.


---

Comment by mabshoff created at 2008-08-30 01:48:25

Merged in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-30 01:48:25

Resolution: fixed
