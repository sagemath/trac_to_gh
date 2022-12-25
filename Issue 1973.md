# Issue 1973: native partition_associated function

archive/issues_001973.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nThis patch replaces the wrapper around Gap to give the conjugate partition.  It speeds up the computation quite a bit.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1973\n\n",
    "created_at": "2008-01-29T16:13:05Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "native partition_associated function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1973",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

CC:  sage-combinat

This patch replaces the wrapper around Gap to give the conjugate partition.  It speeds up the computation quite a bit.


Issue created by migration from https://trac.sagemath.org/ticket/1973





---

archive/issue_comments_012739.json:
```json
{
    "body": "Attachment [conjugate-partition.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.patch) by mabshoff created at 2008-01-29 16:21:35",
    "created_at": "2008-01-29T16:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12739",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [conjugate-partition.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.patch) by mabshoff created at 2008-01-29 16:21:35



---

archive/issue_comments_012740.json:
```json
{
    "body": "I'd say it's an improvement, but it may be better to avoid code duplication with the following:\n\n\n```\nsage: Partition([3,1]).conjugate()\n[2, 1, 1]\n```\n",
    "created_at": "2008-01-29T17:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12740",
    "user": "https://github.com/mwhansen"
}
```

I'd say it's an improvement, but it may be better to avoid code duplication with the following:


```
sage: Partition([3,1]).conjugate()
[2, 1, 1]
```




---

archive/issue_comments_012741.json:
```json
{
    "body": "With the patch:\n\n\n```\nsage: %timeit partition_associated([6,5,5,4,2,2,1])\n100000 loops, best of 3: 9.21 \u00b5s per loop\nsage: %timeit Partition([6,5,5,4,2,2,1]).conjugate()\n10000 loops, best of 3: 154 \u00b5s per loop\nsage: a=Partition([6,5,5,4,2,2,1])\nsage: %timeit a.conjugate()\n1000 loops, best of 3: 268 \u00b5s per loop\n```\n\n\nSo I'll probably delete the partition_associated function and replace the Partition.conjugate() function, if that's all right, and post up another patch.",
    "created_at": "2008-01-29T18:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12741",
    "user": "https://github.com/jasongrout"
}
```

With the patch:


```
sage: %timeit partition_associated([6,5,5,4,2,2,1])
100000 loops, best of 3: 9.21 µs per loop
sage: %timeit Partition([6,5,5,4,2,2,1]).conjugate()
10000 loops, best of 3: 154 µs per loop
sage: a=Partition([6,5,5,4,2,2,1])
sage: %timeit a.conjugate()
1000 loops, best of 3: 268 µs per loop
```


So I'll probably delete the partition_associated function and replace the Partition.conjugate() function, if that's all right, and post up another patch.



---

archive/issue_comments_012742.json:
```json
{
    "body": "Well, the resason partition_associated is still there is for backward compatibility reasons.  I would make it so that partition_associated returns list(Partition(p).conjugate()). \n\n\nYou can modify Partition_class.conjugate, but make sure you return Partition_class objects.  Within the function, you can eliminate some overhead by replacing \"return Partition...\" with \"return Partition_class...\" since Partition is a wrapper function which does type-checking, etc.",
    "created_at": "2008-01-29T19:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12742",
    "user": "https://github.com/mwhansen"
}
```

Well, the resason partition_associated is still there is for backward compatibility reasons.  I would make it so that partition_associated returns list(Partition(p).conjugate()). 


You can modify Partition_class.conjugate, but make sure you return Partition_class objects.  Within the function, you can eliminate some overhead by replacing "return Partition..." with "return Partition_class..." since Partition is a wrapper function which does type-checking, etc.



---

archive/issue_comments_012743.json:
```json
{
    "body": "Some timings after I put my code into partition.py:\n\n\n```\n[15:42] <jason-> sage: a=Partition(sum([[i]*20 for i in range(50,1,-1)],[]))\n[15:42] <jason-> sage: print len(a), len(a.conjugate('mike'))\n[15:42] <jason-> 980 50\n[15:42] <jason-> sage: %timeit a.conjugate('jason')\n[15:42] <jason-> 100 loops, best of 3: 3.34 ms per loop\n[15:42] <jason-> sage: %timeit a.conjugate('mike')\n[15:42] <jason-> 100 loops, best of 3: 3.25 ms per loop\n[15:42] <jason-> sage: %timeit a.conjugate('mikeandjason')\n[15:42] <jason-> 100 loops, best of 3: 3.05 ms per loop\n[15:42] <jason-> sage: a=Partition(sum([[i]*2 for i in range(5000,1,-1)],[]))\n[15:42] <jason-> sage: print len(a), len(a.conjugate('mike'))\n[15:42] <jason-> 9998 5000\n[15:42] <jason-> sage: %timeit a.conjugate('jason')\n[15:42] <jason-> 10 loops, best of 3: 246 ms per loop\n[15:42] <jason-> sage: %timeit a.conjugate('mike')\n[15:42] <jason-> 10 loops, best of 3: 34.8 ms per loop\n[15:42] <jason-> sage: %timeit a.conjugate('mikeandjason')\n[15:42] <jason-> 10 loops, best of 3: 32.4 ms per loop\n[15:42] <jason-> we both win this time.\n[15:42] <jason-> 'mikeandjason' is making a few slight modifications to your algorithm (like using .extend instead of +=, etc.)\n```\n\n\nSo I'll post a minor patch to Mike's code.",
    "created_at": "2008-01-29T21:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12743",
    "user": "https://github.com/jasongrout"
}
```

Some timings after I put my code into partition.py:


```
[15:42] <jason-> sage: a=Partition(sum([[i]*20 for i in range(50,1,-1)],[]))
[15:42] <jason-> sage: print len(a), len(a.conjugate('mike'))
[15:42] <jason-> 980 50
[15:42] <jason-> sage: %timeit a.conjugate('jason')
[15:42] <jason-> 100 loops, best of 3: 3.34 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mike')
[15:42] <jason-> 100 loops, best of 3: 3.25 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mikeandjason')
[15:42] <jason-> 100 loops, best of 3: 3.05 ms per loop
[15:42] <jason-> sage: a=Partition(sum([[i]*2 for i in range(5000,1,-1)],[]))
[15:42] <jason-> sage: print len(a), len(a.conjugate('mike'))
[15:42] <jason-> 9998 5000
[15:42] <jason-> sage: %timeit a.conjugate('jason')
[15:42] <jason-> 10 loops, best of 3: 246 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mike')
[15:42] <jason-> 10 loops, best of 3: 34.8 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mikeandjason')
[15:42] <jason-> 10 loops, best of 3: 32.4 ms per loop
[15:42] <jason-> we both win this time.
[15:42] <jason-> 'mikeandjason' is making a few slight modifications to your algorithm (like using .extend instead of +=, etc.)
```


So I'll post a minor patch to Mike's code.



---

archive/issue_comments_012744.json:
```json
{
    "body": "Attachment [conjugate-partition.2.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.2.patch) by @jasongrout created at 2008-01-29 22:00:45\n\napply instead of first patch.",
    "created_at": "2008-01-29T22:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12744",
    "user": "https://github.com/jasongrout"
}
```

Attachment [conjugate-partition.2.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.2.patch) by @jasongrout created at 2008-01-29 22:00:45

apply instead of first patch.



---

archive/issue_comments_012745.json:
```json
{
    "body": "apply instead of first two patches.",
    "created_at": "2008-01-29T22:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12745",
    "user": "https://github.com/jasongrout"
}
```

apply instead of first two patches.



---

archive/issue_comments_012746.json:
```json
{
    "body": "Attachment [conjugate-partition.3.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.3.patch) by @jasongrout created at 2008-01-29 22:17:05\n\nYet again, apply this instead of the previous patches.",
    "created_at": "2008-01-29T22:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12746",
    "user": "https://github.com/jasongrout"
}
```

Attachment [conjugate-partition.3.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.3.patch) by @jasongrout created at 2008-01-29 22:17:05

Yet again, apply this instead of the previous patches.



---

archive/issue_comments_012747.json:
```json
{
    "body": "Attachment [conjugate-partition.4.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.4.patch) by @mwhansen created at 2008-01-29 22:18:28\n\nLooks good to me.",
    "created_at": "2008-01-29T22:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12747",
    "user": "https://github.com/mwhansen"
}
```

Attachment [conjugate-partition.4.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.4.patch) by @mwhansen created at 2008-01-29 22:18:28

Looks good to me.



---

archive/issue_comments_012748.json:
```json
{
    "body": "Merged conjugate-partition.4.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T02:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12748",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged conjugate-partition.4.patch in Sage 2.10.1.rc3



---

archive/issue_events_004771.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-30T02:51:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1973#event-4771"
}
```



---

archive/issue_comments_012749.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T02:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12749",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012750.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-01-30T04:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_012751.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-01-30T04:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12751",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004772.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-30T04:07:09Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1973#event-4772"
}
```



