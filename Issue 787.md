# Issue 787: quotient spaces of vector spaces

archive/issues_000787.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf V is a subspace of W then W.quotient(V) should give the quotient space U=W/V.\n\nLeft TODO:\n- overload \"/\" constructor ?\n- provide a section map U->W ?\n- install appropriate coercions ?\n\nIssue created by migration from https://trac.sagemath.org/ticket/787\n\n",
    "created_at": "2007-10-02T13:41:40Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "quotient spaces of vector spaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/787",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

If V is a subspace of W then W.quotient(V) should give the quotient space U=W/V.

Left TODO:
- overload "/" constructor ?
- provide a section map U->W ?
- install appropriate coercions ?

Issue created by migration from https://trac.sagemath.org/ticket/787





---

archive/issue_comments_004697.json:
```json
{
    "body": "Attachment [fix.patch](tarball://root/attachments/some-uuid/ticket787/fix.patch) by @nbruin created at 2007-10-02 13:42:51\n\nimplementation",
    "created_at": "2007-10-02T13:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4697",
    "user": "https://github.com/nbruin"
}
```

Attachment [fix.patch](tarball://root/attachments/some-uuid/ticket787/fix.patch) by @nbruin created at 2007-10-02 13:42:51

implementation



---

archive/issue_events_002168.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T18:45:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2168"
}
```



---

archive/issue_comments_004698.json:
```json
{
    "body": "I think this should be replaced by Soroosh's code, which does this and much more.",
    "created_at": "2007-10-04T18:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4698",
    "user": "https://github.com/williamstein"
}
```

I think this should be replaced by Soroosh's code, which does this and much more.



---

archive/issue_comments_004699.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-10-04T18:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4699",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_comments_004700.json:
```json
{
    "body": "```\nWhat? and ditch my 2 lines of haiku-like sage code?\n\nSeriously, though. The attached patch contains quite a bit more than\n\"quotient\", as you are probably woefully aware of. Easiest is probably\n\n - apply the patch\n - delete \"quotient\" from sage/modules/free_module.py\n\nCheers,\n```",
    "created_at": "2007-10-05T07:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4700",
    "user": "https://github.com/williamstein"
}
```

```
What? and ditch my 2 lines of haiku-like sage code?

Seriously, though. The attached patch contains quite a bit more than
"quotient", as you are probably woefully aware of. Easiest is probably

 - apply the patch
 - delete "quotient" from sage/modules/free_module.py

Cheers,
```



---

archive/issue_events_002169.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-05T07:54:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2169"
}
```



---

archive/issue_comments_004701.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2007-10-05T07:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4701",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_004702.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-05T07:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4702",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002170.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-05T07:54:16Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2170"
}
```



---

archive/issue_events_002171.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-18T14:10:11Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2171"
}
```



---

archive/issue_events_002172.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-18T14:10:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2172"
}
```



---

archive/issue_comments_004703.json:
```json
{
    "body": "We need to figure out if this still applies.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-18T14:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We need to figure out if this still applies.

Cheers,

Michael



---

archive/issue_events_002173.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T03:32:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2173"
}
```



---

archive/issue_events_002174.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T03:32:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2174"
}
```



---

archive/issue_events_002175.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:09:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2175"
}
```



---

archive/issue_events_002176.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:09:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2176"
}
```



---

archive/issue_events_002177.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T14:59:57Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2177"
}
```



---

archive/issue_events_002178.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T14:59:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2178"
}
```



---

archive/issue_comments_004704.json:
```json
{
    "body": "This has lingered too long -- I need to deal with it.",
    "created_at": "2007-11-03T15:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4704",
    "user": "https://github.com/williamstein"
}
```

This has lingered too long -- I need to deal with it.



---

archive/issue_events_002179.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-16T11:56:05Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2179"
}
```



---

archive/issue_events_002180.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-16T11:56:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2180"
}
```



---

archive/issue_comments_004705.json:
```json
{
    "body": "NOT ready: I still think \"I think this should be replaced by Soroosh's code, which does this and much more.\"  I don't know the status of Soroosh's code.",
    "created_at": "2007-11-18T03:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4705",
    "user": "https://github.com/williamstein"
}
```

NOT ready: I still think "I think this should be replaced by Soroosh's code, which does this and much more."  I don't know the status of Soroosh's code.



---

