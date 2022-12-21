# Issue 9211: graph vertices cut off

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-11 06:48:32

Assignee: jason, mvngu, ncohen, rlm

CC:  rbeezer kcrisman kini

Though #7299 helped, graph vertices are still cut off.

With the updated matplotlib spkg at #9210, we can turn off clipping of the matplotlib scatterplot, or with a more recent (SVN right now) version of matplotlib, we could probably add some bbox_extra_artists to the savefig which takes those artists into account when calculating the bounding box (when bbox_inches='tight').

Either way, a real fix should be possible soon.


---

Comment by jason created at 2010-06-11 06:49:44

Here is a good example showing the problem (still):


```
a=matrix([[1,2],[3,4]])

var('x y z w')
b=matrix([[x,y],[z,w]])

a.set_immutable()
b.set_immutable()

K=DiGraph({a:[b]})
show(K, vertex_size=800)

```



---

Attachment


---

Comment by jason created at 2010-06-12 21:24:40

This patch depends on the matplotlib spkg at #9221.  I don't know if the patch is very elegant.  I'll trust the reviewer's comments on that.  The problem is that it lets the scatter plot vertices extend beyond the frame (relying on the user adjusting the axes_pad option to extend the frame).


---

Comment by jason created at 2010-06-12 21:24:40

Changing status from new to needs_review.


---

Comment by jason created at 2010-06-12 22:34:03

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-06-12 22:34:03

The patch doesn't work for multiple-edge graphs (they are drawn completely differently than graphs without multiple edges).  In fact, we probably ought to draw all graphs using CircleCollection objects rather than scatter_plot or Circles.


---

Comment by jason created at 2010-08-28 14:06:25

Here's how to draw circles like the ones in scatter plot (where the size doesn't change as you make the figure smaller or bigger: use a CircleCollection argument and use different transforms to specify location and size coordinates.  See http://sourceforge.net/mailarchive/forum.php?thread_name=AANLkTim6ZnGiOV1RTRBz0uBMF5y67xyrDp%2BkVSCBtkrB%40mail.gmail.com&forum_name=matplotlib-users


---

Comment by jason created at 2010-08-28 20:02:56

See also http://groups.google.com/group/networkx-discuss/browse_thread/thread/b95fda9813fae67d for code/ideas for rewriting the graph drawing.


---

Comment by jason created at 2011-03-23 02:41:22

I think this patch might take just a little to clean up.  Most of the patch is just adding comments to explain the code or reformatting long lines.  The big key is the clip=False arguments and the code to add things to the bbox_extra_artists.

I think the patch might just need some doctests and testing.  The other comments I put in above can be moved to another ticket that does a bigger revamp of graph drawing.


---

Comment by ppurka created at 2011-10-11 09:28:52

( Fix cut off vertices in graphs ) Apply to devel/sage/


---

Attachment

( Add additional padding to graphs ) Apply to devel/sage


---

Comment by ppurka created at 2011-10-11 09:46:15

Output with only the earlier patch (modified for 4.7.2)


---

Attachment

Output with patch for additional padding


---

Comment by ppurka created at 2011-10-11 09:57:32

Changing status from needs_work to needs_review.


---

Attachment

Added two patches. The [attachment:trac-9211-fix_cut_vertices_in_graphs.patch first one] is essentially the patch by jason redone to work with 4.7.2_alpha3.

The [attachment:trac-9211-add_padding_to_graphs.patch second patch] adds extra padding to all graphs. The two pngs attached are the output of


```
M = matrix(RDF, [[1/3, 1/3, 1/3], [0, 1/4, 3/4], [1/2, 1/4, 1/4]])
G=DiGraph(M, format='weighted_adjacency_matrix')
G.show(vertex_size=800, edge_labels=True)
```


The file [attachment:with-additional-padding.png] is the result of both the patches being applied.

Graphs currently look really bad without either of the two patches. The second patch is not a panacea for all cut off graph plots since it doesn't fix all cases. But my hope is that it fixes most commonly used cases.


---

Comment by jason created at 2011-10-11 13:14:32

I'm curious why you need the extra padding patch.  Are vertices still cut off using just the first patch?


---

Comment by ppurka created at 2011-10-11 13:38:16

Replying to [comment:12 jason]:

> I'm curious why you need the extra padding patch.  Are vertices still cut off using just the first patch?

Yes. Check [attachment:with-earlier-patch-modified-for-4.7.2.png the plot after the first patch] against the [attachment:with-additional-padding.png the plot after first+second patch]


---

Comment by jason created at 2011-10-11 14:15:41

Ah, right, because the first patch only fixes undirected graphs.  You are plotting a directed graph, so the changes in the patch don't apply.  I'm uploading a new patch that doesn't clip digraph circles or text.


---

Attachment

apply after trac-9211-fix_cut_vertices_in_graphs.patch


---

Comment by jason created at 2011-10-11 14:17:02

