# Issue 8775: Bug in conjugate of symbolic ring

archive/issues_008775.json:
```json
{
    "body": "Assignee: @burcin\n\nFrom [http://groups.google.com/group/sage-devel/browse_thread/thread/9f941378a95c0191](http://groups.google.com/group/sage-devel/browse_thread/thread/9f941378a95c0191):\n\n```\nsage: a = sqrt(-3) \nsage: a \nsqrt(-3) \nsage: a.conjugate() \nsqrt(-3) \nsage: bool(a==a.conjugate()) \nTrue \n```\nCould this be related to #6244?  Anyway, presumably conjugate should remain unevaluated on this sort of thing, while still being evaluated on things like a+I or 33.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8775\n\n",
    "created_at": "2010-04-27T01:02:12Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Bug in conjugate of symbolic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8775",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @burcin

From [http://groups.google.com/group/sage-devel/browse_thread/thread/9f941378a95c0191](http://groups.google.com/group/sage-devel/browse_thread/thread/9f941378a95c0191):

```
sage: a = sqrt(-3) 
sage: a 
sqrt(-3) 
sage: a.conjugate() 
sqrt(-3) 
sage: bool(a==a.conjugate()) 
True 
```
Could this be related to #6244?  Anyway, presumably conjugate should remain unevaluated on this sort of thing, while still being evaluated on things like a+I or 33.

Issue created by migration from https://trac.sagemath.org/ticket/8775





---

archive/issue_comments_080193.json:
```json
{
    "body": "From Burcin Erocal on the same thread:\n\n```\nThis is a bug in GiNaC: \nginsh - GiNaC Interactive Shell (ginac V1.5.7) \n  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz, \n (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY. \n  ._) i N a C | You are welcome to redistribute it under certain conditions. \n<-------------' For details type `warranty;'. \nType ?? for a list of help topics. \n> sqrt(-3); \nsqrt(-3) \n> conjugate(sqrt(-3)); \n\nsqrt(-3) \nFor conjugation, power objects just compute the conjugate of the basis \nand the exponent, and construct a new power object from these. Here is \nthe relevant function: \nhttp://pynac.sagemath.org/hg/file/3ece9ba22005/ginac/power.cpp#l805 \n```\nI'm changing this to \"not yet reported upstream\".",
    "created_at": "2010-04-27T13:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80193",
    "user": "https://github.com/kcrisman"
}
```

From Burcin Erocal on the same thread:

```
This is a bug in GiNaC: 
ginsh - GiNaC Interactive Shell (ginac V1.5.7) 
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz, 
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY. 
  ._) i N a C | You are welcome to redistribute it under certain conditions. 
<-------------' For details type `warranty;'. 
Type ?? for a list of help topics. 
> sqrt(-3); 
sqrt(-3) 
> conjugate(sqrt(-3)); 

