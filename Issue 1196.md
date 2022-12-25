# Issue 1196: inefficiency and inconsistency in calculus numerical conversion

archive/issues_001196.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n> David Harvey did mention to\n> me that getting a numerical approximation of sqrt(2) called maxima, so\n\nThat's not exactly true, since \"Exiting Maxima...\" is not printed out below:\n\nsage: float(sqrt(2))\n1.4142135623730951\nsage: quit\nExiting SAGE (CPU time 0m0.01s, Wall time 0m5.91s).\n\nWhat happens is that if one requests a numerical *float* approximation\nto sqrt(2), then first a float approximation to 2 is computed, then\nthe math.sqrt method is called on it.  \n\nUnfortunately, evidently right now if one requests a high-precision\nnumerical approximation Sage currently does\nend up calling Maxima:\n\n\nsage: RealField(100) ( sqrt(2) )\n1.4142135623730950488016887242\nsage: \nExiting spawned Maxima process.\n\nI consider this a mistake in implementation, which should be optimized. \n\nNotice that\n\nsage: sqrt( RealField(100)(2) )\n1.4142135623730950488016887242\n\ndoes not call Maxima anywhere. \n\nI just investigated, and n(sqrt(2), 100) calls maxima only to simplify\nsqrt(2) before even beginning to do any numerical approximation. \nThis isn't consistent with how the other coercions (e.g., to float) work.   So I've posted\na patch that changes this behavior.  After applying this patch:\n\nsage: RealField(100) ( sqrt(2) )\n1.4142135623730950488016887242\nsage: quit\n(no \"exiting maxima\") \n```\n\n\nNOTE: I've attached two patches.  The first implements the change described above.\nThe second fixes some resulting doctest failures, and also optimizes computation\nof sec, csc, and cot for mpfr elements. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1196\n\n",
    "created_at": "2007-11-18T04:14:40Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "inefficiency and inconsistency in calculus numerical conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1196",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
> David Harvey did mention to
> me that getting a numerical approximation of sqrt(2) called maxima, so

That's not exactly true, since "Exiting Maxima..." is not printed out below:

sage: float(sqrt(2))
1.4142135623730951
sage: quit
Exiting SAGE (CPU time 0m0.01s, Wall time 0m5.91s).

What happens is that if one requests a numerical *float* approximation
to sqrt(2), then first a float approximation to 2 is computed, then
the math.sqrt method is called on it.  

Unfortunately, evidently right now if one requests a high-precision
numerical approximation Sage currently does
end up calling Maxima:


sage: RealField(100) ( sqrt(2) )
1.4142135623730950488016887242
sage: 
Exiting spawned Maxima process.

I consider this a mistake in implementation, which should be optimized. 

Notice that

sage: sqrt( RealField(100)(2) )
1.4142135623730950488016887242

does not call Maxima anywhere. 

I just investigated, and n(sqrt(2), 100) calls maxima only to simplify
sqrt(2) before even beginning to do any numerical approximation. 
This isn't consistent with how the other coercions (e.g., to float) work.   So I've posted
a patch that changes this behavior.  After applying this patch:

sage: RealField(100) ( sqrt(2) )
1.4142135623730950488016887242
sage: quit
(no "exiting maxima") 
```


NOTE: I've attached two patches.  The first implements the change described above.
The second fixes some resulting doctest failures, and also optimizes computation
of sec, csc, and cot for mpfr elements. 


Issue created by migration from https://trac.sagemath.org/ticket/1196





---

archive/issue_comments_007398.json:
```json
{
    "body": "Attachment [7330.patch](tarball://root/attachments/some-uuid/ticket1196/7330.patch) by @williamstein created at 2007-11-18 04:15:01\n\npatch 1 of 2",
    "created_at": "2007-11-18T04:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1196#issuecomment-7398",
    "user": "https://github.com/williamstein"
}
```

Attachment [7330.patch](tarball://root/attachments/some-uuid/ticket1196/7330.patch) by @williamstein created at 2007-11-18 04:15:01

patch 1 of 2



---

archive/issue_comments_007399.json:
```json
{
    "body": "patch 2 of 2",
    "created_at": "2007-11-18T04:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1196#issuecomment-7399",
    "user": "https://github.com/williamstein"
}
```

patch 2 of 2



---

archive/issue_comments_007400.json:
```json
{
    "body": "Attachment [7332.patch](tarball://root/attachments/some-uuid/ticket1196/7332.patch) by @williamstein created at 2007-11-18 04:15:57",
    "created_at": "2007-11-18T04:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1196#issuecomment-7400",
    "user": "https://github.com/williamstein"
}
```

Attachment [7332.patch](tarball://root/attachments/some-uuid/ticket1196/7332.patch) by @williamstein created at 2007-11-18 04:15:57



---

archive/issue_events_003195.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-18T04:15:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1196#event-3195"
}
```



---

archive/issue_comments_007401.json:
```json
{
    "body": "Merged in 2.8.13.rc1.",
    "created_at": "2007-11-20T15:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1196#issuecomment-7401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.rc1.



---

archive/issue_events_003196.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-20T15:50:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1196#event-3196"
}
```



---

archive/issue_comments_007402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-20T15:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1196#issuecomment-7402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
