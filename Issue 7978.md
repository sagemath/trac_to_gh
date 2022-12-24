# Issue 7978: The file sage/combinat/affine.py contains lots of 'tab' characters

archive/issues_007978.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nThey should be replaced with spaces.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7978\n\n",
    "created_at": "2010-01-18T14:43:28Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "The file sage/combinat/affine.py contains lots of 'tab' characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7978",
    "user": "@jbandlow"
}
```
Assignee: sage-combinat

CC:  sage-combinat

They should be replaced with spaces.

Issue created by migration from https://trac.sagemath.org/ticket/7978





---

archive/issue_comments_069599.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-18T15:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69599",
    "user": "@jbandlow"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069600.json:
```json
{
    "body": "Attachment [trac_7978_fix_tabs_in_affine_py-jb.patch](tarball://root/attachments/some-uuid/ticket7978/trac_7978_fix_tabs_in_affine_py-jb.patch) by @jbandlow created at 2010-01-18 15:17:51\n\nOops.  This patch depends on some patches in the combinat stack.  (I suspect the 'crystal-cleanup' patches.)  The change is trivial, but I'll coordinate with the sage-combinat list before marking this ready for review.",
    "created_at": "2010-01-18T15:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69600",
    "user": "@jbandlow"
}
```

Attachment [trac_7978_fix_tabs_in_affine_py-jb.patch](tarball://root/attachments/some-uuid/ticket7978/trac_7978_fix_tabs_in_affine_py-jb.patch) by @jbandlow created at 2010-01-18 15:17:51

Oops.  This patch depends on some patches in the combinat stack.  (I suspect the 'crystal-cleanup' patches.)  The change is trivial, but I'll coordinate with the sage-combinat list before marking this ready for review.



---

archive/issue_comments_069601.json:
```json
{
    "body": "Attachment [trac_7978_crystal_cleanup-as.patch](tarball://root/attachments/some-uuid/ticket7978/trac_7978_crystal_cleanup-as.patch) by @anneschilling created at 2010-01-25 06:27:16",
    "created_at": "2010-01-25T06:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69601",
    "user": "@anneschilling"
}
```

Attachment [trac_7978_crystal_cleanup-as.patch](tarball://root/attachments/some-uuid/ticket7978/trac_7978_crystal_cleanup-as.patch) by @anneschilling created at 2010-01-25 06:27:16



---

archive/issue_comments_069602.json:
```json
{
    "body": "The patch trac_7978_crystal_cleanup-as.patch supersedes Jason's patch. It fixes the whitespace issues in combinat/crystals/affine.py and does a lot more improvements in crystals (see description).",
    "created_at": "2010-01-25T06:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69602",
    "user": "@anneschilling"
}
```

The patch trac_7978_crystal_cleanup-as.patch supersedes Jason's patch. It fixes the whitespace issues in combinat/crystals/affine.py and does a lot more improvements in crystals (see description).



---

archive/issue_comments_069603.json:
```json
{
    "body": "Changing keywords from \"\" to \"crystals\".",
    "created_at": "2010-01-25T06:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69603",
    "user": "@anneschilling"
}
```

Changing keywords from "" to "crystals".



---

archive/issue_comments_069604.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-25T06:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69604",
    "user": "@anneschilling"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069605.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-25T21:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69605",
    "user": "@nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_069606.json:
```json
{
    "body": "Updated patch updates one doctest.",
    "created_at": "2010-01-27T01:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69606",
    "user": "@nthiery"
}
```

Updated patch updates one doctest.



---

archive/issue_comments_069607.json:
```json
{
    "body": "Attachment [trac_7978_crystal_cleanup-as.2.patch](tarball://root/attachments/some-uuid/ticket7978/trac_7978_crystal_cleanup-as.2.patch) by @dwbump created at 2010-02-02 14:45:40\n\nI checked that the patch passes sage --testall, either with or without #8028.\n\nI checked that it does not break latex method for classical crystals or metapost method for fastcrystals. I think the latex changes are specific to\naffine crystals.\n\nThe patch does not seem to break anything, and fixes some problems. I recommend merging it.",
    "created_at": "2010-02-02T14:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69607",
    "user": "@dwbump"
}
```

Attachment [trac_7978_crystal_cleanup-as.2.patch](tarball://root/attachments/some-uuid/ticket7978/trac_7978_crystal_cleanup-as.2.patch) by @dwbump created at 2010-02-02 14:45:40

I checked that the patch passes sage --testall, either with or without #8028.

I checked that it does not break latex method for classical crystals or metapost method for fastcrystals. I think the latex changes are specific to
affine crystals.

The patch does not seem to break anything, and fixes some problems. I recommend merging it.



---

archive/issue_comments_069608.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-02T14:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69608",
    "user": "@dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069609.json:
```json
{
    "body": "I've added the ticket number in the refreshed patch I'm applying to 4.3.3.alpha0.",
    "created_at": "2010-02-10T14:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69609",
    "user": "@qed777"
}
```

I've added the ticket number in the refreshed patch I'm applying to 4.3.3.alpha0.



---

archive/issue_comments_069610.json:
```json
{
    "body": "I'm having trouble parsing mpatel's message. Does this mean the patch is to be merged in 4.3.3.alpha0?\n\nWhat \"refreshed patch\" does this message refer to?  The patch trac_7978_crystal_cleanup-as.2.patch\napplies cleanly to sage-4.3.2 and does not break anything in sage/combinat/crystals.",
    "created_at": "2010-02-11T13:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69610",
    "user": "@dwbump"
}
```

I'm having trouble parsing mpatel's message. Does this mean the patch is to be merged in 4.3.3.alpha0?

What "refreshed patch" does this message refer to?  The patch trac_7978_crystal_cleanup-as.2.patch
applies cleanly to sage-4.3.2 and does not break anything in sage/combinat/crystals.



---

archive/issue_comments_069611.json:
```json
{
    "body": "I'll merge this ticket into 4.3.3.alpha0.  I mean only that I've prepended the ticket number to the first line of the commit string of the patch I've added to my working tree for 4.3.3.alpha0.  I apologize for being so cryptic.",
    "created_at": "2010-02-11T13:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69611",
    "user": "@qed777"
}
```

I'll merge this ticket into 4.3.3.alpha0.  I mean only that I've prepended the ticket number to the first line of the commit string of the patch I've added to my working tree for 4.3.3.alpha0.  I apologize for being so cryptic.



---

archive/issue_comments_069612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7978#issuecomment-69612",
    "user": "@qed777"
}
```

Resolution: fixed
