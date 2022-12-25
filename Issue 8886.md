# Issue 8886: tutorial on Python object and classes

archive/issues_008886.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  @nexttime @nthiery\n\nAs the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8275334246de4531) thread for some background information. This should be coordinated with #8470.\n\n**Apply:**\n\n1. [attachment:trac_8886-objects-classes_tutorial-fh-jhp-rebased.patch]\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8886\n\n",
    "closed_at": "2011-10-08T18:15:05Z",
    "created_at": "2010-05-05T11:12:50Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "tutorial on Python object and classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @hivert

CC:  @nexttime @nthiery

As the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8275334246de4531) thread for some background information. This should be coordinated with #8470.

**Apply:**

1. [attachment:trac_8886-objects-classes_tutorial-fh-jhp-rebased.patch]


Issue created by migration from https://trac.sagemath.org/ticket/8886





---

archive/issue_comments_081547.json:
```json
{
    "body": "Changing assignee from mvngu to @hivert.",
    "created_at": "2010-05-05T11:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81547",
    "user": "https://github.com/hivert"
}
```

Changing assignee from mvngu to @hivert.



---

archive/issue_comments_081548.json:
```json
{
    "body": "I'm preparing a patch on sage-combinat queue... I took ownership of the ticket (to have it in the my ticket report).\n\nFlorent",
    "created_at": "2010-05-05T11:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81548",
    "user": "https://github.com/hivert"
}
```

I'm preparing a patch on sage-combinat queue... I took ownership of the ticket (to have it in the my ticket report).

Florent



---

