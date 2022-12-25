# Issue 7754: Weyl group optimizations

archive/issues_007754.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  @dwbump\n\nKeywords: Weyl groups\n\n- faster hash method calling the hash of the underlying matrix\n   (which is set as immutable for that purpose)\n  - new __eq__ method\n  - action on the weight lattice realization:\n   optimization of the matrix multiplication\n\nIssue created by migration from https://trac.sagemath.org/ticket/7754\n\n",
    "created_at": "2009-12-23T23:13:29Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Weyl group optimizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7754",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  @dwbump

Keywords: Weyl groups

- faster hash method calling the hash of the underlying matrix
   (which is set as immutable for that purpose)
  - new __eq__ method
  - action on the weight lattice realization:
   optimization of the matrix multiplication

Issue created by migration from https://trac.sagemath.org/ticket/7754





---

archive/issue_comments_066663.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-23T23:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66663",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066664.json:
```json
{
    "body": "Attachment [trac_7754_weyl_group_optimizations-nt.patch](tarball://root/attachments/some-uuid/ticket7754/trac_7754_weyl_group_optimizations-nt.patch) by @nthiery created at 2009-12-23 23:15:15",
    "created_at": "2009-12-23T23:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66664",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7754_weyl_group_optimizations-nt.patch](tarball://root/attachments/some-uuid/ticket7754/trac_7754_weyl_group_optimizations-nt.patch) by @nthiery created at 2009-12-23 23:15:15



---

archive/issue_comments_066665.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-01T21:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66665",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066666.json:
```json
{
    "body": "I tested this patch without #7753. I tested it with and without the\npatch in #7751.\n\nIt is a very substantial speedup. It cuts a few \nseconds off `sage -t weyl_groups.py` but more importantly it about doubles the speed of computing the reduced word of a Weyl group element, which is the basis of most combinatorial algorithms.\n\nThere are three patch fragments, one replacing the hash method with the hash of the underlying matrix, one replacing the `__eq__` method, and\none unraveling some unnecessary complexity in the Weyl group action. I tested each patch fragment separately and found that they are all speedups, the last one being very significant.",
    "created_at": "2010-01-01T21:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66666",
    "user": "https://github.com/dwbump"
}
```

I tested this patch without #7753. I tested it with and without the
patch in #7751.

It is a very substantial speedup. It cuts a few 
seconds off `sage -t weyl_groups.py` but more importantly it about doubles the speed of computing the reduced word of a Weyl group element, which is the basis of most combinatorial algorithms.

There are three patch fragments, one replacing the hash method with the hash of the underlying matrix, one replacing the `__eq__` method, and
one unraveling some unnecessary complexity in the Weyl group action. I tested each patch fragment separately and found that they are all speedups, the last one being very significant.



---

archive/issue_comments_066667.json:
```json
{
    "body": "Thanks Dan for the review!",
    "created_at": "2010-01-03T15:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66667",
    "user": "https://github.com/nthiery"
}
```

Thanks Dan for the review!



---

archive/issue_comments_066668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66668",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007966.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-03T21:45:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7754#event-7966"
}
```



---

archive/issue_comments_066669.json:
```json
{
    "body": "Replying to [comment:2 bump]:\n> It is a very substantial speed-up. It cuts a few \n> seconds off `sage -t weyl_groups.py` but more importantly it about doubles the speed of computing the reduced word of a Weyl group element, which is the basis of most combinatorial algorithms.\n\nHi Dan and Nicolas,\n\n\n\nI'm doing a release tour of the features of this ticket, see the [Sage wiki](http://wiki.sagemath.org/ReleaseTours/sage-4.3.1) page. Is there some sample code I could use to show the speed-up implemented by this ticket?",
    "created_at": "2010-01-12T03:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 bump]:
> It is a very substantial speed-up. It cuts a few 
> seconds off `sage -t weyl_groups.py` but more importantly it about doubles the speed of computing the reduced word of a Weyl group element, which is the basis of most combinatorial algorithms.

Hi Dan and Nicolas,



I'm doing a release tour of the features of this ticket, see the [Sage wiki](http://wiki.sagemath.org/ReleaseTours/sage-4.3.1) page. Is there some sample code I could use to show the speed-up implemented by this ticket?



---

archive/issue_comments_066670.json:
```json
{
    "body": "> Hi Dan and Nicolas,\n> \n\n\n> I'm doing a release tour of the features of this ticket, see the [Sage wiki](http://wiki.sagemath.org/ReleaseTours/sage-4.3.1) page. Is there some sample code I could use to show the speed-up implemented by this ticket?\n\nYup, see the updated description!",
    "created_at": "2010-01-12T10:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7754#issuecomment-66670",
    "user": "https://github.com/nthiery"
}
```

> Hi Dan and Nicolas,
> 


> I'm doing a release tour of the features of this ticket, see the [Sage wiki](http://wiki.sagemath.org/ReleaseTours/sage-4.3.1) page. Is there some sample code I could use to show the speed-up implemented by this ticket?

Yup, see the updated description!
