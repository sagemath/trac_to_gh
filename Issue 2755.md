# Issue 2755: [with patch, needs review] lattice_polytope.py update

Issue created by migration from https://trac.sagemath.org/ticket/2755

Original creator: novoselt

Original creation time: 2008-04-01 17:19:58

Assignee: mhampton

Finally, the patch with the second version of the module... Does what was proposed on Sage Days 7 and has doctests for all functions (tests for such things as setstate  do not have explicit calls but certainly use the required functions).

ADDITIONS:

convex_hull(), minkowski_sum(), NEFPartition.dual()

ReflexivePolytope(), ReflexivePolytopes()

LatticePolytopeClass.plot3d(), LatticePolytopeClass.skeleton* (points, graph, plot)

Vertices of polytopes are now computed by default.

Little shortcuts like edges() or point().

Examples/tests for each function.

ATTACHED FILES:

Saved Sage objects for sequences of all reflexive polytopes in 2 and 3 dimensions with some precomputed data and dictionaries to these sequences allowing fast identification of the isomorphism class under GL(Z) action.

The module assumes they are located in DB_HOME/reflexive_polytopes/


---

Attachment


---

Attachment


---

Attachment


---

Attachment

There is one more file which is too big for attaching it to the ticket. All four are available at
http://sage.math.washington.edu/home/novoselt/patch%202008-04-01/


---

Comment by mhampton created at 2008-04-02 01:20:53

Changing status from new to assigned.


---

Comment by mhampton created at 2008-04-02 18:27:30

Changing assignee from mhampton to mabshoff.


---

Comment by mhampton created at 2008-04-02 18:27:30

Nice job!  This is a positive review, pending the very minor changes I am attaching as a patch.  100% coverage, passes all tests on my mac intel 10.4.11 machine.  

In the future, it might be worth replacing the convex_hull function by my cddlib interface, since it seems that PALP is not configured to handle large polytopes in higher dimensions (for example, it seems extremely fragile starting in dimension 5).

The patch makes convex_hull a little more robust by explicitly casting the input to ZZ; previously it would crash on python int lists.


---

Comment by mhampton created at 2008-04-02 18:27:30

Changing status from assigned to new.


---

Comment by mhampton created at 2008-04-02 18:27:30

Changing priority from major to minor.


---

Attachment

minor changes; apply after previous patch


---

Comment by novoselt created at 2008-04-02 18:46:38

Sorry for crashes on large dimension - it is my fault, not PALP. I have encountered this issue before but forgot about it since usually polytopes I work with are small enough.

The problem is in piping to poly.x - if the output is too big to fit into the buffer, the output is never read. A fast workaround is to use temp files as it is done in lattice_polytope._palp function, but it maybe slower. On the other hand, I didn't actually benchmark it and interface to a C-library definitely should be better.


---

Comment by mabshoff created at 2008-04-26 04:20:13

Let's make a push to get this merged. What is the status on the requested changes? Or should we merge this as is and then hope that people will finish to polish this code?

Cheers,

Michael


---

Comment by was created at 2008-04-26 19:59:30

I think we should merge this as is.  Andrey wrote to me just now and wrote: "I had the impression that the "minor change" was the extra patch with ZZ-conversion and otherwise the current version is adequate."


---

Comment by mabshoff created at 2008-04-30 02:24:31

Ok, where do we stick the sobj files? I think they should end up in "data_location = DB_HOME + '/reflexive_polytopes/'". This is $SAGE_ROOT/data/reflexive_polytopes/ - so I would need to create that directory. I will play around with this and see what happens.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-30 02:31:38

Looking at the problem some more it seems that we need an lattice_polytope-db.spkg. That is the way we deal with all the other databases in the SAGE_DATA directory. This should be fairly trivial to do and not require formal voting due to its minuscule size.

Cheers,

Michael


---

Comment by novoselt created at 2008-04-30 05:57:44

What exactly this package should do? Should it be an optional package? (In this case some functions should probably be rewritten to react in a nice way to the absence of data files.)


---

Comment by mabshoff created at 2008-04-30 06:10:04

Nah, it will be standard and I will take care of it shortly. You can take over from there and maybe add larger optional databases for polytopes of higher dimension if that makes sense.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-01 06:50:01

Ok, good news and bad news:

Bad news first: tice_polytope2.patch needs a rebase against Sage 3.0.1.alpha1 - out in 10 minutes.

```
sage-3.0.1.alpha1/devel/sage$ patch -p1 --dry-run < lattice_polytope2.patch
patching file sage/geometry/all.py
Hunk #1 succeeded at 3 with fuzz 1 (offset 2 lines).
patching file sage/geometry/lattice_polytope.py
Hunk #2 FAILED at 57.
1 out of 50 hunks FAILED -- saving rejects to file sage/geometry/lattice_polytope.py.rej
```

But I create a spkg with the polytope db data with all four files, which has been merged in Sage 3.0.1.alpha1.

Cheers,

Michael


---

Comment by novoselt created at 2008-05-01 06:59:41

Sorry for a probably dumb question, but what is a "rebase?"


---

Comment by mabshoff created at 2008-05-01 07:10:40

Replying to [comment:12 novoselt]:
> Sorry for a probably dumb question, but what is a "rebase?"

Hi,

no dumb questions here, just dumb answers. "rebase" in this context means that you should fix the patch so it does apply cleanly against the latest release. 3.0.1.alpha1 just came out and there is a binary for sage.math in case you don't want to build from scratch yourself. The problem in the patch was in the second hunk and since that was a rather large one I didn't want to fiddle in it and potentially break things. 

Let me know if you have any more questions.

Cheers,

Michael


---

Attachment

Updated patch


---

Comment by novoselt created at 2008-05-02 00:00:42

ZZ conversion patch still should be applied, I forgot about that one.


---

Comment by mabshoff created at 2008-05-02 10:20:16

The two new patches apply, but now I get the following, probably harmless, doctest failure:

```
sage -t  devel/sage/sage/rings/number_field/totallyreal_rel.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.rc0/tmp/totallyreal_rel.py", line 98:
    sage: sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, [[0,5],[0,5]])
Expected:
    [0, 5, 3, -alpha + 2, -alpha + 3, 1, 2, 4, alpha + 2, alpha + 3]
Got:
    [0, 5, -alpha + 2, -alpha + 3, 1, 2, 3, 4, alpha + 2, alpha + 3]
**********************************************************************
```

I will contact Craig Citro and John Voight to see what their take on this is. Once this is resolved I will merge both patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 17:28:03

John says:

```
Yes, the ordering of the elements does not at all affect the
correctness of the output--the most mathematically correct thing would
be to output a set.   This change can be due to any number of things,
but it's probably not worth ascertaining the exact cause.

JV 
```

Ergo: positive review since I will fix the doctest issue. Let's hope this is not CPU or endianess dependent.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 17:38:34

Resolution: fixed


---

Comment by mabshoff created at 2008-05-02 17:38:34

Merged in Sage 3.0.1.rc0
