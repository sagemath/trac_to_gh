# Issue 9580: Check in, ignore, or delete sagenb.po in SageNB package

archive/issues_009580.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @TimDumol\n\nNoted by Leif Leonhardy in a [comment:ticket:9554:5 comment] at #9554:\n\n```sh\nleif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status\n? sagenb/sagenb.po\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9580\n\n",
    "closed_at": "2010-07-25T07:56:46Z",
    "created_at": "2010-07-23T06:28:05Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Check in, ignore, or delete sagenb.po in SageNB package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9580",
    "user": "https://github.com/qed777"
}
```
Assignee: jason, was

CC:  @TimDumol

Noted by Leif Leonhardy in a [comment:ticket:9554:5 comment] at #9554:

```sh
leif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status
? sagenb/sagenb.po
```


Issue created by migration from https://trac.sagemath.org/ticket/9580





---

archive/issue_comments_092373.json:
```json
{
    "body": "```\n<timdumol> _leif: Thanks for spotting the rogue .po file (I forgot to remove it from #9428 when I build 0.8.1)\n```\n(About 14 hours ago.)\n\nNevertheless, I'll add it to #9572 (SageNB 0.8.2).",
    "created_at": "2010-07-23T07:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92373",
    "user": "https://github.com/nexttime"
}
```

```
<timdumol> _leif: Thanks for spotting the rogue .po file (I forgot to remove it from #9428 when I build 0.8.1)
```
(About 14 hours ago.)

Nevertheless, I'll add it to #9572 (SageNB 0.8.2).



---

archive/issue_comments_092374.json:
```json
{
    "body": "```sh\nfind . -name .hg -exec sh -c \"cd {}; hg status\" \\;\n```\n\n;-)",
    "created_at": "2010-07-23T07:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92374",
    "user": "https://github.com/nexttime"
}
```

```sh
find . -name .hg -exec sh -c "cd {}; hg status" \;
```

;-)



---

archive/issue_comments_092375.json:
```json
{
    "body": "Just to check:  Should I just delete `sagenb/sagenb.po`?",
    "created_at": "2010-07-23T07:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92375",
    "user": "https://github.com/qed777"
}
```

Just to check:  Should I just delete `sagenb/sagenb.po`?



---

archive/issue_comments_092376.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Just to check:  Should I just delete `sagenb/sagenb.po`?\n\n\nAccording to what Tim said, I think yes.",
    "created_at": "2010-07-23T07:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92376",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 mpatel]:
> Just to check:  Should I just delete `sagenb/sagenb.po`?


According to what Tim said, I think yes.



---

archive/issue_comments_092377.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-25T07:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92377",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023859.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-25T07:18:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "milestone": "sage-4.5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9580#event-23859"
}
```



---

archive/issue_comments_092378.json:
```json
{
    "body": "If no one objects, I'll list Tim as this ticket's author.",
    "created_at": "2010-07-25T07:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92378",
    "user": "https://github.com/qed777"
}
```

If no one objects, I'll list Tim as this ticket's author.



---

archive/issue_comments_092379.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-25T07:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92379",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092380.json:
```json
{
    "body": "It should be safe to delete `sagenb/sagenb.po`, particularly since #9428 has not merged.",
    "created_at": "2010-07-25T07:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92380",
    "user": "https://github.com/qed777"
}
```

It should be safe to delete `sagenb/sagenb.po`, particularly since #9428 has not merged.



---

archive/issue_comments_092381.json:
```json
{
    "body": "I've merged this ticket into the latest SageNB 0.8.2 at #9572.",
    "created_at": "2010-07-25T07:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92381",
    "user": "https://github.com/qed777"
}
```

I've merged this ticket into the latest SageNB 0.8.2 at #9572.



---

archive/issue_comments_092382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-25T07:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92382",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023860.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-25T07:56:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9580#event-23860"
}
```
