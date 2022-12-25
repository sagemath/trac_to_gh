# Issue 1449: [with bundle, very positive review] very serious (but trivial to fix) notebook bug: shift-enter doesn't work on macs; it's shift-return!

archive/issues_001449.json:
```json
{
    "body": "Assignee: boothby\n\n```\n\n\nOn Dec 10, 2007 6:08 AM, G. Edgar <edgar@math.ohio-state.edu> wrote:\n> \n> It says to use \"shift enter\" to evaluate an input cell.\n> But it seems this is wrong on Mac, and one should use \"shift return\".\n> Return and Enter are separate keys on the Mac keyboard.\n\nYou're right.  And this is especially bad since right now on a Mac\n\"shift enter\" doesn't work.   I can't believe we missed this, given that\nso many Sage developers (like me) work on Macs!\n\nI think the fix will be to make it so \"shift return\" does work on macs,\nin addition to \"shift enter\".  This will make the documentation stay\nuniform (but we'll also mention shift-enter in the docs). \n\nWilliam\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1449\n\n",
    "closed_at": "2008-01-05T02:23:53Z",
    "created_at": "2007-12-10T15:50:19Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "[with bundle, very positive review] very serious (but trivial to fix) notebook bug: shift-enter doesn't work on macs; it's shift-return!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1449",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

```


On Dec 10, 2007 6:08 AM, G. Edgar <edgar@math.ohio-state.edu> wrote:
> 
> It says to use "shift enter" to evaluate an input cell.
> But it seems this is wrong on Mac, and one should use "shift return".
> Return and Enter are separate keys on the Mac keyboard.

You're right.  And this is especially bad since right now on a Mac
"shift enter" doesn't work.   I can't believe we missed this, given that
so many Sage developers (like me) work on Macs!

I think the fix will be to make it so "shift return" does work on macs,
in addition to "shift enter".  This will make the documentation stay
uniform (but we'll also mention shift-enter in the docs). 

William
```

Issue created by migration from https://trac.sagemath.org/ticket/1449





---

archive/issue_comments_009309.json:
```json
{
    "body": "```\nWith my Mac G5, uising Safari...\nshift-return and option-return evaluate the cell\nshift-enter, option-enter do not. \n```\n\nTom Boothby asked for some specific details from the poster about this.\nI don't know what happened as a result yet.",
    "created_at": "2007-12-12T13:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9309",
    "user": "https://github.com/williamstein"
}
```

```
With my Mac G5, uising Safari...
shift-return and option-return evaluate the cell
shift-enter, option-enter do not. 
```

Tom Boothby asked for some specific details from the poster about this.
I don't know what happened as a result yet.



---

archive/issue_events_003702.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-12T13:26:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1449#event-3702"
}
```



---

archive/issue_comments_009310.json:
```json
{
    "body": "This *should* fix the problem, but hasn't been tested on the target platform.",
    "created_at": "2008-01-02T23:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9310",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

This *should* fix the problem, but hasn't been tested on the target platform.



---

archive/issue_comments_009311.json:
```json
{
    "body": "Attachment [1449.hg](tarball://root/attachments/some-uuid/ticket1449/1449.hg) by mabshoff created at 2008-01-03 05:01:32\n\nThe bundle also seems to contain the fix for #1661.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T05:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [1449.hg](tarball://root/attachments/some-uuid/ticket1449/1449.hg) by mabshoff created at 2008-01-03 05:01:32

The bundle also seems to contain the fix for #1661.

Cheers,

Michael



---

archive/issue_comments_009312.json:
```json
{
    "body": "Works in Camino and Firefox for me, but not in Safari...",
    "created_at": "2008-01-04T20:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9312",
    "user": "https://github.com/robertwb"
}
```

Works in Camino and Firefox for me, but not in Safari...



---

archive/issue_comments_009313.json:
```json
{
    "body": "Attachment [referee.patch](tarball://root/attachments/some-uuid/ticket1449/referee.patch) by @williamstein created at 2008-01-05 02:11:23\n\nGreat idea!!\n\nI posted a slight polish patch.",
    "created_at": "2008-01-05T02:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9313",
    "user": "https://github.com/williamstein"
}
```

Attachment [referee.patch](tarball://root/attachments/some-uuid/ticket1449/referee.patch) by @williamstein created at 2008-01-05 02:11:23

Great idea!!

I posted a slight polish patch.



---

archive/issue_events_003703.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-05T02:23:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1449#event-3703"
}
```



---

archive/issue_comments_009314.json:
```json
{
    "body": "Merged in 2.9.2.rc1. I open a new ticket for the remaining Safari issue, see #1690.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-05T02:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.2.rc1. I open a new ticket for the remaining Safari issue, see #1690.

Cheers,

Michael



---

archive/issue_comments_009315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-05T02:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1449#issuecomment-9315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
