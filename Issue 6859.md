# Issue 6859: Add more graph generators

Issue created by migration from https://trac.sagemath.org/ticket/6859

Original creator: myurko

Original creation time: 2009-09-02 01:42:16

Assignee: rlm

This patch add graph generators for the hyper star, (n,k)-star, n-star, and bubble sort graph.


---

Attachment


---

Comment by ncohen created at 2009-09-06 09:54:29

Would it be possible to add to the docstrings the definition of what these graphs should be ?

Nathann


---

Comment by myurko created at 2009-09-06 13:40:02

Sure. I'll add definitions.


---

Comment by ncohen created at 2009-09-06 14:13:35

I do not know if you are aware of it ( I was not until very recently ) but the docstrings are used to generate a very complete documentation accessible through there :

http://www.sagemath.org/doc/reference/graphs.html

This also means that you can use LaTeX in your description if you deem it necessary, and that the formula will be automatically translated into beautiful equations on this page ;-)

Nathann


---

Comment by myurko created at 2009-09-06 14:32:40

Well, I knew that you can use Latex in docstrings, but I tried not to use it since it is hard to read when introspecting.


---

Attachment

Adds definitions of graphs to docstrings


---

Comment by jason created at 2009-09-22 16:45:45

Very nice.

I'm attaching a patch which optimizes some of the code to use more python things (like swapping), plus fixes a few typos.  I think someone needs to review my patch.


---

Attachment

apply on top of previous patches


---

Comment by myurko created at 2009-09-22 17:54:01

I obviously can't review the patch, but the swapping certainly looks better. Coding too long in java has made forget some of the nice python idioms.


---

Comment by jason created at 2009-09-22 19:14:11

Okay, positive review for your patch.

You can review my changes (just make sure that you still get the same graphs).  If you okay my changes, change this ticket to "positive review".


---

Comment by myurko created at 2009-09-22 21:37:52

All the graphs except the n,k star graph worked still. However, it was just a one line fix to keep the v[0] = tmp_bit line inside the for loop (otherwise all the vertices become looped). I've uploaded a one line patch to fix it.


---

Attachment


---

Comment by jason created at 2009-09-22 22:41:55

ah, right.  Okay, then, positive review.


---

Comment by mvngu created at 2009-09-24 10:06:40

The patch `trac_6859-ascii-chars.patch` uses only ASCII characters for quotation marks and long dashes. Without it, merging `trac_6859.patch` and building the reference manual would result in the following error:

```
reading sources... sage/graphs/graph_generators /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/Sphinx-0.5.1-py2.6.egg/sphinx/environment.py:543: DeprecationWarning: BaseException.message has been deprecated as of Python 2.6
  raise SphinxError(err.message)
Sphinx error:
```



---

Comment by mvngu created at 2009-09-24 10:24:22

use ASCII characters for quotation marks and long dashes


---

Attachment

proper formatting of lists


---

Comment by mvngu created at 2009-09-24 10:26:10

The patch `trac_6859-formatting-issues.patch` fixes formatting of lists. Without it, I get the following warnings when building the reference manual:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.HyperStarGraph:22: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.NKStarGraph:25: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.NStarGraph:19: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```



---

Comment by mvngu created at 2009-09-24 10:55:52

Resolution: fixed


---

Comment by mvngu created at 2009-09-24 10:55:52

Merged patches in this order:

 1. `trac_6859.patch`
 1. `trac_6859-ascii-chars.patch`
 1. `trac_6859_definitions.patch`
 1. `trac-6859-optimize.patch`
 1. `trac-6859-optimize-fix.patch`
 1. `trac_6859-formatting-issues.patch`


---

Comment by mvngu created at 2009-09-27 10:19:53

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
