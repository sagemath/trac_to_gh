# Issue 7922: Pickling fails in WeightRing

archive/issues_007922.json:
```json
{
    "body": "Assignee: @dwbump\n\nCC:  @dwbump sage-combinat\n\nFirst issue caught by #7921:\n\n\n```\nsage: A2 = WeylCharacterRing(['A',2])\nsage: a2 = WeightRing(A2)\nsage: TestSuite(a2).run()\nFailure in _test_element_pickling:\nTraceback (most recent call last):\n...\nAssertionError: 2*a2(0,0,0) != 2*a2(0,0,0)\n```\n\n\nIndeed:\n\n```\nsage: x = a2.an_element()\nsage: x == loads(dumps(x))\nFalse\n```\n\n\nI assume that this is an issue in equality test. This should be fixed for free when WeighRing's will use CombinatorialFreeModules\nand categories.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7922\n\n",
    "created_at": "2010-01-13T16:14:55Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Pickling fails in WeightRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7922",
    "user": "@nthiery"
}
```
Assignee: @dwbump

CC:  @dwbump sage-combinat

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

Issue created by migration from https://trac.sagemath.org/ticket/7922





---

archive/issue_comments_068934.json:
```json
{
    "body": "Regarding speed, testing a large number of branching rules show that the patch is a substantial speedup over the old code with a caveat: the old code has an option cache=true for WeylCharacterRings. If this option (which is not the default) is selected for every WeylCharacterRing, then the old code is faster. Typical times:\n\n|        |          |\n|--------|----------|\n|Old Code|48 seconds|\n|New Code|25 seconds|\n|Old Code, cache=true|18 seconds|\nSince I made the method `_irr_weights` a cached method, the caching done in the new code is approximately equivalent to the caching in the old code, so at the moment I don't see any way to improve the situation.",
    "created_at": "2010-09-05T13:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68934",
    "user": "@dwbump"
}
```

Regarding speed, testing a large number of branching rules show that the patch is a substantial speedup over the old code with a caveat: the old code has an option cache=true for WeylCharacterRings. If this option (which is not the default) is selected for every WeylCharacterRing, then the old code is faster. Typical times:

|        |          |
|--------|----------|
|Old Code|48 seconds|
|New Code|25 seconds|
|Old Code, cache=true|18 seconds|
Since I made the method `_irr_weights` a cached method, the caching done in the new code is approximately equivalent to the caching in the old code, so at the moment I don't see any way to improve the situation.



---

archive/issue_comments_068935.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-05T13:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68935",
    "user": "@dwbump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068936.json:
```json
{
    "body": "Revised and reposted the patch in view of Nicolas' comment to use _from_dict(coerce=True).",
    "created_at": "2010-09-06T17:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68936",
    "user": "@dwbump"
}
```

Revised and reposted the patch in view of Nicolas' comment to use _from_dict(coerce=True).



---

archive/issue_comments_068937.json:
```json
{
    "body": "Converts WeylCharacterRings and WeightRings to use category framework",
    "created_at": "2010-09-11T15:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68937",
    "user": "@dwbump"
}
```

Converts WeylCharacterRings and WeightRings to use category framework



---

archive/issue_comments_068938.json:
```json
{
    "body": "Attachment [trac_7922.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922.patch) by @dwbump created at 2010-09-11 15:34:35\n\nI uploaded a revised version of the patch. The only change is in classical_crystals.py, where the revision of WeylCharacterRings necessitated a revision.",
    "created_at": "2010-09-11T15:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68938",
    "user": "@dwbump"
}
```

Attachment [trac_7922.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922.patch) by @dwbump created at 2010-09-11 15:34:35

I uploaded a revised version of the patch. The only change is in classical_crystals.py, where the revision of WeylCharacterRings necessitated a revision.



---

archive/issue_comments_068939.json:
```json
{
    "body": "Requires rebuilding the pickle jar.",
    "created_at": "2010-10-29T00:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68939",
    "user": "@dwbump"
}
```

