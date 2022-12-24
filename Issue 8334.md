# Issue 8334: Improvements to residue fields

archive/issues_008334.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  was\n\nMoves residue fields to the coercion model, makes the reduction and lifting maps morphisms, prepares the way for 7885 (Tate's algorithm for function fields).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8334\n\n",
    "created_at": "2010-02-23T15:16:53Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "Improvements to residue fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8334",
    "user": "roed"
}
```
Assignee: AlexGhitza

CC:  was

Moves residue fields to the coercion model, makes the reduction and lifting maps morphisms, prepares the way for 7885 (Tate's algorithm for function fields).

Issue created by migration from https://trac.sagemath.org/ticket/8334





---

archive/issue_comments_074231.json:
```json
{
    "body": "Attachment [7585_9_1_frac_and_coerce_updates.patch](tarball://root/attachments/some-uuid/ticket8334/7585_9_1_frac_and_coerce_updates.patch) by roed created at 2010-02-23 15:22:47\n\nApply after other patch",
    "created_at": "2010-02-23T15:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74231",
    "user": "roed"
}
```

Attachment [7585_9_1_frac_and_coerce_updates.patch](tarball://root/attachments/some-uuid/ticket8334/7585_9_1_frac_and_coerce_updates.patch) by roed created at 2010-02-23 15:22:47

Apply after other patch



---

archive/issue_comments_074232.json:
```json
{
    "body": "Attachment [8334_residue_fields.patch](tarball://root/attachments/some-uuid/ticket8334/8334_residue_fields.patch) by roed created at 2010-02-23 15:26:47\n\nFixes various bugs and doctest failures introduced in earlier patches.",
    "created_at": "2010-02-23T15:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74232",
    "user": "roed"
}
```

Attachment [8334_residue_fields.patch](tarball://root/attachments/some-uuid/ticket8334/8334_residue_fields.patch) by roed created at 2010-02-23 15:26:47

Fixes various bugs and doctest failures introduced in earlier patches.



---

archive/issue_comments_074233.json:
```json
{
    "body": "Attachment [7585_12_1_fixes.patch](tarball://root/attachments/some-uuid/ticket8334/7585_12_1_fixes.patch) by roed created at 2010-02-23 17:37:23\n\nPart of a series:\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335\n```\n\nI tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.",
    "created_at": "2010-02-23T17:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74233",
    "user": "roed"
}
```

Attachment [7585_12_1_fixes.patch](tarball://root/attachments/some-uuid/ticket8334/7585_12_1_fixes.patch) by roed created at 2010-02-23 17:37:23

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.



---

archive/issue_comments_074234.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T17:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74234",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074235.json:
```json
{
    "body": "FWIW, testing with this and all the prior patches in the series applied under 4.3.4.rc0 brings up exactly 1 doctest failure, in line 321 of sage/rings/finite_rings/finite_field_givaro.py:\n\n```\nFile \"/home/masiao/sage-4.3.4.rc0/devel/sage-working/sage/rings/finite_rings/finite_field_\ngivaro.py\", line 321:\n    sage: F81(F9.gen())\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: unable to coerce from a finite field other than the prime subfield\nGot:\n    Traceback (most recent call last):\n      File \"/home/masiao/sage-4.3.4.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_te\nst\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/masiao/sage-4.3.4.rc0/local/bin/sagedoctest.py\", line 38, in run_one_exa\nmple\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/masiao/sage-4.3.4.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_ex\nample\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[49]>\", line 1, in <module>\n        F81(F9.gen())###line 321:\n    sage: F81(F9.gen())\n      File \"parent.pyx\", line 826, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6232)\n      File \"parent.pyx\", line 1876, in sage.structure.parent.Parent.convert_map_from (sage/structure/parent.c:12773)\n      File \"parent.pyx\", line 1883, in sage.structure.parent.Parent.discover_convert_map_from (sage/structure/parent.c:12925)\n      File \"parent.pyx\", line 1740, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:11546)\n      File \"parent.pyx\", line 1791, in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:11946)\n      File \"parent_old.pyx\", line 503, in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:5943)\n      File \"/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/rings/finite_rings/finite_field_givaro.py\", line 350, in _coerce_map_from_\n        raise NotImplementedError\n    NotImplementedError\n```\n",
    "created_at": "2010-03-18T17:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74235",
    "user": "davidloeffler"
}
```

FWIW, testing with this and all the prior patches in the series applied under 4.3.4.rc0 brings up exactly 1 doctest failure, in line 321 of sage/rings/finite_rings/finite_field_givaro.py:

```
File "/home/masiao/sage-4.3.4.rc0/devel/sage-working/sage/rings/finite_rings/finite_field_
givaro.py", line 321:
    sage: F81(F9.gen())
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unable to coerce from a finite field other than the prime subfield
Got:
    Traceback (most recent call last):
      File "/home/masiao/sage-4.3.4.rc0/local/bin/ncadoctest.py", line 1231, in run_one_te
