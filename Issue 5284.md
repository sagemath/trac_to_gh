# Issue 5284: Set sage-flags.txt up to SSE2 only when building Sage in SSE2 only mode/remove SSSE3 and SSE4 flags (followup to #5219)

archive/issues_005284.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a followup to #5219:\n\n* When building ATLAS in SSE2 only mode the sage-flags should be set accordingly to avoid that Sage complains on startup.\n\n* We do not use any SSE instructions beyond PNI (i.e. SSE3) at the moment, yet we check for SSSE3 and SSE4 flags. So do not add them to sage-flags since they will trigger wrong warning.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5284\n\n",
    "created_at": "2009-02-16T11:54:08Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Set sage-flags.txt up to SSE2 only when building Sage in SSE2 only mode/remove SSSE3 and SSE4 flags (followup to #5219)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5284",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is a followup to #5219:

* When building ATLAS in SSE2 only mode the sage-flags should be set accordingly to avoid that Sage complains on startup.

* We do not use any SSE instructions beyond PNI (i.e. SSE3) at the moment, yet we check for SSSE3 and SSE4 flags. So do not add them to sage-flags since they will trigger wrong warning.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5284





---

archive/issue_comments_040528.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-16T11:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40528",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_012277.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:30:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5284#event-12277"
}
```



---

archive/issue_comments_040529.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_events_012278.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-05T00:54:25Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5284#event-12278"
}
```



---

archive/issue_events_012279.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-05T00:54:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5284#event-12279"
}
```



---

archive/issue_comments_040530.json:
```json
{
    "body": "This needs to be fixed in 3.4.1!\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T07:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This needs to be fixed in 3.4.1!

Cheers,

Michael



---

archive/issue_events_012280.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-18T07:06:27Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5284#event-12280"
}
```



---

archive/issue_events_012281.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-18T07:06:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5284#event-12281"
}
```



---

archive/issue_comments_040531.json:
```json
{
    "body": "We need to check\n\n```\nSAGE_SIMD_MODE\n```\n\nThe only supported value at the moment is `SSE2`. So remove pni, ssse3 from the flags array.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T07:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We need to check

```
SAGE_SIMD_MODE
```

The only supported value at the moment is `SSE2`. So remove pni, ssse3 from the flags array.

Cheers,

Michael



---

archive/issue_comments_040532.json:
```json
{
    "body": "Attachment [trac_5284.patch](tarball://root/attachments/some-uuid/ticket5284/trac_5284.patch) by mabshoff created at 2009-04-22 03:25:12",
    "created_at": "2009-04-22T03:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5284.patch](tarball://root/attachments/some-uuid/ticket5284/trac_5284.patch) by mabshoff created at 2009-04-22 03:25:12



---

archive/issue_comments_040533.json:
```json
{
    "body": "Looks good to me.\n\nFor the record, I want to point out that mpir may be using `lahf` flag, which is *not* among the tested-for flags. Note that `lahf` does not depend on `ssse3` (e.g. a Pentium D 930 has `lahf` but not `ssse3`). Apparently the first intel 64 bit cpus did *not* have `lahf`.",
    "created_at": "2009-04-22T03:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40533",
    "user": "https://github.com/tornaria"
}
```

Looks good to me.

For the record, I want to point out that mpir may be using `lahf` flag, which is *not* among the tested-for flags. Note that `lahf` does not depend on `ssse3` (e.g. a Pentium D 930 has `lahf` but not `ssse3`). Apparently the first intel 64 bit cpus did *not* have `lahf`.



---

archive/issue_comments_040534.json:
```json
{
    "body": "I also tried this and it works fine.\n\ntornaria -- good catch regarding lahf.  We need to make a ticket about that!!",
    "created_at": "2009-04-22T03:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40534",
    "user": "https://github.com/williamstein"
}
```

I also tried this and it works fine.

tornaria -- good catch regarding lahf.  We need to make a ticket about that!!



---

archive/issue_comments_040535.json:
```json
{
    "body": "Replying to [comment:9 was]:\n> I also tried this and it works fine.\n> \n> tornaria -- good catch regarding lahf.  We need to make a ticket about that!!\n\nThat is part of #5849.\n\nA P4 that does not have lahf is exceedingly rare and AFAIK we have never seen a problem with it, but I am sure we will hit it in the future. Note that x86 vs. core2 code in 64 bit MPIR is quote noticeable performance wise for some benchmarks.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T04:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:9 was]:
> I also tried this and it works fine.
> 
> tornaria -- good catch regarding lahf.  We need to make a ticket about that!!

That is part of #5849.

A P4 that does not have lahf is exceedingly rare and AFAIK we have never seen a problem with it, but I am sure we will hit it in the future. Note that x86 vs. core2 code in 64 bit MPIR is quote noticeable performance wise for some benchmarks.

Cheers,

Michael



---

archive/issue_events_012282.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-22T04:12:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5284#event-12282"
}
```



---

archive/issue_comments_040536.json:
```json
{
    "body": "Merged in Sage 3.4.1.final. Last ticket for 3.4.1 - w00000t.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T04:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40536",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.final. Last ticket for 3.4.1 - w00000t.

Cheers,

Michael



---

archive/issue_comments_040537.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-22T04:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5284#issuecomment-40537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
