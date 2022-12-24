# Issue 7478: Remove "..." in the output of TestSuite.

archive/issues_007478.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat\n\nKeywords: TestSuite\n\nWhen testing something in verbose mode the typical output of sage is:\n\n```\n\u00a0 \u00a0sage: P = Sets().example(\"inherits\")\n\u00a0 \u00a0sage: TestSuite(P).run(verbose=True)\n\u00a0 \u00a0running ._test_an_element() ... done\n\u00a0 \u00a0running ._test_element_pickling() ... done\n\u00a0 \u00a0running ._test_not_implemented_methods() ... done\n\u00a0 \u00a0running ._test_pickling() ... done\n\u00a0 \u00a0running ._test_some_elements() ... done\n```\n\nAnd there is some risks that the \"...\" match something they should'nt I change them to \"..\"\n\nCheers,\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7478\n\n",
    "created_at": "2009-11-17T08:03:23Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Remove \"...\" in the output of TestSuite.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7478",
    "user": "hivert"
}
```
Assignee: tbd

CC:  sage-combinat

Keywords: TestSuite

When testing something in verbose mode the typical output of sage is:

```
   sage: P = Sets().example("inherits")
   sage: TestSuite(P).run(verbose=True)
   running ._test_an_element() ... done
   running ._test_element_pickling() ... done
   running ._test_not_implemented_methods() ... done
   running ._test_pickling() ... done
   running ._test_some_elements() ... done
```

And there is some risks that the "..." match something they should'nt I change them to ".."

Cheers,

Florent

Issue created by migration from https://trac.sagemath.org/ticket/7478





---

archive/issue_comments_063124.json:
```json
{
    "body": "Changing assignee from tbd to hivert.",
    "created_at": "2009-11-17T08:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63124",
    "user": "hivert"
}
```

Changing assignee from tbd to hivert.



---

archive/issue_comments_063125.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T15:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63125",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063126.json:
```json
{
    "body": "Changing component from misc to doctest.",
    "created_at": "2009-11-18T15:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63126",
    "user": "nthiery"
}
```

Changing component from misc to doctest.



---

archive/issue_comments_063127.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-18T15:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63127",
    "user": "nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_063128.json:
```json
{
    "body": "There is a spurious \"only\" to \"o..\" change in sets_cat.py.",
    "created_at": "2009-11-18T18:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63128",
    "user": "mhansen"
}
```

There is a spurious "only" to "o.." change in sets_cat.py.



---

archive/issue_comments_063129.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> There is a spurious \"only\" to \"o..\" change in sets_cat.py.\n\nGood spot :-)\n\nI had already found a couple, and thought I had done a systematic search.\n\nFixed in the newly uploaded patch.",
    "created_at": "2009-11-18T18:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63129",
    "user": "nthiery"
}
```

Replying to [comment:4 mhansen]:
> There is a spurious "only" to "o.." change in sets_cat.py.

Good spot :-)

I had already found a couple, and thought I had done a systematic search.

Fixed in the newly uploaded patch.



---

archive/issue_comments_063130.json:
```json
{
    "body": "Updated patch fix a doctest I had missed.",
    "created_at": "2009-11-18T20:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63130",
    "user": "nthiery"
}
```

Updated patch fix a doctest I had missed.



---

archive/issue_comments_063131.json:
```json
{
    "body": "There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review \n`trac_7478_testsuite_dots-fh-review.patch`\non the queue. Then either me or you fold, reupload and set positive review. \n\n...trying to ping you on irc for synchro.",
    "created_at": "2009-11-18T21:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63131",
    "user": "hivert"
}
```

There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review 
`trac_7478_testsuite_dots-fh-review.patch`
on the queue. Then either me or you fold, reupload and set positive review. 

...trying to ping you on irc for synchro.



---

archive/issue_comments_063132.json:
```json
{
    "body": "Attachment [trac_7478_testsuite_dots-fh.patch](tarball://root/attachments/some-uuid/ticket7478/trac_7478_testsuite_dots-fh.patch) by nthiery created at 2009-11-18 22:09:46\n\nReplying to [comment:7 hivert]:\n> There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review \n> `trac_7478_testsuite_dots-fh-review.patch`\n> on the queue. Then either me or you fold, reupload and set positive review. \n> \n> ...trying to ping you on irc for synchro.\n\nReview patch is good. Folded and uploaded. positive review.",
    "created_at": "2009-11-18T22:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63132",
    "user": "nthiery"
}
```

Attachment [trac_7478_testsuite_dots-fh.patch](tarball://root/attachments/some-uuid/ticket7478/trac_7478_testsuite_dots-fh.patch) by nthiery created at 2009-11-18 22:09:46

Replying to [comment:7 hivert]:
> There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review 
> `trac_7478_testsuite_dots-fh-review.patch`
> on the queue. Then either me or you fold, reupload and set positive review. 
> 
> ...trying to ping you on irc for synchro.

Review patch is good. Folded and uploaded. positive review.



---

archive/issue_comments_063133.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-18T22:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63133",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63134",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_063135.json:
```json
{
    "body": "I just \"discovered\" `sage.misc.sage_unittest`.  In case it's of wider use: At #7390 there's a `unittest` HTML report generator that may make it into SageNB.",
    "created_at": "2009-11-27T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63135",
    "user": "mpatel"
}
```

I just "discovered" `sage.misc.sage_unittest`.  In case it's of wider use: At #7390 there's a `unittest` HTML report generator that may make it into SageNB.
