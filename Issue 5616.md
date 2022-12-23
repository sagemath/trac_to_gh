# Issue 5616: speed regression with fast_callable

Issue created by migration from https://trac.sagemath.org/ticket/5616

Original creator: robertwb

Original creation time: 2009-03-26 08:31:17

Assignee: cwitty

Before (vanilla 3.4)


```
sage: var('x,y')
(x, y)
sage: time P = parametric_plot3d((x, y, x*y), (x, -10, 10), (y, -10, 10), plot_points=(500,500))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time P.triangulate()
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.08 s
```


after (3.4 + #5093)


```
sage: sage: var('x,y')
(x, y)
sage: sage: time P = parametric_plot3d((x, y, x*y), (x, -10, 10), (y, -10, 10), plot_points=(500,500))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: sage: time P.triangulate()
CPU times: user 0.28 s, sys: 0.02 s, total: 0.30 s
Wall time: 0.30 s
```


I think this is due to there not being an interface to evaluate fast_callable objects without passing through Python. Perhaps a 


```
cdef int call_c(void* args, void* ret) except -1
```


method should be attached to the generic interpreter wrapper class (to be overridden by the subclasses), and those with specific knowledge about the various implementations could then use this interface (e.g. RDF passes double*). 


---

Attachment


---

Attachment


---

Comment by cwitty created at 2009-03-28 20:37:03

The attached patches should fix this problem.  (Apply both patches, in order.)

I split the fix into two logically separate pieces.  The first only generates .pxd files for the fast_callable interpreters; this should have no observable effect.  The second adds a .call_c() cdef method to the interpreters.  (Each interpreter has its own call_c, rather than inheriting a common method as Robert suggested; I did it this way because I like typechecking.)

The second patch also modifies parametric_surface.pyx to take advantage of the call_c() method when generating the surface.  I left the old code in as well; this means you can benchmark fast_eval vs. fast_callable by setting sage.ext.fast_eval.new_fast_float to False/True.

These patches depend on #5622.


---

Comment by cwitty created at 2009-03-28 20:37:03

Changing status from new to assigned.


---

Comment by robertwb created at 2009-03-29 10:48:19

Excellent. Yes, generating specific pxd files with typed call_c methods is a better way to go. Code is good and this completely resolves the issue.


---

Comment by mabshoff created at 2009-03-31 06:33:01

Resolution: fixed


---

Comment by mabshoff created at 2009-03-31 06:33:01

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael
