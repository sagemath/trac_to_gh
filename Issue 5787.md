# Issue 5787: [with patch, needs review] Improve doctest coverage for sage/modular/hecke (continued)

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-04-14 21:06:02

Assignee: davidloeffler

Keywords: doctests

This is a continuation of #5736. The patch which I am about to upload contains more doctests and bugfixes for sage/modular/hecke. The main change this makes is in the methods for constructing elements of Hecke algebras: previously these accepted more or less arbitrary matrices as input (despite the fact that all Hecke algebras in Sage are supposed to be commutative). Similarly, any element of a full Hecke algebra could be coerced into the corresponding anemic algebra -- including the Hecke operators at primes dividing the level -- which is not great.

I've also added an extra check into the !__mul!__ method of the MatrixMorphism class; what's the point of having morphism objects that remember their domain and codomain if one doesn't check compatibility when composing them?


---

Comment by davidloeffler created at 2009-04-15 14:04:40

Oops -- sorry, I messed up, that patch was incomplete (it applies OK but doctests do not pass). Please use both the patches above; then it will work.


---

Comment by davidloeffler created at 2009-04-15 14:04:40

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-05-04 16:47:26

replaces all previous patches


---

Attachment

The patch I've just uploaded unifies the previous two patches, and adds some more doctests to bring the coverage higher still (although not quite to 100% as I don't have time right now to understand some of the weirder things that are going on in hecke/submodule.py). Note that again this patch is designed to be applied over the patches at #5736.


---

Attachment


---

Comment by craigcitro created at 2009-05-08 09:47:14

This looks good. I started adding a few changes while refereeing, and then I got motivated and went ahead and finished doctesting `sage/modular/hecke`. So positive review for David's part, and now someone needs to review my (much shorter) patch. After this, the only part of `sage/modular` still needing any doctesting is the `modsym` directory.


---

Comment by cremona created at 2009-05-09 17:29:55

Replying to [comment:3 craigcitro]:
> This looks good. I started adding a few changes while refereeing, and then I got motivated and went ahead and finished doctesting `sage/modular/hecke`. So positive review for David's part, and now someone needs to review my (much shorter) patch. After this, the only part of `sage/modular` still needing any doctesting is the `modsym` directory. 

I think it would be better for David to review Craig's extra patch rather than a newcomer.

Last docdays I started properly doctesting modsym, but only got two of the files done.  I do intend to do more.


---

Comment by davidloeffler created at 2009-05-10 12:34:54

At a glance, I can spot two small problems: firstly, the new doctest for `__cmp__` in submodule.py fails on my machine; secondly, Craig's patch changes the intersection method (so it works for modular forms spaces as well as modular symbols) but I also did the same in #4357, so those are going to conflict.

I'm not entirely sure why the first failure happens: although `__cmp__` doctests are always irritatingly machine-dependent when comparing objects of different types, the comparison order for submodules of a common ambient module should be consistent, surely? I'm changing this back to "needs work" until we can get to the bottom of this. Once that's sorted I'll do a rebased version that combines this with #4357.

David


---

Attachment

rebased not  to conflict with #4357


---

Attachment

On inspection, it turns out that the `__cmp__` routine was written stupidly anyway, so I rewrote it. Hence the third patch above. So now applying trac_5787-all.patch, trac_5787_pt2_rebased.patch, and trac_5787_pt3.patch (on top of the already-merged #5736 patches and #4357) should not conflict -- at least it doesn't on my machine.

Craig: I'm entirely happy with the rest of your changes, so if you could just check to make sure that applying #5736 + #4357 + the patches here works for you and passes doctests, I think we can call this a positive review at last.


---

Comment by craigcitro created at 2009-05-11 06:32:48

Yep, I'm happy with the changes. I didn't get a chance to do a full doctest run, but Michael surely will when he commits, so I'm going to leave that to him. :)


---

Comment by mabshoff created at 2009-05-11 08:28:35

Merged 

 * trac_5787-all.patch
 * trac_5787_pt2_rebased.patch
 * trac_5787_pt3.patch

in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 08:28:35

Resolution: fixed
