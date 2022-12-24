# Issue 2709: add a prime_above() function to NumberField_generic for finding prime ideals above other ideals

archive/issues_002709.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan craigcitro\n\nKeywords: number field prime above\n\nMy research requires reducing curves over number fields modulo prime ideals, so I need to find suitable prime ideals all the time.  The attached function does exactly that, albeit naively.  I imagine this is useful to more people than me.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2709\n\n",
    "created_at": "2008-03-28T21:24:02Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "add a prime_above() function to NumberField_generic for finding prime ideals above other ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2709",
    "user": "ncalexan"
}
```
Assignee: was

CC:  ncalexan craigcitro

Keywords: number field prime above

My research requires reducing curves over number fields modulo prime ideals, so I need to find suitable prime ideals all the time.  The attached function does exactly that, albeit naively.  I imagine this is useful to more people than me.

Issue created by migration from https://trac.sagemath.org/ticket/2709





---

archive/issue_comments_018682.json:
```json
{
    "body": "Attachment [2709-ncalexan-nf-prime-above-1.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-1.patch) by ncalexan created at 2008-03-28 21:27:00",
    "created_at": "2008-03-28T21:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18682",
    "user": "ncalexan"
}
```

Attachment [2709-ncalexan-nf-prime-above-1.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-1.patch) by ncalexan created at 2008-03-28 21:27:00



---

archive/issue_comments_018683.json:
```json
{
    "body": "Craig's ticket request is #2711.",
    "created_at": "2008-03-28T21:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18683",
    "user": "ncalexan"
}
```

Craig's ticket request is #2711.



---

archive/issue_comments_018684.json:
```json
{
    "body": "Replying to [comment:2 ncalexan]:\n> Craig's ticket request is #2711.\n\nThis was posted to the wrong ticket.",
    "created_at": "2008-03-28T22:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18684",
    "user": "ncalexan"
}
```

Replying to [comment:2 ncalexan]:
> Craig's ticket request is #2711.

This was posted to the wrong ticket.



---

archive/issue_comments_018685.json:
```json
{
    "body": "Attachment [2709-ncalexan-nf-prime-above-2.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-2.patch) by ncalexan created at 2008-03-28 22:15:26\n\nAfter discussion on IRC, generalized to lists and made to raise an error on individual failure.  Apply both patches -- sorry for the inconvenience, I couldn't figure out how to cut one patch encompassing both changesets.",
    "created_at": "2008-03-28T22:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18685",
    "user": "ncalexan"
}
```

Attachment [2709-ncalexan-nf-prime-above-2.patch](tarball://root/attachments/some-uuid/ticket2709/2709-ncalexan-nf-prime-above-2.patch) by ncalexan created at 2008-03-28 22:15:26

After discussion on IRC, generalized to lists and made to raise an error on individual failure.  Apply both patches -- sorry for the inconvenience, I couldn't figure out how to cut one patch encompassing both changesets.



---

archive/issue_comments_018686.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-29T02:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18686",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018687.json:
```json
{
    "body": "I like it *a lot*.  One small typo: in the docstring for prime_above(), section INPUT, description of the degree, have: \"If one, find a prime...\".  It should be \"If None, find a prime...\"  Of course, one would have to be fairly out of it to be confused by this for too long.\n\nDid I mention that I like it *a lot*?",
    "created_at": "2008-03-29T02:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18687",
    "user": "AlexGhitza"
}
```

I like it *a lot*.  One small typo: in the docstring for prime_above(), section INPUT, description of the degree, have: "If one, find a prime...".  It should be "If None, find a prime..."  Of course, one would have to be fairly out of it to be confused by this for too long.

Did I mention that I like it *a lot*?



---

archive/issue_comments_018688.json:
```json
{
    "body": "Doctests pass for me on sage.math, so I will merge this in Sage 2.11.rc0 :)",
    "created_at": "2008-03-29T14:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18688",
    "user": "mabshoff"
}
```

Doctests pass for me on sage.math, so I will merge this in Sage 2.11.rc0 :)



---

archive/issue_comments_018689.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T14:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18689",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T14:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2709#issuecomment-18690",
    "user": "mabshoff"
}
```

Resolution: fixed
