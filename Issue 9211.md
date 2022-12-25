# Issue 9211: graph vertices cut off

archive/issues_009211.json:
```json
{
    "body": "Assignee: jason, mvngu, ncohen, rlm\n\nCC:  @rbeezer @kcrisman @kini\n\nThough #7299 helped, graph vertices are still cut off.\n\nWith the updated matplotlib spkg at #9210, we can turn off clipping of the matplotlib scatterplot, or with a more recent (SVN right now) version of matplotlib, we could probably add some bbox_extra_artists to the savefig which takes those artists into account when calculating the bounding box (when bbox_inches='tight').\n\nEither way, a real fix should be possible soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9211\n\n",
    "created_at": "2010-06-11T06:48:32Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "graph vertices cut off",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9211",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, mvngu, ncohen, rlm

CC:  @rbeezer @kcrisman @kini

Though #7299 helped, graph vertices are still cut off.

With the updated matplotlib spkg at #9210, we can turn off clipping of the matplotlib scatterplot, or with a more recent (SVN right now) version of matplotlib, we could probably add some bbox_extra_artists to the savefig which takes those artists into account when calculating the bounding box (when bbox_inches='tight').

Either way, a real fix should be possible soon.

Issue created by migration from https://trac.sagemath.org/ticket/9211





---

archive/issue_comments_086138.json:
```json
{
    "body": "Here is a good example showing the problem (still):\n\n\n```\na=matrix([[1,2],[3,4]])\n\nvar('x y z w')\nb=matrix([[x,y],[z,w]])\n\na.set_immutable()\nb.set_immutable()\n\nK=DiGraph({a:[b]})\nshow(K, vertex_size=800)\n\n```\n",
    "created_at": "2010-06-11T06:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86138",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_086139.json:
```json
{
    "body": "Attachment [trac-9211-graph-vertices-cut.patch](tarball://root/attachments/some-uuid/ticket9211/trac-9211-graph-vertices-cut.patch) by @jasongrout created at 2010-06-12 21:22:33",
    "created_at": "2010-06-12T21:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86139",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9211-graph-vertices-cut.patch](tarball://root/attachments/some-uuid/ticket9211/trac-9211-graph-vertices-cut.patch) by @jasongrout created at 2010-06-12 21:22:33



---

archive/issue_comments_086140.json:
```json
{
    "body": "This patch depends on the matplotlib spkg at #9221.  I don't know if the patch is very elegant.  I'll trust the reviewer's comments on that.  The problem is that it lets the scatter plot vertices extend beyond the frame (relying on the user adjusting the axes_pad option to extend the frame).",
    "created_at": "2010-06-12T21:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86140",
    "user": "https://github.com/jasongrout"
}
```

This patch depends on the matplotlib spkg at #9221.  I don't know if the patch is very elegant.  I'll trust the reviewer's comments on that.  The problem is that it lets the scatter plot vertices extend beyond the frame (relying on the user adjusting the axes_pad option to extend the frame).



---

archive/issue_comments_086141.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-12T21:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86141",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086142.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-12T22:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86142",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086143.json:
```json
{
    "body": "The patch doesn't work for multiple-edge graphs (they are drawn completely differently than graphs without multiple edges).  In fact, we probably ought to draw all graphs using CircleCollection objects rather than scatter_plot or Circles.",
    "created_at": "2010-06-12T22:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86143",
    "user": "https://github.com/jasongrout"
}
```

The patch doesn't work for multiple-edge graphs (they are drawn completely differently than graphs without multiple edges).  In fact, we probably ought to draw all graphs using CircleCollection objects rather than scatter_plot or Circles.



---

archive/issue_comments_086144.json:
```json
{
    "body": "Here's how to draw circles like the ones in scatter plot (where the size doesn't change as you make the figure smaller or bigger: use a CircleCollection argument and use different transforms to specify location and size coordinates.  See http://sourceforge.net/mailarchive/forum.php?thread_name=AANLkTim6ZnGiOV1RTRBz0uBMF5y67xyrDp%2BkVSCBtkrB%40mail.gmail.com&forum_name=matplotlib-users",
    "created_at": "2010-08-28T14:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86144",
    "user": "https://github.com/jasongrout"
}
```

Here's how to draw circles like the ones in scatter plot (where the size doesn't change as you make the figure smaller or bigger: use a CircleCollection argument and use different transforms to specify location and size coordinates.  See http://sourceforge.net/mailarchive/forum.php?thread_name=AANLkTim6ZnGiOV1RTRBz0uBMF5y67xyrDp%2BkVSCBtkrB%40mail.gmail.com&forum_name=matplotlib-users



---

archive/issue_comments_086145.json:
```json
{
    "body": "See also http://groups.google.com/group/networkx-discuss/browse_thread/thread/b95fda9813fae67d for code/ideas for rewriting the graph drawing.",
    "created_at": "2010-08-28T20:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86145",
    "user": "https://github.com/jasongrout"
}
```

See also http://groups.google.com/group/networkx-discuss/browse_thread/thread/b95fda9813fae67d for code/ideas for rewriting the graph drawing.



---

archive/issue_comments_086146.json:
```json
{
    "body": "I think this patch might take just a little to clean up.  Most of the patch is just adding comments to explain the code or reformatting long lines.  The big key is the clip=False arguments and the code to add things to the bbox_extra_artists.\n\nI think the patch might just need some doctests and testing.  The other comments I put in above can be moved to another ticket that does a bigger revamp of graph drawing.",
    "created_at": "2011-03-23T02:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86146",
    "user": "https://github.com/jasongrout"
}
```

I think this patch might take just a little to clean up.  Most of the patch is just adding comments to explain the code or reformatting long lines.  The big key is the clip=False arguments and the code to add things to the bbox_extra_artists.

I think the patch might just need some doctests and testing.  The other comments I put in above can be moved to another ticket that does a bigger revamp of graph drawing.



---

archive/issue_comments_086147.json:
```json
{
    "body": "( Fix cut off vertices in graphs ) Apply to devel/sage/",
    "created_at": "2011-10-11T09:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86147",
    "user": "https://github.com/ppurka"
}
```

( Fix cut off vertices in graphs ) Apply to devel/sage/



---

archive/issue_comments_086148.json:
```json
{
    "body": "Attachment [trac-9211-add_padding_to_graphs.patch](tarball://root/attachments/some-uuid/ticket9211/trac-9211-add_padding_to_graphs.patch) by @ppurka created at 2011-10-11 09:45:33\n\n( Add additional padding to graphs ) Apply to devel/sage",
    "created_at": "2011-10-11T09:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86148",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac-9211-add_padding_to_graphs.patch](tarball://root/attachments/some-uuid/ticket9211/trac-9211-add_padding_to_graphs.patch) by @ppurka created at 2011-10-11 09:45:33

( Add additional padding to graphs ) Apply to devel/sage



---

archive/issue_comments_086149.json:
```json
{
    "body": "Output with only the earlier patch (modified for 4.7.2)",
    "created_at": "2011-10-11T09:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86149",
    "user": "https://github.com/ppurka"
}
```

Output with only the earlier patch (modified for 4.7.2)



---

archive/issue_comments_086150.json:
```json
{
    "body": "Attachment [with-earlier-patch-modified-for-4.7.2.png](tarball://root/attachments/some-uuid/ticket9211/with-earlier-patch-modified-for-4.7.2.png) by @ppurka created at 2011-10-11 09:46:37\n\nOutput with patch for additional padding",
    "created_at": "2011-10-11T09:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86150",
    "user": "https://github.com/ppurka"
}
```

Attachment [with-earlier-patch-modified-for-4.7.2.png](tarball://root/attachments/some-uuid/ticket9211/with-earlier-patch-modified-for-4.7.2.png) by @ppurka created at 2011-10-11 09:46:37

Output with patch for additional padding



---

archive/issue_comments_086151.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-11T09:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86151",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086152.json:
```json
{
    "body": "Attachment [with-additional-padding.png](tarball://root/attachments/some-uuid/ticket9211/with-additional-padding.png) by @ppurka created at 2011-10-11 09:57:32\n\nAdded two patches. The [attachment:trac-9211-fix_cut_vertices_in_graphs.patch first one] is essentially the patch by jason redone to work with 4.7.2_alpha3.\n\nThe [attachment:trac-9211-add_padding_to_graphs.patch second patch] adds extra padding to all graphs. The two pngs attached are the output of\n\n\n```\nM = matrix(RDF, [[1/3, 1/3, 1/3], [0, 1/4, 3/4], [1/2, 1/4, 1/4]])\nG=DiGraph(M, format='weighted_adjacency_matrix')\nG.show(vertex_size=800, edge_labels=True)\n```\n\n\nThe file [attachment:with-additional-padding.png] is the result of both the patches being applied.\n\nGraphs currently look really bad without either of the two patches. The second patch is not a panacea for all cut off graph plots since it doesn't fix all cases. But my hope is that it fixes most commonly used cases.",
    "created_at": "2011-10-11T09:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86152",
    "user": "https://github.com/ppurka"
}
```

Attachment [with-additional-padding.png](tarball://root/attachments/some-uuid/ticket9211/with-additional-padding.png) by @ppurka created at 2011-10-11 09:57:32

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

archive/issue_comments_086153.json:
```json
{
    "body": "I'm curious why you need the extra padding patch.  Are vertices still cut off using just the first patch?",
    "created_at": "2011-10-11T13:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86153",
    "user": "https://github.com/jasongrout"
}
```

I'm curious why you need the extra padding patch.  Are vertices still cut off using just the first patch?



---

archive/issue_comments_086154.json:
```json
{
    "body": "Replying to [comment:12 jason]:\n\n> I'm curious why you need the extra padding patch.  Are vertices still cut off using just the first patch?\n\nYes. Check [attachment:with-earlier-patch-modified-for-4.7.2.png the plot after the first patch] against the [attachment:with-additional-padding.png the plot after first+second patch]",
    "created_at": "2011-10-11T13:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86154",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:12 jason]:

> I'm curious why you need the extra padding patch.  Are vertices still cut off using just the first patch?

Yes. Check [attachment:with-earlier-patch-modified-for-4.7.2.png the plot after the first patch] against the [attachment:with-additional-padding.png the plot after first+second patch]



---

archive/issue_comments_086155.json:
```json
{
    "body": "Ah, right, because the first patch only fixes undirected graphs.  You are plotting a directed graph, so the changes in the patch don't apply.  I'm uploading a new patch that doesn't clip digraph circles or text.",
    "created_at": "2011-10-11T14:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86155",
    "user": "https://github.com/jasongrout"
}
```

Ah, right, because the first patch only fixes undirected graphs.  You are plotting a directed graph, so the changes in the patch don't apply.  I'm uploading a new patch that doesn't clip digraph circles or text.



---

archive/issue_comments_086156.json:
```json
{
    "body": "Attachment [trac_9211_digraph_clipping.patch](tarball://root/attachments/some-uuid/ticket9211/trac_9211_digraph_clipping.patch) by @jasongrout created at 2011-10-11 14:16:20\n\napply after trac-9211-fix_cut_vertices_in_graphs.patch",
    "created_at": "2011-10-11T14:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86156",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9211_digraph_clipping.patch](tarball://root/attachments/some-uuid/ticket9211/trac_9211_digraph_clipping.patch) by @jasongrout created at 2011-10-11 14:16:20

apply after trac-9211-fix_cut_vertices_in_graphs.patch



---

archive/issue_comments_086157.json:
```json
{
    "body": "Can you try applying just trac-9211-fix_cut_vertices_in_graphs.patch and  trac_9211_digraph_clipping.patch ?",
    "created_at": "2011-10-11T14:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86157",
    "user": "https://github.com/jasongrout"
}
```

Can you try applying just trac-9211-fix_cut_vertices_in_graphs.patch and  trac_9211_digraph_clipping.patch ?



---

archive/issue_comments_086158.json:
```json
{
    "body": "Replying to [comment:15 jason]:\n\n> Can you try applying just trac-9211-fix_cut_vertices_in_graphs.patch and  trac_9211_digraph_clipping.patch ?\n\nExcellent! Thanks. This does fix the problem for digraphs. Much better than adding random paddings.",
    "created_at": "2011-10-11T14:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86158",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:15 jason]:

> Can you try applying just trac-9211-fix_cut_vertices_in_graphs.patch and  trac_9211_digraph_clipping.patch ?

Excellent! Thanks. This does fix the problem for digraphs. Much better than adding random paddings.



---

archive/issue_comments_086159.json:
```json
{
    "body": "Okay, did you run long tests on Sage?  The new version of my first patch seems okay to me, so if you positively review the patches, I think we are good to go, assuming that you've run long tests and there are no doctest errors.",
    "created_at": "2011-10-11T15:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86159",
    "user": "https://github.com/jasongrout"
}
```

Okay, did you run long tests on Sage?  The new version of my first patch seems okay to me, so if you positively review the patches, I think we are good to go, assuming that you've run long tests and there are no doctest errors.



---

archive/issue_comments_086160.json:
```json
{
    "body": "Replying to [comment:19 jason]:\n\n> Okay, did you run long tests on Sage?  The new version of my first patch seems okay to me, so if you positively review the patches, I think we are good to go, assuming that you've run long tests and there are no doctest errors.\n\nI started the long test (make ptestlong) over an hour ago. I guess there's 3 more hours to go :)",
    "created_at": "2011-10-11T16:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86160",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:19 jason]:

> Okay, did you run long tests on Sage?  The new version of my first patch seems okay to me, so if you positively review the patches, I think we are good to go, assuming that you've run long tests and there are no doctest errors.

I started the long test (make ptestlong) over an hour ago. I guess there's 3 more hours to go :)



---

archive/issue_comments_086161.json:
```json
{
    "body": "A couple of doctests failed. Only in the directory plot/ (and in the files changed by this patch + base.pyx). Will investigate more once I am physically near that machine where the doctest was run.",
    "created_at": "2011-10-12T03:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86161",
    "user": "https://github.com/ppurka"
}
```

A couple of doctests failed. Only in the directory plot/ (and in the files changed by this patch + base.pyx). Will investigate more once I am physically near that machine where the doctest was run.



---

archive/issue_comments_086162.json:
```json
{
    "body": "> A couple of doctests failed. Only in the directory plot/ (and in the files changed by this patch + base.pyx). Will investigate more once I am physically near that machine where the doctest was run.\n\nJust FYI, base.pyx often fails on Mac if you don't have libjpeg or libtiff in the right place - see #7344 and #7345.  If the errors look like \n\n```\n    ImportError: The _imaging C module is not installed\n```\n\nyou can ignore them, they would be unrelated.",
    "created_at": "2011-10-12T03:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86162",
    "user": "https://github.com/kcrisman"
}
```

> A couple of doctests failed. Only in the directory plot/ (and in the files changed by this patch + base.pyx). Will investigate more once I am physically near that machine where the doctest was run.

Just FYI, base.pyx often fails on Mac if you don't have libjpeg or libtiff in the right place - see #7344 and #7345.  If the errors look like 

```
    ImportError: The _imaging C module is not installed
```

you can ignore them, they would be unrelated.



---

archive/issue_comments_086163.json:
```json
{
    "body": "I am running it on x86_64 Linux. The errors were because of the additional 'clip' option introduced in the patches. Attaching a fix for the doctests.",
    "created_at": "2011-10-12T08:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86163",
    "user": "https://github.com/ppurka"
}
```

I am running it on x86_64 Linux. The errors were because of the additional 'clip' option introduced in the patches. Attaching a fix for the doctests.



---

archive/issue_comments_086164.json:
```json
{
    "body": "I wonder why you are concatenating lines in the doctest output - our docstrings are theoretically supposed to be 72 (or 79) characters wide, if I'm not mistaken, which is why they the current test results are broken into multiple lines. The doctester doesn't care about purely whitespace differences between the expected and received output.",
    "created_at": "2011-10-12T08:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86164",
    "user": "https://github.com/kini"
}
```

I wonder why you are concatenating lines in the doctest output - our docstrings are theoretically supposed to be 72 (or 79) characters wide, if I'm not mistaken, which is why they the current test results are broken into multiple lines. The doctester doesn't care about purely whitespace differences between the expected and received output.



---

archive/issue_comments_086165.json:
```json
{
    "body": "Replying to [comment:24 kini]:\n> I wonder why you are concatenating lines in the doctest output - our docstrings are theoretically supposed to be 72 (or 79) characters wide, if I'm not mistaken, which is why they the current test results are broken into multiple lines. The doctester doesn't care about purely whitespace differences between the expected and received output.\nSimply copied the output from \"Expected output\". Will attached a space-ified fix. :)",
    "created_at": "2011-10-12T08:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86165",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:24 kini]:
> I wonder why you are concatenating lines in the doctest output - our docstrings are theoretically supposed to be 72 (or 79) characters wide, if I'm not mistaken, which is why they the current test results are broken into multiple lines. The doctester doesn't care about purely whitespace differences between the expected and received output.
Simply copied the output from "Expected output". Will attached a space-ified fix. :)



---

archive/issue_comments_086166.json:
```json
{
    "body": "I wonder if you are aware of `sage -fixdoctests`, which does basically exactly what you are doing... :) BTW I have the same comment for [attachment:trac-9211-add_padding_to_graphs.patch].",
    "created_at": "2011-10-12T09:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86166",
    "user": "https://github.com/kini"
}
```

I wonder if you are aware of `sage -fixdoctests`, which does basically exactly what you are doing... :) BTW I have the same comment for [attachment:trac-9211-add_padding_to_graphs.patch].



---

archive/issue_comments_086167.json:
```json
{
    "body": "Attachment [trac_9211-fix_doctests.patch](tarball://root/attachments/some-uuid/ticket9211/trac_9211-fix_doctests.patch) by @ppurka created at 2011-10-12 09:09:57\n\nFix doctests for 3d plots (re-uploaded)",
    "created_at": "2011-10-12T09:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86167",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_9211-fix_doctests.patch](tarball://root/attachments/some-uuid/ticket9211/trac_9211-fix_doctests.patch) by @ppurka created at 2011-10-12 09:09:57

Fix doctests for 3d plots (re-uploaded)



---

archive/issue_comments_086168.json:
```json
{
    "body": "Uploaded new patch.\n\nDidn't know about `-fixdoctests` (it wasn't too painful to fix because of vim)\n\nForget about the adding padding patch. Jason did the real fix. :)",
    "created_at": "2011-10-12T09:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86168",
    "user": "https://github.com/ppurka"
}
```

Uploaded new patch.

Didn't know about `-fixdoctests` (it wasn't too painful to fix because of vim)

Forget about the adding padding patch. Jason did the real fix. :)



---

archive/issue_comments_086169.json:
```json
{
    "body": "Previous failures were:\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  -long -force_lib devel/sage/sage/plot/scatter_plot.py # 1 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/plot/text.py # 5 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/plot/circle.py # 8 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/plot/plot3d/base.pyx # 5 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 8844.0 seconds\n```\n\n\nNew doctest on `devel/sage/sage/plot/` passes all doctests:\n\n```\n~/Installations/sage-4.7.2> ./sage -t -long devel/sage/sage/plot\n...\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 520.6 seconds\n```\n\nSo positive review from my side.",
    "created_at": "2011-10-12T09:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86169",
    "user": "https://github.com/ppurka"
}
```

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

archive/issue_comments_086170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-12T09:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86170",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086171.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-10-12T15:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86171",
    "user": "https://github.com/jasongrout"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086172.json:
```json
{
    "body": "Your changes were a little more than just fixing whitespace, so let someone look at it to review your last patch.\n\nSorry---you're right about those doctests.  I shouldn't have been so sloppy as to not fix those doctests before indicating it needed to be reviewed.",
    "created_at": "2011-10-12T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86172",
    "user": "https://github.com/jasongrout"
}
```

Your changes were a little more than just fixing whitespace, so let someone look at it to review your last patch.

Sorry---you're right about those doctests.  I shouldn't have been so sloppy as to not fix those doctests before indicating it needed to be reviewed.



---

archive/issue_comments_086173.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-12T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86173",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086174.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-04T17:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86174",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086175.json:
```json
{
    "body": "Yep, I confirm that normal tests in graphs/ and plot/ pass.  Positive review for the fix doctests patch.  Good job!",
    "created_at": "2011-11-04T17:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86175",
    "user": "https://github.com/jasongrout"
}
```

Yep, I confirm that normal tests in graphs/ and plot/ pass.  Positive review for the fix doctests patch.  Good job!



---

archive/issue_events_022691.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-07T10:10:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9211#event-22691"
}
```



---

archive/issue_comments_086176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-11-07T10:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9211#issuecomment-86176",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