Requires rebuilding the pickle jar.



---

archive/issue_comments_068940.json:
```json
{
    "body": "Attachment [trac_7922-rebased-4.6.1](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.6.1) by @dwbump created at 2010-11-15 19:26:27\n\n#7922: WeylCharacters inherit from CombinatorialFreemodule (substantial speedup)",
    "created_at": "2010-11-15T19:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68940",
    "user": "@dwbump"
}
```

Attachment [trac_7922-rebased-4.6.1](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.6.1) by @dwbump created at 2010-11-15 19:26:27

#7922: WeylCharacters inherit from CombinatorialFreemodule (substantial speedup)



---

archive/issue_comments_068941.json:
```json
{
    "body": "Since #9838 was merged in sage-4.6.1.alpha1, this patch needed rebasing.\n\nI therefore posted trac_7922-rebased-4.6.1.",
    "created_at": "2010-11-15T19:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68941",
    "user": "@dwbump"
}
```

Since #9838 was merged in sage-4.6.1.alpha1, this patch needed rebasing.

I therefore posted trac_7922-rebased-4.6.1.



---

archive/issue_comments_068942.json:
```json
{
    "body": "7922: thematic tutorial revision",
    "created_at": "2011-02-08T19:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68942",
    "user": "@dwbump"
}
```

7922: thematic tutorial revision



---

archive/issue_comments_068943.json:
```json
{
    "body": "Attachment [trac_7922-doc.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-doc.patch) by @dwbump created at 2011-02-08 19:30:18\n\nThis patch slightly conflicts with #8442 which was merged. So I'm posting a second patch trac_7922-doc.patch which revises the thematic tutorial.",
    "created_at": "2011-02-08T19:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68943",
    "user": "@dwbump"
}
```

Attachment [trac_7922-doc.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-doc.patch) by @dwbump created at 2011-02-08 19:30:18

This patch slightly conflicts with #8442 which was merged. So I'm posting a second patch trac_7922-doc.patch which revises the thematic tutorial.



---

archive/issue_comments_068944.json:
```json
{
    "body": "Attachment [trac_7922-rebased-4.7.alpha1.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.7.alpha1.patch) by @dwbump created at 2011-03-18 12:27:29\n\n#7922: Revision of Weyl Character Rings",
    "created_at": "2011-03-18T12:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68944",
    "user": "@dwbump"
}
```

Attachment [trac_7922-rebased-4.7.alpha1.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.7.alpha1.patch) by @dwbump created at 2011-03-18 12:27:29

#7922: Revision of Weyl Character Rings



---

archive/issue_comments_068945.json:
```json
{
    "body": "I have posted trac_7922-rebased-4.7.alpha1.patch, which\naddresses many of the comments in the reviewer patch:\n\nhttp://combinat.sagemath.org/patches/file/tip/trac_7922-review-nt.patch\n\nThose changes that are not addressed are discussed here:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/277e146862632d72",
    "created_at": "2011-03-18T12:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68945",
    "user": "@dwbump"
}
```

I have posted trac_7922-rebased-4.7.alpha1.patch, which
addresses many of the comments in the reviewer patch:

http://combinat.sagemath.org/patches/file/tip/trac_7922-review-nt.patch

Those changes that are not addressed are discussed here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/277e146862632d72



---

archive/issue_comments_068946.json:
```json
{
    "body": "#7922: revised pickle jar",
    "created_at": "2011-03-18T21:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68946",
    "user": "@dwbump"
}
```

#7922: revised pickle jar



---

archive/issue_comments_068947.json:
```json
{
    "body": "Attachment [pickle_jar.tar.bz2](tarball://root/attachments/some-uuid/ticket7922/pickle_jar.tar.bz2) by @dwbump created at 2011-03-18 21:33:59",
    "created_at": "2011-03-18T21:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68947",
    "user": "@dwbump"
}
```

