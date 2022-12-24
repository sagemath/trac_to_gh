# Issue 7880: Category of sets with partial maps.

archive/issues_007880.json:
```json
{
    "body": "Assignee: nthiery\n\nIn support of #7585 and Tate's algorithm over function fields.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7880\n\n",
    "created_at": "2010-01-09T19:40:58Z",
    "labels": [
        "categories",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Category of sets with partial maps.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7880",
    "user": "robertwb"
}
```
Assignee: nthiery

In support of #7585 and Tate's algorithm over function fields.

Issue created by migration from https://trac.sagemath.org/ticket/7880





---

archive/issue_comments_068483.json:
```json
{
    "body": "Attachment [7585_4_sets_with_partial_maps.patch](tarball://root/attachments/some-uuid/ticket7880/7585_4_sets_with_partial_maps.patch) by robertwb created at 2010-01-09 19:41:21",
    "created_at": "2010-01-09T19:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68483",
    "user": "robertwb"
}
```

Attachment [7585_4_sets_with_partial_maps.patch](tarball://root/attachments/some-uuid/ticket7880/7585_4_sets_with_partial_maps.patch) by robertwb created at 2010-01-09 19:41:21



---

archive/issue_comments_068484.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T19:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68484",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068485.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-09T19:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68485",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068486.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-01-09T19:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68486",
    "user": "robertwb"
}
```

Looks good.



---

archive/issue_comments_068487.json:
```json
{
    "body": "I am not convinced about the name, which suggests at first that the objects are Sets with more structure, not less. I don't have a better suggestion though. If nobody comes up with something better (ObjectsWith???) in a day or two, just put back a positive review.",
    "created_at": "2010-01-09T21:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68487",
    "user": "nthiery"
}
```

I am not convinced about the name, which suggests at first that the objects are Sets with more structure, not less. I don't have a better suggestion though. If nobody comes up with something better (ObjectsWith???) in a day or two, just put back a positive review.



---

archive/issue_comments_068488.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-09T21:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68488",
    "user": "nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068489.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-01-09T21:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68489",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_068490.json:
```json
{
    "body": "This is needed for the series of patches starting at 8218.  I agree that the name is not optimal, but nobody's come up with a better one in 6 weeks...",
    "created_at": "2010-02-23T14:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68490",
    "user": "roed"
}
```

This is needed for the series of patches starting at 8218.  I agree that the name is not optimal, but nobody's come up with a better one in 6 weeks...



---

archive/issue_comments_068491.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-23T14:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68491",
    "user": "roed"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_068492.json:
```json
{
    "body": "Part of a series:\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335\n```\n\nI tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.",
    "created_at": "2010-02-23T17:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68492",
    "user": "roed"
}
```

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.



---

archive/issue_comments_068493.json:
```json
{
    "body": "Attachment [trac_7880-sets_with_partial_maps.patch](tarball://root/attachments/some-uuid/ticket7880/trac_7880-sets_with_partial_maps.patch) by davidloeffler created at 2010-03-17 21:41:32\n\nreplaces previous patch",
    "created_at": "2010-03-17T21:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68493",
    "user": "davidloeffler"
}
```

Attachment [trac_7880-sets_with_partial_maps.patch](tarball://root/attachments/some-uuid/ticket7880/trac_7880-sets_with_partial_maps.patch) by davidloeffler created at 2010-03-17 21:41:32

replaces previous patch



---

archive/issue_comments_068494.json:
```json
{
    "body": "Looks good to me. I've made some tiny doctest fixes, and uploaded a new version of the patch, still with roed's user stamp on it. This applies cleanly to 4.3.4.rc0, if you apply the patches in the following order:\n\n```\n$ sage -hg qseries\ntrac_8218_fixes_434alpha1.patch\ntrac_8332_givaro_python.patch\ntrac_8332_reviewer.patch\ntrac_7880-sets_with_partial_maps.patch\n```\n\n\n\non top of the patches at #8218 and #8332.",
    "created_at": "2010-03-17T21:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68494",
    "user": "davidloeffler"
}
```

Looks good to me. I've made some tiny doctest fixes, and uploaded a new version of the patch, still with roed's user stamp on it. This applies cleanly to 4.3.4.rc0, if you apply the patches in the following order:

```
$ sage -hg qseries
trac_8218_fixes_434alpha1.patch
trac_8332_givaro_python.patch
trac_8332_reviewer.patch
trac_7880-sets_with_partial_maps.patch
```



on top of the patches at #8218 and #8332.



---

archive/issue_comments_068495.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-17T21:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68495",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068496.json:
```json
{
    "body": "Oh, just one thing: are objects in SetsWithPartialMaps parents or not?",
    "created_at": "2010-03-20T15:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68496",
    "user": "nthiery"
}
```

Oh, just one thing: are objects in SetsWithPartialMaps parents or not?



---

archive/issue_comments_068497.json:
```json
{
    "body": "Merged \"trac_7880-sets_with_partial_maps.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68497",
    "user": "jhpalmieri"
}
```

Merged "trac_7880-sets_with_partial_maps.patch" in 4.4.alpha0



---

archive/issue_comments_068498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7880#issuecomment-68498",
    "user": "jhpalmieri"
}
```

Resolution: fixed