st
        self.run_one_example(test, example, filename, compileflags)
      File "/home/masiao/sage-4.3.4.rc0/local/bin/sagedoctest.py", line 38, in run_one_exa
mple
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/masiao/sage-4.3.4.rc0/local/bin/ncadoctest.py", line 1172, in run_one_ex
ample
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[49]>", line 1, in <module>
        F81(F9.gen())###line 321:
    sage: F81(F9.gen())
      File "parent.pyx", line 826, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6232)
      File "parent.pyx", line 1876, in sage.structure.parent.Parent.convert_map_from (sage/structure/parent.c:12773)
      File "parent.pyx", line 1883, in sage.structure.parent.Parent.discover_convert_map_from (sage/structure/parent.c:12925)
      File "parent.pyx", line 1740, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:11546)
      File "parent.pyx", line 1791, in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:11946)
      File "parent_old.pyx", line 503, in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:5943)
      File "/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/rings/finite_rings/finite_field_givaro.py", line 350, in _coerce_map_from_
        raise NotImplementedError
    NotImplementedError
```




---

archive/issue_comments_074236.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-18T17:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74236",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074237.json:
```json
{
    "body": "Attachment [8334_residue_fields-rebased_for_8446.patch](tarball://root/attachments/some-uuid/ticket8334/8334_residue_fields-rebased_for_8446.patch) by davidloeffler created at 2010-04-20 10:15:45\n\napply instead of 8334_residue_fields.patch -- rebased to apply after #8446",
    "created_at": "2010-04-20T10:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74237",
    "user": "davidloeffler"
}
```

Attachment [8334_residue_fields-rebased_for_8446.patch](tarball://root/attachments/some-uuid/ticket8334/8334_residue_fields-rebased_for_8446.patch) by davidloeffler created at 2010-04-20 10:15:45

apply instead of 8334_residue_fields.patch -- rebased to apply after #8446



---

archive/issue_comments_074238.json:
```json
{
    "body": "The patch conflicts with #8446, so I've uploaded a rebased version.",
    "created_at": "2010-04-20T10:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74238",
    "user": "davidloeffler"
}
```

The patch conflicts with #8446, so I've uploaded a rebased version.



---

archive/issue_comments_074239.json:
```json
{
    "body": "Apply:\n\n\n```\n7585_9_1_frac_and_coerce_updates.patch\n8334_residue_fields-rebased_for_8446.patch\n7585_12_1_fixes.patch.2\n```\n",
    "created_at": "2010-09-19T13:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74239",
    "user": "roed"
}
```

Apply:


```
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
7585_12_1_fixes.patch.2
```




---

archive/issue_comments_074240.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-19T13:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74240",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074241.json:
```json
{
    "body": "It doesn't work. On vanilla 4.6.alpha1, if I apply \n\n```\n7883_ideals.patch\n7883_fixes.patch\n8333_parent_init.patch\n8333_finite_fields_to_new_coercion.2.patch\n7585_9_1_frac_and_coerce_updates.patch\n8334_residue_fields-rebased_for_8446.patch\n```\n\nthen the first five apply (with minor fuzz) but the last one is completely knackered, with 23 out of 27 hunks failing. I think the problem is caused by #9343/#9400 which both make extensive changes to residue fields.\n\nJust a general observation: you've managed to virtually guarantee that these patches are impossible to review, because they're all linked together in such a way that they fail doctests unless you apply the whole series. So the effect is a huge patch bomb, which is unappealing to review; hence it sits around for ages, and inevitably bitrots. Please, please, please back-port the doctest fixes etc, so each ticket in the series passes doctests on its own. Otherwise this will really never get merged and all of your hard work writing this excellent code (not to mention the work of those who have attempted to review it) will be for nothing.",
    "created_at": "2010-09-23T14:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74241",
    "user": "davidloeffler"
}
```

It doesn't work. On vanilla 4.6.alpha1, if I apply 

```
7883_ideals.patch
7883_fixes.patch
8333_parent_init.patch
8333_finite_fields_to_new_coercion.2.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
```

then the first five apply (with minor fuzz) but the last one is completely knackered, with 23 out of 27 hunks failing. I think the problem is caused by #9343/#9400 which both make extensive changes to residue fields.

Just a general observation: you've managed to virtually guarantee that these patches are impossible to review, because they're all linked together in such a way that they fail doctests unless you apply the whole series. So the effect is a huge patch bomb, which is unappealing to review; hence it sits around for ages, and inevitably bitrots. Please, please, please back-port the doctest fixes etc, so each ticket in the series passes doctests on its own. Otherwise this will really never get merged and all of your hard work writing this excellent code (not to mention the work of those who have attempted to review it) will be for nothing.



---

archive/issue_comments_074242.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T14:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74242",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074243.json:
```json
{
    "body": "Attachment [8334_residue_fields-rebased_for_9343.patch](tarball://root/attachments/some-uuid/ticket8334/8334_residue_fields-rebased_for_9343.patch) by roed created at 2010-09-23 16:35:17\n\nRebased against 4.6.alpha1",
    "created_at": "2010-09-23T16:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74243",
    "user": "roed"
}
```

Attachment [8334_residue_fields-rebased_for_9343.patch](tarball://root/attachments/some-uuid/ticket8334/8334_residue_fields-rebased_for_9343.patch) by roed created at 2010-09-23 16:35:17

Rebased against 4.6.alpha1



---

archive/issue_comments_074244.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-23T16:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74244",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074245.json:
```json
{
    "body": "I'm sorry that this has been so difficult to review.  I've tended to work in chunks: I just start ripping things apart and changing lots of stuff, and then I need to fix it all; by the time I've managed to make all the doctests pass it's turned into a patch-bomb.  I've tried to split things into logically consistent chunks, but it's really frustrating trying to backport fixes.  I also really shouldn't be working on Sage right now: I should be working on my thesis, which has nothing to do with this.\n\nI've tried to get these tickets working against 4.6.alpha1 (in particular, I think they should now).  If they don't get reviewed, I'll try your approach.  In the mean time, the sequence of patches should be \n\n\n```\n7883_ideals.patch\n7883_fixes.patch\n8333_parent_init.patch\n8333_finite_fields_to_new_coercion.2.patch\n7585_9_1_frac_and_coerce_updates.patch\n8334_residue_fields-rebased_for_9343.patch\n7585_12_1_fixes.2.patch\n```\n",
    "created_at": "2010-09-23T16:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74245",
    "user": "roed"
}
```

I'm sorry that this has been so difficult to review.  I've tended to work in chunks: I just start ripping things apart and changing lots of stuff, and then I need to fix it all; by the time I've managed to make all the doctests pass it's turned into a patch-bomb.  I've tried to split things into logically consistent chunks, but it's really frustrating trying to backport fixes.  I also really shouldn't be working on Sage right now: I should be working on my thesis, which has nothing to do with this.

I've tried to get these tickets working against 4.6.alpha1 (in particular, I think they should now).  If they don't get reviewed, I'll try your approach.  In the mean time, the sequence of patches should be 


```
7883_ideals.patch
7883_fixes.patch
8333_parent_init.patch
8333_finite_fields_to_new_coercion.2.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_9343.patch
7585_12_1_fixes.2.patch
```




---

archive/issue_comments_074246.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T16:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74246",
    "user": "roed"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074247.json:
```json
{
    "body": "gah.  Manual merge doesn't build.  Working on it...",
    "created_at": "2010-09-23T16:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74247",
    "user": "roed"
}
```

gah.  Manual merge doesn't build.  Working on it...



---

archive/issue_comments_074248.json:
```json
{
    "body": "Fixed merge error; apply against 4.6.alpha1",
    "created_at": "2010-09-23T16:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74248",
    "user": "roed"
}
```

Fixed merge error; apply against 4.6.alpha1



---

archive/issue_comments_074249.json:
```json
{
    "body": "Attachment [7585_12_1_fixes.2.patch](tarball://root/attachments/some-uuid/ticket8334/7585_12_1_fixes.2.patch) by roed created at 2010-09-23 16:57:35\n\nForgot to delete 4 lines.  I'm still building, but the build has progressed past `residue_field.pyx`.",
    "created_at": "2010-09-23T16:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74249",
    "user": "roed"
}
```

Attachment [7585_12_1_fixes.2.patch](tarball://root/attachments/some-uuid/ticket8334/7585_12_1_fixes.2.patch) by roed created at 2010-09-23 16:57:35

Forgot to delete 4 lines.  I'm still building, but the build has progressed past `residue_field.pyx`.



---

archive/issue_comments_074250.json:
```json
{
    "body": "I'm getting weird doctest failures, as if some of the changes in 7883_ideals.patch didn't get applied.  Then I switched to my main branch and now Pari segfaults upon sage starting up.\n\nI'm going to install a fresh copy of sage-4.6.alpha1, which will take a few hours, and try to figure out what's going on.",
    "created_at": "2010-09-23T17:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74250",
    "user": "roed"
}
```

I'm getting weird doctest failures, as if some of the changes in 7883_ideals.patch didn't get applied.  Then I switched to my main branch and now Pari segfaults upon sage starting up.

I'm going to install a fresh copy of sage-4.6.alpha1, which will take a few hours, and try to figure out what's going on.



---

archive/issue_comments_074251.json:
```json
{
    "body": "Would you mind basing your updated patch series on my folded patch at #7883, the one I gave a positive review to, rather than on your original patches (as you seem to have done judging by your comment 8)? Then we can treat the #7883 stuff as finished and fixed.\n\nDavid",
    "created_at": "2010-09-23T20:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74251",
    "user": "davidloeffler"
}
```

Would you mind basing your updated patch series on my folded patch at #7883, the one I gave a positive review to, rather than on your original patches (as you seem to have done judging by your comment 8)? Then we can treat the #7883 stuff as finished and fixed.

David



---

archive/issue_comments_074252.json:
```json
{
    "body": "sure",
    "created_at": "2010-09-23T22:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74252",
    "user": "roed"
}
```

sure



---

archive/issue_comments_074253.json:
```json
{
    "body": "Includes all patches in 8333 and 8334; based on 4.6.alpha1 with 7883",
    "created_at": "2010-09-24T14:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74253",
    "user": "roed"
}
```

Includes all patches in 8333 and 8334; based on 4.6.alpha1 with 7883



---

archive/issue_comments_074254.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T14:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74254",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074255.json:
```json
{
    "body": "Attachment [8333_8334_ALL.patch](tarball://root/attachments/some-uuid/ticket8334/8333_8334_ALL.patch) by roed created at 2010-09-24 14:30:08\n\nYou now only need to apply one patch.",
    "created_at": "2010-09-24T14:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74255",
    "user": "roed"
}
```

Attachment [8333_8334_ALL.patch](tarball://root/attachments/some-uuid/ticket8334/8333_8334_ALL.patch) by roed created at 2010-09-24 14:30:08

You now only need to apply one patch.



---

archive/issue_comments_074256.json:
```json
{
    "body": "All doctests pass for me, though I didn't run -long (it already takes a couple hours on my laptop)",
    "created_at": "2010-09-24T14:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74256",
    "user": "roed"
}
```

All doctests pass for me, though I didn't run -long (it already takes a couple hours on my laptop)



---

archive/issue_comments_074257.json:
```json
{
    "body": "Sadly this conflicts with the positively-reviewed patch series #9898/#9753/#9764.\n\nI will handle rebasing it past those. You can sit back and relax. Thanks for all your sterling efforts on this particularly frustrating job. I have access to a very fast computer (from Bill Hart's research grant, thanks Bill) which runs long tests in about 10 minutes :-)",
    "created_at": "2010-09-24T14:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74257",
    "user": "davidloeffler"
}
```

Sadly this conflicts with the positively-reviewed patch series #9898/#9753/#9764.

I will handle rebasing it past those. You can sit back and relax. Thanks for all your sterling efforts on this particularly frustrating job. I have access to a very fast computer (from Bill Hart's research grant, thanks Bill) which runs long tests in about 10 minutes :-)



---

archive/issue_comments_074258.json:
```json
{
    "body": "Thanks.  That's especially useful since I just broke my mercurial queues trying to switch back to a more finely grained set of patches than `8333_8334_ALL.patch`.  Oh well, I'll just tell Mercurial that there are no patches there and both it and sage will be happy.",
    "created_at": "2010-09-24T14:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74258",
    "user": "roed"
}
```

Thanks.  That's especially useful since I just broke my mercurial queues trying to switch back to a more finely grained set of patches than `8333_8334_ALL.patch`.  Oh well, I'll just tell Mercurial that there are no patches there and both it and sage will be happy.



---

archive/issue_comments_074259.json:
```json
{
    "body": "Attachment [8333_8334_ALL-rebased_for_9764.patch](tarball://root/attachments/some-uuid/ticket8334/8333_8334_ALL-rebased_for_9764.patch) by davidloeffler created at 2010-09-24 15:23:17\n\nApply only this patch -- see comment below.",
    "created_at": "2010-09-24T15:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74259",
    "user": "davidloeffler"
}
```

Attachment [8333_8334_ALL-rebased_for_9764.patch](tarball://root/attachments/some-uuid/ticket8334/8333_8334_ALL-rebased_for_9764.patch) by davidloeffler created at 2010-09-24 15:23:17

Apply only this patch -- see comment below.



---

archive/issue_comments_074260.json:
```json
{
    "body": "Right, so I have rebased roed's last patch and uploaded my rebased patch as `8333_8334_ALL-rebased_for_9764.patch`. This patch will apply cleanly to 4.6.alpha1 on top of the folded patch from #7883 and the series #9898/#9753/#9764.\n\nThis patch incorporates everything from #8333 as well, so this is the only patch that needs to be applied to close both #8333 and this ticket.",
    "created_at": "2010-09-24T15:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74260",
    "user": "davidloeffler"
}
```

Right, so I have rebased roed's last patch and uploaded my rebased patch as `8333_8334_ALL-rebased_for_9764.patch`. This patch will apply cleanly to 4.6.alpha1 on top of the folded patch from #7883 and the series #9898/#9753/#9764.

This patch incorporates everything from #8333 as well, so this is the only patch that needs to be applied to close both #8333 and this ticket.



---

archive/issue_comments_074261.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-24T15:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74261",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074262.json:
```json
{
    "body": "Yay!  Thank you for your work on these patches.",
    "created_at": "2010-09-24T15:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74262",
    "user": "roed"
}
```

Yay!  Thank you for your work on these patches.



---

archive/issue_comments_074263.json:
```json
{
    "body": "Incidentally, are you running a 32-bit or a 64-bit machine? I don't have access to any 32-bit boxes. If you have access to a 32-bit machine, it would be great if you could do the following:\n\n- Install #9898/#9753/#9764 and test everything in sage/rings.\n- Then install #7883 and the combined patch from this ticket, and do sage/rings again.\n- Then install #9359 and repeat.\n\nI'm a little nervous about silly doctest failures coming up from Pari's unpredictable choices of generators of ideals, and this would set my mind at rest a bit :-)",
    "created_at": "2010-09-24T15:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74263",
    "user": "davidloeffler"
}
```

Incidentally, are you running a 32-bit or a 64-bit machine? I don't have access to any 32-bit boxes. If you have access to a 32-bit machine, it would be great if you could do the following:

- Install #9898/#9753/#9764 and test everything in sage/rings.
- Then install #7883 and the combined patch from this ticket, and do sage/rings again.
- Then install #9359 and repeat.

I'm a little nervous about silly doctest failures coming up from Pari's unpredictable choices of generators of ideals, and this would set my mind at rest a bit :-)



---

archive/issue_comments_074264.json:
```json
{
    "body": "In fact, I can think of one hashing doctest which will fail on a 32-bit machine.  Unfortunately I'm running on 64-bit.",
    "created_at": "2010-09-24T15:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74264",
    "user": "roed"
}
```

In fact, I can think of one hashing doctest which will fail on a 32-bit machine.  Unfortunately I'm running on 64-bit.



---

archive/issue_comments_074265.json:
```json
{
    "body": "Replying to [comment:20 davidloeffler]:\n> - Install #9898/#9753/#9764 and test everything in sage/rings.\n> - Then install #7883 and the combined patch from this ticket, and do sage/rings again.\n> - Then install #9359 and repeat.\n> \n> I'm a little nervous about silly doctest failures coming up from Pari's unpredictable choices of generators of ideals, and this would set my mind at rest a bit :-)\n\nI will do this (and should have done it for my patches).",
    "created_at": "2010-09-25T09:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74265",
    "user": "jdemeyer"
}
```

Replying to [comment:20 davidloeffler]:
> - Install #9898/#9753/#9764 and test everything in sage/rings.
> - Then install #7883 and the combined patch from this ticket, and do sage/rings again.
> - Then install #9359 and repeat.
> 
> I'm a little nervous about silly doctest failures coming up from Pari's unpredictable choices of generators of ideals, and this would set my mind at rest a bit :-)

I will do this (and should have done it for my patches).



---

archive/issue_comments_074266.json:
```json
{
    "body": "I have testing the following chain of patches on a 32-bit PPC machine:\n\n```\ntrac_7883-ideals-folded.patch\n9898_pari_decl.patch\n9753.patch\n9764_ideal_repr_new.patch\n8333_8334_ALL-rebased_for_9764.patch\n```\n\n\nThe only failure was in `sage/schemes/generic/toric_divisor.py`, which is a known problem.",
    "created_at": "2010-09-26T10:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74266",
    "user": "jdemeyer"
}
```

I have testing the following chain of patches on a 32-bit PPC machine:

```
trac_7883-ideals-folded.patch
9898_pari_decl.patch
9753.patch
9764_ideal_repr_new.patch
8333_8334_ALL-rebased_for_9764.patch
```


The only failure was in `sage/schemes/generic/toric_divisor.py`, which is a known problem.



---

archive/issue_comments_074267.json:
```json
{
    "body": "Could someone please update the commit string of [attachment:8333_8334_ALL-rebased_for_9764.patch] so its first line is a < 80 (or so) character summary that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.",
    "created_at": "2010-09-28T09:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74267",
    "user": "mpatel"
}
```

Could someone please update the commit string of [attachment:8333_8334_ALL-rebased_for_9764.patch] so its first line is a < 80 (or so) character summary that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.



---

archive/issue_comments_074268.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T09:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74268",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074269.json:
```json
{
    "body": "Attachment [8333_8334_ALL-better_commit_string.patch](tarball://root/attachments/some-uuid/ticket8334/8333_8334_ALL-better_commit_string.patch) by davidloeffler created at 2010-09-28 10:18:43\n\nVersion with better commit string.",
    "created_at": "2010-09-28T10:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74269",
    "user": "davidloeffler"
}
```

Attachment [8333_8334_ALL-better_commit_string.patch](tarball://root/attachments/some-uuid/ticket8334/8333_8334_ALL-better_commit_string.patch) by davidloeffler created at 2010-09-28 10:18:43

Version with better commit string.



---

archive/issue_comments_074270.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T10:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74270",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_074271.json:
```json
{
    "body": "Done.",
    "created_at": "2010-09-28T10:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74271",
    "user": "davidloeffler"
}
```

Done.



---

archive/issue_comments_074272.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74272",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_074273.json:
```json
{
    "body": "This seems to have sorted #9409, which needs a reviewer to verify my check.",
    "created_at": "2010-10-03T16:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74273",
    "user": "cremona"
}
```

This seems to have sorted #9409, which needs a reviewer to verify my check.



---

archive/issue_comments_074274.json:
```json
{
    "body": "David, I'm not very satisfied with the change in `french_book/numbertheory.py` done by this patch, for two reasons:\n\n(1) the previous error message was better. (In the book we wanted to show that the isomorphism\n    between two instances of GF(3<sup>2</sup>) is not automatic in Sage.)\n\n(2) this is more serious. We have put this doctest in Sage so that the examples of our book (which\n    is now published) still work with future versions of Sage. By changing the error message you\n    did break the examples on http://sagebook.gforge.inria.fr/. Moreover you did not even contact\n    us to discuss this change.\n\nFor (1) is it possible to revert to the previous error message?\n\nFor (2) in case you want to change some file in the tests directory, please first inform the\ncorresponding author.\n\nPaul Zimmermann",
    "created_at": "2011-11-23T09:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74274",
    "user": "zimmerma"
}
```

David, I'm not very satisfied with the change in `french_book/numbertheory.py` done by this patch, for two reasons:

(1) the previous error message was better. (In the book we wanted to show that the isomorphism
    between two instances of GF(3<sup>2</sup>) is not automatic in Sage.)

(2) this is more serious. We have put this doctest in Sage so that the examples of our book (which
    is now published) still work with future versions of Sage. By changing the error message you
    did break the examples on http://sagebook.gforge.inria.fr/. Moreover you did not even contact
    us to discuss this change.

For (1) is it possible to revert to the previous error message?

For (2) in case you want to change some file in the tests directory, please first inform the
corresponding author.

Paul Zimmermann



---

archive/issue_comments_074275.json:
```json
{
    "body": "Paul: I'm sorry, I didn't mean to break anything -- I didn't know there was an official policy of not making changes to the tests directory. Can you point me to where this policy is explicitly written down?",
    "created_at": "2011-11-23T10:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74275",
    "user": "davidloeffler"
}
```

Paul: I'm sorry, I didn't mean to break anything -- I didn't know there was an official policy of not making changes to the tests directory. Can you point me to where this policy is explicitly written down?



---

archive/issue_comments_074276.json:
```json
{
    "body": "David (Loeffler), I didn't write to you, but to David Roe... You are just the reviewer.\nThis policy is explained in http://groups.google.com/group/sage-support/msg/3ea7ed2eeab0824a :\n\n```\n\nNote that you could also submit a patch to Sage with the code you're doctesting.\nI did that with all the tests from both of the books I published, and\nI encourage you and many others to do the same with the code from your\narticle.  The code would go in a file\n\n    devel/sage/sage/tests/\n\nlike the file devel/sage/sage/tests/book_stein_modform.py\n\nIn fact, I could imagine having dozens of files in that directory, and\nwhen doctests break there, we could notify the authors before\nreleasing the version of Sage that breaks their doctests for feedback\n-- then they could update their papers or Sage.\n```\n\n\nMy personal opinion is that \"we could notify\" should read \"we should notify\"...\n\nPaul",
    "created_at": "2011-11-23T10:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74276",
    "user": "zimmerma"
}
```

David (Loeffler), I didn't write to you, but to David Roe... You are just the reviewer.
This policy is explained in http://groups.google.com/group/sage-support/msg/3ea7ed2eeab0824a :

```

