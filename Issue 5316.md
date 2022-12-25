# Issue 5316: some elements of NumberField_quadratic are NumberFieldElement_absolute --> segfault

archive/issues_005316.json:
```json
{
    "body": "Assignee: cwitty\n\nBased on a question from Alex Raichev (http://groups.google.com/group/sage-support/browse_thread/thread/71483789bc7fefb7#), I discovered this:\n\n```\nsage: var('t')\nt\nsage: F = NumberField(t^2+1, 'a')\nsage: R.<x,y> = F[]\nsage: type(x.coefficients()[0])\n<type 'sage.rings.number_field.number_field_element.NumberFieldElement_absolute'>\nsage: F(1) + x.coefficients()[0]\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5316\n\n",
    "created_at": "2009-02-20T06:15:51Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "some elements of NumberField_quadratic are NumberFieldElement_absolute --> segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5316",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

Based on a question from Alex Raichev (http://groups.google.com/group/sage-support/browse_thread/thread/71483789bc7fefb7#), I discovered this:

```
sage: var('t')
t
sage: F = NumberField(t^2+1, 'a')
sage: R.<x,y> = F[]
sage: type(x.coefficients()[0])
<type 'sage.rings.number_field.number_field_element.NumberFieldElement_absolute'>
sage: F(1) + x.coefficients()[0]


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

Issue created by migration from https://trac.sagemath.org/ticket/5316





---

archive/issue_comments_040862.json:
```json
{
    "body": "Attachment [trac5316-nf-quadratic-elements.patch](tarball://root/attachments/some-uuid/ticket5316/trac5316-nf-quadratic-elements.patch) by cwitty created at 2009-02-20 07:03:23",
    "created_at": "2009-02-20T07:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5316#issuecomment-40862",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac5316-nf-quadratic-elements.patch](tarball://root/attachments/some-uuid/ticket5316/trac5316-nf-quadratic-elements.patch) by cwitty created at 2009-02-20 07:03:23



---

archive/issue_comments_040863.json:
```json
{
    "body": "The attached patch fixes the crash (and also fixes Alex's original problem.)  All doctests pass.",
    "created_at": "2009-02-20T07:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5316#issuecomment-40863",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The attached patch fixes the crash (and also fixes Alex's original problem.)  All doctests pass.



---

archive/issue_comments_040864.json:
```json
{
    "body": "If this passes doctests then I give it a positive review.",
    "created_at": "2009-02-20T07:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5316#issuecomment-40864",
    "user": "https://github.com/williamstein"
}
```

If this passes doctests then I give it a positive review.



---

archive/issue_comments_040865.json:
```json
{
    "body": "Positive review via William's review since all doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5316#issuecomment-40865",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review via William's review since all doctests pass.

Cheers,

Michael



---

archive/issue_comments_040866.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T07:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5316#issuecomment-40866",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040867.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5316#issuecomment-40867",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_events_012381.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T07:58:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5316",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5316#event-12381"
}
```
