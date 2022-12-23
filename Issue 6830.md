# Issue 6830: [with patch, needs review] Ideals of a Hecke Algebra

Issue created by migration from https://trac.sagemath.org/ticket/6830

Original creator: wakep

Original creation time: 2009-08-26 22:20:44

Assignee: craigcitro

CC:  robharron

Keywords: ideal, hecke

Added code for ideals of a Hecke algebra.


---

Comment by wakep created at 2009-08-26 22:32:16

This patch depends on the basis of a Hecke algebra code from ticket #6768


---

Attachment


---

Comment by cremona created at 2009-08-27 20:27:51

The patch is now visible;  I don't have time to test it very soon , sorry.


---

Comment by cremona created at 2009-12-10 21:40:36

Could you rebase this to apply to 4.3.alpha1?  As it stands the patch does not apply, but I expect it will be an easy fix.

Generally the code looks good to me (though there is at least one functions with no doctests at present).

Once rebased, I'll test it properly.


---

Comment by cremona created at 2009-12-10 21:40:36

Changing status from needs_review to needs_work.


---

Comment by kedlaya created at 2016-08-16 19:36:22

Just discovered this moribund ticket. I might actually find this useful! Does anyone intend to revisit this?


---

Comment by kedlaya created at 2016-08-19 23:22:13

To quote an email from wakep:
"I wrote that code as part of an undergraduate summer research program. I was not particularly savvy with Sage development then (and even less-so now). As far as I understand, the reason that it became moribund is that it took some time to get an initial review, and by the time it got one, Sage was on to a new version. I was asked to "rebase" it to the new version, but I didn't know how to do that. (I had started graduate school by then and had no time to play with Sage.)

The upshot is that I have no particular intention to revisit the code, but I think that it wouldn't take much to get it working. I'd be happy to work on it, but I wouldn't know what to do."

So I (kedlaya) took the liberty of manually rebasing the patch. I haven't even tried to build this yet; probably that will reveal some other issues.

----
New commits:


---

Comment by kedlaya created at 2016-08-20 03:39:54

robharron points out that it would be more robust to create the Hecke algebra as an abstract ring (represented internally as a quotient of a polynomial ring over Z) plus maps back and forth (e.g., given N, turn the N-th Hecke operator into an abstract ring element). Then one could deal with ideals on the ring side, which would give access to all existing commutative algebra functionality.


---

Comment by git created at 2016-08-20 21:04:35

Branch pushed to git repo; I updated commit sha1. New commits:
