# Issue 9580: Check in or ignore sagenb.po in SageNB package

Issue created by migration from https://trac.sagemath.org/ticket/9580

Original creator: mpatel

Original creation time: 2010-07-23 06:28:05

Assignee: jason, was

CC:  timdumol

Noted by Leif Leonhardy in a [comment:ticket:9554:5 comment] at #9554:

```sh
leif@portland:~/Sage/spkgs/sagenb-0.8.1.p1/src/sagenb$ hg status
? sagenb/sagenb.po
```




---

Comment by leif created at 2010-07-23 07:03:14


```
<timdumol> _leif: Thanks for spotting the rogue .po file (I forgot to remove it from #9428 when I build 0.8.1)
```

(About 14 hours ago.)

Nevertheless, I'll add it to #9572 (SageNB 0.8.2).


---

Comment by leif created at 2010-07-23 07:16:58


```sh
find . -name .hg -exec sh -c "cd {}; hg status" \;
```


;-)


---

Comment by mpatel created at 2010-07-23 07:26:30

Just to check:  Should I just delete `sagenb/sagenb.po`?


---

Comment by leif created at 2010-07-23 07:27:35

Replying to [comment:3 mpatel]:
> Just to check:  Should I just delete `sagenb/sagenb.po`?

According to what Tim said, I think yes.


---

Comment by mpatel created at 2010-07-25 07:18:08

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-07-25 07:18:08

If no one objects, I'll list Tim as this ticket's author.


---

Comment by mpatel created at 2010-07-25 07:21:03

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-25 07:21:03

It should be safe to delete `sagenb/sagenb.po`, particularly since #9428 has not merged.


---

Comment by mpatel created at 2010-07-25 07:55:35

I've merged this ticket into the latest SageNB 0.8.2 at #9572.


---

Comment by mpatel created at 2010-07-25 07:56:46

Resolution: fixed
