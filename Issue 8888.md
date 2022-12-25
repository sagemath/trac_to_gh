# Issue 8888: Returns the frontier of a partition

archive/issues_008888.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: Partitions border rim\n\nThe name of the actual method is being discussed on [sage-combinat](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/27e68b86cf8e0578/1869144ca150bda6?hl=en&lnk=gst&q=frontier#1869144ca150bda6)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8888\n\n",
    "created_at": "2010-05-05T11:33:20Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Returns the frontier of a partition",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8888",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: Partitions border rim

The name of the actual method is being discussed on [sage-combinat](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/27e68b86cf8e0578/1869144ca150bda6?hl=en&lnk=gst&q=frontier#1869144ca150bda6)

Issue created by migration from https://trac.sagemath.org/ticket/8888





---

archive/issue_comments_081577.json:
```json
{
    "body": "Attachment [trac_8888_partition_rim-fh.patch](tarball://root/attachments/some-uuid/ticket8888/trac_8888_partition_rim-fh.patch) by @hivert created at 2010-05-05 17:01:29\n\nPlease review.",
    "created_at": "2010-05-05T17:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81577",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8888_partition_rim-fh.patch](tarball://root/attachments/some-uuid/ticket8888/trac_8888_partition_rim-fh.patch) by @hivert created at 2010-05-05 17:01:29

Please review.



---

archive/issue_comments_081578.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T17:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81578",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081579.json:
```json
{
    "body": "Hi Florent,\n\nI've tried to apply this patch to a clean sage-4.4.1, and I'm getting strange behavior.  After applying your patch, the entire code for the `quotient` method in `partition.py` (after the docstring) looks like this:\n\n```\n        p = self\n        #Normalize the length\n        remainder = len(p) % length\n        part = p[:] + [0]*(length-remainder)\n```\n\n\nThe rest is just gone, and obviously this causes doctest failures.  Looking at the patch file, I don't understand why this should happen.  It looks fine!  But I can't approve with this behavior.  Can you rebase?  Or explain what might be going on?",
    "created_at": "2010-05-12T02:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81579",
    "user": "https://github.com/jbandlow"
}
```

Hi Florent,

I've tried to apply this patch to a clean sage-4.4.1, and I'm getting strange behavior.  After applying your patch, the entire code for the `quotient` method in `partition.py` (after the docstring) looks like this:

```
        p = self
        #Normalize the length
        remainder = len(p) % length
        part = p[:] + [0]*(length-remainder)
```


The rest is just gone, and obviously this causes doctest failures.  Looking at the patch file, I don't understand why this should happen.  It looks fine!  But I can't approve with this behavior.  Can you rebase?  Or explain what might be going on?



---

archive/issue_comments_081580.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-12T02:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81580",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081581.json:
```json
{
    "body": "Hi Jason,\n\nThanks for taking care of this review\n\n> The rest is just gone, and obviously this causes doctest failures.  Looking at the patch file, I don't understand why this should happen.  It looks fine!  But I can't approve with this behavior.  Can you rebase?  Or explain what might be going on?\n\nOups ! I didn't realize that this patch depend on #6655 (allready merged in 4.4.2.rc0). Sorry for the trouble.",
    "created_at": "2010-05-12T17:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81581",
    "user": "https://github.com/hivert"
}
```

Hi Jason,

Thanks for taking care of this review

> The rest is just gone, and obviously this causes doctest failures.  Looking at the patch file, I don't understand why this should happen.  It looks fine!  But I can't approve with this behavior.  Can you rebase?  Or explain what might be going on?

Oups ! I didn't realize that this patch depend on #6655 (allready merged in 4.4.2.rc0). Sorry for the trouble.



---

archive/issue_comments_081582.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-12T17:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81582",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081583.json:
```json
{
    "body": "Attachment [trac_8888_reviewer_jb.patch](tarball://root/attachments/some-uuid/ticket8888/trac_8888_reviewer_jb.patch) by @jbandlow created at 2010-05-13 14:57:55",
    "created_at": "2010-05-13T14:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81583",
    "user": "https://github.com/jbandlow"
}
```

Attachment [trac_8888_reviewer_jb.patch](tarball://root/attachments/some-uuid/ticket8888/trac_8888_reviewer_jb.patch) by @jbandlow created at 2010-05-13 14:57:55



---

archive/issue_comments_081584.json:
```json
{
    "body": "After applying #6655 everything applies fine.  Thanks.  I give a positive review to the code, but  I included a trivial reviewer patch to clean up the doc a little bit.",
    "created_at": "2010-05-13T15:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81584",
    "user": "https://github.com/jbandlow"
}
```

After applying #6655 everything applies fine.  Thanks.  I give a positive review to the code, but  I included a trivial reviewer patch to clean up the doc a little bit.



---

archive/issue_comments_081585.json:
```json
{
    "body": "Replying to [comment:5 jbandlow]:\nJason's reviewer patch looks perfectly good to me. Positive review\n\nJason: Can you push your review patch to combinat server ?",
    "created_at": "2010-05-13T15:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81585",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:5 jbandlow]:
Jason's reviewer patch looks perfectly good to me. Positive review

Jason: Can you push your review patch to combinat server ?



---

archive/issue_comments_081586.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-13T15:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81586",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081587.json:
```json
{
    "body": "Replying to [comment:6 hivert]:\n> Replying to [comment:5 jbandlow]:\n> Jason's reviewer patch looks perfectly good to me. Positive review\n> \n> Jason: Can you push your review patch to combinat server ? \n\nDone.",
    "created_at": "2010-05-13T20:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81587",
    "user": "https://github.com/jbandlow"
}
```

Replying to [comment:6 hivert]:
> Replying to [comment:5 jbandlow]:
> Jason's reviewer patch looks perfectly good to me. Positive review
> 
> Jason: Can you push your review patch to combinat server ? 

Done.



---

archive/issue_events_009045.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:23:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8888#event-9045"
}
```



---

archive/issue_comments_081588.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8888#issuecomment-81588",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