archive/issue_comments_081549.json:
```json
{
    "body": "Attachment [trac_8886-config.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-config.patch) by mvngu created at 2010-05-05 14:02:16",
    "created_at": "2010-05-05T14:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8886-config.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-config.patch) by mvngu created at 2010-05-05 14:02:16



---

archive/issue_comments_081550.json:
```json
{
    "body": "The patch [trac_8886-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8886/trac_8886-config.patch) contains the Sphinx configuration and build files. Such files are required to get Sphinx to build documents in the category \"Thematic Tutorials\". When #8468 was merged, the prerequisites listed on that ticket were not merged at all. This meant that the relevant build and configuration files did not go into Sage 4.4.1. The patch [trac_8886-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8886/trac_8886-config.patch) is an attempt to fix this. You should apply this patch prior to adding any new documents to \"Thematic Tutorials\".",
    "created_at": "2010-05-05T14:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch [trac_8886-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8886/trac_8886-config.patch) contains the Sphinx configuration and build files. Such files are required to get Sphinx to build documents in the category "Thematic Tutorials". When #8468 was merged, the prerequisites listed on that ticket were not merged at all. This meant that the relevant build and configuration files did not go into Sage 4.4.1. The patch [trac_8886-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8886/trac_8886-config.patch) is an attempt to fix this. You should apply this patch prior to adding any new documents to "Thematic Tutorials".



---

archive/issue_comments_081551.json:
```json
{
    "body": "I have sage 4.3.5 and have been manually applying the doc patches. This one does not apply even though I have the prereqs. I have applied 8464, 8465, 8469, and 8442. Is that the wrong order?\n~Mark",
    "created_at": "2010-05-05T19:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81551",
    "user": "https://trac.sagemath.org/admin/accounts/users/mjordan7"
}
```

I have sage 4.3.5 and have been manually applying the doc patches. This one does not apply even though I have the prereqs. I have applied 8464, 8465, 8469, and 8442. Is that the wrong order?
~Mark



---

archive/issue_comments_081552.json:
```json
{
    "body": "Replying to [comment:3 mjordan7]:\n> I have sage 4.3.5 and have been manually applying the doc patches. This one does not apply even though I have the prereqs.\n\n\nI didn't mention that you need to apply patches on top of Sage 4.4.1. The patches on this ticket and the prequisite ticket were produced on top of Sage 4.4.1. Sorry for the inconvenience.",
    "created_at": "2010-05-05T20:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81552",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 mjordan7]:
> I have sage 4.3.5 and have been manually applying the doc patches. This one does not apply even though I have the prereqs.


I didn't mention that you need to apply patches on top of Sage 4.4.1. The patches on this ticket and the prequisite ticket were produced on top of Sage 4.4.1. Sorry for the inconvenience.



---

archive/issue_comments_081553.json:
```json
{
    "body": "If #8465 is merged, then trac_8886-config.patch is no longer needed.",
    "created_at": "2010-07-28T01:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81553",
    "user": "https://github.com/jhpalmieri"
}
```

If #8465 is merged, then trac_8886-config.patch is no longer needed.



---

archive/issue_comments_081554.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-28T08:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81554",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081555.json:
```json
{
    "body": "Attachment [trac_8886-objects-classes_tutorial-fh.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-fh.patch) by @hivert created at 2011-06-28 12:51:38",
    "created_at": "2011-06-28T12:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81555",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8886-objects-classes_tutorial-fh.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-fh.patch) by @hivert created at 2011-06-28 12:51:38



---

archive/issue_comments_081556.json:
```json
{
    "body": "There is a mistake in thematic_tutorials/conf.py which prevents math like `\\QQ` from being rendered properly.  This is fixed in #11632, so I've made that a dependency for this ticket.  (Please review it!)\n\nI've fixed some typos and grammatical errors.  See the \"delta\" patch for the differences between my patch and the previous one.  I'm happy with what you've done, so if you're happy with my changes, give the ticket a positive review.",
    "created_at": "2011-07-26T23:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81556",
    "user": "https://github.com/jhpalmieri"
}
```

There is a mistake in thematic_tutorials/conf.py which prevents math like `\QQ` from being rendered properly.  This is fixed in #11632, so I've made that a dependency for this ticket.  (Please review it!)

I've fixed some typos and grammatical errors.  See the "delta" patch for the differences between my patch and the previous one.  I'm happy with what you've done, so if you're happy with my changes, give the ticket a positive review.



---

archive/issue_comments_081557.json:
```json
{
    "body": "Attachment [trac_8886-delta.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-delta.patch) by @jhpalmieri created at 2011-07-26 23:28:28",
    "created_at": "2011-07-26T23:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81557",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8886-delta.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-delta.patch) by @jhpalmieri created at 2011-07-26 23:28:28



---

archive/issue_comments_081558.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-07-28T08:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81558",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081559.json:
```json
{
    "body": "Attachment [trac_8886-objects-classes_tutorial-jhp.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-jhp.patch) by @hivert created at 2011-07-28 08:24:19\n\nReplying to [comment:9 jhpalmieri]:\n> There is a mistake in thematic_tutorials/conf.py which prevents math like\n> `\\QQ` from being rendered properly.  This is fixed in #11632, so I've made\n> that a dependency for this ticket.  (Please review it!)\n\n\nI'll do it. \n\n\n> I've fixed some typos and grammatical errors.  See the \"delta\" patch for the\n> differences between my patch and the previous one.  I'm happy with what\n> you've done, so if you're happy with my changes, give the ticket a positive\n> review.\n\n\nThanks for correcting my bad English. I'm mostly happy with your change. The\nonly remark I have is the removal of the link\n`:ref:`tutorial-programming-python``. It is an up coming tutorial which is\nnot yet fully finished. I'm creating a new ticket (#11633) and reinstating the pointer\nthere.\n\nThanks for your careful review.\n\nFlorent",
    "created_at": "2011-07-28T08:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81559",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8886-objects-classes_tutorial-jhp.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-jhp.patch) by @hivert created at 2011-07-28 08:24:19

Replying to [comment:9 jhpalmieri]:
> There is a mistake in thematic_tutorials/conf.py which prevents math like
> `\QQ` from being rendered properly.  This is fixed in #11632, so I've made
> that a dependency for this ticket.  (Please review it!)


I'll do it. 


> I've fixed some typos and grammatical errors.  See the "delta" patch for the
> differences between my patch and the previous one.  I'm happy with what
> you've done, so if you're happy with my changes, give the ticket a positive
> review.


Thanks for correcting my bad English. I'm mostly happy with your change. The
only remark I have is the removal of the link
`:ref:`tutorial-programming-python``. It is an up coming tutorial which is
not yet fully finished. I'm creating a new ticket (#11633) and reinstating the pointer
there.

Thanks for your careful review.

Florent



---

archive/issue_events_021686.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-28T10:26:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8886#event-21686"
}
```



---

archive/issue_comments_081560.json:
```json
{
    "body": "Nicolas pointed out the following typo:\n\nline 14: \n\n``functions (see the \"Programming\" section of the Sage tutorial) -- but now further\n+knowledge``\n\n\"now\" should be \"no\". I'm updating a corrected patch.",
    "created_at": "2011-08-31T09:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81560",
    "user": "https://github.com/hivert"
}
```

Nicolas pointed out the following typo:

line 14: 

``functions (see the "Programming" section of the Sage tutorial) -- but now further
+knowledge``

"now" should be "no". I'm updating a corrected patch.



---

archive/issue_comments_081561.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-08-31T09:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81561",
    "user": "https://github.com/hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081562.json:
```json
{
    "body": "Attachment [trac_8886-objects-classes_tutorial-fh-jhp.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-fh-jhp.patch) by @hivert created at 2011-08-31 09:40:51",
    "created_at": "2011-08-31T09:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81562",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8886-objects-classes_tutorial-fh-jhp.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-fh-jhp.patch) by @hivert created at 2011-08-31 09:40:51



---