Can you try applying just trac-9211-fix_cut_vertices_in_graphs.patch and  trac_9211_digraph_clipping.patch ?


---

Comment by ppurka created at 2011-10-11 14:45:32

Replying to [comment:15 jason]:

> Can you try applying just trac-9211-fix_cut_vertices_in_graphs.patch and  trac_9211_digraph_clipping.patch ?

Excellent! Thanks. This does fix the problem for digraphs. Much better than adding random paddings.


---

Comment by jason created at 2011-10-11 15:32:00

Okay, did you run long tests on Sage?  The new version of my first patch seems okay to me, so if you positively review the patches, I think we are good to go, assuming that you've run long tests and there are no doctest errors.


---

Comment by ppurka created at 2011-10-11 16:02:20

Replying to [comment:19 jason]:

> Okay, did you run long tests on Sage?  The new version of my first patch seems okay to me, so if you positively review the patches, I think we are good to go, assuming that you've run long tests and there are no doctest errors.

I started the long test (make ptestlong) over an hour ago. I guess there's 3 more hours to go :)


---

Comment by ppurka created at 2011-10-12 03:37:41

A couple of doctests failed. Only in the directory plot/ (and in the files changed by this patch + base.pyx). Will investigate more once I am physically near that machine where the doctest was run.


---

Comment by kcrisman created at 2011-10-12 03:53:32

> A couple of doctests failed. Only in the directory plot/ (and in the files changed by this patch + base.pyx). Will investigate more once I am physically near that machine where the doctest was run.

Just FYI, base.pyx often fails on Mac if you don't have libjpeg or libtiff in the right place - see #7344 and #7345.  If the errors look like 

```
    ImportError: The _imaging C module is not installed
```

you can ignore them, they would be unrelated.


---

Comment by ppurka created at 2011-10-12 08:52:05

I am running it on x86_64 Linux. The errors were because of the additional 'clip' option introduced in the patches. Attaching a fix for the doctests.


---

Comment by kini created at 2011-10-12 08:56:57

I wonder why you are concatenating lines in the doctest output - our docstrings are theoretically supposed to be 72 (or 79) characters wide, if I'm not mistaken, which is why they the current test results are broken into multiple lines. The doctester doesn't care about purely whitespace differences between the expected and received output.


---

Comment by ppurka created at 2011-10-12 08:58:20

Replying to [comment:24 kini]:
> I wonder why you are concatenating lines in the doctest output - our docstrings are theoretically supposed to be 72 (or 79) characters wide, if I'm not mistaken, which is why they the current test results are broken into multiple lines. The doctester doesn't care about purely whitespace differences between the expected and received output.
Simply copied the output from "Expected output". Will attached a space-ified fix. :)


---

Comment by kini created at 2011-10-12 09:06:04

I wonder if you are aware of `sage -fixdoctests`, which does basically exactly what you are doing... :) BTW I have the same comment for [attachment:trac-9211-add_padding_to_graphs.patch].


---

Attachment

Fix doctests for 3d plots (re-uploaded)


---

Comment by ppurka created at 2011-10-12 09:11:58

Uploaded new patch.

Didn't know about `-fixdoctests` (it wasn't too painful to fix because of vim)

Forget about the adding padding patch. Jason did the real fix. :)


---

Comment by ppurka created at 2011-10-12 09:14:27

Previous failures were:

```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long -force_lib devel/sage/sage/plot/scatter_plot.py # 1 doctests failed
	sage -t  -long -force_lib devel/sage/sage/plot/text.py # 5 doctests failed
	sage -t  -long -force_lib devel/sage/sage/plot/circle.py # 8 doctests failed
	sage -t  -long -force_lib devel/sage/sage/plot/plot3d/base.pyx # 5 doctests failed
----------------------------------------------------------------------
Total time for all tests: 8844.0 seconds
```


New doctest on `devel/sage/sage/plot/` passes all doctests:

```
~/Installations/sage-4.7.2> ./sage -t -long devel/sage/sage/plot
...
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 520.6 seconds
```

So positive review from my side.


---

Comment by ppurka created at 2011-10-12 09:14:27

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-10-12 15:05:30

Changing status from positive_review to needs_work.


---

Comment by jason created at 2011-10-12 15:06:45

Your changes were a little more than just fixing whitespace, so let someone look at it to review your last patch.

Sorry---you're right about those doctests.  I shouldn't have been so sloppy as to not fix those doctests before indicating it needed to be reviewed.


---

Comment by jason created at 2011-10-12 15:06:45

Changing status from needs_work to needs_review.


---

Comment by jason created at 2011-11-04 17:53:54

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-11-04 17:53:54

Yep, I confirm that normal tests in graphs/ and plot/ pass.  Positive review for the fix doctests patch.  Good job!


---

Comment by jdemeyer created at 2011-11-07 10:10:28

Resolution: fixed
