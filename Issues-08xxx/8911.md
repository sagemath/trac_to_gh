# Issue 8911: Categorification of Crystals

archive/issues_008911.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: crystals,  categories\n\nThis patch let the crystal code use the category framework\n\nNew crystal categories:\n\n* Crystals\n* FiniteCrystals\n* HighestWeightCrystals\n* ClassicalCrystals\n\ntogether with a template in categories/example/crystals on how to\nimplement a new crystal.\n\nThe files\n\n* combinat/crystals/letters.py\n* combinat/crystals/tensor_product.py\n* combinat/crystals/spins.py\n* combinat/crystals/fast_crystals.py\n* combinat/crystals/highest_weight_crystals.py\n* combinat/crystals/direct_sum.py\n* combinat/crystals/affine.py\n* combinat/crystals/kirillov_reshetikhin.py\n\nhave been categorified. What was before in\n\n* combinat/crystals\n\nis now mostly in the various categories except for the BackTracker class and the documentation about crystals.\n\nThis patch breaks old crystal pickles. Well, those were actually\nsilently broken since #7978 four months ago, and no-one voted for\nagainst this on sage-combinat-devel.\n\nDepends on #8881. Requires updating Sage's pickle jar.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8911\n\n",
    "closed_at": "2010-06-09T02:42:18Z",
    "created_at": "2010-05-07T13:47:43Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Categorification of Crystals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8911",
    "user": "https://github.com/anneschilling"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: crystals,  categories

This patch let the crystal code use the category framework

New crystal categories:

* Crystals
* FiniteCrystals
* HighestWeightCrystals
* ClassicalCrystals

together with a template in categories/example/crystals on how to
implement a new crystal.

The files

* combinat/crystals/letters.py
* combinat/crystals/tensor_product.py
* combinat/crystals/spins.py
* combinat/crystals/fast_crystals.py
* combinat/crystals/highest_weight_crystals.py
* combinat/crystals/direct_sum.py
* combinat/crystals/affine.py
* combinat/crystals/kirillov_reshetikhin.py

have been categorified. What was before in

* combinat/crystals

is now mostly in the various categories except for the BackTracker class and the documentation about crystals.

This patch breaks old crystal pickles. Well, those were actually
silently broken since #7978 four months ago, and no-one voted for
against this on sage-combinat-devel.

Depends on #8881. Requires updating Sage's pickle jar.



Issue created by migration from https://trac.sagemath.org/ticket/8911





---

archive/issue_comments_081954.json:
```json
{
    "body": "Changing keywords from \"\" to \"crystals,  categories\".",
    "created_at": "2010-05-12T01:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81954",
    "user": "https://github.com/anneschilling"
}
```

Changing keywords from "" to "crystals,  categories".



---

archive/issue_comments_081955.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-12T01:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81955",
    "user": "https://github.com/anneschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081956.json:
```json
{
    "body": "Nicolas set a positive review on this provided that the old crystal pickle jars can be replaced by new ones (nobody seemed to complain that they needed the old ones, see\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7b20c1bef1598707/5a98f8b5f3443cfd?hl=en&lnk=gst&q=unpickling+of+crystals#5a98f8b5f3443cfd",
    "created_at": "2010-06-05T16:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81956",
    "user": "https://github.com/anneschilling"
}
```

Nicolas set a positive review on this provided that the old crystal pickle jars can be replaced by new ones (nobody seemed to complain that they needed the old ones, see

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7b20c1bef1598707/5a98f8b5f3443cfd?hl=en&lnk=gst&q=unpickling+of+crystals#5a98f8b5f3443cfd



---

archive/issue_comments_081957.json:
```json
{
    "body": "This is the pickle jar from sage-4.4.2 (and most likely sage-4.4.3), with the crystal pickles updated",
    "created_at": "2010-06-07T15:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81957",
    "user": "https://github.com/nthiery"
}
```

This is the pickle jar from sage-4.4.2 (and most likely sage-4.4.3), with the crystal pickles updated



---

archive/issue_comments_081958.json:
```json
{
    "body": "Attachment [pickle_jar.tar.bz2](tarball://root/attachments/some-uuid/ticket8911/pickle_jar.tar.bz2) by @nthiery created at 2010-06-07 16:00:26",
    "created_at": "2010-06-07T16:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81958",
    "user": "https://github.com/nthiery"
}
```

Attachment [pickle_jar.tar.bz2](tarball://root/attachments/some-uuid/ticket8911/pickle_jar.tar.bz2) by @nthiery created at 2010-06-07 16:00:26



---

archive/issue_comments_081959.json:
```json
{
    "body": "Attachment [trac_8911_categorification_crystals-as.patch](tarball://root/attachments/some-uuid/ticket8911/trac_8911_categorification_crystals-as.patch) by @anneschilling created at 2010-06-07 23:22:36",
    "created_at": "2010-06-07T23:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81959",
    "user": "https://github.com/anneschilling"
}
```

Attachment [trac_8911_categorification_crystals-as.patch](tarball://root/attachments/some-uuid/ticket8911/trac_8911_categorification_crystals-as.patch) by @anneschilling created at 2010-06-07 23:22:36



---

archive/issue_comments_081960.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-09T02:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81960",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_081961.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-09T02:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81961",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8911#issuecomment-81962",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021769.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-09T02:42:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8911#event-21769"
}
```



---

archive/issue_events_021770.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-09T04:34:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8911",
    "milestone": "sage-4.4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8911#event-21770"
}
```
