# Issue 2716: convex hulls and polyhedral functions

Issue created by migration from https://trac.sagemath.org/ticket/2716

Original creator: mhampton

Original creation time: 2008-03-29 13:49:51

Assignee: mabshoff

The patch adds functions to compute convex hulls and change back and forth from vertices to inequality descriptions of polytopes/polyhedra, using only cddlib and not polymake.


---

Comment by mabshoff created at 2008-03-29 13:57:51

Changing component from Cygwin to linear algebra.


---

Comment by mabshoff created at 2008-03-29 13:57:51

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2008-03-29 13:58:42

Changing component from linear algebra to geometry.


---

Comment by mabshoff created at 2008-03-29 13:58:42

Changing assignee from was to mhampton.


---

Comment by mhampton created at 2008-03-29 14:30:31

Changing priority from major to minor.


---

Comment by mhampton created at 2008-03-29 14:30:31

Changing type from defect to enhancement.


---

Comment by mhampton created at 2008-04-05 16:56:37

A much improved version is attached as a patch against sage-2.11.  I have moved some general functionality to a polyhedra.py module, which I hope will eventually provide most of what polytope.py does not, but without polymake (just cddlib).  These functions are also used for a 3D groebner fan function.


---

Comment by mhampton created at 2008-04-05 16:56:37

Changing assignee from mhampton to somebody.


---

Comment by malb created at 2008-04-05 22:30:05

*Review*
 * I cannot vouch for the math
 * `trac_2716_gfan_polyhedra.patch` applies cleanly against `3.0.alpha1`
 * all methods have doctests
 * I find the coding/interface style slightly strange and un-Sage-ish:

```
sage: po = extreme_verts([[1,2],[2,2],[2,1],[0,0]]) 
sage: po.ex_vertices 
[[1, 1, 2], [1, 2, 2], [1, 2, 1], [1, 0, 0]] 
```

 * But that shouldn't be a show-stopper, I'm giving it a preliminary positive review
 * PS: My first review with mercurial queues ;-)


---

Comment by mhampton created at 2008-04-05 23:04:52

I do plan on cleaning this up more; I am still giving a lot of thought
to what polytope classes there should be, and how they should behave,
etc.   When I rearrange things again I will try to give variable names
more suggestive names.    In the example below, "po" was my temporary
shorthand for PolyhedralObject, which is a class that I know I will
change.

Thanks for the review.


---

Comment by malb created at 2008-04-05 23:21:26

Replying to [comment:7 mhampton]:
> I do plan on cleaning this up more; I am still giving a lot of thought
> to what polytope classes there should be, and how they should behave,
> etc.   When I rearrange things again I will try to give variable names
> more suggestive names.    In the example below, "po" was my temporary
> shorthand for PolyhedralObject, which is a class that I know I will
> change.

Sorry for not being more precise:
 * it might be fine for the particular situation but general, having functions rather than methods feels odd to me. However, in some cases it is just better.
 * It is quite seldom in the Sage library that attributes are actually accessed as attributes, like: `po.ex_vertices`, whereas in Sage it is more likely to meet `po.ex_vertices()`. However, Python encourages your coding style and I think Sage is off the path here.


---

Comment by mabshoff created at 2008-04-26 04:17:55

Marshall, trac_2716_gfan_polyhedra.patch fails quiet badly when I attempt to merge this into 3.0. Can you rebase this? I know you spend a lot of time in this area, so let's get this finally merged.

Cheers,

Michael


---

Comment by mhampton created at 2008-04-27 15:35:26

Attaching patch against 3.0; passes tests for me.  Several bugfixes from previous patch as well.


---

Comment by mhampton created at 2008-04-27 15:35:26

Changing keywords from "" to "polyhedra, convex hull, polytope, gfan".


---

Comment by wdj created at 2008-04-27 20:08:44

Installs cleanly. sage -testall passed all tests (on an old rather cantankerous machine) but 

```
The following tests failed:


        sage -t  devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
```

However, when I reran sage -t devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py,
I got all tests passed. I especially like the render_wireframe plotting function.

Looks like a very interesting patch and I vote to apply it.


---

Comment by mabshoff created at 2008-04-28 00:14:39

We frown upon `from foo.bar import *`, so please fix those.

Cheers,

Michael


---

Attachment

improved improved patch (cleaned up import * issues)


---

Comment by mhampton created at 2008-04-28 18:59:59

I believe I have made my imports explicit and minimal.


---

Comment by mabshoff created at 2008-04-29 00:18:48

Resolution: fixed


---

Comment by mabshoff created at 2008-04-29 00:18:48

Merged trac_2716_improved.patch in Sage 3.0.1.alpha1
