# Issue 9749: huge performance regression in computing with level one modular forms

archive/issues_009749.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  alexghitza @craigcitro\n\nI was working on the Ribet-Stein book, and a computation that is trivial in Magma, and must have been trivial in Sage until recently is now impossibly hard.\n\n\n```\nsage: M = ModularForms(1,512)\nsage: time M.hecke_matrix(5)\n[[takes a very, very long time indeed.]]\n```\n\nThis is very sad, since M has dimension only 43. Also, it is easy to get the answer directly --from start to finish in less than a second! -- as follows:\n\n```\nsage: time B = victor_miller_basis(512,5*43+1)\nCPU times: user 0.21 s, sys: 0.00 s, total: 0.21 s\nWall time: 0.21 s\nsage: time t5 = hecke_operator_on_basis(B, 5, 512)\nCPU times: user 0.61 s, sys: 0.00 s, total: 0.61 s\nWall time: 0.61 s\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9749\n\n",
    "created_at": "2010-08-14T19:06:36Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "huge performance regression in computing with level one modular forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9749",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

CC:  alexghitza @craigcitro

I was working on the Ribet-Stein book, and a computation that is trivial in Magma, and must have been trivial in Sage until recently is now impossibly hard.


```
sage: M = ModularForms(1,512)
sage: time M.hecke_matrix(5)
[[takes a very, very long time indeed.]]
```

This is very sad, since M has dimension only 43. Also, it is easy to get the answer directly --from start to finish in less than a second! -- as follows:

```
sage: time B = victor_miller_basis(512,5*43+1)
CPU times: user 0.21 s, sys: 0.00 s, total: 0.21 s
Wall time: 0.21 s
sage: time t5 = hecke_operator_on_basis(B, 5, 512)
CPU times: user 0.61 s, sys: 0.00 s, total: 0.61 s
Wall time: 0.61 s
```



Issue created by migration from https://trac.sagemath.org/ticket/9749





---

archive/issue_comments_095314.json:
```json
{
    "body": "Attachment [trac_9749.patch](tarball://root/attachments/some-uuid/ticket9749/trac_9749.patch) by @aghitza created at 2010-08-31 08:55:52",
    "created_at": "2010-08-31T08:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95314",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_9749.patch](tarball://root/attachments/some-uuid/ticket9749/trac_9749.patch) by @aghitza created at 2010-08-31 08:55:52



---

archive/issue_comments_095315.json:
```json
{
    "body": "The attached patch makes ambient spaces of level 1 modular forms use the Victor Miller basis for Hecke matrix computations.",
    "created_at": "2010-08-31T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95315",
    "user": "https://github.com/aghitza"
}
```

The attached patch makes ambient spaces of level 1 modular forms use the Victor Miller basis for Hecke matrix computations.



---

archive/issue_comments_095316.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-31T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95316",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095317.json:
```json
{
    "body": "Positive review.  Note -- I made a new patch that fixes a typo: \"Endusers\" --> \"End users\".",
    "created_at": "2010-09-07T17:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95317",
    "user": "https://github.com/williamstein"
}
```

Positive review.  Note -- I made a new patch that fixes a typo: "Endusers" --> "End users".



---

archive/issue_comments_095318.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-07T17:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95318",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095319.json:
```json
{
    "body": "apply this one only.",
    "created_at": "2010-09-07T17:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95319",
    "user": "https://github.com/williamstein"
}
```

apply this one only.



---

archive/issue_events_009881.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T10:39:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9749#event-9881"
}
```



---

archive/issue_comments_095320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95320",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_095321.json:
```json
{
    "body": "Attachment [trac_9749.2.patch](tarball://root/attachments/some-uuid/ticket9749/trac_9749.2.patch) by @qed777 created at 2010-09-15 10:39:46",
    "created_at": "2010-09-15T10:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9749#issuecomment-95321",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9749.2.patch](tarball://root/attachments/some-uuid/ticket9749/trac_9749.2.patch) by @qed777 created at 2010-09-15 10:39:46
