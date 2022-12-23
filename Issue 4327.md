# Issue 4327: Root systems plots

Issue created by migration from https://trac.sagemath.org/ticket/4327

Original creator: nthiery

Original creation time: 2008-10-20 08:40:33

Assignee: mhansen

CC:  sage-combinat alubovsky

Port from MuPAD-Combinat the plotting facilities for (affine) root systems.

This will require in particular the port of:
 - row/column annihilator
 - a,acheck,c coeffs
 - translation factors


---

Comment by nborie created at 2009-07-29 08:22:04

I find this ticket is completely integrated inside #4326

I remember that i did this job. So feel free to merge/destroy/erase this ticket. I don't know the current way to dealt with such ticket...


---

Comment by nthiery created at 2009-07-30 13:45:17

Actually, there is still room for improvement to the current plots. So let's keep this open. I'll just update the description.


---

Comment by nborie created at 2012-09-13 12:30:33

Hello,

Here is a patch which realize the  porting of what was done in MuPAD... I tried to do my best but this patch really need a strong English language review. For anybody interssinting in reviewing, commenting, or anything... here are some pointers :

MuPAD example :
http://wstein.org/home/wstein/www/home/nthiery/2008-03-01-RootSystemPlots.html

Sage-support discussion :
https://groups.google.com/forum/?hl=fr&fromgroups=#!topic/sage-support/fRTEE_IECzU


---

Comment by ncohen created at 2013-01-21 14:02:29

Hellooooooooooo !!

Nicolas M. Thiéry : that's the ticket that should have been set to `needs_review` ages ago and never was. It would be nice to have this into Sage, if only to be able to print beautifu Sage-combinat posters with fancy pictures inside.

Nathann


---

Comment by ncohen created at 2013-01-21 14:02:29

Changing status from new to needs_review.


---

Comment by nthiery created at 2013-02-25 01:37:52

I'll upload a (quite heavily) refactored patch shortly.


---

Comment by nthiery created at 2013-02-25 01:37:52

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2013-03-04 03:50:41

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2013-03-05 05:32:27

So, the test pass, but the startup module complains about the new module that is imported on startup. I'll try with a lazy import tomorrow. I leave it as needs review, as the review of all the rest can continue!


---

Comment by nthiery created at 2013-03-06 03:22:40

Replying to [comment:8 nthiery]:
> So, the test pass, but the startup module complains about the new module that is imported on startup. I'll try with a lazy import tomorrow. I leave it as needs review, as the review of all the rest can continue!

Hmm, I just had a look, but am not sure how to handle this. Lazy importing works just fine for the code, but then:

```
    sage: sage.combinat.root_system.plot?
```


fails, whereas I think we want to support this natural way to access
this tutorial.

The seemingly natural solution would be to lazy import the full module. However:

```
sage: sage.misc.lazy_import.lazy_import('sage.combinat.root_system', 'plot')
sage: type(plot)
sage.misc.lazy_import.LazyImport
sage: plot
/opt/sage/sage : ligne 135 :  6989 Erreur de segmentation  (core dumped) "$SAGE_ROOT/spkg/bin/sage" "$@"
Process SAGE exited abnormally with code 139
```


I'll post on Sage-devel on this topic. In the mean time the rest of
the review can continue!

If we can't get a good solution shortly, I am at this point in favor
of sticking to a non lazy import in order to allow for accessing the
tutorial as above, even if the price is to import (yet another) new
module in Sage.

Cheers,
                         Nicolas


---

Comment by nthiery created at 2013-03-11 03:32:31

The updated patch implements wireframe drawing for 3D alcoves, and specifying a color as None to disable certain pieces. It also fixes a couple typos here and there in the doc.


---

Comment by tscrim created at 2013-04-13 20:22:50

Hey Nicolas<sup>2</sup>,

Does this conflict with #2023, and if so, which patch do you want to have the dependency?

Thanks,

Travis


---

Comment by nthiery created at 2013-04-13 20:31:53

It could possibly conflict. Both patches should get soon into Sage, and I already had a good look at #2023. So once we have had that little discussion with Dan, we should just get it in. And then #4327 which is already based on it anyway.


---

Comment by nthiery created at 2013-05-07 20:12:03

Folded in Travis' reviewers patch and reuploaded.


---

Comment by tscrim created at 2013-05-07 20:41:08

Looks good. Thank you.


---

Comment by tscrim created at 2013-05-07 20:41:08

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2013-05-08 18:04:22

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2013-05-08 19:34:00

