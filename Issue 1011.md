# Issue 1011: [with patch] MagmaElement.__nonzero__

archive/issues_001011.json:
```json
{
    "body": "Assignee: @malb\n\nThis used to not work: `bool(magma('true'))` with the attached tiny patch it does.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1011\n\n",
    "created_at": "2007-10-27T13:59:24Z",
    "labels": [
        "component: interfaces",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "[with patch] MagmaElement.__nonzero__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1011",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

This used to not work: `bool(magma('true'))` with the attached tiny patch it does.

Issue created by migration from https://trac.sagemath.org/ticket/1011





---

archive/issue_comments_006173.json:
```json
{
    "body": "Mmmh, any chance this is related to/also  fixes #845?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-27T16:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1011#issuecomment-6173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmmh, any chance this is related to/also  fixes #845?

Cheers,

Michael



---

archive/issue_comments_006174.json:
```json
{
    "body": "Wouldn't that break `magma(25).is_zero()`?\n\n```\nsage: magma(25).is_zero()\nFalse\nsage: magma(25).bool()\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n[... elided ...]\n<type 'exceptions.RuntimeError'>: Error evaluation Magma code.\nIN:_sage_[18] eq true;\nOUT:\n>> _sage_[18] eq true;\n              ^\nRuntime error in 'eq': Bad argument types\nArgument types given: RngIntElt, BoolElt\n```\n",
    "created_at": "2007-10-27T19:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1011#issuecomment-6174",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Wouldn't that break `magma(25).is_zero()`?

```
sage: magma(25).is_zero()
False
sage: magma(25).bool()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)
[... elided ...]
<type 'exceptions.RuntimeError'>: Error evaluation Magma code.
IN:_sage_[18] eq true;
OUT:
>> _sage_[18] eq true;
              ^
Runtime error in 'eq': Bad argument types
Argument types given: RngIntElt, BoolElt
```




---

archive/issue_comments_006175.json:
```json
{
    "body": "Attachment [magma_nonzero.patch](tarball://root/attachments/some-uuid/ticket1011/magma_nonzero.patch) by @malb created at 2007-10-30 16:28:25\n\nReplying to [comment:2 cwitty]:\n> Wouldn't that break `magma(25).is_zero()`?\n\nYou are right and thus I updated the patch:\n\n\n```\nsage: magma(9).is_zero()\nFalse\nsage: magma(0).is_zero()\nTrue\nsage: magma('false').bool()\nFalse\nsage: bool(magma(9).IsPrime())\nFalse\nsage: bool(magma(7).IsPrime())\nTrue\n```\n",
    "created_at": "2007-10-30T16:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1011#issuecomment-6175",
    "user": "https://github.com/malb"
}
```

Attachment [magma_nonzero.patch](tarball://root/attachments/some-uuid/ticket1011/magma_nonzero.patch) by @malb created at 2007-10-30 16:28:25

Replying to [comment:2 cwitty]:
> Wouldn't that break `magma(25).is_zero()`?

You are right and thus I updated the patch:


```
sage: magma(9).is_zero()
False
sage: magma(0).is_zero()
True
sage: magma('false').bool()
False
sage: bool(magma(9).IsPrime())
False
sage: bool(magma(7).IsPrime())
True
```




---

archive/issue_events_001135.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-01T09:41:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1011",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1011#event-1135"
}
```



---

archive/issue_comments_006176.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1011#issuecomment-6176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0



---

archive/issue_comments_006177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1011#issuecomment-6177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
