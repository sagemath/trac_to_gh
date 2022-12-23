# Issue 3877: fix arrow so that they scale properly

archive/issues_003877.json:
```json
{
    "body": "Assignee: was\n\nLook at the differences between\n\n\n```\nsage: arrow((0,0), (100, 100))\n```\n\n\nand\n\n\n```\nsage: arrow((0,0), (1/1000, 1/1000))\n```\n\n\nThis depends on #3806.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3877\n\n",
    "created_at": "2008-08-15T21:35:54Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "fix arrow so that they scale properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3877",
    "user": "mhansen"
}
```
Assignee: was

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

archive/issue_comments_027654.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-15T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27654",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_027655.json:
```json
{
    "body": "Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.",
    "created_at": "2008-08-16T19:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27655",
    "user": "itolkov"
}
```

Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.



---

archive/issue_comments_027656.json:
```json
{
    "body": "Replying to [comment:2 itolkov]:\n> Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.\n\nYou are overriding passed width and other parameters. According to the docs,\n\n```\nsage: arrow((1, 1), (3, 3), width=0.05)\n```\n\n\nI didn't notice this before.",
    "created_at": "2008-08-16T19:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27656",
    "user": "itolkov"
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

archive/issue_comments_027657.json:
```json
{
    "body": "We are in freeze, so only critical bugs will get fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-16T19:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27657",
    "user": "mabshoff"
}
```

We are in freeze, so only critical bugs will get fixed.

Cheers,

Michael



---

archive/issue_comments_027658.json:
```json
{
    "body": "It looks like `width` is actually the only parameter being overridden, so doing something like checking to see if width was passed, and if it wasn't making the default the scalar*length should do it.",
    "created_at": "2008-08-18T20:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27658",
    "user": "jason"
}
```

It looks like `width` is actually the only parameter being overridden, so doing something like checking to see if width was passed, and if it wasn't making the default the scalar*length should do it.



---

archive/issue_comments_027659.json:
```json
{
    "body": "Actually, this patch makes it so that all arrows have different sized lines and arrow heads.  That sounds bad, especially if you are combining arrows of different lengths in the same graphic.  Or if you are putting a really small arrow in a really large graphic; it sounds like it would get lost.\n\nI guess the real way to do things would be to have the arrow/head width a constant in screen coordinates rather than in plot coordinates.",
    "created_at": "2008-08-18T20:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27659",
    "user": "jason"
}
```

Actually, this patch makes it so that all arrows have different sized lines and arrow heads.  That sounds bad, especially if you are combining arrows of different lengths in the same graphic.  Or if you are putting a really small arrow in a really large graphic; it sounds like it would get lost.

I guess the real way to do things would be to have the arrow/head width a constant in screen coordinates rather than in plot coordinates.



---

archive/issue_comments_027660.json:
```json
{
    "body": "Reading the matplotlib-0.98.3 source, there are two arrows in patches.py:\n\n1. FancyArrow, which is drawn in plot coordinates\n\n2. YAArrow (Yet Another Arrow), which is drawn in display coordinates.\n\nIt sounds like we want the YAArrow class, which would provide the same \"look\", no matter the zoom level.",
    "created_at": "2008-08-18T22:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27660",
    "user": "jason"
}
```

Reading the matplotlib-0.98.3 source, there are two arrows in patches.py:

1. FancyArrow, which is drawn in plot coordinates

2. YAArrow (Yet Another Arrow), which is drawn in display coordinates.

It sounds like we want the YAArrow class, which would provide the same "look", no matter the zoom level.



---

archive/issue_comments_027661.json:
```json
{
    "body": "We need to upgrade to that version of matplotlib first.",
    "created_at": "2008-08-18T22:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27661",
    "user": "mhansen"
}
```

We need to upgrade to that version of matplotlib first.



---

archive/issue_comments_027662.json:
```json
{
    "body": "YAArrow exists in the current matplotlib that Sage uses, but has a bug that has been fixed since then in the getpoints() function.  Also, I didn't get YAArrow to look nice, no matter the scale, and have run out of time for now.",
    "created_at": "2008-08-18T23:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27662",
    "user": "jason"
}
```

YAArrow exists in the current matplotlib that Sage uses, but has a bug that has been fixed since then in the getpoints() function.  Also, I didn't get YAArrow to look nice, no matter the scale, and have run out of time for now.



---

archive/issue_comments_027663.json:
```json
{
    "body": "This should be taken care of at the same time as #3880",
    "created_at": "2008-08-18T23:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27663",
    "user": "rlm"
}
```

This should be taken care of at the same time as #3880



---

archive/issue_comments_027664.json:
```json
{
    "body": "Take it back, this is different from #3880. I also wonder why arrows are skewed so badly: after #3880, take a look at\n\n```\nsage: arrow((-.1,-.1), (0,0))\n```\n\nThe skewing isn't as bad here as I've seen it elsewhere, but I wonder why it is doing this...",
    "created_at": "2008-08-19T01:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27664",
    "user": "rlm"
}
```

Take it back, this is different from #3880. I also wonder why arrows are skewed so badly: after #3880, take a look at

```
sage: arrow((-.1,-.1), (0,0))
```

The skewing isn't as bad here as I've seen it elsewhere, but I wonder why it is doing this...



---

archive/issue_comments_027665.json:
```json
{
    "body": "Fixed by #3880.\n\nCheers,\n\nMcihael",
    "created_at": "2008-08-19T01:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27665",
    "user": "mabshoff"
}
```

Fixed by #3880.

Cheers,

Mcihael



---

archive/issue_comments_027666.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T01:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27666",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027667.json:
```json
{
    "body": "Fixed by #3880. Hence: closed.\n\nCheers, \n\nMichael",
    "created_at": "2008-08-19T01:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27667",
    "user": "mabshoff"
}
```

Fixed by #3880. Hence: closed.

Cheers, 

Michael



---

archive/issue_comments_027668.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-19T01:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27668",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_027669.json:
```json
{
    "body": "Oops, rlm says this is a different issue. Sorry Mike.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T01:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27669",
    "user": "mabshoff"
}
```

Oops, rlm says this is a different issue. Sorry Mike.

Cheers,

Michael



---

archive/issue_comments_027670.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-08-19T01:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27670",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_027671.json:
```json
{
    "body": "I'm working on a patch for #3922 which will make this issue obsolete.",
    "created_at": "2008-08-27T09:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27671",
    "user": "jason"
}
```

I'm working on a patch for #3922 which will make this issue obsolete.



---

archive/issue_comments_027672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T02:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27672",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027673.json:
```json
{
    "body": "Fixed since #3922 has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T02:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3877#issuecomment-27673",
    "user": "mabshoff"
}
```

Fixed since #3922 has been merged.

Cheers,

Michael