Uploaded a new version (double checked by Travis) fixing one of the long doctest failure on 5.10. It was caused by the new matplotlib that emits a warning for arrows of length 0:

```
sage: arrow([1,1],[1,1])
/home/nthiery/sage-5.10.beta1/local/lib/python2.7/site-packages/matplotlib/patches.py:3039: RuntimeWarning: invalid value encountered in double_scalars
  ddx = pad_projected * dx / cp_distance
/home/nthiery/sage-5.10.beta1/local/lib/python2.7/site-packages/matplotlib/patches.py:3040: RuntimeWarning: invalid value encountered in double_scalars
  ddy = pad_projected * dy / cp_distance
/home/nthiery/sage-5.10.beta1/local/lib/python2.7/site-packages/matplotlib/patches.py:3043: RuntimeWarning: invalid value encountered in double_scalars
  dx = dx / cp_distance * head_dist
/home/nthiery/sage-5.10.beta1/local/lib/python2.7/site-packages/matplotlib/patches.py:3044: RuntimeWarning: invalid value encountered in double_scalars
  dy = dy / cp_distance * head_dist
```


The other failure is due to some doctests being ignored. See:

 https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/4m1ydGdiGf8


---

Comment by nthiery created at 2013-05-09 01:50:28

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2013-05-09 01:50:28

Hi Travis,

The updated patch fixes the doc so that later on doctests won't be
ignored, and update the number of ignored doctests in the mean time.

All long tests passed.

Here is the metadiff:

```
diff --git a/trac_4327-root_system_plot_refactor-nt.patch b/trac_4327-root_system_plot_refactor-nt.patch
--- a/trac_4327-root_system_plot_refactor-nt.patch
+++ b/trac_4327-root_system_plot_refactor-nt.patch
@@ -1,5 +1,5 @@
 # HG changeset patch
-# Parent aa718acb2dbac8faab463c994aa7f4052a546363
+# Parent 89d0e0f941ae79ca2d8dd83d3ac6d20a4b82382a
 #4327: Refactor and extend root systems plots
 
 diff --git a/doc/en/reference/combinat/root_systems.rst b/doc/en/reference/combinat/root_systems.rst
@@ -2569,7 +2569,7 @@ diff --git a/sage/combinat/root_system/t
  import ambient_space
  
  class AmbientSpace(ambient_space.AmbientSpace):
-@@ -135,13 +136,38 @@ class AmbientSpace(ambient_space.Ambient
+@@ -135,13 +136,36 @@ class AmbientSpace(ambient_space.Ambient
          given, returns (k, ... ,k), the k-th power of the
          determinant.
  
@@ -2582,14 +2582,8 @@ diff --git a/sage/combinat/root_system/t
          """
          return self.sum(self.monomial(j)*k for j in range(self.n))
  
-+    """
-+    Use barycentric projection by default
-+
-+    .. SEEALSO::
-+
-+        - :meth:`sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations._plot_projection`
-+
-+    EXAMPLES::
++    __doc__ += """
++    By default, this ambient space uses the barycentric projection for plotting::
 +
 +        sage: L = RootSystem(["A",2]).ambient_space()
 +        sage: e = L.basis()
@@ -2604,6 +2598,10 @@ diff --git a/sage/combinat/root_system/t
 +        (2, 2, 3, 0)
 +        sage: L._plot_projection(l)
 +        (0, -1121/1189, 7/3)
++
++    .. SEEALSO::
++
++        - :meth:`sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ParentMethods._plot_projection`
 +    """
 +    _plot_projection = RootLatticeRealizations.ParentMethods.__dict__['_plot_projection_barycentric']
  
@@ -2621,18 +2619,12 @@ diff --git a/sage/combinat/root_system/t
  class AmbientSpace(ambient_space.AmbientSpace):
      """
      EXAMPLES::
-@@ -82,6 +82,32 @@ class AmbientSpace(ambient_space.Ambient
+@@ -82,6 +82,30 @@ class AmbientSpace(ambient_space.Ambient
          return Family({ 1: self([1,0,-1]),
                          2: self([2,-1,-1])})
  
-+    """
-+    Use barycentric projection by default
-+
-+    .. SEEALSO::
-+
-+        - :meth:`sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations._plot_projection`
-+
-+    EXAMPLES::
++    __doc__ += """
++    By default, this ambient space uses the barycentric projection for plotting::
 +
 +        sage: L = RootSystem(["G",2]).ambient_space()
 +        sage: e = L.basis()
@@ -2647,6 +2639,10 @@ diff --git a/sage/combinat/root_system/t
 +        (2, 2, 3, 0)
 +        sage: L._plot_projection(l)
 +        (0, -1121/1189, 7/3)
++
++    .. SEEALSO::
++
++        - :meth:`sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ParentMethods._plot_projection`
 +    """
 +    _plot_projection = RootLatticeRealizations.ParentMethods.__dict__['_plot_projection_barycentric']
 +
@@ -3011,3 +3007,15 @@ diff --git a/sage/combinat/root_system/w
 -            G.axes(False)
 -            return G
 -
+diff --git a/sage/doctest/sources.py b/sage/doctest/sources.py
+--- a/sage/doctest/sources.py
++++ b/sage/doctest/sources.py
+@@ -675,6 +675,8 @@ class FileDocTestSource(DocTestSource):
+             There are 18 tests in sage/combinat/partition.py that are not being run
+             There are 12 tests in sage/combinat/tableau.py that are not being run
+             There are 15 tests in sage/combinat/root_system/cartan_type.py that are not being run
++            There are 8 tests in sage/combinat/root_system/type_A.py that are not being run
++            There are 8 tests in sage/combinat/root_system/type_G.py that are not being run
+             There are 3 unexpected tests being run in sage/doctest/parsing.py
+             There are 1 unexpected tests being run in sage/doctest/reporting.py
+             There are 9 tests in sage/graphs/graph_plot.py that are not being run
```



