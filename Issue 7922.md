# Issue 7922: Pickling fails in WeightRing

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-01-13 16:14:55

Assignee: bump

CC:  bump sage-combinat

First issue caught by #7921:


```
sage: A2 = WeylCharacterRing(['A',2])
sage: a2 = WeightRing(A2)
sage: TestSuite(a2).run()
Failure in _test_element_pickling:
Traceback (most recent call last):
...
AssertionError: 2*a2(0,0,0) != 2*a2(0,0,0)
```


Indeed:

```
sage: x = a2.an_element()
sage: x == loads(dumps(x))
False
```


I assume that this is an issue in equality test. This should be fixed for free when WeighRing's will use CombinatorialFreeModules
and categories.


---

Comment by bump created at 2010-09-05 13:08:00

Regarding speed, testing a large number of branching rules show that the patch is a substantial speedup over the old code with a caveat: the old code has an option cache=true for WeylCharacterRings. If this option (which is not the default) is selected for every WeylCharacterRing, then the old code is faster. Typical times:

|        |          |
|--------|----------|
|Old Code|48 seconds|
|New Code|25 seconds|
|Old Code, cache=true|18 seconds|
Since I made the method `_irr_weights` a cached method, the caching done in the new code is approximately equivalent to the caching in the old code, so at the moment I don't see any way to improve the situation.


---

Comment by bump created at 2010-09-05 13:08:00

Changing status from new to needs_review.


---

Comment by bump created at 2010-09-06 17:08:40

Revised and reposted the patch in view of Nicolas' comment to use _from_dict(coerce=True).


---

Comment by bump created at 2010-09-11 15:31:00

Converts WeylCharacterRings and WeightRings to use category framework


---

Attachment

I uploaded a revised version of the patch. The only change is in classical_crystals.py, where the revision of WeylCharacterRings necessitated a revision.


---

Comment by bump created at 2010-10-29 00:31:14

Requires rebuilding the pickle jar.


---

Attachment

#7922: WeylCharacters inherit from CombinatorialFreemodule (substantial speedup)


---

Comment by bump created at 2010-11-15 19:28:22

Since #9838 was merged in sage-4.6.1.alpha1, this patch needed rebasing.

I therefore posted trac_7922-rebased-4.6.1.


---

Comment by bump created at 2011-02-08 19:25:41

7922: thematic tutorial revision


---

Attachment

This patch slightly conflicts with #8442 which was merged. So I'm posting a second patch trac_7922-doc.patch which revises the thematic tutorial.


---

Attachment

#7922: Revision of Weyl Character Rings


---

Comment by bump created at 2011-03-18 12:36:27

I have posted trac_7922-rebased-4.7.alpha1.patch, which
addresses many of the comments in the reviewer patch:

http://combinat.sagemath.org/patches/file/tip/trac_7922-review-nt.patch

Those changes that are not addressed are discussed here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/277e146862632d72


---

Comment by bump created at 2011-03-18 21:28:49

#7922: revised pickle jar


---

Attachment


---

Attachment

#7922: explanation of how the pickle jar is remade


---

Comment by bump created at 2011-03-18 21:38:13

See [attachment: pickle-notes] for an explanation of how the pickle jar was remade.


---

Comment by bump created at 2011-03-22 20:33:30

The revised patch [attachment:trac_7922-rebased-4.7.alpha2] includes the revised coercion mechanism and other changes proposed by Nicolas.

In view of this message:

http://trac.sagemath.org/sage_trac/ticket/10354#comment:11

I posted a tarball containing only the new pickles, and a list of obsolete pickles to be discarded.


---

Comment by bump created at 2011-03-24 18:42:55

#7922: revision of Weyl Character Rings


---

Attachment

#7922: replacement pickles


---

Attachment

Hi Dan,

I just did a final proofreading, fixed a couple typos, updated coerce_to_sl in the doctests of the thematic tutorials, and removed some trailing white space and tabs.

For me it is now all good to go. Please check my reviewer's patch on the sage-combinat patch server. If it's ok with you, you can fold/upload and set a positive review here on my behalf.

[http://combinat.sagemath.org/patches/file/tip/trac_7922-final-review-nt.patch](http://combinat.sagemath.org/patches/file/tip/trac_7922-final-review-nt.patch)

Cheers,
                       Nicolas


---

Comment by nthiery created at 2011-04-05 08:48:06

Changing type from defect to enhancement.


---

Comment by bump created at 2011-04-06 23:09:00

#7922: Categories for Weyl character rings and weight rings


---

Attachment

Hi Dan,

I just checked out your final changes on the Sage-Combinat queue (trac_7922_alpha3-changes.patch), and it looks all good. So the final rebased patch you just posted (and which includes the above) is good to go.

Positive review!


---

Comment by nthiery created at 2011-04-07 14:29:48

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-31 17:11:48

Resolution: fixed


---

Comment by jdemeyer created at 2011-06-22 20:17:49

This needs a few small fixes:
 1. at various places `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the indentation is inconsistent.  It should be 4 spaces but in the newly added examples it is more or less random.
 1. in `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the test on line 250 takes a very long time but is not marked as such.

Please add an additional patch fixing these issues.


---

Comment by jdemeyer created at 2011-06-22 20:17:49

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-06-22 20:17:49

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2013-06-03 12:54:14

Resolution: fixed


---

Comment by nthiery created at 2013-06-03 13:35:51

Replying to [comment:18 jdemeyer]:
> This needs a few small fixes:
>  1. at various places `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the indentation is inconsistent.  It should be 4 spaces but in the newly added examples it is more or less random.
>  1. in `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the test on line 250 takes a very long time but is not marked as such.
> 
> Please add an additional patch fixing these issues.

Fixing the indentation is now #14678. The very long time is not necessary anymore, most likely thanks to the optimizations in #13391 (the example takes 0.22s on my machine).
