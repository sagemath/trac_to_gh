# Issue 4326: Root systems improvements

Issue created by migration from https://trac.sagemath.org/ticket/4326

Original creator: nthiery

Original creation time: 2008-10-20 08:17:24

Assignee: nthiery

CC:  sage-combinat

Doc:
 - Use $F_4$ instead of F4 

DynkinDiagram:
 - allow for slicing notation for column/row extraction: c[i,:]

AmbientSpace:
 - fundamental coweights by appropriate scaling of the fundamental weights
 - embedding coweight lattice

WeightLatticeRealization
 - scalar product with coweight lattice in finite dimension

Generic:
 - (signed) reduced word for a chamber/alcove

Classical case:
 - reverse map to coroot space and coroot lattice by scalar product with the fundamental weights
 - => associated coroot
 - s_\alpha on the (co)root and (co)weight lattice for any root \alpha

Affine case:
 - analogues whenever well defined 
 - reduced words for translations elements.


---

Comment by nthiery created at 2009-05-19 06:23:07

Changing status from new to assigned.


---

Attachment


---

Comment by nthiery created at 2009-06-11 05:54:59

Changing keywords from "" to "root systems".


---

Comment by bump created at 2009-07-21 23:10:29

Normally I would have waited for the category patches to be merged
before reviewing this patch. However I recieved an email from Tom Boothby
urging me to do the review now, so here it is.

This review is based on the version of the patches in the
combinat queue. This is because it depends on patches that
have not been merged yet.

After qpushing the combinat queue up to this patch but
not beyond, all tests pass. This is with Sage 4.1 and
the last changeset is this one:


```
changeset:   1520:188022ff52b9
tag:         tip
user:        Nicolas M. Thiery <nthiery@users.sf.net>
date:        Tue Jul 21 01:13:42 2009 +0200
summary:     Update
```


The patch adds quite a bit of new functionality for working
with Coxeter groups and affine Weyl groups. The following
new files are added. There are new categories added for
CoxeterGroups and WeylGroups. There is an extensive
ChangeLog in the comments at the beginning of the patch.

Since the patch is over 11,000 lines of code, there could
very well be bugs in it. However it probably does not
introduce significant new bugs in the portion of the
code that deals with classical root systems, since I
used it extensively during the spring of 2009 in
connection with #5794. Every classical Cartan type
and many reducible types have been created and worked
with. What problems I found then were fixed. Moreover
the portion of the code that deals with affine root
systems was similarly very tested by Anne Schilling
in connection with affine crystals.

Therefore the most uncertainty in my is with the new
functionality for Coxeter groups. I will mention one
"wish" in this direction, which is that in addition
to implementing the Bruhat covers, the Bruhat order
be properly implemented. This could be done efficiently
using Proposition 1.1 in Stembridge, A Short
Derivation of the Möbius Function for the Bruhat
Order, Journal of Algebraic Combinatorics 25,
(2007).

This wish is not a reason to hold up merging the
patch. Rather the patch should be merged as soon as
possible and such changes can be made later.


---

Comment by mvngu created at 2009-07-23 08:43:55

Let me get this straight. Tickets #6136, #6253, #6250, and #5891 must first be merged before merging this ticket?


---

Comment by nthiery created at 2009-07-23 08:58:35

Replying to [comment:8 mvngu]:
> Let me get this straight. Tickets #6136, #6253, #6250, and #5891 must first be merged before merging this ticket?

Indeed. Should we use a specific subject for patches that have a positive review, but have dependencies on not yet merged tickets?
Something like:

[with patch, positive review, depends on #6136, #6253, #6250, #5891] ...


---

Comment by mvngu created at 2009-07-23 09:04:31

Replying to [comment:9 nthiery]:
> Indeed. Should we use a specific subject for patches that have a positive review, but have dependencies on not yet merged tickets?
> Something like:
> 
> [with patch, positive review, depends on #6136, #6253, #6250, #5891] ...
No, not really. I just want to double check since the patch is rather huge and I was concerned about it getting bit rotten. Anyway, people who uses the merge script would not be able to easily tell whether a positive-reviewed ticket has other dependencies.


---

Comment by nthiery created at 2009-11-06 14:16:55

Latest version of the patch from the Sage-Combinat patch server (no change since Dan's review)


---

Attachment


---

Comment by nthiery created at 2009-11-18 13:27:24

Fix ClassicalWeylSubgroup and remove unneeded long time, as spotted by Mike


---

Attachment


---

Comment by nthiery created at 2009-11-18 13:27:39

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2009-11-18 13:28:52

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-11-18 13:34:34

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-18 13:34:34

The new patch looks okay to me.


---

Comment by mhansen created at 2009-11-19 17:00:28

Resolution: fixed
