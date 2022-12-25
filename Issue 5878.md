# Issue 5878: Add support for constructing irreducible matrix representations of the symmetric group

archive/issues_005878.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\nKeywords: sage-combinat\n\nIt would be great to be able to construct the matrices for the irreducible representations of the symmetric group.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5878\n\n",
    "created_at": "2009-04-23T16:57:53Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Add support for constructing irreducible matrix representations of the symmetric group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5878",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat

Keywords: sage-combinat

It would be great to be able to construct the matrices for the irreducible representations of the symmetric group.

Issue created by migration from https://trac.sagemath.org/ticket/5878





---

archive/issue_comments_046348.json:
```json
{
    "body": "Attachment [trac_5878.patch](tarball://root/attachments/some-uuid/ticket5878/trac_5878.patch) by @saliola created at 2009-04-23 17:05:46\n\nThe patch adds functionality to construct Young's seminormal and orthogonal representations as well as the Specht representation. This is done via Yang-Baxter graphs, so the patch implements that as well.",
    "created_at": "2009-04-23T17:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46348",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_5878.patch](tarball://root/attachments/some-uuid/ticket5878/trac_5878.patch) by @saliola created at 2009-04-23 17:05:46

The patch adds functionality to construct Young's seminormal and orthogonal representations as well as the Specht representation. This is done via Yang-Baxter graphs, so the patch implements that as well.



---

archive/issue_comments_046349.json:
```json
{
    "body": "Warning: The patch depends on #5877.\n\nBut it doesn't have to though: #5877 fixes an issue that is required for the `to_character` method, and this method is not necessary for the rest of the code.",
    "created_at": "2009-04-23T17:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46349",
    "user": "https://github.com/saliola"
}
```

Warning: The patch depends on #5877.

But it doesn't have to though: #5877 fixes an issue that is required for the `to_character` method, and this method is not necessary for the rest of the code.



---

archive/issue_comments_046350.json:
```json
{
    "body": "Using sage-4.0.alpha0 with patch from #6048, doctesting with options `-t -long` gave me BOOM!:\n\n```\n[mvngu@sage sage-4.0.alpha0]$ ./sage -t -long devel/sage-5878/sage/combinat/symmetric_group_representations.py\n<LOTS_OF_BOOM!>\n```\n\n[Here's](http://sage.math.washington.edu/home/mvngu/patch/5878/log.txt) the full (but very long) error log from the doctests.",
    "created_at": "2009-05-19T05:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46350",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Using sage-4.0.alpha0 with patch from #6048, doctesting with options `-t -long` gave me BOOM!:

```
[mvngu@sage sage-4.0.alpha0]$ ./sage -t -long devel/sage-5878/sage/combinat/symmetric_group_representations.py
<LOTS_OF_BOOM!>
```

[Here's](http://sage.math.washington.edu/home/mvngu/patch/5878/log.txt) the full (but very long) error log from the doctests.



---

archive/issue_comments_046351.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> Using sage-4.0.alpha0 with patch from #6048, doctesting with options `-t -long` gave me BOOM!:\n\nI can't reproduce this. When I run the tests, with or without #6048, I get no failures:\n\n\n```\nkarkwa: sage-4.0 -version\n| Sage Version 4.0.alpha0, Release Date: 2009-05-15                  |\nkarkwa: hg qapplied \nnon-ascii.patch\ntrac_5878.patch\n\nkarkwa: sage-4.0 -b && sage-4.0 -t -long symmetric_group_representations.py yang_baxter_graph.py \n...\nreal    0m1.263s\nuser    0m1.004s\nsys     0m0.244s\nsage -t -long \"devel/sage-main/sage/combinat/symmetric_group_representations.py\"\n         [5.8 s]\nsage -t -long \"devel/sage-main/sage/combinat/yang_baxter_graph.py\"\n         [3.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 9.2 seconds\n```\n\n\nCan you re-check this?\n\nThanks,\nFranco",
    "created_at": "2009-05-19T08:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46351",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:3 mvngu]:
> Using sage-4.0.alpha0 with patch from #6048, doctesting with options `-t -long` gave me BOOM!:

I can't reproduce this. When I run the tests, with or without #6048, I get no failures:


```
karkwa: sage-4.0 -version
| Sage Version 4.0.alpha0, Release Date: 2009-05-15                  |
karkwa: hg qapplied 
non-ascii.patch
trac_5878.patch

karkwa: sage-4.0 -b && sage-4.0 -t -long symmetric_group_representations.py yang_baxter_graph.py 
...
real    0m1.263s
user    0m1.004s
sys     0m0.244s
sage -t -long "devel/sage-main/sage/combinat/symmetric_group_representations.py"
         [5.8 s]
sage -t -long "devel/sage-main/sage/combinat/yang_baxter_graph.py"
         [3.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.2 seconds
```


Can you re-check this?

Thanks,
Franco



---

archive/issue_comments_046352.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T18:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46352",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046353.json:
```json
{
    "body": "Changing assignee from @saliola to @mwhansen.",
    "created_at": "2009-06-04T18:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46353",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @saliola to @mwhansen.



---

archive/issue_comments_046354.json:
```json
{
    "body": "Attachment [trac_5878-review.patch](tarball://root/attachments/some-uuid/ticket5878/trac_5878-review.patch) by @mwhansen created at 2009-06-04 18:48:09\n\nThings look good to me after I've applied my reviewer patch which takes care of the issues with the upgrade to 4.0.\n\nFranco, can you just check over these?",
    "created_at": "2009-06-04T18:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46354",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5878-review.patch](tarball://root/attachments/some-uuid/ticket5878/trac_5878-review.patch) by @mwhansen created at 2009-06-04 18:48:09

Things look good to me after I've applied my reviewer patch which takes care of the issues with the upgrade to 4.0.

Franco, can you just check over these?



---

archive/issue_comments_046355.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> Things look good to me after I've applied my reviewer patch which takes care of the issues with the upgrade to 4.0.\n> \n> Franco, can you just check over these?\n\nChecked. They are correct.\n\nPositive review for the reviewer patch.",
    "created_at": "2009-06-04T22:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46355",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:5 mhansen]:
> Things look good to me after I've applied my reviewer patch which takes care of the issues with the upgrade to 4.0.
> 
> Franco, can you just check over these?

Checked. They are correct.

Positive review for the reviewer patch.



---

archive/issue_comments_046356.json:
```json
{
    "body": "So all patches have proper review? If so, then the summary should be changed.",
    "created_at": "2009-06-08T03:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

So all patches have proper review? If so, then the summary should be changed.



---

archive/issue_comments_046357.json:
```json
{
    "body": "Patch looks good, tests pass on sage.math and my OS X 10.5 laptop.  I'm not expert enough to say the code is correct.  Is this positive review?",
    "created_at": "2009-06-15T20:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46357",
    "user": "https://github.com/ncalexan"
}
```

Patch looks good, tests pass on sage.math and my OS X 10.5 laptop.  I'm not expert enough to say the code is correct.  Is this positive review?



---

archive/issue_comments_046358.json:
```json
{
    "body": "This is ridiculous.  Mhansen gave it a positive review pending saliola's opinion.  Saliola confirmed mhansen's review and +1'd mhansen's patch.  I'm merging this one.",
    "created_at": "2009-06-19T18:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46358",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

This is ridiculous.  Mhansen gave it a positive review pending saliola's opinion.  Saliola confirmed mhansen's review and +1'd mhansen's patch.  I'm merging this one.



---

archive/issue_comments_046359.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5878#issuecomment-46359",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_013812.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T09:58:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5878",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5878#event-13812"
}
```
