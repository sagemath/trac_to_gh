# Issue 5236: x^(-pm) in ramified extensions of Qp

archive/issues_005236.json:
```json
{
    "body": "Assignee: @roed314\n\nThis is probably a problem with some of the shifting code in pow_computer_ext, since it only occurs when raising an element to a power that's a negative multiple of p.  pow_computer_ext needs cleaning up and doctesting anyway.\n\n```\nsage: W.<w> = Qp(5,6).ext(x^2+5)\nsage: (5+w)^-4\nw^-4 + 4*w^-3 + 3 + 2*w + 3*w^2 + 3*w^5 + w^6 + O(w^8)\nsage: (5+w)^-5\nRuntimeError: ZZ_p: division by non-invertible element\nsage: W(5)^-5\n4*w^-10 + w^-8 + O(w^2)\nsage: w^-5\nw^-5 + O(w^7)\nsage: (1+w)^-5\nRuntimeError: ZZ_p: division by non-invertible element\nsage: (1+w)^5\n1 + 4*w^3 + 3*w^4 + O(w^12)\nsage: (1+w)^-7\n1 + 3*w + 3*w^2 + 3*w^3 + 3*w^6 + 3*w^7 + 2*w^8 + w^9 + 3*w^10 + O(w^12)\nsage: (1+w)^-10\nRuntimeError: ZZ_p: division by non-invertible element\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5236\n\n",
    "created_at": "2009-02-11T21:46:13Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "x^(-pm) in ramified extensions of Qp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5236",
    "user": "https://github.com/roed314"
}
```
Assignee: @roed314

This is probably a problem with some of the shifting code in pow_computer_ext, since it only occurs when raising an element to a power that's a negative multiple of p.  pow_computer_ext needs cleaning up and doctesting anyway.

```
sage: W.<w> = Qp(5,6).ext(x^2+5)
sage: (5+w)^-4
w^-4 + 4*w^-3 + 3 + 2*w + 3*w^2 + 3*w^5 + w^6 + O(w^8)
sage: (5+w)^-5
RuntimeError: ZZ_p: division by non-invertible element
sage: W(5)^-5
4*w^-10 + w^-8 + O(w^2)
sage: w^-5
w^-5 + O(w^7)
sage: (1+w)^-5
RuntimeError: ZZ_p: division by non-invertible element
sage: (1+w)^5
1 + 4*w^3 + 3*w^4 + O(w^12)
sage: (1+w)^-7
1 + 3*w + 3*w^2 + 3*w^3 + 3*w^6 + 3*w^7 + 2*w^8 + w^9 + 3*w^10 + O(w^12)
sage: (1+w)^-10
RuntimeError: ZZ_p: division by non-invertible element
```


Issue created by migration from https://trac.sagemath.org/ticket/5236





---

archive/issue_comments_040042.json:
```json
{
    "body": "Changing keywords from \"\" to \"padics, exponentiation\".",
    "created_at": "2009-02-11T21:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40042",
    "user": "https://github.com/roed314"
}
```

Changing keywords from "" to "padics, exponentiation".



---

archive/issue_comments_040043.json:
```json
{
    "body": "The problem is just in the exponentiation code.  I need to use my own newton's method inverse (in ntl_wrap.cpp) rather than NTL's InvMod.  A bit annoying: I don't really know what the relative speeds are.  But it should produce the correct answer at least.",
    "created_at": "2009-02-13T05:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40043",
    "user": "https://github.com/roed314"
}
```

The problem is just in the exponentiation code.  I need to use my own newton's method inverse (in ntl_wrap.cpp) rather than NTL's InvMod.  A bit annoying: I don't really know what the relative speeds are.  But it should produce the correct answer at least.



---

archive/issue_comments_040044.json:
```json
{
    "body": "Looks good, applies against 3.4, passes doctests, and withstands some additional poking. Positive review.",
    "created_at": "2009-03-17T03:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40044",
    "user": "https://github.com/kedlaya"
}
```

Looks good, applies against 3.4, passes doctests, and withstands some additional poking. Positive review.



---

archive/issue_comments_040045.json:
```json
{
    "body": "I found another case of this, for capped absolute extensions.",
    "created_at": "2009-03-17T09:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40045",
    "user": "https://github.com/roed314"
}
```

I found another case of this, for capped absolute extensions.



---

archive/issue_comments_040046.json:
```json
{
    "body": "Rebased against 5778.",
    "created_at": "2009-04-25T07:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40046",
    "user": "https://github.com/roed314"
}
```

Rebased against 5778.



---

archive/issue_comments_040047.json:
```json
{
    "body": "Attachment [trac5236.patch](tarball://root/attachments/some-uuid/ticket5236/trac5236.patch) by @roed314 created at 2009-04-25 07:51:38",
    "created_at": "2009-04-25T07:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40047",
    "user": "https://github.com/roed314"
}
```

Attachment [trac5236.patch](tarball://root/attachments/some-uuid/ticket5236/trac5236.patch) by @roed314 created at 2009-04-25 07:51:38



---

archive/issue_comments_040048.json:
```json
{
    "body": "Changing component from basic arithmetic to padics.",
    "created_at": "2009-04-26T19:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from basic arithmetic to padics.



---

archive/issue_comments_040049.json:
```json
{
    "body": "Includes commit message, rebased against 3.4.2 and #5778.",
    "created_at": "2009-05-11T09:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40049",
    "user": "https://github.com/roed314"
}
```

Includes commit message, rebased against 3.4.2 and #5778.



---

archive/issue_comments_040050.json:
```json
{
    "body": "Attachment [trac5236.2.patch](tarball://root/attachments/some-uuid/ticket5236/trac5236.2.patch) by @kedlaya created at 2009-05-19 16:07:43\n\nApplies against 4.0alpha0, passes all doctests, looks reasonable to me. Positive review.",
    "created_at": "2009-05-19T16:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40050",
    "user": "https://github.com/kedlaya"
}
```

Attachment [trac5236.2.patch](tarball://root/attachments/some-uuid/ticket5236/trac5236.2.patch) by @kedlaya created at 2009-05-19 16:07:43

Applies against 4.0alpha0, passes all doctests, looks reasonable to me. Positive review.



---

archive/issue_events_005492.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T17:00:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5236#event-5492"
}
```



---

archive/issue_comments_040051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T17:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40051",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040052.json:
```json
{
    "body": "Merged trac5236.2.patch in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T17:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5236#issuecomment-40052",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac5236.2.patch in Sage 4.0.rc0.

Cheers,

Michael