Attachment [pickle_jar.tar.bz2](tarball://root/attachments/some-uuid/ticket7922/pickle_jar.tar.bz2) by @dwbump created at 2011-03-18 21:33:59



---

archive/issue_comments_068948.json:
```json
{
    "body": "Attachment [pickle-notes](tarball://root/attachments/some-uuid/ticket7922/pickle-notes) by @dwbump created at 2011-03-18 21:36:23\n\n#7922: explanation of how the pickle jar is remade",
    "created_at": "2011-03-18T21:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68948",
    "user": "@dwbump"
}
```

Attachment [pickle-notes](tarball://root/attachments/some-uuid/ticket7922/pickle-notes) by @dwbump created at 2011-03-18 21:36:23

#7922: explanation of how the pickle jar is remade



---

archive/issue_comments_068949.json:
```json
{
    "body": "See [attachment: pickle-notes] for an explanation of how the pickle jar was remade.",
    "created_at": "2011-03-18T21:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68949",
    "user": "@dwbump"
}
```

See [attachment: pickle-notes] for an explanation of how the pickle jar was remade.



---

archive/issue_comments_068950.json:
```json
{
    "body": "The revised patch [attachment:trac_7922-rebased-4.7.alpha2] includes the revised coercion mechanism and other changes proposed by Nicolas.\n\nIn view of this message:\n\nhttp://trac.sagemath.org/sage_trac/ticket/10354#comment:11\n\nI posted a tarball containing only the new pickles, and a list of obsolete pickles to be discarded.",
    "created_at": "2011-03-22T20:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68950",
    "user": "@dwbump"
}
```

The revised patch [attachment:trac_7922-rebased-4.7.alpha2] includes the revised coercion mechanism and other changes proposed by Nicolas.

In view of this message:

http://trac.sagemath.org/sage_trac/ticket/10354#comment:11

I posted a tarball containing only the new pickles, and a list of obsolete pickles to be discarded.



---

archive/issue_comments_068951.json:
```json
{
    "body": "#7922: revision of Weyl Character Rings",
    "created_at": "2011-03-24T18:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68951",
    "user": "@dwbump"
}
```

#7922: revision of Weyl Character Rings



---

archive/issue_comments_068952.json:
```json
{
    "body": "Attachment [trac_7922-rebased-4.7.alpha2.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.7.alpha2.patch) by @dwbump created at 2011-03-25 13:09:59\n\n#7922: replacement pickles",
    "created_at": "2011-03-25T13:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68952",
    "user": "@dwbump"
}
```

Attachment [trac_7922-rebased-4.7.alpha2.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.7.alpha2.patch) by @dwbump created at 2011-03-25 13:09:59

#7922: replacement pickles



---

archive/issue_comments_068953.json:
```json
{
    "body": "Attachment [trac_7922-new_pickles.tar.gz](tarball://root/attachments/some-uuid/ticket7922/trac_7922-new_pickles.tar.gz) by @nthiery created at 2011-04-05 08:48:06\n\nHi Dan,\n\nI just did a final proofreading, fixed a couple typos, updated coerce_to_sl in the doctests of the thematic tutorials, and removed some trailing white space and tabs.\n\nFor me it is now all good to go. Please check my reviewer's patch on the sage-combinat patch server. If it's ok with you, you can fold/upload and set a positive review here on my behalf.\n\n[http://combinat.sagemath.org/patches/file/tip/trac_7922-final-review-nt.patch](http://combinat.sagemath.org/patches/file/tip/trac_7922-final-review-nt.patch)\n\nCheers,\n                       Nicolas",
    "created_at": "2011-04-05T08:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68953",
    "user": "@nthiery"
}
```

Attachment [trac_7922-new_pickles.tar.gz](tarball://root/attachments/some-uuid/ticket7922/trac_7922-new_pickles.tar.gz) by @nthiery created at 2011-04-05 08:48:06

Hi Dan,

I just did a final proofreading, fixed a couple typos, updated coerce_to_sl in the doctests of the thematic tutorials, and removed some trailing white space and tabs.

For me it is now all good to go. Please check my reviewer's patch on the sage-combinat patch server. If it's ok with you, you can fold/upload and set a positive review here on my behalf.

[http://combinat.sagemath.org/patches/file/tip/trac_7922-final-review-nt.patch](http://combinat.sagemath.org/patches/file/tip/trac_7922-final-review-nt.patch)

Cheers,
                       Nicolas



---

archive/issue_comments_068954.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2011-04-05T08:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68954",
    "user": "@nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_068955.json:
```json
{
    "body": "#7922: Categories for Weyl character rings and weight rings",
    "created_at": "2011-04-06T23:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68955",
    "user": "@dwbump"
}
```

#7922: Categories for Weyl character rings and weight rings



---

archive/issue_comments_068956.json:
```json
{
    "body": "Attachment [trac_7922-rebased-4.7.alpha3.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.7.alpha3.patch) by @nthiery created at 2011-04-07 14:29:48\n\nHi Dan,\n\nI just checked out your final changes on the Sage-Combinat queue (trac_7922_alpha3-changes.patch), and it looks all good. So the final rebased patch you just posted (and which includes the above) is good to go.\n\nPositive review!",
    "created_at": "2011-04-07T14:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68956",
    "user": "@nthiery"
}
```

Attachment [trac_7922-rebased-4.7.alpha3.patch](tarball://root/attachments/some-uuid/ticket7922/trac_7922-rebased-4.7.alpha3.patch) by @nthiery created at 2011-04-07 14:29:48

Hi Dan,

I just checked out your final changes on the Sage-Combinat queue (trac_7922_alpha3-changes.patch), and it looks all good. So the final rebased patch you just posted (and which includes the above) is good to go.

Positive review!



---

archive/issue_comments_068957.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-07T14:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68957",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-31T17:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68958",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_068959.json:
```json
{
    "body": "This needs a few small fixes:\n1. at various places `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the indentation is inconsistent.  It should be 4 spaces but in the newly added examples it is more or less random.\n2. in `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the test on line 250 takes a very long time but is not marked as such.\n\nPlease add an additional patch fixing these issues.",
    "created_at": "2011-06-22T20:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68959",
    "user": "@jdemeyer"
}
```

This needs a few small fixes:
1. at various places `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the indentation is inconsistent.  It should be 4 spaces but in the newly added examples it is more or less random.
2. in `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the test on line 250 takes a very long time but is not marked as such.

Please add an additional patch fixing these issues.



---

archive/issue_comments_068960.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-06-22T20:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68960",
    "user": "@jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_068961.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-06-22T20:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68961",
    "user": "@jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_068962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-03T12:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68962",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_068963.json:
```json
{
    "body": "Replying to [comment:18 jdemeyer]:\n> This needs a few small fixes:\n>  1. at various places `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the indentation is inconsistent.  It should be 4 spaces but in the newly added examples it is more or less random.\n>  1. in `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the test on line 250 takes a very long time but is not marked as such.\n> \n> Please add an additional patch fixing these issues.\n\nFixing the indentation is now #14678. The very long time is not necessary anymore, most likely thanks to the optimizations in #13391 (the example takes 0.22s on my machine).",
    "created_at": "2013-06-03T13:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7922#issuecomment-68963",
    "user": "@nthiery"
}
```

Replying to [comment:18 jdemeyer]:
> This needs a few small fixes:
>  1. at various places `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the indentation is inconsistent.  It should be 4 spaces but in the newly added examples it is more or less random.
>  1. in `doc/en/thematic_tutorials/lie/weyl_character_ring.rst`, the test on line 250 takes a very long time but is not marked as such.
> 
> Please add an additional patch fixing these issues.

Fixing the indentation is now #14678. The very long time is not necessary anymore, most likely thanks to the optimizations in #13391 (the example takes 0.22s on my machine).
