# Issue 9359: Get number field coverage up to 100%

archive/issues_009359.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  rishi jdemeyer\n\nKeywords: doctest\n\nThis patch removes the outdated file sage.rings.number_field.totallyreal_dsage (DSage was removed months ago), adds several number field files to the reference manual, and adds a number of missing doctests. Together with the independent but complementary patch at #9336 this gets doctest coverage up to 100%.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9359\n\n",
    "created_at": "2010-06-28T16:50:54Z",
    "labels": [
        "number fields",
        "major",
        "enhancement"
    ],
    "title": "Get number field coverage up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9359",
    "user": "davidloeffler"
}
```
Assignee: davidloeffler

CC:  rishi jdemeyer

Keywords: doctest

This patch removes the outdated file sage.rings.number_field.totallyreal_dsage (DSage was removed months ago), adds several number field files to the reference manual, and adds a number of missing doctests. Together with the independent but complementary patch at #9336 this gets doctest coverage up to 100%.

Issue created by migration from https://trac.sagemath.org/ticket/9359





---

archive/issue_comments_088854.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T16:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88854",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088855.json:
```json
{
    "body": "Here's a patch; it depends on #9244 (but *not* on #9336).",
    "created_at": "2010-06-28T16:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88855",
    "user": "davidloeffler"
}
```

Here's a patch; it depends on #9244 (but *not* on #9336).



---

archive/issue_comments_088856.json:
```json
{
    "body": "I've now moved one doctest from here to #9244, with the result that this patch is now independent of #9244 (and #9336). It does require the (positively-reviewed) patch at #9242. (Without #9242 it applies but one `TestSuite` doctest fails.)",
    "created_at": "2010-06-28T20:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88856",
    "user": "davidloeffler"
}
```

I've now moved one doctest from here to #9244, with the result that this patch is now independent of #9244 (and #9336). It does require the (positively-reviewed) patch at #9242. (Without #9242 it applies but one `TestSuite` doctest fails.)



---

archive/issue_comments_088857.json:
```json
{
    "body": "Do you thing that\n\n\n```\n                # TODO -- relative extensions need to be completely rewritten, so one\n                # can get easy access to representation of elements in their relative\n                # form.  Functions like matrix below can't be done until relative\n                # extensions are re-written this way.  Also there needs to be class\n                # hierarchy for number field elements, integers, etc.  This is a\n                # nontrivial project, and it needs somebody to attack it.  I'm amazed\n                # how long this has gone unattacked.\n\n                # Relative elements need to be a derived class or something.  This is\n                # terrible as it is now. \n```\n\n\nis no longer valid?",
    "created_at": "2010-07-02T19:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88857",
    "user": "lftabera"
}
```

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

archive/issue_comments_088858.json:
```json
{
    "body": "I confirm that I think that comment is no longer valid.\n\nThe comment has been lying undisturbed in the code for more than three years now (i.e. more than half of the entire lifespan of the Sage project), as \"hg annotate\" will show you. There were issues with matrix, getitem, etc for relative number field elements (e.g. #2551) but they have all been fixed now (a large number of them thanks to fwclarke's sterling work at #5508, which closed five or six tickets in one go).",
    "created_at": "2010-07-02T20:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88858",
    "user": "davidloeffler"
}
```

I confirm that I think that comment is no longer valid.

The comment has been lying undisturbed in the code for more than three years now (i.e. more than half of the entire lifespan of the Sage project), as "hg annotate" will show you. There were issues with matrix, getitem, etc for relative number field elements (e.g. #2551) but they have all been fixed now (a large number of them thanks to fwclarke's sterling work at #5508, which closed five or six tickets in one go).



---

archive/issue_comments_088859.json:
```json
{
    "body": "Well, I think that it still applies the fact that relative number fields are slow. The construction of an underlying absolute number field to make computations has coefficient explosion problems. Also, there should be smarter calls to pari_nf pari_rnf that are operations that can be very costly.\n\nSo yes, the code works but it is inefficient in some interesting cases.",
    "created_at": "2010-07-06T10:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88859",
    "user": "lftabera"
}
```

Well, I think that it still applies the fact that relative number fields are slow. The construction of an underlying absolute number field to make computations has coefficient explosion problems. Also, there should be smarter calls to pari_nf pari_rnf that are operations that can be very costly.

So yes, the code works but it is inefficient in some interesting cases.



---

archive/issue_comments_088860.json:
```json
{
    "body": "I've uploaded a new patch which works with 4.6.alpha1 (no massive changes, just a chunk that was rejected because it fixed a whitespace error also fixed by #8680, and two doctests that needed fixing because of the PARI update). Please, someone review this, before it bitrots again!",
    "created_at": "2010-09-22T09:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88860",
    "user": "davidloeffler"
}
```

I've uploaded a new patch which works with 4.6.alpha1 (no massive changes, just a chunk that was rejected because it fixed a whitespace error also fixed by #8680, and two doctests that needed fixing because of the PARI update). Please, someone review this, before it bitrots again!



---

archive/issue_comments_088861.json:
```json
{
    "body": "I still think that the comment about rewriting relative extensions still apply. But there have been changes, so I will think some alternative to that text.",
    "created_at": "2010-09-23T09:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88861",
    "user": "lftabera"
}
```

I still think that the comment about rewriting relative extensions still apply. But there have been changes, so I will think some alternative to that text.



---

archive/issue_comments_088862.json:
```json
{
    "body": "I fully agree that relative extensions are not optimally implemented. By all means open another trac ticket for that if you like; but the specific issues (with matrix, etc) that the comment refers to are fixed (see #2551).",
    "created_at": "2010-09-23T09:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88862",
    "user": "davidloeffler"
}
```

I fully agree that relative extensions are not optimally implemented. By all means open another trac ticket for that if you like; but the specific issues (with matrix, etc) that the comment refers to are fixed (see #2551).



---

archive/issue_comments_088863.json:
```json
{
    "body": "I personally prefer to leave\n\n```\nsage: I.ideal_below() \nFractional ideal (b)   # 32-bit \nFractional ideal (-b)  # 64-bit \n```\n\nas it is, instead of\n\n```\nsage: I.ideal_below() == F.ideal(b) \nTrue\n```\n\n\nAs an example, the first is more clear. But as I said, this is just a personal preference.",
    "created_at": "2010-09-23T09:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88863",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_088864.json:
```json
{
    "body": "Also, the hunk\n\n```\n-            sage: I.ideal_below()\n-            Fractional ideal (-b)  # 32-bit\n-            Fractional ideal (b)   # 64-bit\n+            sage: I.ideal_below() == F.ideal(b)\n+            True\n```\n\nconflicts with #9764. So would you mind removing it?\n\nApart from that, the patch applies fine and doctests fine, even with #9753 and #9764 applied.",
    "created_at": "2010-09-23T10:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88864",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_088865.json:
```json
{
    "body": "Attachment\n\nNew version without change to \"ideal_below\"",
    "created_at": "2010-09-23T10:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88865",
    "user": "davidloeffler"
}
```

Attachment

New version without change to "ideal_below"



---

archive/issue_comments_088866.json:
```json
{
    "body": "OK, I'm fine with that. I've just uploaded a patch with that hunk removed.",
    "created_at": "2010-09-23T10:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88866",
    "user": "davidloeffler"
}
```

OK, I'm fine with that. I've just uploaded a patch with that hunk removed.



---

archive/issue_comments_088867.json:
```json
{
    "body": "I think you should put\n\n```\nR.<x> = PolynomialRing(QQ)\n```\n\nor\n\n```\nx = polygen(QQ)\n```\n\neverywhere before\n\n```\nK.<foo> = NumberField(some_polynomial_in_x)\n```\n\n\nI imagine users copy-pasting the examples and finding they don't work because `x` is something else.",
    "created_at": "2010-09-23T10:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88867",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_088868.json:
```json
{
    "body": "In my defence, I'd like to point out that your comment applies to most of the 600 or so number field doctests that were already there -- not just the 38 that I added -- and nobody's complained about it before :-) So we could have another ticket if you think it's an issue, but I claim it's orthogonal to this ticket.\n\n(I personally think having the doctests this way is a *good* thing, as it makes it clear that you can start Sage and type `K.<a> = Number Field(x^2 - 37)` and it will Just Work (tm), unlike in Magma for instance.)",
    "created_at": "2010-09-23T10:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88868",
    "user": "davidloeffler"
}
```

In my defence, I'd like to point out that your comment applies to most of the 600 or so number field doctests that were already there -- not just the 38 that I added -- and nobody's complained about it before :-) So we could have another ticket if you think it's an issue, but I claim it's orthogonal to this ticket.

(I personally think having the doctests this way is a *good* thing, as it makes it clear that you can start Sage and type `K.<a> = Number Field(x^2 - 37)` and it will Just Work (tm), unlike in Magma for instance.)



---

archive/issue_comments_088869.json:
```json
{
    "body": "Nice job, looks good to me!",
    "created_at": "2010-09-24T08:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88869",
    "user": "jdemeyer"
}
```

Nice job, looks good to me!



---

archive/issue_comments_088870.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-24T08:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88870",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088871.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-27T09:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88871",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_088872.json:
```json
{
    "body": "There are a few conflicts with #8334. I will rebase this patch.",
    "created_at": "2010-09-27T09:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88872",
    "user": "jdemeyer"
}
```

There are a few conflicts with #8334. I will rebase this patch.



---

archive/issue_comments_088873.json:
```json
{
    "body": "Attachment\n\nApply on top of #7883, #9898, #9753, #9764, #8334 and trac_9359.patch",
    "created_at": "2010-09-27T21:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88873",
    "user": "jdemeyer"
}
```

Attachment

Apply on top of #7883, #9898, #9753, #9764, #8334 and trac_9359.patch



---

archive/issue_comments_088874.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-27T21:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88874",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088875.json:
```json
{
    "body": "With the attached patch, `make ptestlong` succeeds on 32-bit and 64-bit systems.",
    "created_at": "2010-09-27T21:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88875",
    "user": "jdemeyer"
}
```

With the attached patch, `make ptestlong` succeeds on 32-bit and 64-bit systems.



---

archive/issue_comments_088876.json:
```json
{
    "body": "David, can you review my additions?",
    "created_at": "2010-09-27T21:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88876",
    "user": "jdemeyer"
}
```

David, can you review my additions?



---

archive/issue_comments_088877.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T07:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88877",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088878.json:
```json
{
    "body": "Looks fine -- thanks for cleaning that up.",
    "created_at": "2010-09-28T07:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88878",
    "user": "davidloeffler"
}
```

Looks fine -- thanks for cleaning that up.



---

archive/issue_comments_088879.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T09:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88879",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_088880.json:
```json
{
    "body": "Could someone update the commit string of the patch so its first line is a < 80 (or so) character summary of the changes that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.",
    "created_at": "2010-09-28T09:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88880",
    "user": "mpatel"
}
```

Could someone update the commit string of the patch so its first line is a < 80 (or so) character summary of the changes that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.



---

archive/issue_comments_088881.json:
```json
{
    "body": "Attachment\n\nQfolded patch with better commit string. Apply only this patch.",
    "created_at": "2010-09-28T10:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88881",
    "user": "davidloeffler"
}
```

Attachment

Qfolded patch with better commit string. Apply only this patch.



---

archive/issue_comments_088882.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T10:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88882",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_088883.json:
```json
{
    "body": "Done. I also qfolded into one patch.",
    "created_at": "2010-09-28T10:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88883",
    "user": "davidloeffler"
}
```

Done. I also qfolded into one patch.



---

archive/issue_comments_088884.json:
```json
{
    "body": "Thanks, David.  I get some docbuild warnings\n\n```\n/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:71: WARNING: duplicate citation C, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/small_primes_of_degree_one.rst\n/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:75: WARNING: duplicate citation M, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/crypto/lfsr.rst\n/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:82: WARNING: duplicate citation V, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/matrix/matrix2.rst\n```\n\nwith the current [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2) \"applied\" to 4.6.alpha1.\n\nCould you or Jeroen add a docfix patch?",
    "created_at": "2010-09-28T10:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88884",
    "user": "mpatel"
}
```

Thanks, David.  I get some docbuild warnings

```
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:71: WARNING: duplicate citation C, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/small_primes_of_degree_one.rst
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:75: WARNING: duplicate citation M, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/crypto/lfsr.rst
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/rings/number_field/totallyreal.rst:82: WARNING: duplicate citation V, other instance in /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/doc/en/reference/sage/matrix/matrix2.rst
```

with the current [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2) "applied" to 4.6.alpha1.

Could you or Jeroen add a docfix patch?



---

archive/issue_comments_088885.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T10:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88885",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_088886.json:
```json
{
    "body": "fix duplicate citation",
    "created_at": "2010-09-28T11:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88886",
    "user": "davidloeffler"
}
```

fix duplicate citation



---

archive/issue_comments_088887.json:
```json
{
    "body": "Attachment\n\nDocfix patch as requested. We should really have a single table of citations for the whole reference manual -- one of the conflicts here was with another file citing 'the same textbook' -- but this'll do for now.",
    "created_at": "2010-09-28T11:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88887",
    "user": "davidloeffler"
}
```

Attachment

Docfix patch as requested. We should really have a single table of citations for the whole reference manual -- one of the conflicts here was with another file citing 'the same textbook' -- but this'll do for now.



---

archive/issue_comments_088888.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T11:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88888",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_088889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T03:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88889",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_088890.json:
```json
{
    "body": "Replying to [comment:26 davidloeffler]:\n> Docfix patch as requested. We should really have a single table of citations for the whole reference manual -- one of the conflicts here was with another file citing 'the same textbook' -- but this'll do for now.\n\n[This sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/dba6129183b3b6eb/b41ce82a5ee589fe?#b41ce82a5ee589fe) seems related.",
    "created_at": "2010-09-29T03:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9359#issuecomment-88890",
    "user": "mpatel"
}
```

Replying to [comment:26 davidloeffler]:
> Docfix patch as requested. We should really have a single table of citations for the whole reference manual -- one of the conflicts here was with another file citing 'the same textbook' -- but this'll do for now.

[This sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/dba6129183b3b6eb/b41ce82a5ee589fe?#b41ce82a5ee589fe) seems related.
