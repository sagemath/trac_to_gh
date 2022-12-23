# Issue 2134: arrows for digraphs

Issue created by migration from https://trac.sagemath.org/ticket/2134

Original creator: rlm

Original creation time: 2008-02-10 00:25:14

Assignee: was

note - author of patch doesn't give a hoot. do what you will with it, i won't touch it again. several things may break, for example, the only guaranteed color format is a float tuple. also, no new documentation.

everybody wants it, so here it is... :-D


---

Attachment


---

Comment by was created at 2008-02-10 06:47:30

Note -- the author rlm of the patch was days without sleep at time of writing... :-)


---

Attachment


---

Comment by rlm created at 2008-02-11 21:03:32

Oops, I touched it again... But this is after 14 straight hours of sleep.


---

Comment by robertwb created at 2008-02-12 01:40:36

Looking a bit at this patch, does NetworkX do much for graph drawing that we couldn't be doing ourselves with matplotlib. Right now, for instance, it doesn't play well with the 2d->3d command because you can't (easily) get at the primitives that make up a graph. 

That being said, I think arrows are much nicer than sleeves.


---

Comment by rlm created at 2008-02-12 20:25:21

I might have the exact details wrong, but NetworkX uses pylab, which uses matplotlib. In fact, after trying to implement the arrows in NX, I think it would be easier to ultimately phase NX out of graph plotting completely. (After reimplementing the base structure, I'm starting to wonder how much NX we ultimately need...)


---

Comment by robertwb created at 2008-02-14 05:48:11

Looks good to me. I've created a ticket for phasing NetworkX out of the graph plotting code: #2157, though I bet it implements lots of other useful stuff.


---

Comment by mabshoff created at 2008-02-14 09:56:57

Robert, the patch currently doesn't apply cleanly any more due to

```
changeset:   8329:657c0727bbd2
user:        Robert L. Miller <rlm@rlmiller.org>
date:        Thu Feb 07 00:18:51 2008 -0800
summary:     plot loops.
```

The issue is with the second hunk in `sage/graphs/graph.py`, so could you rebase the patch with your plot loop patch applied?

Cheers,

Michael


---

Comment by rlm created at 2008-02-15 00:42:43

Apply this instead of the others.


---

Attachment

Rebased- in doing so, I uncovered two bugs:
1 Graphics import depended magically on it happening on another level
2 Arrow plotting would have crashed on plotting loops

Should now be ready to include.


---

Comment by mabshoff created at 2008-02-15 02:18:26

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 02:18:26

Merged in Sage 2.10.2.alpha0