---

archive/issue_comments_012752.json:
```json
{
    "body": "The following is probably trivial to fix:\n\n```\n\nException exceptions.ImportError: 'cannot import name is_FractionFieldElement' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n```\n\nbut it happens after a `sage -ba`\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T04:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12752",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The following is probably trivial to fix:

```

Exception exceptions.ImportError: 'cannot import name is_FractionFieldElement' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)
```

but it happens after a `sage -ba`

Cheers,

Michael



---

archive/issue_comments_012753.json:
```json
{
    "body": "Reverted for good. Somebody needs to revisit this with 2.10.1.rc3 or later.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T08:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Reverted for good. Somebody needs to revisit this with 2.10.1.rc3 or later.

Cheers,

Michael



---

archive/issue_comments_012754.json:
```json
{
    "body": "The error apparently has to do with the top-level import in combinat.py:\n\n    from sage.combinat.partition import Partition\n\nWhen I move the top-level import into the associated_partition function, the failing doctest passes.\n\nMike, do you know what is going on?",
    "created_at": "2008-01-30T16:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12754",
    "user": "https://github.com/jasongrout"
}
```

The error apparently has to do with the top-level import in combinat.py:

    from sage.combinat.partition import Partition

When I move the top-level import into the associated_partition function, the failing doctest passes.

Mike, do you know what is going on?



---

archive/issue_comments_012755.json:
```json
{
    "body": "Attachment [conjugate-partition.5.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.5.patch) by @mwhansen created at 2008-01-31 06:35:15\n\nI posted a new patch which should take care of this issue (although I never experienced the -ba issue on my machine).",
    "created_at": "2008-01-31T06:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12755",
    "user": "https://github.com/mwhansen"
}
```

Attachment [conjugate-partition.5.patch](tarball://root/attachments/some-uuid/ticket1973/conjugate-partition.5.patch) by @mwhansen created at 2008-01-31 06:35:15

I posted a new patch which should take care of this issue (although I never experienced the -ba issue on my machine).



---

archive/issue_comments_012756.json:
```json
{
    "body": "Attachment [1973.patch](tarball://root/attachments/some-uuid/ticket1973/1973.patch) by @mwhansen created at 2008-02-01 04:19:42",
    "created_at": "2008-02-01T04:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12756",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1973.patch](tarball://root/attachments/some-uuid/ticket1973/1973.patch) by @mwhansen created at 2008-02-01 04:19:42



---

archive/issue_comments_012757.json:
```json
{
    "body": "Merged 1973.patch in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T04:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1973.patch in Sage 2.10.1.rc4



---

archive/issue_comments_012758.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T04:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004773.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-01T04:24:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1973#event-4773"
}
```



---

archive/issue_comments_012759.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-01T04:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1973#issuecomment-12759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael
