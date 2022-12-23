# Issue 2519: Add support for posets, semi-lattices, etc. to Sage

Issue created by migration from https://trac.sagemath.org/ticket/2519

Original creator: saliola

Original creation time: 2008-03-14 19:49:15

Assignee: saliola

CC:  sage-combinat




---

Attachment

Initial support for finite posets. (Patch against sage-3.0.)


---

Comment by saliola created at 2008-04-23 18:02:04

See announcement and discussion on sage-devel:

  http://groups.google.com/group/sage-devel/browse_thread/thread/b6fcc3a134abe22c


---

Comment by rlm created at 2008-05-10 21:55:15

Some comments:

 1. `Lattice` should be `LatticePoset` or something similar. Same comment for `Chain`, `Antichain`, `Pentagon` and `Diamond`.

 1. This is a great example of good code. The docstrings are generous and everything is well tested. Nice work!


---

Comment by saliola created at 2008-05-15 23:05:09

>  1. `Lattice` should be `LatticePoset` or something similar. Same comment for `Chain`, `Antichain`, `Pentagon` and `Diamond`.

Done. As a remark: we eventually want to create a poset database similar to the graph
database. So these poset examples will be moved into the database.

>  1. This is a great example of good code. The docstrings are generous and everything is well tested. Nice work!

Thank you!


```
There are a few other differences between the original patch and the new patch:

1. Added "or equal to" to the docstrings for is_gequal and is_lequal.

2. I redefined the show methods for FinitePoset and HasseDiagram. Before it
was just show = plot, but I since realized this is wrong: show should show the
Graphics object returned by the plot method.

3. Added the methods interval, closed_interval and open_interval to the FinitePoset
class. These already existed for the HasseDiagram class; so the new methods
just expose these methods from the FinitePoset class. It was an oversight not
to have done this originally.

4. I slightly modified HasseDiagram.antichains to return the empty list as an
antichain. And added tests.
```



---

Comment by rlm created at 2008-05-16 04:25:52

Regarding `show` versus `plot`, you don't even really need a `show`: most Sage objects give LaTeX when you call `show`, and if you do `sage: P.plot()`, the graphics object will appear.

Also, it looks like you need both patches in order, right?


---

Comment by saliola created at 2008-05-16 07:04:03

Apply both patches in order!


---

Attachment

Replying to [comment:5 rlm]:
> Regarding `show` versus `plot`, you don't even really need a `show`: most Sage objects give LaTeX when you call `show`, and if you do `sage: P.plot()`, the graphics object will appear.

I'll leave it as is, as this is how it is implemented for Graphs/DiGraphs.
 
> Also, it looks like you need both patches in order, right?

Yes, I patched against the previous patch. I've corrected what I wrote.

I can provide a single patch instead if that is easier.


---

Comment by rlm created at 2008-05-22 23:17:31

As long as it applies cleanly and passes all tests...


---

Comment by mabshoff created at 2008-05-22 23:56:28

With both patches applied the doctests pass. Two comments:

 * sage/combinat/posets/__init__.py is zero bytes, so the patch doesn't create it. I fixed that manually
 * these patches are regular diffs and not mercurial patches, so I ended up with the formal credit when applying them. I did however state in the changelog:

```
changeset:   9746:0f14afe7ba00
tag:         tip
user:        mabshoff@sage.math.washington.edu
date:        Thu May 22 16:52:19 2008 -0700
summary:     Apply patch by Peter Jipsen and Franco Saliola: Add support for posets, semi-lattices, etc

changeset:   9745:0716b13a9e12
user:        mabshoff@sage.math.washington.edu
date:        Thu May 22 16:52:08 2008 -0700
summary:     Apply patch by Peter Jipsen and Franco Saliola: Add support for posets, semi-lattices, etc.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 00:07:04

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 00:07:04

Merged in Sage 3.0.2.rc0
