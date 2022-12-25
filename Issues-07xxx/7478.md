# Issue 7478: TestSuite improvements

archive/issues_007478.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: TestSuite\n\n- Changes \"... done\" to \". . . pass\" in the output of TestSuite().run(verbose = True) to avoid unintentional matches\n- Fix the doctests accordingly.\n- Adds skip option; use it in sage/combinat/sf/jack.py and orthotriang.py\n- In case of failure, execute the following tests after printing out a traceback, and write a summary at the end\n- Only use verbose=True in the doctests when useful (category examples)\n\n\nRationale for the ...: when testing something in verbose mode the typical output of sage is:\n\n```\n   sage: P = Sets().example(\"inherits\")\n   sage: TestSuite(P).run(verbose=True)\n   running ._test_an_element() ... done\n   running ._test_element_pickling() ... done\n   running ._test_not_implemented_methods() ... done\n   running ._test_pickling() ... done\n   running ._test_some_elements() ... done\n```\nAnd there is some risks that the \"...\" match something they should'nt I change them to \". . .\"\n\nSee discussion on sage-devel\n\nIssue created by migration from https://trac.sagemath.org/ticket/7478\n\n",
    "closed_at": "2009-11-19T17:01:35Z",
    "created_at": "2009-11-17T08:03:23Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "TestSuite improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7478",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: TestSuite

- Changes "... done" to ". . . pass" in the output of TestSuite().run(verbose = True) to avoid unintentional matches
- Fix the doctests accordingly.
- Adds skip option; use it in sage/combinat/sf/jack.py and orthotriang.py
- In case of failure, execute the following tests after printing out a traceback, and write a summary at the end
- Only use verbose=True in the doctests when useful (category examples)


Rationale for the ...: when testing something in verbose mode the typical output of sage is:

```
   sage: P = Sets().example("inherits")
   sage: TestSuite(P).run(verbose=True)
   running ._test_an_element() ... done
   running ._test_element_pickling() ... done
   running ._test_not_implemented_methods() ... done
   running ._test_pickling() ... done
   running ._test_some_elements() ... done
```
And there is some risks that the "..." match something they should'nt I change them to ". . ."

See discussion on sage-devel

Issue created by migration from https://trac.sagemath.org/ticket/7478





---

archive/issue_comments_063009.json:
```json
{
    "body": "Changing assignee from tbd to @hivert.",
    "created_at": "2009-11-17T08:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63009",
    "user": "https://github.com/hivert"
}
```

Changing assignee from tbd to @hivert.



---

archive/issue_comments_063010.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T15:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63010",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063011.json:
```json
{
    "body": "Changing component from misc to doctest.",
    "created_at": "2009-11-18T15:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63011",
    "user": "https://github.com/nthiery"
}
```

Changing component from misc to doctest.



---

archive/issue_comments_063012.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-18T15:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63012",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_063013.json:
```json
{
    "body": "There is a spurious \"only\" to \"o..\" change in sets_cat.py.",
    "created_at": "2009-11-18T18:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63013",
    "user": "https://github.com/mwhansen"
}
```

There is a spurious "only" to "o.." change in sets_cat.py.



---

archive/issue_comments_063014.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> There is a spurious \"only\" to \"o..\" change in sets_cat.py.\n\n\nGood spot :-)\n\nI had already found a couple, and thought I had done a systematic search.\n\nFixed in the newly uploaded patch.",
    "created_at": "2009-11-18T18:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63014",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 mhansen]:
> There is a spurious "only" to "o.." change in sets_cat.py.


Good spot :-)

I had already found a couple, and thought I had done a systematic search.

Fixed in the newly uploaded patch.



---

archive/issue_comments_063015.json:
```json
{
    "body": "Updated patch fix a doctest I had missed.",
    "created_at": "2009-11-18T20:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63015",
    "user": "https://github.com/nthiery"
}
```

Updated patch fix a doctest I had missed.



---

archive/issue_comments_063016.json:
```json
{
    "body": "There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review \n`trac_7478_testsuite_dots-fh-review.patch`\non the queue. Then either me or you fold, reupload and set positive review. \n\n...trying to ping you on irc for synchro.",
    "created_at": "2009-11-18T21:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63016",
    "user": "https://github.com/hivert"
}
```

There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review 
`trac_7478_testsuite_dots-fh-review.patch`
on the queue. Then either me or you fold, reupload and set positive review. 

...trying to ping you on irc for synchro.



---

archive/issue_comments_063017.json:
```json
{
    "body": "Attachment [trac_7478_testsuite_dots-fh.patch](tarball://root/attachments/some-uuid/ticket7478/trac_7478_testsuite_dots-fh.patch) by @nthiery created at 2009-11-18 22:09:46\n\nReplying to [comment:7 hivert]:\n> There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review \n> `trac_7478_testsuite_dots-fh-review.patch`\n> on the queue. Then either me or you fold, reupload and set positive review. \n> \n> ...trying to ping you on irc for synchro.\n\n\nReview patch is good. Folded and uploaded. positive review.",
    "created_at": "2009-11-18T22:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63017",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7478_testsuite_dots-fh.patch](tarball://root/attachments/some-uuid/ticket7478/trac_7478_testsuite_dots-fh.patch) by @nthiery created at 2009-11-18 22:09:46

Replying to [comment:7 hivert]:
> There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review 
> `trac_7478_testsuite_dots-fh-review.patch`
> on the queue. Then either me or you fold, reupload and set positive review. 
> 
> ...trying to ping you on irc for synchro.


Review patch is good. Folded and uploaded. positive review.



---

archive/issue_comments_063018.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-18T22:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63018",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63019",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017730.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-19T17:01:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7478#event-17730"
}
```



---

archive/issue_comments_063020.json:
```json
{
    "body": "I just \"discovered\" `sage.misc.sage_unittest`.  In case it's of wider use: At #7390 there's a `unittest` HTML report generator that may make it into SageNB.",
    "created_at": "2009-11-27T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7478#issuecomment-63020",
    "user": "https://github.com/qed777"
}
```

I just "discovered" `sage.misc.sage_unittest`.  In case it's of wider use: At #7390 there's a `unittest` HTML report generator that may make it into SageNB.
