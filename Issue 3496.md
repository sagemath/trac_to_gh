# Issue 3496: [with patch, positive review] charpoly for 0 dimensional matrices is broken for cyclotomic matrices

archive/issues_003496.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  alexghitza\n\nThis should be fixed over all kinds of rings -- it's supposed to be `0` everywhere. It's currently either broken (e.g. over `CyclotomicField`s) or wrong (e.g. it's `1` over `QQ`) in lots of places.\n\nI'll do this soon if no one beats me to it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3496\n\n",
    "closed_at": "2008-10-28T12:18:43Z",
    "created_at": "2008-06-23T19:14:46Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] charpoly for 0 dimensional matrices is broken for cyclotomic matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3496",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  alexghitza

This should be fixed over all kinds of rings -- it's supposed to be `0` everywhere. It's currently either broken (e.g. over `CyclotomicField`s) or wrong (e.g. it's `1` over `QQ`) in lots of places.

I'll do this soon if no one beats me to it.

Issue created by migration from https://trac.sagemath.org/ticket/3496





---

archive/issue_comments_024567.json:
```json
{
    "body": "Sorry, why should the charpoly be zero? I would have thought it should be 1.",
    "created_at": "2008-06-23T22:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24567",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Sorry, why should the charpoly be zero? I would have thought it should be 1.



---

archive/issue_comments_024568.json:
```json
{
    "body": "Alright, I'm convinced. The best argument for me was that if $V = W \\oplus W'$, and you have an operator on $V$, you want to be able to say things like \"the charpoly on the sum is the product of the charpolys.\"\n\nI still need to fix it for cyclotomic fields.",
    "created_at": "2008-06-23T22:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24568",
    "user": "https://github.com/craigcitro"
}
```

Alright, I'm convinced. The best argument for me was that if $V = W \oplus W'$, and you have an operator on $V$, you want to be able to say things like "the charpoly on the sum is the product of the charpolys."

I still need to fix it for cyclotomic fields.



---

archive/issue_comments_024569.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-23T18:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24569",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024570.json:
```json
{
    "body": "Attachment [trac-3496.patch](tarball://root/attachments/some-uuid/ticket3496/trac-3496.patch) by @craigcitro created at 2008-10-23 18:56:21\n\nThis patch fixes the charpoly for 0-dimensional matrices, along with a bunch of other little issues in the cyclotomic linear algebra code. This code was written during the L-functions and Modular Forms Workshop in Seattle, mostly while discussing the code with Clement Pernet.",
    "created_at": "2008-10-23T18:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24570",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3496.patch](tarball://root/attachments/some-uuid/ticket3496/trac-3496.patch) by @craigcitro created at 2008-10-23 18:56:21

This patch fixes the charpoly for 0-dimensional matrices, along with a bunch of other little issues in the cyclotomic linear algebra code. This code was written during the L-functions and Modular Forms Workshop in Seattle, mostly while discussing the code with Clement Pernet.



---

archive/issue_comments_024571.json:
```json
{
    "body": "Alex,\n\nsince you are reviewing can you take a shot at this one, too?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T01:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24571",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Alex,

since you are reviewing can you take a shot at this one, too?

Cheers,

Michael



---

archive/issue_comments_024572.json:
```json
{
    "body": "I'm pretty happy with this, except that it would be nice to have an actual doctest showing that the original issue (charpolys for 0 dimensional matrices) now works (yes, I can see it fixed in the new code, but let's have an explicit doctest).  So positive review with this tiny proviso.\n\nI'll add a minipatch for this the next time I get a chance (soon), unless Craig (or someone else) beats me to it.",
    "created_at": "2008-10-27T05:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24572",
    "user": "https://github.com/aghitza"
}
```

I'm pretty happy with this, except that it would be nice to have an actual doctest showing that the original issue (charpolys for 0 dimensional matrices) now works (yes, I can see it fixed in the new code, but let's have an explicit doctest).  So positive review with this tiny proviso.

I'll add a minipatch for this the next time I get a chance (soon), unless Craig (or someone else) beats me to it.



---

archive/issue_comments_024573.json:
```json
{
    "body": "Attachment [trac-3496-pt2.patch](tarball://root/attachments/some-uuid/ticket3496/trac-3496-pt2.patch) by @craigcitro created at 2008-10-27 05:52:21",
    "created_at": "2008-10-27T05:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24573",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3496-pt2.patch](tarball://root/attachments/some-uuid/ticket3496/trac-3496-pt2.patch) by @craigcitro created at 2008-10-27 05:52:21



---

archive/issue_comments_024574.json:
```json
{
    "body": "Oh, good call, Alex. I've added that doctest in the second patch.",
    "created_at": "2008-10-27T05:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24574",
    "user": "https://github.com/craigcitro"
}
```

Oh, good call, Alex. I've added that doctest in the second patch.



---

archive/issue_comments_024575.json:
```json
{
    "body": "I'm happy.",
    "created_at": "2008-10-27T06:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24575",
    "user": "https://github.com/aghitza"
}
```

I'm happy.



---

archive/issue_events_007968.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-28T12:18:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3496#event-7968"
}
```



---

archive/issue_comments_024576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-28T12:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024577.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha2",
    "created_at": "2008-10-28T12:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3496#issuecomment-24577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.alpha2



---

archive/issue_events_007969.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-28T12:18:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3496",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3496#event-7969"
}
```
