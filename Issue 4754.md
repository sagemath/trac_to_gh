# Issue 4754: Merge minimum rank code

archive/issues_004754.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  mvngu\n\nBased on the discussion at http://groups.google.com/group/sage-support/browse_thread/thread/3ec4cc026e9c65bd, it would be great to merge the code found at http://arxiv.org/abs/0812.1616 into the Sage library.  Several functions should probably go into the main graph library (e.g., the edge clique cover function), while others probably ought to go into a minimum_rank.sage file.\n\nI am one of the developers and hereby give my permission to incorporate the code into Sage.  I will ask the other developers as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4754\n\n",
    "created_at": "2008-12-11T04:15:52Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Merge minimum rank code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4754",
    "user": "jason"
}
```
Assignee: rlm

CC:  mvngu

Based on the discussion at http://groups.google.com/group/sage-support/browse_thread/thread/3ec4cc026e9c65bd, it would be great to merge the code found at http://arxiv.org/abs/0812.1616 into the Sage library.  Several functions should probably go into the main graph library (e.g., the edge clique cover function), while others probably ought to go into a minimum_rank.sage file.

I am one of the developers and hereby give my permission to incorporate the code into Sage.  I will ask the other developers as well.

Issue created by migration from https://trac.sagemath.org/ticket/4754





---

archive/issue_comments_035997.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T04:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-35997",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035998.json:
```json
{
    "body": "Changing assignee from rlm to jason.",
    "created_at": "2008-12-11T04:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-35998",
    "user": "jason"
}
```

Changing assignee from rlm to jason.



---

archive/issue_comments_035999.json:
```json
{
    "body": "I also have a *much* faster Cython zero-forcing-set tester that I could donate to Sage.",
    "created_at": "2008-12-11T04:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-35999",
    "user": "jason"
}
```

I also have a *much* faster Cython zero-forcing-set tester that I could donate to Sage.



---

archive/issue_comments_036000.json:
```json
{
    "body": "> while others probably ought to go into a minimum_rank.sage file. \n\nI don't think anything included in the core main sage library should go in a .sage file.  It should go in a .py file.\n\nWilliam",
    "created_at": "2008-12-11T04:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36000",
    "user": "was"
}
```

> while others probably ought to go into a minimum_rank.sage file. 

I don't think anything included in the core main sage library should go in a .sage file.  It should go in a .py file.

William



---

archive/issue_comments_036001.json:
```json
{
    "body": "From personal email from Geoff Tims, 13 Dec 2008:\n\n\n```\nHey Jason,\n \nI don't know exactly how I feel.  I'm probably fine with it.\n \nI agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later\n \nGeoff\n```\n",
    "created_at": "2008-12-22T18:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36001",
    "user": "jason"
}
```

From personal email from Geoff Tims, 13 Dec 2008:


```
Hey Jason,
 
I don't know exactly how I feel.  I'm probably fine with it.
 
I agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later
 
Geoff
```




---

archive/issue_comments_036002.json:
```json
{
    "body": "From personal email from Tracy McKay, 11 Dec 2008:\n\n\n```\nHi Jason,\n\nI agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later. \n\nThanks,\n\nTracy McKay\n```\n",
    "created_at": "2008-12-22T18:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36002",
    "user": "jason"
}
```

From personal email from Tracy McKay, 11 Dec 2008:


```
Hi Jason,

I agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later. 

Thanks,

Tracy McKay
```




---

archive/issue_comments_036003.json:
```json
{
    "body": "From personal email from Laura DeLoss, 11 Dec 2008:\n\n\n```\nI agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later and for the EGR group (Jason, Jason, Geoff, Tracy and myself) to be listed as the Sage contributors. \n```\n",
    "created_at": "2008-12-22T18:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36003",
    "user": "jason"
}
```

From personal email from Laura DeLoss, 11 Dec 2008:


```
I agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later and for the EGR group (Jason, Jason, Geoff, Tracy and myself) to be listed as the Sage contributors. 
```




---

archive/issue_comments_036004.json:
```json
{
    "body": "CC'ing myself",
    "created_at": "2009-06-27T00:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36004",
    "user": "mvngu"
}
```

CC'ing myself



---

archive/issue_comments_036005.json:
```json
{
    "body": "Jason Smith also verbally gave me permission to license the code GPLv2 or later.",
    "created_at": "2010-01-05T04:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36005",
    "user": "jason"
}
```

Jason Smith also verbally gave me permission to license the code GPLv2 or later.



---

archive/issue_comments_036006.json:
```json
{
    "body": "Attachment\n\napply on top of previous patch",
    "created_at": "2010-02-02T10:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36006",
    "user": "jason"
}
```

Attachment

apply on top of previous patch



---

archive/issue_comments_036007.json:
```json
{
    "body": "Attachment\n\napply on top of previous patches",
    "created_at": "2010-02-02T10:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36007",
    "user": "jason"
}
```

Attachment

apply on top of previous patches



---

archive/issue_comments_036008.json:
```json
{
    "body": "Attachment\n\nAdded rough versions of patches.",
    "created_at": "2010-02-02T10:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36008",
    "user": "jason"
}
```

Attachment

Added rough versions of patches.



---

archive/issue_comments_036009.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-02T10:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36009",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_036010.json:
```json
{
    "body": "Is it best to merge the code or to make https://github.com/jasongrout/minimum_rank an optional package ?",
    "created_at": "2021-10-02T14:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4754#issuecomment-36010",
    "user": "dcoudert"
}
```

Is it best to merge the code or to make https://github.com/jasongrout/minimum_rank an optional package ?
