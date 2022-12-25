# Issue 8702: Datastructure for objects with prototype (clone) design pattern.

archive/issues_008702.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  @novoselt @mwhansen sage-combinat\n\nThis is the future Cython replacement for CombinatorialObject. \n\nPatch in preparation in sage-combinat queue\n\nIssue created by migration from https://trac.sagemath.org/ticket/8702\n\n",
    "created_at": "2010-04-17T09:32:15Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Datastructure for objects with prototype (clone) design pattern.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8702",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  @novoselt @mwhansen sage-combinat

This is the future Cython replacement for CombinatorialObject. 

Patch in preparation in sage-combinat queue

Issue created by migration from https://trac.sagemath.org/ticket/8702





---

archive/issue_comments_079178.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-10T17:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79178",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079179.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-06-10T19:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79179",
    "user": "https://github.com/novoselt"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_079180.json:
```json
{
    "body": "Hi mike,\n\nI adressed your comment:\n\n> 2. Is there a good use case for allowing None to be passed in to\n> ClonableArray, ClonableList, and ConableIntArray.  There is a bit of\n> mental overhead in always having to remember to check that self._list\n> is always an actual list.\n\nand updated a new patch... Please review.",
    "created_at": "2010-10-24T09:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79180",
    "user": "https://github.com/hivert"
}
```

Hi mike,

I adressed your comment:

> 2. Is there a good use case for allowing None to be passed in to
> ClonableArray, ClonableList, and ConableIntArray.  There is a bit of
> mental overhead in always having to remember to check that self._list
> is always an actual list.

and updated a new patch... Please review.



---

archive/issue_comments_079181.json:
```json
{
    "body": "> and updated a new patch... Please review.\n\nSorry: I should have said that I also folded your review patch... Thanks for it.",
    "created_at": "2010-10-24T09:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79181",
    "user": "https://github.com/hivert"
}
```

> and updated a new patch... Please review.

Sorry: I should have said that I also folded your review patch... Thanks for it.



---

archive/issue_comments_079182.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-11-04T04:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79182",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_079183.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-04T04:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79183",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079184.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n> Looks good to me.\n\nThanks for the review !",
    "created_at": "2010-11-04T19:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79184",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:6 mhansen]:
> Looks good to me.

Thanks for the review !



---

archive/issue_comments_079185.json:
```json
{
    "body": "I get doctest errors:\n\n```\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/devel/sage-main/sage/structure/list_clone_timings.py\", line 8:\n    sage: from sage.structure.list_clone_timmings import *\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        from sage.structure.list_clone_timmings import *###line 8:\n    sage: from sage.structure.list_clone_timmings import *\n    ImportError: No module named list_clone_timmings\n**********************************************************************\n```\n",
    "created_at": "2010-11-06T07:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79185",
    "user": "https://github.com/jdemeyer"
}
```

I get doctest errors:

```
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/devel/sage-main/sage/structure/list_clone_timings.py", line 8:
    sage: from sage.structure.list_clone_timmings import *
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from sage.structure.list_clone_timmings import *###line 8:
    sage: from sage.structure.list_clone_timmings import *
    ImportError: No module named list_clone_timmings
**********************************************************************
```




---

archive/issue_comments_079186.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-06T07:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79186",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079187.json:
```json
{
    "body": "Attachment [diff-8702](tarball://root/attachments/some-uuid/ticket8702/diff-8702) by @hivert created at 2010-11-19 08:53:09",
    "created_at": "2010-11-19T08:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79187",
    "user": "https://github.com/hivert"
}
```

Attachment [diff-8702](tarball://root/attachments/some-uuid/ticket8702/diff-8702) by @hivert created at 2010-11-19 08:53:09



---

archive/issue_comments_079188.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-19T08:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79188",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079189.json:
```json
{
    "body": "Replying to [comment:8 jdemeyer]:\n> I get doctest errors:\n\n```\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/devel/sage-main/sage/structure/list_clone_timings.py\", line 8:\n    sage: from sage.structure.list_clone_timmings import *\n[...]\n```\n\n\nOups ! I forgot to fold some corrective patches. I just resubmitted the corrected version. To ease the review I also uploaded the [diff](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/diff-8702) between the older version and the new one. Do not apply this chunk of code.\n\nOnly apply [trac_8702-list_clone-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.patch)",
    "created_at": "2010-11-19T08:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79189",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:8 jdemeyer]:
> I get doctest errors:

```
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/devel/sage-main/sage/structure/list_clone_timings.py", line 8:
    sage: from sage.structure.list_clone_timmings import *
[...]
```


Oups ! I forgot to fold some corrective patches. I just resubmitted the corrected version. To ease the review I also uploaded the [diff](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/diff-8702) between the older version and the new one. Do not apply this chunk of code.

Only apply [trac_8702-list_clone-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.patch)



---

archive/issue_comments_079190.json:
```json
{
    "body": "Attachment [trac_8702-list_clone-fh.2.patch](tarball://root/attachments/some-uuid/ticket8702/trac_8702-list_clone-fh.2.patch) by @hivert created at 2010-11-19 09:56:33",
    "created_at": "2010-11-19T09:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79190",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8702-list_clone-fh.2.patch](tarball://root/attachments/some-uuid/ticket8702/trac_8702-list_clone-fh.2.patch) by @hivert created at 2010-11-19 09:56:33



---

archive/issue_comments_079191.json:
```json
{
    "body": "Added a missing utf8 tag on the file `list_clone_timings.py`... \n\nApply only [trac_8702-list_clone-fh.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.2.patch)",
    "created_at": "2010-11-19T09:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79191",
    "user": "https://github.com/hivert"
}
```

Added a missing utf8 tag on the file `list_clone_timings.py`... 

Apply only [trac_8702-list_clone-fh.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.2.patch)



---

archive/issue_comments_079192.json:
```json
{
    "body": "Attachment [trac_8702-list_clone-fh.patch](tarball://root/attachments/some-uuid/ticket8702/trac_8702-list_clone-fh.patch) by @hivert created at 2010-11-19 10:04:17\n\nOops ! I forgot to add Copyright notices... Sorry for the mess.\n\nApply only [trac_8702-list_clone-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.patch)",
    "created_at": "2010-11-19T10:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79192",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8702-list_clone-fh.patch](tarball://root/attachments/some-uuid/ticket8702/trac_8702-list_clone-fh.patch) by @hivert created at 2010-11-19 10:04:17

Oops ! I forgot to add Copyright notices... Sorry for the mess.

Apply only [trac_8702-list_clone-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.patch)



---

archive/issue_comments_079193.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-19T10:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79193",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8702#issuecomment-79194",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
