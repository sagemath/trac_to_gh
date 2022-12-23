# Issue 9359: Get number field coverage up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/9359

Original creator: davidloeffler

Original creation time: 2010-06-28 16:50:54

Assignee: davidloeffler

CC:  rishi jdemeyer

Keywords: doctest

This patch removes the outdated file sage.rings.number_field.totallyreal_dsage (DSage was removed months ago), adds several number field files to the reference manual, and adds a number of missing doctests. Together with the independent but complementary patch at #9336 this gets doctest coverage up to 100%.


---

Comment by davidloeffler created at 2010-06-28 16:56:37

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-28 16:56:37

Here's a patch; it depends on #9244 (but *not* on #9336).


---

Comment by davidloeffler created at 2010-06-28 20:35:07

I've now moved one doctest from here to #9244, with the result that this patch is now independent of #9244 (and #9336). It does require the (positively-reviewed) patch at #9242. (Without #9242 it applies but one `TestSuite` doctest fails.)


---

Comment by lftabera created at 2010-07-02 19:51:58

Do you thing that


```
                # TODO -- relative extensions need to be completely rewritten, so one
                # can get easy access to representation of elements in their relative
                # form.  Functions like matrix below can't be done until relative
                # extensions are re-written this way.  Also there needs to be class
                # hierarchy for number field elements, integers, etc.  This is a
                # nontrivial project, and it needs somebody to attack it.  I'm amazed
                # how long this has gone unattacked.

                # Relative elements need to be a derived class or something.  This is
                # terrible as it is now. 
```


is no longer valid?


---

Comment by davidloeffler created at 2010-07-02 20:06:11

I confirm that I think that comment is no longer valid.

The comment has been lying undisturbed in the code for more than three years now (i.e. more than half of the entire lifespan of the Sage project), as "hg annotate" will show you. There were issues with matrix, getitem, etc for relative number field elements (e.g. #2551) but they have all been fixed now (a large number of them thanks to fwclarke's sterling work at #5508, which closed five or six tickets in one go).


---

Comment by lftabera created at 2010-07-06 10:50:32

Well, I think that it still applies the fact that relative number fields are slow. The construction of an underlying absolute number field to make computations has coefficient explosion problems. Also, there should be smarter calls to pari_nf pari_rnf that are operations that can be very costly.

So yes, the code works but it is inefficient in some interesting cases.


---

Comment by davidloeffler created at 2010-09-22 09:18:06

I've uploaded a new patch which works with 4.6.alpha1 (no massive changes, just a chunk that was rejected because it fixed a whitespace error also fixed by #8680, and two doctests that needed fixing because of the PARI update). Please, someone review this, before it bitrots again!


---

Comment by lftabera created at 2010-09-23 09:03:23

I still think that the comment about rewriting relative extensions still apply. But there have been changes, so I will think some alternative to that text.


---

Comment by davidloeffler created at 2010-09-23 09:25:17

I fully agree that relative extensions are not optimally implemented. By all means open another trac ticket for that if you like; but the specific issues (with matrix, etc) that the comment refers to are fixed (see #2551).


---

Comment by jdemeyer created at 2010-09-23 09:40:17

I personally prefer to leave

```
sage: I.ideal_below() 
Fractional ideal (b)   # 32-bit 
Fractional ideal (-b)  # 64-bit 
```

as it is, instead of

```
sage: I.ideal_below() == F.ideal(b) 
True
```


As an example, the first is more clear. But as I said, this is just a personal preference.


---

Comment by jdemeyer created at 2010-09-23 10:17:01

Also, the hunk

```
-            sage: I.ideal_below()
-            Fractional ideal (-b)  # 32-bit
-            Fractional ideal (b)   # 64-bit
+            sage: I.ideal_below() == F.ideal(b)
+            True
```

conflicts with #9764. So would you mind removing it?

Apart from that, the patch applies fine and doctests fine, even with #9753 and #9764 applied.


---

Attachment

New version without change to "ideal_below"


---

Comment by davidloeffler created at 2010-09-23 10:23:16

OK, I'm fine with that. I've just uploaded a patch with that hunk removed.


---

Comment by jdemeyer created at 2010-09-23 10:26:12

I think you should put

```
R.<x> = PolynomialRing(QQ)
```

or

```
x = polygen(QQ)
```

everywhere before

```
K.<foo> = NumberField(some_polynomial_in_x)
```


I imagine users copy-pasting the examples and finding they don't work because `x` is something else.


---

Comment by davidloeffler created at 2010-09-23 10:38:44

In my defence, I'd like to point out that your comment applies to most of the 600 or so number field doctests that were already there -- not just the 38 that I added -- and nobody's complained about it before :-) So we could have another ticket if you think it's an issue, but I claim it's orthogonal to this ticket.

(I personally think having the doctests this way is a _good_ thing, as it makes it clear that you can start Sage and type `K.<a> = Number Field(x^2 - 37)` and it will Just Work (tm), unlike in Magma for instance.)


---

Comment by jdemeyer created at 2010-09-24 08:09:05

Nice job, looks good to me!


---

Comment by jdemeyer created at 2010-09-24 08:09:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-27 09:34:42

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-09-27 09:34:42

There are a few conflicts with #8334. I will rebase this patch.


---

Attachment

Apply on top of #7883, #9898, #9753, #9764, #8334 and trac_9359.patch


---

Comment by jdemeyer created at 2010-09-27 21:05:25

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-27 21:05:25

With the attached patch, `make ptestlong` succeeds on 32-bit and 64-bit systems.


---

Comment by jdemeyer created at 2010-09-27 21:08:31

David, can you review my additions?


---

Comment by davidloeffler created at 2010-09-28 07:32:27

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-28 07:32:27

Looks fine -- thanks for cleaning that up.


---

Comment by mpatel created at 2010-09-28 09:48:53

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-28 09:48:53

Could someone update the commit string of the patch so its first line is a < 80 (or so) character summary of the changes that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.


---

Attachment

Qfolded patch with better commit string. Apply only this patch.


---

Comment by davidloeffler created at 2010-09-28 10:14:44

Changing status from needs_work to positive_review.


---

Comment by davidloeffler created at 2010-09-28 10:14:44

Done. I also qfolded into one patch.


---

Comment by mpatel created at 2010-09-28 10:54:08

Thanks, David.  I get some docbuild warnings

```
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:71: WARNING: duplicate citation C, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/small_primes_of_degree_one.rst
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:75: WARNING: duplicate citation M, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/crypto/lfsr.rst
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:82: WARNING: duplicate citation V, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/matrix/matrix2.rst
```

with the current [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2) "applied" to 4.6.alpha1.

Could you or Jeroen add a docfix patch?


---

Comment by mpatel created at 2010-09-28 10:54:08

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-09-28 11:17:30

fix duplicate citation


---

Attachment

Docfix patch as requested. We should really have a single table of citations for the whole reference manual -- one of the conflicts here was with another file citing 'the same textbook' -- but this'll do for now.


---

Comment by davidloeffler created at 2010-09-28 11:18:58

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-09-29 03:49:07

Resolution: fixed


---

Comment by mpatel created at 2010-09-29 03:54:02

Replying to [comment:26 davidloeffler]:
> Docfix patch as requested. We should really have a single table of citations for the whole reference manual -- one of the conflicts here was with another file citing 'the same textbook' -- but this'll do for now.

[This sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/dba6129183b3b6eb/b41ce82a5ee589fe?#b41ce82a5ee589fe) seems related.
