# Issue 6572: tutorial: put double colon on its own line

Issue created by migration from https://trac.sagemath.org/ticket/6572

Original creator: mvngu

Original creation time: 2009-07-20 20:11:48

Assignee: tba

CC:  jhpalmieri ncohen

Keywords: tutorial

See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/85929d86accdf94d) thread for some background information. John Palmieri suggests that all doctests in the Sage tutorial be preceded with a double colon on its own line. That way, the doctest script would pick up all doctests in the tutorial.


---

Comment by jhpalmieri created at 2009-07-21 03:29:07

Here are two patches, one for the main repository and one for the scripts repository.  

The scripts patch does the following: first, previously, doctests had to be preceded by a double colon at the beginning of a line, and now they only need to be preceded by a line which starts with white space then a double colon -- the double colon no longer has to be at the left margin.  This is important for some files (like constructions/algebraic_geometry.rst), in which indentations might break if we had to move the double colons to the left.   The second change is figuring out when the doctest block ends: it looks for text indented no farther than the double colons were.  (Previously, it looked for text which wasn't indented at all, so if a paragraph was indented, then some doctests were indented further, then a paragraph unindented one level, that second paragaph was treated as part of the doctest block.)

As a result of all of this, some more doctests are found by `sage -t`.  The other patch does two things: it makes the change advertised in the summary for the ticket, moving double colons onto lines of their own where necessary.  It also tries to fix the newly discovered broken doctests.  I don't know how to fix some of these, and so they are being skipped.  These include the one which triggered this whole episode:

```
     sage: theta = var('theta')
     sage: solve(cos(theta)==sin(theta))
     [sin(theta) == cos(theta)]
```

as well as some doctests involving starting and stopping the Singular console, for example.

For me, this passes all tests on Mac OS X (both 32-bit and 64-bit), and also on a 32-bit linux box (an old Ubuntu machine) and a 64-bit linux box (sage.math).  It would be best to fix the skipped tests, but that can go in another ticket if no one knows how to do it right now.


---

Attachment

See #6642 for the problem with the 'solve' doctest.


---

Comment by kcrisman created at 2009-08-26 21:22:00

Replying to [comment:3 jhpalmieri]:
> See #6642 for the problem with the 'solve' doctest.

This may be fixed now - see #6642.  If so, I guess one could put that back in the tutorial.


---

Comment by jhpalmieri created at 2009-09-08 20:40:35

Here is a patch against 4.1.2.alpha1; this depends on #6642.


---

Comment by mhansen created at 2009-10-05 13:12:15

Doesn't it make more sense to detect double colons at the end of a line?

In restructured text, the two should be equivalent.  It should be the same for the doctests as well.


---

Attachment

apply on top of other scripts patch


---

Comment by jhpalmieri created at 2009-10-05 15:14:36

Replying to [comment:6 mhansen]:
> Doesn't it make more sense to detect double colons at the end of a line?
> 
> In restructured text, the two should be equivalent.  It should be the same for the doctests as well.

Okay, that makes sense.  The new scripts patch changes the regular expression to fix this, I think.

Now the problem is that the file (added since this ticket was opened) `tour_graphtheory.rst` is a *complete* disaster, with 15 doctest failures.  I can fix lots of the failed doctests by adding "..." and ".. link" in various places, but I don't know what to do about failures like these:

```
    sage: g.plot(edge_colors=g.edge_coloring(hex_colors=True))
    AttributeError: 'Graph' object has no attribute 'edge_coloring'

    sage: g.vertex_coloring()
    AttributeError: 'Graph' object has no attribute 'vertex_coloring'

    sage: print g.max_matching()
    AttributeError: 'Graph' object has no attribute 'max_matching'
```

I don't know what was intended and therefore I don't know how to fix it.  I'll post a patch that fixes what I can.


---

Comment by jhpalmieri created at 2009-10-05 15:18:45

I'll post a replacement for "trac_6572-double-colon.patch" soon.  That patch shouldn't have to be as large, if double colons at the end of lines work right.


---

Attachment

depends on #6642


---

Comment by jhpalmieri created at 2009-10-06 01:29:20

Here's a new version of "trac_6572-double-colon.patch".  This fixes a few more doctest failures uncovered by the script patches.  Apply both script patches, this patch, and the graph theory patch.  Together with the patch at #6642, this means that most doctests pass in the documentation.  `tutorial/tour_graphtheory.rst` is the only problem now.


---

Comment by jhpalmieri created at 2009-10-08 01:32:22

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2009-10-08 01:32:22

With the patch at #7149, this is now ready for review.  Ignore the graph theory patch, since that is now taken care of by #7149.


---

Comment by jhpalmieri created at 2009-10-08 01:32:47

ignore this patch!


---

Comment by mhansen created at 2009-10-15 09:17:06

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-10-15 09:17:17

Resolution: fixed
