# Issue 8001: Stronger category tests

archive/issues_008001.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: TestSuite, Category\n\n- More category tests: _test_category, _test_elements\n- Improvements to TestSuite\n  - Partial support for nested test suites\n  - Support for basic TestSuite(x) for x any Python object\n- Added TestSuite call for Spec and ref to #7946\n- Corresponding doctest updates\n\nDepends on #7921\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8001\n\n",
    "created_at": "2010-01-19T18:20:02Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Stronger category tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8001",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: TestSuite, Category

- More category tests: _test_category, _test_elements
- Improvements to TestSuite
  - Partial support for nested test suites
  - Support for basic TestSuite(x) for x any Python object
- Added TestSuite call for Spec and ref to #7946
- Corresponding doctest updates

Depends on #7921


Issue created by migration from https://trac.sagemath.org/ticket/8001





---

archive/issue_comments_069798.json:
```json
{
    "body": "Attachment [trac_8001-categories_testsuite-nt.patch](tarball://root/attachments/some-uuid/ticket8001/trac_8001-categories_testsuite-nt.patch) by @nthiery created at 2010-01-19 18:29:31",
    "created_at": "2010-01-19T18:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69798",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8001-categories_testsuite-nt.patch](tarball://root/attachments/some-uuid/ticket8001/trac_8001-categories_testsuite-nt.patch) by @nthiery created at 2010-01-19 18:29:31



---

archive/issue_comments_069799.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T18:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69799",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069800.json:
```json
{
    "body": "I briefly glanced at the patch when doing #7921, and what I saw looks good (though I didn't read it all thoroughly enough to call it a review).",
    "created_at": "2010-01-19T20:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69800",
    "user": "https://github.com/robertwb"
}
```

I briefly glanced at the patch when doing #7921, and what I saw looks good (though I didn't read it all thoroughly enough to call it a review).



---

archive/issue_comments_069801.json:
```json
{
    "body": "I'm uploading a small trivial review patch. Here are the comment:\n- Add a missing \"`\";\n- Improve the layout of an enumeration;\n- replace `ZZ._tester` with `QQ._tester` to show that the gadget is automatically attached (Noting to do with the previous call on `ZZ`.\n\nOtherwise the patch is ready to go. \n\nNicolas: You can add positive review once you had a look on my review patch.",
    "created_at": "2010-01-23T10:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69801",
    "user": "https://github.com/hivert"
}
```

I'm uploading a small trivial review patch. Here are the comment:
- Add a missing "`";
- Improve the layout of an enumeration;
- replace `ZZ._tester` with `QQ._tester` to show that the gadget is automatically attached (Noting to do with the previous call on `ZZ`.

Otherwise the patch is ready to go. 

Nicolas: You can add positive review once you had a look on my review patch.



---

archive/issue_comments_069802.json:
```json
{
    "body": "Attachment [trac_8001-categories_testsuite-review-fh.patch](tarball://root/attachments/some-uuid/ticket8001/trac_8001-categories_testsuite-review-fh.patch) by @hivert created at 2010-01-23 11:00:09",
    "created_at": "2010-01-23T11:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69802",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8001-categories_testsuite-review-fh.patch](tarball://root/attachments/some-uuid/ticket8001/trac_8001-categories_testsuite-review-fh.patch) by @hivert created at 2010-01-23 11:00:09



---

archive/issue_comments_069803.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T14:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69803",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069804.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> I'm uploading a small trivial review patch. Here are the comment:\n>  - Add a missing \"`\";\n>  - Improve the layout of an enumeration;\n>  - replace `ZZ._tester` with `QQ._tester` to show that the gadget is automatically attached (Noting to do with the previous call on `ZZ`.\n> \n> Otherwise the patch is ready to go. \n\nThanks for the review!\n\n> Nicolas: You can add positive review once you had a look on my review patch.  \n\nDone!",
    "created_at": "2010-01-23T14:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69804",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 hivert]:
> I'm uploading a small trivial review patch. Here are the comment:
>  - Add a missing "`";
>  - Improve the layout of an enumeration;
>  - replace `ZZ._tester` with `QQ._tester` to show that the gadget is automatically attached (Noting to do with the previous call on `ZZ`.
> 
> Otherwise the patch is ready to go. 

Thanks for the review!

> Nicolas: You can add positive review once you had a look on my review patch.  

Done!



---

archive/issue_events_019174.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-23T14:58:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8001#event-19174"
}
```



---

archive/issue_comments_069805.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T14:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_069806.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8001-categories_testsuite-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8001/trac_8001-categories_testsuite-nt.patch)\n2. [trac_8001-categories_testsuite-review-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8001/trac_8001-categories_testsuite-review-fh.patch)",
    "created_at": "2010-01-23T14:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8001#issuecomment-69806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_8001-categories_testsuite-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8001/trac_8001-categories_testsuite-nt.patch)
2. [trac_8001-categories_testsuite-review-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8001/trac_8001-categories_testsuite-review-fh.patch)
