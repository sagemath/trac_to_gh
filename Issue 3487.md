# Issue 3487: mercurial and sage

Issue created by migration from Trac.

Original creator: ghtdak

Original creation time: 2008-06-20 21:02:04

Assignee: was

When sage comes up it announces:

Loading SAGE library. Current Mercurial branch is: worldDomination

turns out, this is the current "clone"... when you are using "hg branches" in your clone it would be nice for it to say something like:

Loading SAGE library. Current Mercurial clone is: worldDomination on branch: riemannProof


---

Comment by ghtdak created at 2008-06-20 21:12:23

In thinking about it, I think this is more general.

So, one clones using sage -clone worldDomination

and then one asks what branch one is on with sage -branch

but, we should be able to clone and branch with the right syntax.  given the current switches, we need to be careful, but we should be able to clone and branch with switches to sage and ask where we are.

so, sage -branch could simply spit out clone and branch... but "sage -b" is an issue


---

Comment by AlexGhitza created at 2009-01-23 07:10:37

Changing type from defect to enhancement.


---

Comment by chapoton created at 2014-03-14 19:32:16

we have switched to git, this is obsolete


---

Comment by chapoton created at 2014-03-14 19:32:16

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-03-15 13:27:58

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:41:22

Resolution: wontfix