archive/issue_comments_081563.json:
```json
{
    "body": "New new patch is updated it should be reviewed. The diff from the preceding patch is:\n\n```\n1.1 --- a/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 09:50:46 2011 +0200 \n1.2 +++ b/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 11:37:04 2011 +0200 \n1.3 @@ -890,7 +890,7 @@ \n1.4 +This tutorial is an introduction to object-oriented programming in Python and \n1.5 +Sage. It requires basic knowledge about imperative/procedural programming (the \n1.6 +most common programming style) -- that is, conditional instructions, loops, \n1.7 -+functions (see the \"Programming\" section of the Sage tutorial) -- but now further knowledge \n1.8 ++functions (see the \"Programming\" section of the Sage tutorial) -- but no further knowledge \n1.9 +about objects and classes is assumed. It is designed as an alternating \n1.10 +sequence of formal introduction and exercises. :ref:`solutions` are given at \n1.11 +the end. \n```",
    "created_at": "2011-08-31T09:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81563",
    "user": "https://github.com/hivert"
}
```

New new patch is updated it should be reviewed. The diff from the preceding patch is:

```
1.1 --- a/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 09:50:46 2011 +0200 
1.2 +++ b/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 11:37:04 2011 +0200 
1.3 @@ -890,7 +890,7 @@ 
1.4 +This tutorial is an introduction to object-oriented programming in Python and 
1.5 +Sage. It requires basic knowledge about imperative/procedural programming (the 
1.6 +most common programming style) -- that is, conditional instructions, loops, 
1.7 -+functions (see the "Programming" section of the Sage tutorial) -- but now further knowledge 
1.8 ++functions (see the "Programming" section of the Sage tutorial) -- but no further knowledge 
1.9 +about objects and classes is assumed. It is designed as an alternating 
1.10 +sequence of formal introduction and exercises. :ref:`solutions` are given at 
1.11 +the end. 
```



---

archive/issue_comments_081564.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-31T09:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81564",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081565.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-31T11:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81565",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081566.json:
```json
{
    "body": "Replying to [comment:14 hivert]:\n> New new patch is updated it should be reviewed. The diff from the preceding patch is:\n> \n> \n> ```\n> 1.1 --- a/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 09:50:46 2011 +0200 \n> 1.2 +++ b/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 11:37:04 2011 +0200 \n> 1.3 @@ -890,7 +890,7 @@ \n> 1.4 +This tutorial is an introduction to object-oriented programming in Python and \n> 1.5 +Sage. It requires basic knowledge about imperative/procedural programming (the \n> 1.6 +most common programming style) -- that is, conditional instructions, loops, \n> 1.7 -+functions (see the \"Programming\" section of the Sage tutorial) -- but now further knowledge \n> 1.8 ++functions (see the \"Programming\" section of the Sage tutorial) -- but no further knowledge \n> 1.9 +about objects and classes is assumed. It is designed as an alternating \n> 1.10 +sequence of formal introduction and exercises. :ref:`solutions` are given at \n> 1.11 +the end. \n> ```\n\n\nI suggested that tiny change, so positive review on it :-)",
    "created_at": "2011-08-31T11:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81566",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:14 hivert]:
> New new patch is updated it should be reviewed. The diff from the preceding patch is:
> 
> 
> ```
> 1.1 --- a/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 09:50:46 2011 +0200 
> 1.2 +++ b/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 11:37:04 2011 +0200 
> 1.3 @@ -890,7 +890,7 @@ 
> 1.4 +This tutorial is an introduction to object-oriented programming in Python and 
> 1.5 +Sage. It requires basic knowledge about imperative/procedural programming (the 
> 1.6 +most common programming style) -- that is, conditional instructions, loops, 
> 1.7 -+functions (see the "Programming" section of the Sage tutorial) -- but now further knowledge 
> 1.8 ++functions (see the "Programming" section of the Sage tutorial) -- but no further knowledge 
> 1.9 +about objects and classes is assumed. It is designed as an alternating 
> 1.10 +sequence of formal introduction and exercises. :ref:`solutions` are given at 
> 1.11 +the end. 
> ```


I suggested that tiny change, so positive review on it :-)



---

archive/issue_events_021687.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-06T11:54:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8886#event-21687"
}
```



---

archive/issue_events_021688.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-06T11:54:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8886#event-21688"
}
```



---

archive/issue_comments_081567.json:
```json
{
    "body": "Attachment [trac_8886-objects-classes_tutorial-fh-jhp-rebased.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-fh-jhp-rebased.patch) by @jdemeyer created at 2011-10-06 11:54:40",
    "created_at": "2011-10-06T11:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81567",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_8886-objects-classes_tutorial-fh-jhp-rebased.patch](tarball://root/attachments/some-uuid/ticket8886/trac_8886-objects-classes_tutorial-fh-jhp-rebased.patch) by @jdemeyer created at 2011-10-06 11:54:40



---

archive/issue_events_021689.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-08T18:15:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8886#event-21689"
}
```



---

archive/issue_comments_081568.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-08T18:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8886#issuecomment-81568",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
