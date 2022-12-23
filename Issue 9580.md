# Issue 9580: Check in or ignore sagenb.po in SageNB package

archive/issues_009580.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  timdumol\n\nNoted by Leif Leonhardy in a [comment:ticket:9554:5 comment] at #9554:\n\n```sh\nleif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status\n? sagenb/sagenb.po\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9580\n\n",
    "created_at": "2010-07-23T06:28:05Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Check in or ignore sagenb.po in SageNB package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9580",
    "user": "mpatel"
}
```
Assignee: jason, was

CC:  timdumol

Noted by Leif Leonhardy in a [comment:ticket:9554:5 comment] at #9554:

```sh
leif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status
? sagenb/sagenb.po
```



Issue created by migration from https://trac.sagemath.org/ticket/9580





---

archive/issue_comments_092527.json:
```json
{
    "body": "\n```\n<timdumol> _leif: Thanks for spotting the rogue .po file (I forgot to remove it from #9428 when I build 0.8.1)\n```\n\n(About 14 hours ago.)\n\nNevertheless, I'll add it to #9572 (SageNB 0.8.2).",
    "created_at": "2010-07-23T07:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92527",
    "user": "leif"
}
```


```
<timdumol> _leif: Thanks for spotting the rogue .po file (I forgot to remove it from #9428 when I build 0.8.1)
```

(About 14 hours ago.)

Nevertheless, I'll add it to #9572 (SageNB 0.8.2).



---

archive/issue_comments_092528.json:
```json
{
    "body": "\n```sh\nfind . -name .hg -exec sh -c \"cd {}; hg status\" \\;\n```\n\n\n;-)",
    "created_at": "2010-07-23T07:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92528",
    "user": "leif"
}
```


```sh
find . -name .hg -exec sh -c "cd {}; hg status" \;
```


;-)



---

archive/issue_comments_092529.json:
```json
{
    "body": "Just to check:  Should I just delete `sagenb/sagenb.po`?",
    "created_at": "2010-07-23T07:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92529",
    "user": "mpatel"
}
```

Just to check:  Should I just delete `sagenb/sagenb.po`?



---

archive/issue_comments_092530.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Just to check:  Should I just delete `sagenb/sagenb.po`?\n\nAccording to what Tim said, I think yes.",
    "created_at": "2010-07-23T07:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92530",
    "user": "leif"
}
```

Replying to [comment:3 mpatel]:
> Just to check:  Should I just delete `sagenb/sagenb.po`?

According to what Tim said, I think yes.



---

archive/issue_comments_092531.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-25T07:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92531",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092532.json:
```json
{
    "body": "If no one objects, I'll list Tim as this ticket's author.",
    "created_at": "2010-07-25T07:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92532",
    "user": "mpatel"
}
```

If no one objects, I'll list Tim as this ticket's author.



---

archive/issue_comments_092533.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-25T07:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92533",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092534.json:
```json
{
    "body": "It should be safe to delete `sagenb/sagenb.po`, particularly since #9428 has not merged.",
    "created_at": "2010-07-25T07:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92534",
    "user": "mpatel"
}
```

It should be safe to delete `sagenb/sagenb.po`, particularly since #9428 has not merged.



---

archive/issue_comments_092535.json:
```json
{
    "body": "I've merged this ticket into the latest SageNB 0.8.2 at #9572.",
    "created_at": "2010-07-25T07:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92535",
    "user": "mpatel"
}
```

I've merged this ticket into the latest SageNB 0.8.2 at #9572.



---

archive/issue_comments_092536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-25T07:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9580#issuecomment-92536",
    "user": "mpatel"
}
```

Resolution: fixed
