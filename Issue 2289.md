# Issue 2289: [with doc patch, needs review] make the constructions document prettier and more consistent

Issue created by migration from https://trac.sagemath.org/ticket/2289

Original creator: AlexGhitza

Original creation time: 2008-02-24 04:08:14

Assignee: tba

The patch is somewhat big but most of the changes are cosmetic, aimed at making const.tex more consistent internally (and with the tutorial) and prettier to behold.

I've also exposed a number of examples that were %skip-ped previously, tested them and fixed a few of them that were buggy.



---

Comment by wdj created at 2008-02-24 14:10:28

I think this patch should be made after applying the earlier patch at
http://trac.sagemath.org/sage_trac/ticket/2274
(which is still waiting for review) for const.tex. However, that patch requires the coding theory patch (also in ticket 2274) as well to pass sage -t.


---

Comment by wdj created at 2008-02-24 19:58:06

The above-mentioned patch for 2274 just got a positive review, so it is okay to make your change on top of it now.


---

Comment by AlexGhitza created at 2008-02-24 20:19:26

OK, so I incorporated David's 435.patch from #2274, and retested after applying 8672.patch also from #2274.

I replaced my old patch with the new and improved one.


---

Comment by wdj created at 2008-02-26 23:55:21

I applied this patch to const.tex in sage-2.10.3.alpha0 and got:
4 out of 153 hunks FAILED -- saving rejects to file devel/doc/const/const.tex.rej

I'm not sure that the problem is. Could the patch possibly be recreated using
sage-2.10.3.alpha0?


---

Comment by AlexGhitza created at 2008-02-27 00:44:10

Hi, I know exactly what the problem is.  When your coding theory patch from #2274 got merged, so did your modifications to const.tex that you had made there.  But I had already merged them into my patch here, so mercurial got confused.

But no worries.  I've fixed things and rebased the patch against sage-2.10.3.alpha0, so it should all be good now.

Note that if you take a look at const.pdf, there are still a few long lines.  They are trickier to deal with (wrapping them breaks doctests, etc.) so I'm still thinking about it.  This is also an issue with tut.tex (in a few places).  It will have to get fixed later...


---

Attachment

fixed some doctest failures


---

Comment by wdj created at 2008-02-27 11:43:27

This patch is rather large and does not apply cleanly for me to the 2.10.3.alpha0 base (there were 4 rejects, but does now pass sage -t and I recommend acceptance.


---

Comment by mabshoff created at 2008-02-27 21:25:26

Resolution: fixed


---

Comment by mabshoff created at 2008-02-27 21:25:26

Merged in Sage 2.10.3.rc0
