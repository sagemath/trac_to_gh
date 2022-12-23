# Issue 7983: Notion of descent/major index in tableau.py is not mathematically standard

Issue created by migration from https://trac.sagemath.org/ticket/7983

Original creator: jbandlow

Original creation time: 2010-01-18 19:39:19

Assignee: sage-combinat

CC:  darij sage-combinat aschilling tscrim

The 'descents' and 'major_index' methods of a Tableau return what are more properly known as 'i_descents' and the 'i_maj' statistic.  These should be renamed accordingly, and the proper statistics put in their place.  See, eg., Richard Stanley--Enumerative Combinatorics, Vol. 2 for a reference to the usual definition.


---

Comment by arattan created at 2010-11-15 17:30:43

I have made a patch that resolves this issue.

What I have done is renamed the old methods 'major_index' and 'descents' to 'i_major_index' and 'i_descents'.  From what I can tell, only one other method refers to either of these methods and that is 'inversion', and I have not changed that at all except to refer to the new 'i_descents' (in particular I have not changed the name of 'inversion').

I have then made new methods called 'major_index' and 'descents' which use a more standard definition (i.e. the one on pages 361 and 363 of Enumerative Combinatorics Vol 2 by R. Stanley).


---

Comment by arattan created at 2010-11-15 17:30:43

Changing status from new to needs_review.


---

Comment by arattan created at 2010-11-15 17:32:29

patch to fix tableaux major index


---

Attachment

Thanks for the patch!  While I don't have time for a full review now, the main issue with this patch is going to be backward compatibility.  I'm pretty sure that the Macdonald polynomial code uses these functions, so sage --testall will probably fail after applying your patch.  That part will not be too hard to fix, but the bigger problem is for people who have sage code on their own machine.  When people upgrade sage and this change is included (without them necessarily knowing about it) this change could make their code behave in slightly wrong ways that are not obvious.  We really try to avoid that.

So I think the thing to do is to deprecate 'descents' and 'major_index' (look up deprecation in the developers guide), use 'i_descents' and 'i_major_index' for the existing statistics (as you have done) and give the classical statistics some new name. (Suggestions welcome!)


---

Comment by jbandlow created at 2010-11-16 14:11:26

Changing status from needs_review to needs_work.


---

Comment by arattan created at 2010-11-16 14:34:17

Replying to [comment:2 jbandlow]:
> Thanks for the patch!  While I don't have time for a full review now, the main issue with this patch is going to be backward compatibility.  I'm pretty sure that the Macdonald polynomial code uses these functions, so sage --testall will probably fail after applying your patch.  That part will not be too hard to fix, but the bigger problem is for people who have sage code on their own machine.  When people upgrade sage and this change is included (without them necessarily knowing about it) this change could make their code behave in slightly wrong ways that are not obvious.  We really try to avoid that.
> 
> So I think the thing to do is to deprecate 'descents' and 'major_index' (look up deprecation in the developers guide), use 'i_descents' and 'i_major_index' for the existing statistics (as you have done) and give the classical statistics some new name. (Suggestions welcome!)

Yes, I thought this would be an issue.  I actually made the patch a while ago but thought that precisely your objection would be raised.  Anyways, I decided to send it in and see what would happen.  It sounds like you have a good solution.

About a new name:  is "Major_Index" a bad idea?  I don't know about sage's naming conventions.


---

Comment by darij created at 2013-06-15 22:15:20

Changing keywords from "" to "combinat, tableaux".


---

Comment by darij created at 2013-06-15 22:15:20

Changing status from needs_work to needs_review.


---

Comment by darij created at 2013-06-15 22:27:33

3 years... not bad.

I've remade the patch from scratch (arattan's one didn't apply, unsurprisingly given its age) without renaming the existing `descents`, `major_index` etc. functions. While I agree with arattan that these functions should be deprecated and renamed, I think it's a top priority to get the correct ones out ASAP, under whatever name possible (I chose `standard_descents` and `standard_major_index`). I have taken the liberty to edit the docstrings of the old functions to explain that they are not what they seem to be; Jason and me are hardly the only people to trip over this. (To make things worse, the only two examples for the `major_index` function used to be cases where it happens to have the same values as the "correct" one!!)

The patch I attached does a few more things:

