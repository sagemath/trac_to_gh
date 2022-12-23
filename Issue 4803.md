# Issue 4803: improvements to the polyhedra module documentation

Issue created by migration from https://trac.sagemath.org/ticket/4803

Original creator: sbarthelemy

Original creation time: 2008-12-15 09:50:23

Assignee: sbarthelemy

CC:  mhampton

The attached patch corrects some imprecisions in the polyhedra module documentation.


---

Attachment


---

Comment by mhampton created at 2008-12-15 10:15:00

There are a couple typos in this proposed documentation change:

"minkowsky sum" should be "Minkowski sum"
"positive (aka conic) combination" should be "positive (aka convex) combination"

(unless there is a meaning of conic combination that I don't know).

The Fukuda reference is good, it would be better to add a "REFERENCES" section since eventually such sections might be searched for and organized.

Thanks for working on this!
Marshall Hampton


---

Comment by mhampton created at 2008-12-15 10:15:00

Changing component from algebra to geometry.


---

Comment by sbarthelemy created at 2008-12-15 11:04:57

Here is a new patch, against the previous

> "minkowsky sum" should be "Minkowski sum"

I fixed that thanks

> "positive (aka conic) combination" should be "positive (aka convex) combination"
> (unless there is a meaning of conic combination that I don't know).

see http://en.wikipedia.org/wiki/Conical_combination

Dattorro [1] uses "conic hull" instead of "conical hull". Fukuda uses noneg(ray1, ray2,...). I don't know which term is better. In the new patch I chose "conic hull", change it to what sounds best to you, english speakers.

> The Fukuda reference is good, it would be better to add a "REFERENCES" section since eventually such sections might be searched for and organized.

You're right, fixed in the patch

> Thanks for working on this!

Thanks for the feedback!

Sébastien

[1] http://meboo.convexoptimization.com/BOOK/convexgeometry.pdf


---

Attachment


---

Comment by mhampton created at 2008-12-16 14:09:07

Great, I think with those changes it should go in.  Its unclear to me what the best term is for the "conic hull" but that can be tweaked later.


---

Comment by mabshoff created at 2008-12-17 14:37:46

Resolution: fixed


---

Comment by mabshoff created at 2008-12-17 14:37:46

Merged in Sage 3.2.2.rc1
