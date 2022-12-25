# Issue 3877: fix arrow so that they scale properly

archive/issues_003877.json:
```json
{
    "body": "Assignee: @williamstein\n\nLook at the differences between\n\n\n```\nsage: arrow((0,0), (100, 100))\n```\n\n\nand\n\n\n```\nsage: arrow((0,0), (1/1000, 1/1000))\n```\n\n\nThis depends on #3806.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3877\n\n",
    "created_at": "2008-08-15T21:35:54Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "fix arrow so that they scale properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3877",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein

Look at the differences between


```
sage: arrow((0,0), (100, 100))
```


and


```
sage: arrow((0,0), (1/1000, 1/1000))
```


This depends on #3806.

Issue created by migration from https://trac.sagemath.org/ticket/3877





---

archive/issue_comments_027596.json:
```json
{
    "body": "Attachment [trac_3877.patch](tarball://root/attachments/some-uuid/ticket3877/trac_3877.patch) by @mwhansen created at 2008-08-15 21:44:27",
    "created_at": "2008-08-15T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27596",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3877.patch](tarball://root/attachments/some-uuid/ticket3877/trac_3877.patch) by @mwhansen created at 2008-08-15 21:44:27



---

archive/issue_comments_027597.json:
```json
{
    "body": "Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.",
    "created_at": "2008-08-16T19:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27597",
    "user": "https://github.com/itolkov"
}
```

Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.



---

archive/issue_comments_027598.json:
```json
{
    "body": "Replying to [comment:2 itolkov]:\n> Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.\n\nYou are overriding passed width and other parameters. According to the docs,\n\n```\nsage: arrow((1, 1), (3, 3), width=0.05)\n```\n\n\nI didn't notice this before.",
    "created_at": "2008-08-16T19:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27598",
    "user": "https://github.com/itolkov"
}
```

Replying to [comment:2 itolkov]:
> Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.

You are overriding passed width and other parameters. According to the docs,

```
sage: arrow((1, 1), (3, 3), width=0.05)
```


I didn't notice this before.



---

archive/issue_comments_027599.json:
```json
{
    "body": "We are in freeze, so only critical bugs will get fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-16T19:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We are in freeze, so only critical bugs will get fixed.

Cheers,

Michael



---

archive/issue_comments_027600.json:
```json
{
    "body": "It looks like `width` is actually the only parameter being overridden, so doing something like checking to see if width was passed, and if it wasn't making the default the scalar*length should do it.",
    "created_at": "2008-08-18T20:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27600",
    "user": "https://github.com/jasongrout"
}
```

It looks like `width` is actually the only parameter being overridden, so doing something like checking to see if width was passed, and if it wasn't making the default the scalar*length should do it.



---

archive/issue_comments_027601.json:
```json
{
    "body": "Actually, this patch makes it so that all arrows have different sized lines and arrow heads.  That sounds bad, especially if you are combining arrows of different lengths in the same graphic.  Or if you are putting a really small arrow in a really large graphic; it sounds like it would get lost.\n\nI guess the real way to do things would be to have the arrow/head width a constant in screen coordinates rather than in plot coordinates.",
    "created_at": "2008-08-18T20:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27601",
    "user": "https://github.com/jasongrout"
}
```

Actually, this patch makes it so that all arrows have different sized lines and arrow heads.  That sounds bad, especially if you are combining arrows of different lengths in the same graphic.  Or if you are putting a really small arrow in a really large graphic; it sounds like it would get lost.

I guess the real way to do things would be to have the arrow/head width a constant in screen coordinates rather than in plot coordinates.



---

archive/issue_comments_027602.json:
```json
{
    "body": "Reading the matplotlib-0.98.3 source, there are two arrows in patches.py:\n\n1. FancyArrow, which is drawn in plot coordinates\n\n2. YAArrow (Yet Another Arrow), which is drawn in display coordinates.\n\nIt sounds like we want the YAArrow class, which would provide the same \"look\", no matter the zoom level.",
    "created_at": "2008-08-18T22:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27602",
    "user": "https://github.com/jasongrout"
}
```

Reading the matplotlib-0.98.3 source, there are two arrows in patches.py:

1. FancyArrow, which is drawn in plot coordinates

2. YAArrow (Yet Another Arrow), which is drawn in display coordinates.

It sounds like we want the YAArrow class, which would provide the same "look", no matter the zoom level.



---

archive/issue_comments_027603.json:
```json
{
    "body": "We need to upgrade to that version of matplotlib first.",
    "created_at": "2008-08-18T22:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27603",
    "user": "https://github.com/mwhansen"
}
```

We need to upgrade to that version of matplotlib first.



---

archive/issue_comments_027604.json:
```json
{
    "body": "YAArrow exists in the current matplotlib that Sage uses, but has a bug that has been fixed since then in the getpoints() function.  Also, I didn't get YAArrow to look nice, no matter the scale, and have run out of time for now.",
    "created_at": "2008-08-18T23:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27604",
    "user": "https://github.com/jasongrout"
}
```

YAArrow exists in the current matplotlib that Sage uses, but has a bug that has been fixed since then in the getpoints() function.  Also, I didn't get YAArrow to look nice, no matter the scale, and have run out of time for now.



---

archive/issue_comments_027605.json:
```json
{
    "body": "This should be taken care of at the same time as #3880",
    "created_at": "2008-08-18T23:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27605",
    "user": "https://github.com/rlmill"
}
```

This should be taken care of at the same time as #3880



---

archive/issue_comments_027606.json:
```json
{
    "body": "Take it back, this is different from #3880. I also wonder why arrows are skewed so badly: after #3880, take a look at\n\n```\nsage: arrow((-.1,-.1), (0,0))\n```\n\nThe skewing isn't as bad here as I've seen it elsewhere, but I wonder why it is doing this...",
    "created_at": "2008-08-19T01:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27606",
    "user": "https://github.com/rlmill"
}
```

Take it back, this is different from #3880. I also wonder why arrows are skewed so badly: after #3880, take a look at

```
sage: arrow((-.1,-.1), (0,0))
```

The skewing isn't as bad here as I've seen it elsewhere, but I wonder why it is doing this...



---

archive/issue_comments_027607.json:
```json
{
    "body": "Fixed by #3880.\n\nCheers,\n\nMcihael",
    "created_at": "2008-08-19T01:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by #3880.

Cheers,

Mcihael



---

archive/issue_comments_027608.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T01:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004100.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-19T01:49:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3877#event-4100"
}
```



---

archive/issue_comments_027609.json:
```json
{
    "body": "Fixed by #3880. Hence: closed.\n\nCheers, \n\nMichael",
    "created_at": "2008-08-19T01:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by #3880. Hence: closed.

Cheers, 

Michael



---

archive/issue_comments_027610.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-19T01:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004101.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-19T01:49:56Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3877#event-4101"
}
```



---

archive/issue_comments_027611.json:
```json
{
    "body": "Oops, rlm says this is a different issue. Sorry Mike.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T01:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, rlm says this is a different issue. Sorry Mike.

Cheers,

Michael



---

archive/issue_comments_027612.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-08-19T01:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_027613.json:
```json
{
    "body": "I'm working on a patch for #3922 which will make this issue obsolete.",
    "created_at": "2008-08-27T09:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27613",
    "user": "https://github.com/jasongrout"
}
```

I'm working on a patch for #3922 which will make this issue obsolete.



---

archive/issue_comments_027614.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T02:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004102.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T02:04:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3877#event-4102"
}
```



---

archive/issue_comments_027615.json:
```json
{
    "body": "Fixed since #3922 has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T02:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed since #3922 has been merged.

Cheers,

Michael