---

Comment by tscrim created at 2013-05-09 14:45:27

Looks good to me. Thanks Nicolas.


---

Comment by tscrim created at 2013-05-09 14:45:27

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-13 16:16:22

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-05-13 16:16:22

The PDF documentation doesn't build:

```
! Package inputenc Error: Keyboard character used is undefined
(inputenc)                in inputencoding `utf8x'.

See the inputenc package documentation for explanation.
Type  H <return>  for immediate help.
 ...

l.96802 ...}1\PYGZcb{}\$' at the point (0.0,1.0)]}

?  [54]
! Emergency stop.
 ...

l.96802 ...}1\PYGZcb{}\$' at the point (0.0,1.0)]}

!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on combinat.log.
```



---

Attachment


---

Comment by nthiery created at 2013-05-13 20:08:13

Replying to [comment:23 jdemeyer]:
> The PDF documentation doesn't build:
> {{{
> ! Package inputenc Error: Keyboard character used is undefined
> (inputenc)                in inputencoding `utf8x'.
> ...
> }}}

Ah shoot, sorry about that. The docstrings for this method was missing its starting 'r', and which caused a `\a` in it to be misinterpreted as a non UTF-8 character.

The newly updated patch fixes this. While I was at it, it fixes half a dozen other missing 'r' in other methods introduced by this patch.

Since the change is trivial, I am allowing myself to put it back to positive review.

For the record, here is the diff between the two patches:

```
diff --git a/trac_4327-root_system_plot_refactor-nt.patch b/trac_4327-root_system_plot_refactor-nt.patch
--- a/trac_4327-root_system_plot_refactor-nt.patch
+++ b/trac_4327-root_system_plot_refactor-nt.patch
@@ -1,5 +1,5 @@
 # HG changeset patch
-# Parent 89d0e0f941ae79ca2d8dd83d3ac6d20a4b82382a
+# Parent 75e26170e32bcbb5f78e1784a1df985ecb71e1db
 #4327: Refactor and extend root systems plots
 
 diff --git a/doc/en/reference/combinat/root_systems.rst b/doc/en/reference/combinat/root_systems.rst
@@ -631,7 +631,7 @@ new file mode 100644
 +lazy_import("sage.combinat.root_system.root_lattice_realizations", "RootLatticeRealizations")
 +
 +class PlotOptions:
-+    """
++    r"""
 +    A class for plotting options for root lattice realizations.
 +
 +    .. SEEALSO::
@@ -740,7 +740,7 @@ new file mode 100644
 +
 +    @cached_method
 +    def in_bounding_box(self, x):
-+        """
++        r"""
 +        Return whether ``x`` is in the bounding box.
 +
 +        INPUT:
@@ -763,7 +763,7 @@ new file mode 100644
 +        return self.bounding_box.contains(self.projection(x))
 +
 +    def text(self, label, position):
-+        """
++        r"""
 +        Return text widget with label ``label`` at position ``position``
 +
 +        INPUT:
@@ -851,7 +851,7 @@ new file mode 100644
 +                return self._color("other")
 +
 +    def projection(self, v):
-+        """
++        r"""
 +        Return the projection of ``v``.
 +
 +        INPUT:
@@ -880,7 +880,7 @@ new file mode 100644
 +        return v
 +
 +    def intersection_at_level_1(self, x):
-+        """
++        r"""
 +        Return ``x`` scaled at the appropriate level, if level is set;
 +        otherwise return ``x``.
 +
@@ -912,7 +912,7 @@ new file mode 100644
 +            return x
 +
 +    def empty(self, *args):
-+        """
++        r"""
 +        Return an empty plot.
 +
 +        EXAMPLES::
@@ -1255,7 +1255,7 @@ new file mode 100644
 +
 +@cached_function
 +def barycentric_projection_matrix(n, angle=0):
-+    """
++    r"""
 +    Returns a family of `n+1` vectors evenly spaced in a real vector space of dimension `n`
 +
 +    Those vectors are of norm `1`, the scalar product between any two
@@ -2339,7 +2339,7 @@ diff --git a/sage/combinat/root_system/r
 +
 +
 +        def plot_bounding_box(self, **options):
-+            """
++            r"""
 +            Plot the bounding box.
 +
 +            INPUT:

```



