# Issue 1494: bug coercing from maximal order of cyclotomic field into cyclotomic field

archive/issues_001494.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: K.<z> = CyclotomicField(7)\nsage: O = K.maximal_order()\nsage: K(O.1)\nTraceback (most recent call last):\n...\nTypeError: Cannot coerce element into this number field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1494\n\n",
    "created_at": "2007-12-13T22:08:23Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "bug coercing from maximal order of cyclotomic field into cyclotomic field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1494",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
sage: K.<z> = CyclotomicField(7)
sage: O = K.maximal_order()
sage: K(O.1)
Traceback (most recent call last):
...
TypeError: Cannot coerce element into this number field
```


Issue created by migration from https://trac.sagemath.org/ticket/1494





---

archive/issue_comments_009573.json:
```json
{
    "body": "Attachment [trac-1494.patch](tarball://root/attachments/some-uuid/ticket1494/trac-1494.patch) by @williamstein created at 2007-12-13 22:15:50",
    "created_at": "2007-12-13T22:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9573",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1494.patch](tarball://root/attachments/some-uuid/ticket1494/trac-1494.patch) by @williamstein created at 2007-12-13 22:15:50



---

archive/issue_comments_009574.json:
```json
{
    "body": "I am wary of this patch, but will look into it more.",
    "created_at": "2007-12-15T07:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9574",
    "user": "https://github.com/robertwb"
}
```

I am wary of this patch, but will look into it more.



---

archive/issue_comments_009575.json:
```json
{
    "body": "Attachment [trac-1494-fixdoctest.patch](tarball://root/attachments/some-uuid/ticket1494/trac-1494-fixdoctest.patch) by cwitty created at 2007-12-15 08:16:56",
    "created_at": "2007-12-15T08:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9575",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-1494-fixdoctest.patch](tarball://root/attachments/some-uuid/ticket1494/trac-1494-fixdoctest.patch) by cwitty created at 2007-12-15 08:16:56



---

archive/issue_comments_009576.json:
```json
{
    "body": "Looks OK to me.  The new doctest passes (after applying the trivial patch in trac-1494-fixdoctest.patch).",
    "created_at": "2007-12-15T08:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9576",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks OK to me.  The new doctest passes (after applying the trivial patch in trac-1494-fixdoctest.patch).



---

archive/issue_comments_009577.json:
```json
{
    "body": "I was worried if there was some special reason we were calling _coerce_from_other_number_field here previously, but it looks OK. \n\nThis will probably be revised when coercion is flushed throughout the system anyways.",
    "created_at": "2007-12-15T08:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9577",
    "user": "https://github.com/robertwb"
}
```

I was worried if there was some special reason we were calling _coerce_from_other_number_field here previously, but it looks OK. 

This will probably be revised when coercion is flushed throughout the system anyways.



---

archive/issue_comments_009578.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T09:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009579.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T09:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1494#issuecomment-9579",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003800.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T09:42:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1494",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1494#event-3800"
}
```
