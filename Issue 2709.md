# Issue 2709: add a prime_above() function to NumberField_generic for finding prime ideals above other ideals

archive/issues_002709.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan @craigcitro\n\nKeywords: number field prime above\n\nMy research requires reducing curves over number fields modulo prime ideals, so I need to find suitable prime ideals all the time.  The attached function does exactly that, albeit naively.  I imagine this is useful to more people than me.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2709\n\n",
    "created_at": "2008-03-28T21:24:02Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "add a prime_above() function to NumberField_generic for finding prime ideals above other ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2709",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan @craigcitro

Keywords: number field prime above

My research requires reducing curves over number fields modulo prime ideals, so I need to find suitable prime ideals all the time.  The attached function does exactly that, albeit naively.  I imagine this is useful to more people than me.

Issue created by migration from https://trac.sagemath.org/ticket/2709





---

archive/issue_comments_018643.json:
```json
{
    "body": "Attachment [2709-ncalexan-nf-prime-above-1.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-1.patch) by @ncalexan created at 2008-03-28 21:27:00",
    "created_at": "2008-03-28T21:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18643",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2709-ncalexan-nf-prime-above-1.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-1.patch) by @ncalexan created at 2008-03-28 21:27:00



---

archive/issue_comments_018644.json:
```json
{
    "body": "Craig's ticket request is #2711.",
    "created_at": "2008-03-28T21:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18644",
    "user": "https://github.com/ncalexan"
}
```

Craig's ticket request is #2711.



---

archive/issue_comments_018645.json:
```json
{
    "body": "Replying to [comment:2 ncalexan]:\n> Craig's ticket request is #2711.\n\nThis was posted to the wrong ticket.",
    "created_at": "2008-03-28T22:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18645",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:2 ncalexan]:
> Craig's ticket request is #2711.

This was posted to the wrong ticket.



---

archive/issue_comments_018646.json:
```json
{
    "body": "Attachment [2709-ncalexan-nf-prime-above-2.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-2.patch) by @ncalexan created at 2008-03-28 22:15:26\n\nAfter discussion on IRC, generalized to lists and made to raise an error on individual failure.  Apply both patches -- sorry for the inconvenience, I couldn't figure out how to cut one patch encompassing both changesets.",
    "created_at": "2008-03-28T22:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18646",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2709-ncalexan-nf-prime-above-2.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-2.patch) by @ncalexan created at 2008-03-28 22:15:26

After discussion on IRC, generalized to lists and made to raise an error on individual failure.  Apply both patches -- sorry for the inconvenience, I couldn't figure out how to cut one patch encompassing both changesets.



---

archive/issue_comments_018647.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-29T02:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18647",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018648.json:
```json
{
    "body": "I like it *a lot*.  One small typo: in the docstring for prime_above(), section INPUT, description of the degree, have: \"If one, find a prime...\".  It should be \"If None, find a prime...\"  Of course, one would have to be fairly out of it to be confused by this for too long.\n\nDid I mention that I like it *a lot*?",
    "created_at": "2008-03-29T02:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18648",
    "user": "https://github.com/aghitza"
}
```

I like it *a lot*.  One small typo: in the docstring for prime_above(), section INPUT, description of the degree, have: "If one, find a prime...".  It should be "If None, find a prime..."  Of course, one would have to be fairly out of it to be confused by this for too long.

Did I mention that I like it *a lot*?



---

archive/issue_comments_018649.json:
```json
{
    "body": "Doctests pass for me on sage.math, so I will merge this in Sage 2.11.rc0 :)",
    "created_at": "2008-03-29T14:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18649",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests pass for me on sage.math, so I will merge this in Sage 2.11.rc0 :)



---

archive/issue_comments_018650.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T14:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18650",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018651.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T14:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18651",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002898.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T14:36:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2709#event-2898"
}
```
