# Issue 9667: Use PARI's hash_GEN() for gen.__hash__

archive/issues_009667.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe latest version of PARI has a function `hash_GEN` which hashes a PARI `GEN`.  Since this is very likely faster than hashing the string representation of a `GEN`, we should use this for the `gen` class in sage/libs/pari/gen.pyx\n\nIssue created by migration from https://trac.sagemath.org/ticket/9667\n\n",
    "created_at": "2010-08-02T09:47:20Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Use PARI's hash_GEN() for gen.__hash__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9667",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

The latest version of PARI has a function `hash_GEN` which hashes a PARI `GEN`.  Since this is very likely faster than hashing the string representation of a `GEN`, we should use this for the `gen` class in sage/libs/pari/gen.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9667





---

archive/issue_comments_093697.json:
```json
{
    "body": "Patch to be applied on top of #9343",
    "created_at": "2010-08-02T12:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93697",
    "user": "https://github.com/jdemeyer"
}
```

Patch to be applied on top of #9343



---

archive/issue_comments_093698.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-15T17:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93698",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093699.json:
```json
{
    "body": "Attachment [9667.patch](tarball://root/attachments/some-uuid/ticket9667/9667.patch) by @jdemeyer created at 2010-09-15 17:12:33",
    "created_at": "2010-09-15T17:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93699",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9667.patch](tarball://root/attachments/some-uuid/ticket9667/9667.patch) by @jdemeyer created at 2010-09-15 17:12:33



---

archive/issue_comments_093700.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-15T17:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93700",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093701.json:
```json
{
    "body": "Ignore this ticket, see #9764 instead.",
    "created_at": "2010-09-15T17:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93701",
    "user": "https://github.com/jdemeyer"
}
```

Ignore this ticket, see #9764 instead.



---

archive/issue_comments_093702.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-28T11:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93702",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_events_009802.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T11:15:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9667#event-9802"
}
```



---

archive/issue_comments_093703.json:
```json
{
    "body": "Hi,\n\nFor the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.  For example, by playing with ideals in Sage (code is complicated though...), I quickly got into this situation:\n\n```\nsage: n0\n[11, 3; 0, 1]\nsage: n1\n[11, 3; 0, 1]\nsage: hash(n0)\n-7493989779944505307\nsage: hash(n1)\n-6341068275337658331\n```\n",
    "created_at": "2011-07-29T20:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93703",
    "user": "https://github.com/williamstein"
}
```

Hi,

For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.  For example, by playing with ideals in Sage (code is complicated though...), I quickly got into this situation:

```
sage: n0
[11, 3; 0, 1]
sage: n1
[11, 3; 0, 1]
sage: hash(n0)
-7493989779944505307
sage: hash(n1)
-6341068275337658331
```




---

archive/issue_comments_093704.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.\nSee #11611, I have not tracked it down precisely.",
    "created_at": "2011-08-01T10:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93704",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:5 was]:
> For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.
See #11611, I have not tracked it down precisely.



---

archive/issue_comments_093705.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> Hi,\n> \n> For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.\nDon't blaim PARI when the fault is the Sage->PARI interface. The issue is not `hash_GEN()`, it is a problem with how integers are converted from Sage to PARI.  I have a patch for this issue at #11611.",
    "created_at": "2011-08-03T13:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9667#issuecomment-93705",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:5 was]:
> Hi,
> 
> For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.
Don't blaim PARI when the fault is the Sage->PARI interface. The issue is not `hash_GEN()`, it is a problem with how integers are converted from Sage to PARI.  I have a patch for this issue at #11611.
