# Issue 4561: [with patch, positive review] _fast_float_ for sin/cos, etc., in caculus.py is implemented stupidly

archive/issues_004561.json:
```json
{
    "body": "Assignee: @burcin\n\nSee #4557.\n\n```\n>\n> Why are we using math.sin/math.cos at all? Really, it should use the\n> native C sin and cos.\n>\n> - Robert\n\nYou're right Robert, and that definition of _fast_float_ for sin and cos\nis totally the wrong approach.  E.g., observe that your _fast_float_ sin\nis twice as fast as math.sin:\n\nsage: a = sin._fast_float_()\nsage: timeit('a(3.4r)')\n625 loops, best of 3: 469 ns per loop\nsage: a = sin(x)._fast_float_()\nsage: timeit('a(3.4r)')\n625 loops, best of 3: 254 ns per loop\n\nNote that the code in calculus.py is *not* just returning math.sin,\nactually, but constructing a fast_float object, which is actually\nway *WORSE* than math.sin, even:\n\nsage: a = sin._fast_float_()\nsage: timeit('a(3.4r)')\n625 loops, best of 3: 809 ns per loop\nsage: type(a)\n<type 'sage.ext.fast_eval.FastDoubleFunc'>\n\n\nWilliam\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4561\n\n",
    "closed_at": "2008-11-21T19:13:57Z",
    "created_at": "2008-11-20T01:55:11Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, positive review] _fast_float_ for sin/cos, etc., in caculus.py is implemented stupidly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4561",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin

See #4557.

```
>
> Why are we using math.sin/math.cos at all? Really, it should use the
> native C sin and cos.
>
> - Robert

You're right Robert, and that definition of _fast_float_ for sin and cos
is totally the wrong approach.  E.g., observe that your _fast_float_ sin
is twice as fast as math.sin:

sage: a = sin._fast_float_()
sage: timeit('a(3.4r)')
625 loops, best of 3: 469 ns per loop
sage: a = sin(x)._fast_float_()
sage: timeit('a(3.4r)')
625 loops, best of 3: 254 ns per loop

Note that the code in calculus.py is *not* just returning math.sin,
actually, but constructing a fast_float object, which is actually
way *WORSE* than math.sin, even:

sage: a = sin._fast_float_()
sage: timeit('a(3.4r)')
625 loops, best of 3: 809 ns per loop
sage: type(a)
<type 'sage.ext.fast_eval.FastDoubleFunc'>


William
```

Issue created by migration from https://trac.sagemath.org/ticket/4561





---

archive/issue_comments_034101.json:
```json
{
    "body": "Attachment [4561-PrimitiveFunction-fastfloat.patch](tarball://root/attachments/some-uuid/ticket4561/4561-PrimitiveFunction-fastfloat.patch) by @robertwb created at 2008-11-21 06:48:09",
    "created_at": "2008-11-21T06:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4561#issuecomment-34101",
    "user": "https://github.com/robertwb"
}
```

Attachment [4561-PrimitiveFunction-fastfloat.patch](tarball://root/attachments/some-uuid/ticket4561/4561-PrimitiveFunction-fastfloat.patch) by @robertwb created at 2008-11-21 06:48:09



---

archive/issue_comments_034102.json:
```json
{
    "body": "This is much better than my implementation :-)\n\nApplies to 3.2 and passes tests.",
    "created_at": "2008-11-21T17:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4561#issuecomment-34102",
    "user": "https://github.com/mwhansen"
}
```

This is much better than my implementation :-)

Applies to 3.2 and passes tests.



---

archive/issue_events_010396.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-21T19:13:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4561",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4561#event-10396"
}
```



---

archive/issue_comments_034103.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T19:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4561#issuecomment-34103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_034104.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T19:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4561#issuecomment-34104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
