# Issue 8666: Bug in cyclotomic linear algebra

archive/issues_008666.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @robertwb\n\nDavid Loeffler ran into this bug:\n\n\n```\nsage: K.<zeta4> = CyclotomicField(4) \nsage: m = matrix(K, [186]) \nsage: n = matrix(K, [125]) \nsage: m * n \n[-23087] \n```\n\n\n(See http://groups.google.com/group/sage-devel/browse_thread/thread/4f8633d6acf1c4ef# for the full thread.)\n\nThe issue is that the bound for what modulus the entries can be computed modulo is off by a factor of 2, because it doesn't take the sign into consideration. (Amusingly, this was basically the same fix as in #4823.) \n\nIssue created by migration from https://trac.sagemath.org/ticket/8666\n\n",
    "created_at": "2010-04-09T22:11:38Z",
    "labels": [
        "component: algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Bug in cyclotomic linear algebra",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8666",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @aghitza

CC:  @robertwb

David Loeffler ran into this bug:


```
sage: K.<zeta4> = CyclotomicField(4) 
sage: m = matrix(K, [186]) 
sage: n = matrix(K, [125]) 
sage: m * n 
[-23087] 
```


(See http://groups.google.com/group/sage-devel/browse_thread/thread/4f8633d6acf1c4ef# for the full thread.)

The issue is that the bound for what modulus the entries can be computed modulo is off by a factor of 2, because it doesn't take the sign into consideration. (Amusingly, this was basically the same fix as in #4823.) 

Issue created by migration from https://trac.sagemath.org/ticket/8666





---

archive/issue_comments_078705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-09T22:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78705",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078706.json:
```json
{
    "body": "Attachment [trac_8666.patch](tarball://root/attachments/some-uuid/ticket8666/trac_8666.patch) by @craigcitro created at 2010-04-09 22:14:23",
    "created_at": "2010-04-09T22:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78706",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_8666.patch](tarball://root/attachments/some-uuid/ticket8666/trac_8666.patch) by @craigcitro created at 2010-04-09 22:14:23



---

archive/issue_comments_078707.json:
```json
{
    "body": "Yep, that should do it.",
    "created_at": "2010-04-09T22:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78707",
    "user": "https://github.com/robertwb"
}
```

Yep, that should do it.



---

archive/issue_comments_078708.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-09T22:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78708",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078709.json:
```json
{
    "body": "This is a duplicate of #8541. Since this already has a patch with positive review, we should close #8541.",
    "created_at": "2010-04-11T12:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78709",
    "user": "https://github.com/burcin"
}
```

This is a duplicate of #8541. Since this already has a patch with positive review, we should close #8541.



---

archive/issue_events_008840.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:41:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8666#event-8840"
}
```



---

archive/issue_comments_078710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78710",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_078711.json:
```json
{
    "body": "Merged trac_8666.patch in 4.4.alpha0.",
    "created_at": "2010-04-16T18:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8666#issuecomment-78711",
    "user": "https://github.com/jhpalmieri"
}
```

Merged trac_8666.patch in 4.4.alpha0.
