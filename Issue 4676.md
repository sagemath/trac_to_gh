# Issue 4676: Polyhedral improvements

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-12-02 17:17:34

Assignee: mhampton

Keywords: polyhedra, polytopes

This adds more built-in polytopes (more Archimedean solids) and some new methods such as the Gale transform, bipyramid construction, edge truncation, and perspective projection with (optionally) hidden faces invisible.  The Schlegel projection code has also been somewhat refactored to make it more general in the future.


---

Attachment

based against 3.2.1-rc1


---

Comment by mabshoff created at 2008-12-05 09:46:18

Arnaud,

can you review this?

Cheers,

Michael


---

Comment by jason created at 2008-12-24 16:46:26

I applied this to 3.2.2 successfully.  No doctests were broken in the affected file (there was one doctest that returned an error both before and after the patch, but the warning points to an error in my install, not in the code).  I generated lots of pretty pictures, one for each of the new polytopes.  Everything seemed to work.  However, it would probably be good to have someone who is more familiar with the math look at this.


---

Comment by wdj created at 2008-12-25 16:01:23

I like this too. I checked the Gale transform against section 5.3 in Ewald, Combinatorial convexity and algebraic geometry, and it agreed with the example there.

I wish there was a way to use tachyon to plot the objects but the viewer='tachyon' option is ignored. I agree with Jason that the plots are beautiful anyway.

I give this a thumbs up but maybe Arnaud should review this too? Based on a recent "code freeze" email from Michael Abshoff, it seems as though it will not make 3.3.


---

Comment by abergeron created at 2008-12-30 20:54:46

Only two small stylistic points:

- Gale_transform() -> gale_transform()
- Schlegel_transform() -> schlegel_transform()

I don't think it's good style to have methods begin with a capital, even when they refer to a person's name.

Otherwise, I don't know since when I was familiar with the math involved.  I did look up references though, and everything looks good.

If the two points above are fixed, then I give it a positive review.


---

Comment by mhampton created at 2009-01-11 17:02:02

rebased on 3.2.3, supercedes previous patch, addresses review


---

Attachment


---

Comment by mabshoff created at 2009-01-12 00:39:29

Resolution: fixed


---

Comment by mabshoff created at 2009-01-12 00:39:29

Merged in Sage 3.3.alpha0
