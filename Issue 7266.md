# Issue 7266: implement computation of Silverman height bounds

archive/issues_007266.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  robertwb cremona\n\nThe Silverman height bound isn't necessarily as tight at the CPS bound, but it works uniformly over all field extensions, which makes it very useful for some applications, e.g., computing mordell-weil groups over number fields.   So let's add it to Sage!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7266\n\n",
    "created_at": "2009-10-23T03:16:15Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "implement computation of Silverman height bounds",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7266",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  robertwb cremona

The Silverman height bound isn't necessarily as tight at the CPS bound, but it works uniformly over all field extensions, which makes it very useful for some applications, e.g., computing mordell-weil groups over number fields.   So let's add it to Sage!

Issue created by migration from https://trac.sagemath.org/ticket/7266





---

archive/issue_comments_060256.json:
```json
{
    "body": "Attachment [trac_7266.patch](tarball://root/attachments/some-uuid/ticket7266/trac_7266.patch) by @williamstein created at 2009-10-23 06:38:55",
    "created_at": "2009-10-23T06:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60256",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7266.patch](tarball://root/attachments/some-uuid/ticket7266/trac_7266.patch) by @williamstein created at 2009-10-23 06:38:55



---

archive/issue_comments_060257.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T06:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60257",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060258.json:
```json
{
    "body": "Is there any particular reason for using a native Sage implementation instead of using mwrank/eclib?\n\nI know that #360 has still not been done, but I can't quite see the  point of this patch for curves over Q.",
    "created_at": "2009-10-23T20:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60258",
    "user": "https://github.com/JohnCremona"
}
```

Is there any particular reason for using a native Sage implementation instead of using mwrank/eclib?

I know that #360 has still not been done, but I can't quite see the  point of this patch for curves over Q.



---

archive/issue_comments_060259.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-25T06:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60259",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060260.json:
```json
{
    "body": "Looks good to me. It's a simple enough formula that I'd say the redundant implementation is worth it if just for the ease of introspection. \n\nWe're looking at using this for provable computations of Heegner points, where the field of definition is not a priori known.",
    "created_at": "2009-10-25T06:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60260",
    "user": "https://github.com/robertwb"
}
```

Looks good to me. It's a simple enough formula that I'd say the redundant implementation is worth it if just for the ease of introspection. 

We're looking at using this for provable computations of Heegner points, where the field of definition is not a priori known.



---

archive/issue_comments_060261.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> Looks good to me. It's a simple enough formula that I'd say the redundant implementation is worth it if just for the ease of introspection. \n> \n> We're looking at using this for provable computations of Heegner points, where the field of definition is not a priori known. \n\nFair point(s).  One reason for getting better (usually) bounds for *rational* points via the CPS method is precisely due to this restriction.  I have no objection!",
    "created_at": "2009-10-25T14:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60261",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 robertwb]:
> Looks good to me. It's a simple enough formula that I'd say the redundant implementation is worth it if just for the ease of introspection. 
> 
> We're looking at using this for provable computations of Heegner points, where the field of definition is not a priori known. 

Fair point(s).  One reason for getting better (usually) bounds for *rational* points via the CPS method is precisely due to this restriction.  I have no objection!



---

archive/issue_events_007487.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T15:48:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7266#event-7487"
}
```



---

archive/issue_comments_060262.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60262",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060263.json:
```json
{
    "body": "But I read here that the Sage project \"religiously avoiding redundant code.\": http://www.metafilter.com/86262/unbump",
    "created_at": "2009-10-31T21:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7266#issuecomment-60263",
    "user": "https://github.com/williamstein"
}
```

But I read here that the Sage project "religiously avoiding redundant code.": http://www.metafilter.com/86262/unbump
