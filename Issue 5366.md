# Issue 5366: graphplot arrowheads are hidden in multi-edge digraphs

Issue created by migration from https://trac.sagemath.org/ticket/5366

Original creator: ekirkman

Original creation time: 2009-02-24 23:53:18

Assignee: ekirkman, rlm

Kristin Lauter pointed out that the following input:

```
sage: S = SupersingularModule(389)
sage: D = DiGraph(S.hecke_matrix(2))
sage: D.plot(vertex_size=50).show(figsize=10)
```

produces a graph where the arrowheads of some edges are hidden by the vertex.  (See attachment t2.png for output).

This is going to be a one-ish line fix that I can post as soon as I'm done building 3.3.



---

Comment by ekirkman created at 2009-02-24 23:57:52

Current buggy output.  (I will repost a new picture with the patch).


---

Attachment

here's the fix...


---

Attachment

And the new plot output...


---

Comment by rlm created at 2009-02-26 23:28:17

I tested the patch against sage-3.3, and the first run gave errors of the form

```
sage -t  sage/graphs/graph.py
Traceback (most recent call last):
  File "/Users/rlmill/sage-3.3/tmp/graph.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/misc/all.py", line 70, in <module>
    from sage_input import sage_input
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/misc/sage_input.py", line 163, in <module>
    from sage.misc.functional import parent
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/misc/functional.py", line 34, in <module>
    from sage.rings.complex_double import CDF
  File "complex_double.pyx", line 85, in sage.rings.complex_double (sage/rings/complex_double.c:11756)
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/rings/complex_field.py", line 81, in ComplexField
    C = ComplexField_class(prec)
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/rings/complex_field.py", line 161, in __init__
    self._populate_coercion_lists_(coerce_list=[complex_number.RRtoCC(self._real_field(), self)])
  File "complex_number.pyx", line 1745, in sage.rings.complex_number.RRtoCC.__init__ (sage/rings/complex_number.c:11017)
  File "map.pyx", line 41, in sage.categories.map.Map.__init__ (sage/categories/map.c:1772)
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/categories/homset.py", line 140, in Hom
    from sage.rings.homset import RingHomset
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/rings/homset.py", line 17, in <module>
    import quotient_ring
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py", line 30, in <module>
    import sage.rings.polynomial.multi_polynomial_ideal
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 206, in <module>
    from sage.interfaces.all import (singular as singular_default,
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/interfaces/all.py", line 7, in <module>
    from gap import gap, gap_reset_workspace, gap_console, gap_version, is_GapElement, Gap
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 902, in <module>
    age = now - os.path.getatime(GAP_DIR + '/' + F)
  File "/Users/rlmill/sage-3.3/local/lib/python2.5/posixpath.py", line 147, in getatime
    return os.stat(filename).st_atime
OSError: [Errno 2] No such file or directory: '/Users/rlmill/.sage//gap//workspace-90824993'
```

but the second run passed all tests. Since this has nothing to do with the patch, I'm assuming this was one-time weirdness.


---

Comment by mabshoff created at 2009-02-26 23:34:22

Replying to [comment:2 rlm]:
> I tested the patch against sage-3.3, and the first run gave errors of the form

<SNIP>
> OSError: [Errno 2] No such file or directory: '/Users/rlmill/.sage//gap//workspace-90824993'

If you used -tp there is a race condition in the creation of the GAP workspace, so not surprises there if this was how you tested.

> but the second run passed all tests. Since this has nothing to do with the patch, I'm assuming this was one-time weirdness.

Yep, the fix is to run "sage -c" once before doctesting with -tp so the GAP workspace is current and then the race condition goes away. This has annoyed me enough on sage.math [with -tp 18 :)] that I made this #5389 even though rlm's problem might be unrelated.

Cheers,

Michael


---

Comment by rlm created at 2009-02-26 23:38:44

I was testing in parallel, so that must have been what happened, since testing the individually failing files with -t worked fine.


---

Comment by mabshoff created at 2009-02-28 15:57:48

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 15:57:48

Resolution: fixed