sqrt(-3) 
For conjugation, power objects just compute the conjugate of the basis 
and the exponent, and construct a new power object from these. Here is 
the relevant function: 
http://pynac.sagemath.org/hg/file/3ece9ba22005/ginac/power.cpp#l805 
```
I'm changing this to "not yet reported upstream".



---

archive/issue_comments_080194.json:
```json
{
    "body": "Changing upstream report - too early for feedback at this point.",
    "created_at": "2010-04-27T15:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80194",
    "user": "https://github.com/kcrisman"
}
```

Changing upstream report - too early for feedback at this point.



---

archive/issue_comments_080195.json:
```json
{
    "body": "add doctests",
    "created_at": "2010-05-06T03:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80195",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_comments_080196.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-05-06T04:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80196",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_080197.json:
```json
{
    "body": "Attachment [trac_8775-conjugate.patch](tarball://root/attachments/some-uuid/ticket8775/trac_8775-conjugate.patch) by @burcin created at 2010-05-06 04:27:18\n\nThis is fixed by the new pynac package at #8903. attachment:trac_8775-conjugate.patch contains doctest fixes.\n\nNote that the new pynac version also fixes #8542, #8651, and #8688. Patches from these tickets should be applied before running doctests.",
    "created_at": "2010-05-06T04:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80197",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8775-conjugate.patch](tarball://root/attachments/some-uuid/ticket8775/trac_8775-conjugate.patch) by @burcin created at 2010-05-06 04:27:18

This is fixed by the new pynac package at #8903. attachment:trac_8775-conjugate.patch contains doctest fixes.

Note that the new pynac version also fixes #8542, #8651, and #8688. Patches from these tickets should be applied before running doctests.



---

archive/issue_comments_080198.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T04:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80198",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080199.json:
```json
{
    "body": "For some reason, although Sage 4.4.4.alpha0 has pynac-0.2.0.p3\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: N(sqrt(-2),200)\n8.0751148893563733350506651837615871941533119425962889089783e-62 + 1.4142135623730950488016887242096980785696718753769480731767*I\nsage: conjugate(sqrt(-3))\nsqrt(-3)\n```\nDid this change not end up making it into the Pynac package after all?  According to [http://pynac.sagemath.org/hg/rev/60acd6985820](http://pynac.sagemath.org/hg/rev/60acd6985820), it should be in there, but now I find it hard to explain the above.",
    "created_at": "2010-06-10T01:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80199",
    "user": "https://github.com/kcrisman"
}
```

For some reason, although Sage 4.4.4.alpha0 has pynac-0.2.0.p3

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: N(sqrt(-2),200)
8.0751148893563733350506651837615871941533119425962889089783e-62 + 1.4142135623730950488016887242096980785696718753769480731767*I
sage: conjugate(sqrt(-3))
sqrt(-3)
```
Did this change not end up making it into the Pynac package after all?  According to [http://pynac.sagemath.org/hg/rev/60acd6985820](http://pynac.sagemath.org/hg/rev/60acd6985820), it should be in there, but now I find it hard to explain the above.



---

archive/issue_comments_080200.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-10T01:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80200",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080201.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n> Did this change not end up making it into the Pynac package after all?  According to [http://pynac.sagemath.org/hg/rev/60acd6985820](http://pynac.sagemath.org/hg/rev/60acd6985820), it should be in there, but now I find it hard to explain the above.\n\n\nThat patched was backed out since it caused some problems with doctests in `sage/rings/qqbar.py`.\n\nI merged the upstream patch from GiNaC fixing this problem in the latest version of pynac. I will upload a new patch with doctest fixes later.",
    "created_at": "2010-09-12T16:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80201",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:4 kcrisman]:
> Did this change not end up making it into the Pynac package after all?  According to [http://pynac.sagemath.org/hg/rev/60acd6985820](http://pynac.sagemath.org/hg/rev/60acd6985820), it should be in there, but now I find it hard to explain the above.


That patched was backed out since it caused some problems with doctests in `sage/rings/qqbar.py`.

I merged the upstream patch from GiNaC fixing this problem in the latest version of pynac. I will upload a new patch with doctest fixes later.



---

archive/issue_comments_080202.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-09-12T22:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80202",
    "user": "https://github.com/burcin"
}
```

apply only this patch



---

archive/issue_comments_080203.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-12T22:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80203",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080204.json:
```json
{
    "body": "Attachment [trac_8775-conjugate.take2.patch](tarball://root/attachments/some-uuid/ticket8775/trac_8775-conjugate.take2.patch) by @burcin created at 2010-09-12 22:16:08\n\nI uploaded a new patch to add doctests for the fixes in Pynac. Only attachment:trac_8775-conjugate.take2.patch should be applied.\n\nThis depends on #9901.",
    "created_at": "2010-09-12T22:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80204",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8775-conjugate.take2.patch](tarball://root/attachments/some-uuid/ticket8775/trac_8775-conjugate.take2.patch) by @burcin created at 2010-09-12 22:16:08

I uploaded a new patch to add doctests for the fixes in Pynac. Only attachment:trac_8775-conjugate.take2.patch should be applied.

This depends on #9901.



---

archive/issue_comments_080205.json:
```json
{
    "body": "The issue seems to be solved. I have tried other examples and it works as expected. The doctest passes.\nPositive review",
    "created_at": "2010-11-06T11:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80205",
    "user": "https://github.com/lftabera"
}
```

The issue seems to be solved. I have tried other examples and it works as expected. The doctest passes.
Positive review



---

archive/issue_comments_080206.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-06T11:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80206",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080207.json:
```json
{
    "body": "There is a typo in the ticket number in the commit message :-)",
    "created_at": "2010-11-07T10:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80207",
    "user": "https://github.com/jdemeyer"
}
```

There is a typo in the ticket number in the commit message :-)



---

archive/issue_comments_080208.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-07T10:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80208",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080209.json:
```json
{
    "body": "Same patch with fixed commit message",
    "created_at": "2010-11-11T13:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80209",
    "user": "https://github.com/jdemeyer"
}
```

Same patch with fixed commit message



---

archive/issue_events_021383.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-11T13:42:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8775#event-21383"
}
```



---

archive/issue_comments_080210.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T13:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80210",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_080211.json:
```json
{
    "body": "Attachment [trac_8775-conjugate-fixed-message.patch](tarball://root/attachments/some-uuid/ticket8775/trac_8775-conjugate-fixed-message.patch) by @jdemeyer created at 2010-11-11 13:42:34",
    "created_at": "2010-11-11T13:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8775#issuecomment-80211",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_8775-conjugate-fixed-message.patch](tarball://root/attachments/some-uuid/ticket8775/trac_8775-conjugate-fixed-message.patch) by @jdemeyer created at 2010-11-11 13:42:34