---

Comment by nthiery created at 2013-05-13 20:08:33

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-05-13 20:18:18

Replying to [comment:24 nthiery]:
> Since the change is trivial, I am allowing myself to put it back to positive review.

Assuming that you checked that the PDF documentation does build, that's okay.


---

Comment by nthiery created at 2013-05-13 21:09:32

Replying to [comment:26 jdemeyer]:
> Assuming that you checked that the PDF documentation does build, that's okay.

Yup, I did. Well at least for reference/combinat.


---

Comment by jdemeyer created at 2013-05-16 06:19:03

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-05-16 06:19:03


```
sage -t devel/sage/sage/combinat/root_system/root_lattice_realizations.py
**********************************************************************
File "devel/sage/sage/combinat/root_system/root_lattice_realizations.py", line 1840, in sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.Pare
ntMethods.plot_roots
Failed example:
    list(RootSystem(["A",2]).root_lattice().plot_roots("all"))
Expected:
    [Arrow from (0.0,0.0) to (1.0,0.0),
     Text '$\alpha_{1}$' at the point (1.05,0.0),
     Arrow from (0.0,0.0) to (0.0,1.0),
     Text '$\alpha_{2}$' at the point (0.0,1.05),
     Arrow from (0.0,0.0) to (1.0,1.0),
     Text '$\alpha_{1} + \alpha_{2}$' at the point (1.05,1.05),
     Arrow from (0.0,0.0) to (-1.0,0.0),
     Text '$\left(-1\right)\alpha_{1}$' at the point (-1.05,0.0),
     Arrow from (0.0,0.0) to (0.0,-1.0),
     Text '$\left(-1\right)\alpha_{2}$' at the point (0.0,-1.05),
     Arrow from (0.0,0.0) to (-1.0,-1.0),
     Text '$\left(-1\right)\alpha_{1} + \left(-1\right)\alpha_{2}$' at the point (-1.05,-1.05)]
Got:
    [Arrow from (0.0,0.0) to (1.0,0.0), Text '$\alpha_{1}$' at the point (1.05,0.0), Arrow from (0.0,0.0) to (0.0,1.0), Text '$\alpha_{2}$' at the point (0.0,1.05), Arr
ow from (0.0,0.0) to (1.0,1.0), Text '$\alpha_{1} + \alpha_{2}$' at the point (1.05,1.05), Arrow from (0.0,0.0) to (-1.0,0.0), Text '$-\alpha_{1}$' at the point (-1.05,
0.0), Arrow from (0.0,0.0) to (0.0,-1.0), Text '$-\alpha_{2}$' at the point (0.0,-1.05), Arrow from (0.0,0.0) to (-1.0,-1.0), Text '$-\alpha_{1} - \alpha_{2}$' at the p
oint (-1.05,-1.05)]
**********************************************************************
```



---

Comment by jdemeyer created at 2013-05-16 06:28:33

Never mind, last doctest failure is because of #13735.


---

Comment by jdemeyer created at 2013-05-16 06:28:33

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-05-17 06:33:19

Resolution: fixed


---

Comment by nthiery created at 2013-05-19 22:16:25

Yippee!

Thanks Nicolas, Travis, and everyone who contributed to get this done!


---

Comment by vbraun created at 2013-05-25 10:57:10

The `plot_expose()` function should be a method of plot objects. Its definitely useful outside of root lattices. See #14640