Note that you could also submit a patch to Sage with the code you're doctesting.
I did that with all the tests from both of the books I published, and
I encourage you and many others to do the same with the code from your
article.  The code would go in a file

    devel/sage/sage/tests/

like the file devel/sage/sage/tests/book_stein_modform.py

In fact, I could imagine having dozens of files in that directory, and
when doctests break there, we could notify the authors before
releasing the version of Sage that breaks their doctests for feedback
-- then they could update their papers or Sage.
```


My personal opinion is that "we could notify" should read "we should notify"...

Paul



---

archive/issue_comments_074277.json:
```json
{
    "body": "Sorry for the change to the tests folder.  When I split up a patchbomb into #8334 and #8335 (among others), I changed some errors to `NotImplementedError` for coercions that would soon work in #8335.  Unfortunately that ticket has stagnated.\n\nWhile I'm working on fixing #8335, I've made a new ticket (#12084) that restores the original `TypeError`.  It's ready for review.  Sorry for the trouble, and I'll be more careful with the `sage/tests` directory in the future.",
    "created_at": "2011-11-25T21:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74277",
    "user": "roed"
}
```

Sorry for the change to the tests folder.  When I split up a patchbomb into #8334 and #8335 (among others), I changed some errors to `NotImplementedError` for coercions that would soon work in #8335.  Unfortunately that ticket has stagnated.

While I'm working on fixing #8335, I've made a new ticket (#12084) that restores the original `TypeError`.  It's ready for review.  Sorry for the trouble, and I'll be more careful with the `sage/tests` directory in the future.



---

archive/issue_comments_074278.json:
```json
{
    "body": "What's with all the commented-out doctests added here? See #16946.",
    "created_at": "2014-09-08T20:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8334#issuecomment-74278",
    "user": "jdemeyer"
}
```

What's with all the commented-out doctests added here? See #16946.
