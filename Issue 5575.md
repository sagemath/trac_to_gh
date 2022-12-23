# Issue 5575: bug in span

Issue created by migration from https://trac.sagemath.org/ticket/5575

Original creator: was

Original creation time: 2009-03-20 11:03:00

Assignee: was


```
sage: V = QQ^4
sage: a = [V.random_element() for _ in range(4)]
sage: span(a)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/19499/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(gens, base_ring, check, already_echelonized)
    456         base_ring, gens = gens, base_ring
    457         
--> 458     R = self.base_ring() if base_ring is None else base_ring
    459 
    460     if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):

NameError: global name 'self' is not defined
```



---

Attachment


---

Comment by cremona created at 2009-03-21 19:12:00

Review:  patch looks fine and applies ok to 3.4.   There is an appropriate doctest and all tests in sage/modules pass.   Good!


---

Comment by mabshoff created at 2009-03-23 19:36:14

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 19:36:14

Resolution: fixed
