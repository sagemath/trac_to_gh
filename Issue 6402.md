# Issue 6402: Fix bugs + improve documentation for overconvergent modular forms

Issue created by migration from https://trac.sagemath.org/ticket/6402

Original creator: davidloeffler

Original creation time: 2009-06-25 12:11:59

Assignee: craigcitro

CC:  was

This patch fixes lots of bugs + adds a substantial amount of documentation and examples, based on my talk at Sage Days 16.


---

Comment by davidloeffler created at 2009-06-25 12:13:47

patch against 4.0.2


---

Attachment

Here's a patch.


---

Comment by AlexGhitza created at 2009-08-19 09:44:33

Looks good, and the added documentation is really great.

I'm attaching a tiny referee patch fixing a few typos, and if you are ok with it we can give this a positive review.

There is one small issue, which I leave up to you whether you want to fix it or not: in the method `valuation_plot`, you added an optional argument `rmax`, but the docstring says nothing about its role.


---

Comment by AlexGhitza created at 2009-08-19 09:45:16

apply after the previous patch


---

Attachment

Fine by me.


---

Comment by mvngu created at 2009-08-23 13:27:37

reviewer patch: more typo fixes


---

Attachment

The reviewer patch `trac_6402-typos.patch` fixes some typos left over from the previous two patches. If that is OK, then the whole ticket can be merged.


---

Comment by davidloeffler created at 2009-08-24 08:30:07

I certainly have no problems with Minh's suggestions. Can I suggest we get this in soon, rather than fixing every conceivable micro-bug, since the initial patch fixes some rather major and embarassing bugs that render the whole module basically unusable?


---

Comment by mvngu created at 2009-08-24 12:34:57

Resolution: fixed


---

Comment by mvngu created at 2009-08-24 12:36:33

Merged all three patches in this order:

 1. `trac_6402-overconvergent_fixes.patch`
 1. `trac_6402-referee.patch`
 1. `trac_6402-typos.patch`