archive/issue_comments_004706.json:
```json
{
    "body": "Soroosh's code, i.e. #1029 got merged. So should we invalidate this ticket?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T14:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Soroosh's code, i.e. #1029 got merged. So should we invalidate this ticket?

Cheers,

Michael



---

archive/issue_comments_004707.json:
```json
{
    "body": "Almost done:\n\n```\nwas_: sage: R = QQ^3; S = R.span([[1,2,3]])\n[10:14am] was_: sage: w = R.quotient(S)\n[10:14am] was_: sage: w = R / S\n[10:14am] was_: But the last goes boom.\n[10:14am] was_: It would be 3-4 lines of code to fix that.\n[10:14am] was_: Once that is fixed, then 787 is done\n```",
    "created_at": "2007-11-25T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4707",
    "user": "https://github.com/williamstein"
}
```

Almost done:

```
was_: sage: R = QQ^3; S = R.span([[1,2,3]])
[10:14am] was_: sage: w = R.quotient(S)
[10:14am] was_: sage: w = R / S
[10:14am] was_: But the last goes boom.
[10:14am] was_: It would be 3-4 lines of code to fix that.
[10:14am] was_: Once that is fixed, then 787 is done
```



---

archive/issue_comments_004708.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2007-12-01T20:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4708",
    "user": "https://github.com/williamstein"
}
```

Changing status from reopened to new.



---

archive/issue_comments_004709.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-01T20:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4709",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004710.json:
```json
{
    "body": "A quick comment.  Even as is this is WRONG -- the algorithm used is buggy, evidently, or something, since\n\n```\nsage: A = QQ^3; V = A.span([[1,2,3], [4,5,6]])\nsage: Q = V.quotient( V.span([V.0 + V.1]) ); Q\nsage: Q[1](V.0 + V.1)\n(1)\n```\n\nBut Q[1] is the quotient map so should have `V.0 + V.1` in its kernel.",
    "created_at": "2007-12-01T20:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4710",
    "user": "https://github.com/williamstein"
}
```

A quick comment.  Even as is this is WRONG -- the algorithm used is buggy, evidently, or something, since

```
sage: A = QQ^3; V = A.span([[1,2,3], [4,5,6]])
sage: Q = V.quotient( V.span([V.0 + V.1]) ); Q
sage: Q[1](V.0 + V.1)
(1)
```

But Q[1] is the quotient map so should have `V.0 + V.1` in its kernel.



---

archive/issue_comments_004711.json:
```json
{
    "body": "Attachment [trac787.patch](tarball://root/attachments/some-uuid/ticket787/trac787.patch) by @williamstein created at 2007-12-02 00:47:48\n\nThis I think correctly really implements quotients of vector spaces.",
    "created_at": "2007-12-02T00:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4711",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac787.patch](tarball://root/attachments/some-uuid/ticket787/trac787.patch) by @williamstein created at 2007-12-02 00:47:48

This I think correctly really implements quotients of vector spaces.



---

archive/issue_comments_004712.json:
```json
{
    "body": "Attachment [trac787-part2.patch](tarball://root/attachments/some-uuid/ticket787/trac787-part2.patch) by @williamstein created at 2007-12-02 03:05:01\n\nThis is also needed (it fixes a docstring)",
    "created_at": "2007-12-02T03:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4712",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac787-part2.patch](tarball://root/attachments/some-uuid/ticket787/trac787-part2.patch) by @williamstein created at 2007-12-02 03:05:01

This is also needed (it fixes a docstring)



---

archive/issue_comments_004713.json:
```json
{
    "body": "this is also needed.",
    "created_at": "2007-12-02T03:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4713",
    "user": "https://github.com/williamstein"
}
```

this is also needed.



---

archive/issue_comments_004714.json:
```json
{
    "body": "Attachment [trac787-bundle.hg](tarball://root/attachments/some-uuid/ticket787/trac787-bundle.hg) by @williamstein created at 2007-12-02 03:14:44\n\ninstead of applying those three patches, this is a clean bundle.",
    "created_at": "2007-12-02T03:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4714",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac787-bundle.hg](tarball://root/attachments/some-uuid/ticket787/trac787-bundle.hg) by @williamstein created at 2007-12-02 03:14:44

instead of applying those three patches, this is a clean bundle.



---

archive/issue_events_002181.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T04:50:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/787#event-2181"
}
```



---

archive/issue_comments_004715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T04:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004716.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T04:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha2.



---

archive/issue_comments_004717.json:
```json
{
    "body": "Changes _repr_",
    "created_at": "2007-12-02T05:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4717",
    "user": "https://github.com/roed314"
}
```

Changes _repr_



---

archive/issue_comments_004718.json:
```json
{
    "body": "Attachment [trac787-part4.patch](tarball://root/attachments/some-uuid/ticket787/trac787-part4.patch) by @williamstein created at 2007-12-02 09:45:48\n\nThis was slightly buggy -- see Trac #1368 for a fix.",
    "created_at": "2007-12-02T09:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/787#issuecomment-4718",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac787-part4.patch](tarball://root/attachments/some-uuid/ticket787/trac787-part4.patch) by @williamstein created at 2007-12-02 09:45:48

This was slightly buggy -- see Trac #1368 for a fix.