- Various improvements in the documentation of `tableaux.py`. The doc of `promotion` now warns about its nonstandard definition (#14641). A doctest has been added to check the equivalence between two definitions of promotion (this takes a couple seconds; let me know if that's too much).

- `up` and `down` methods are moved to `StandardTableaux` (look at what they do to see why) and now return the correct result for the empty tableau.

- The empty tableau is now correctly recognized as being rectangular.

Here's stuff that has not been done (partly because I am not sure about them -- comments are welcome):

- Copy/move attacking_pairs method to partitions.

- Generalize promotion_inverse to non-rectangular tableaux (particularly important since I believe promotion_inverse is what many people just call promotion).

- `Tableau([[]])` is standard and distinct from `Tableau([])`. Is this bad?

- Copy/move functionality to skew tableaux (this should be one separate huge ticket once other stuff is done, I guess).

- Allow creating tableaux of various ilks without checking the tableau conditions. This should be mostly called internally, so as to avoid having lots of redundant checking at runtime.

I have been building this patch on sage-5.10rc1 with only #8392 applied.


---

Comment by tscrim created at 2013-06-15 22:40:29

Hey Darij,

Two things I notice from a quick lookthrough:

1. `up()` and friends I think should remain where they are because there's no assumptions made on the initial tableau. However I do think there are some assumptions about standardness made in their implementation...
2. The reference to Stanley is indented one too many times.

I'll do a more through look-through and we can talk about 1. once I get to Orsay tomorrow.

Best,

Travis


---

Comment by darij created at 2013-06-15 22:52:02

Hi Travis,

thanks for looking into this! I've updated the reference; is it correct now?

As for `up`, is it possible that you meant `standard_descents` instead? I can't imagine how `up` and `down` would be used for anything other than standard tableaux; is it really useful to have a function to tell how many ways there are to add a square to a non-standard tableau to get a standard one? On the other hand, descents could indeed survive a generalization, though I don't know which choices are preferred here.

Best regards,
Darij


---

Comment by aschilling created at 2013-06-16 07:51:14

Hi Darij,

Thanks for your work on this. I think it reads a little odd to write that promotion is contrary to the paper by Stanley without giving a reference to what it actually is. Stanley's paper defines promotion on posets, whereas what you touched I think is promotion on tableaux. So it would be good to give a reference, for example the paper by Haiman, Discrete Math 99 (1992) 79-113.

Best,

Anne


---

Comment by darij created at 2013-06-16 08:18:35

Hi Anne,

good point, thanks -- I've added the reference to Haiman, and also a better reference (Sagan's cyclic sieving paper) for the conflicting notation. If you agree, the Stanley reference can be removed (he defines promotion for linear extensions of posets, then claiming that this obviously defines it for tableaux -- this isn't really central to the paper, though).

In other news, I've added documentation to `insert_word`, slightly improved that of `catabolism` and `lambda_catabolism`, and fixed a couple more typos. Since I don't know anything about catabolism, can you tell me if it's OK that `catabolism_sequence(Tableau([]))` does not terminate? I'm hesitating to call it a bug as long as I don't know if this should be defined at all for an empty tableau.

See you both this evening, dg


---

Comment by aschilling created at 2013-06-16 12:42:17

Hi Darij,

> In other news, I've added documentation to `insert_word`, slightly improved that of `catabolism` and `lambda_catabolism`, and fixed a couple more typos. Since I don't know anything about catabolism, can you tell me if it's OK that `catabolism_sequence(Tableau([]))` does not terminate? I'm hesitating to call it a bug as long as I don't know if this should be defined at all for an empty tableau.

Yes, probably you want that catabolism_sequence on the empty tableau is the empty tableau. The code only checks if the tableau is of height 1, but catabolism on the empty tableau is itself and hence it goes into an infinite loop.

Best,

Anne


---

Comment by darij created at 2013-06-16 17:08:44

Hi Anne,

done!

I've made one more minor change right now: `.up()` now outputs standard tableaux, not tableaux (just a question of casting the right type; they were standard, of course).

Best regards,
Darij (in Bures now)

PS, in case this was Travis's concern: I've grepped for appearances of `.up()`, `.up_list()`, `.down()` and `.down_list()` in the source code, and found only 2-3 files apart from `tableau.py` where these were used. They were used in a different context in those files, and my changes didn't break their doctests. Of course, someone's local code might get broken, but I don't know a good way to avoid that making any change at all. One minor issue that I did introduce is that execution of `.up()` and `.down()` now takes a tiny bit longer because of checking for standardness. I'll deal with it when I add a `check_input` parameter throughout `tableaux.py`.


---

Comment by darij created at 2013-06-17 16:16:51

Updated. `promotion_inverse` now works for non-rectangular tableaux as well (using a new `_slide_down` method). Moreover, it works fine for the empty tableau. Furthermore, `promotion` and `promotion_inverse` have been redefined on `StandardTableau` to automatically compute the `n` variable and to cast the result as a `StandardTableau` (not just a `Tableau`).


---

Comment by darij created at 2013-06-17 16:35:40

Changing keywords from "combinat, tableaux" to "combinat, tableaux, days49".


---

Comment by darij created at 2013-06-17 16:43:24

implements the right notions of major index and descents for standard tableaux without changing the old ones; extends promotion_inverse to non-rectangular tableaux; fixes a couple minor issues and improves doc; version 8


---

Attachment

Typo in a docstring fixed.


---

Comment by tscrim created at 2013-06-23 20:16:23

Hey Darij,

Here's the review patch.

Travis


---

Comment by darij created at 2013-06-23 20:42:32

Changing status from needs_review to positive_review.


---

Comment by darij created at 2013-07-16 19:18:20

Let's see if I'm getting the syntax right... patchbot:

apply trac_7983-major_index_and_other_tableau_fixes-dg.patch trac_7983-review-ts.patch


---

Attachment


---

Comment by tscrim created at 2013-07-19 13:15:07

Hey Darij,

I noticed a duplicate reference of `[St2009]`. It's already defined in `posets/poset.py`. I just tweaked my review patch to remove it from `tableau.py`.

Best,

Travis


---

Comment by tscrim created at 2013-07-19 13:25:48

Forgot to give the patchbot info.

For patchbot:

Apply: trac_7983-major_index_and_other_tableau_fixes-dg.patch trac_7983-review-ts.patch


---

Comment by jdemeyer created at 2013-08-02 14:11:45

Resolution: fixed
