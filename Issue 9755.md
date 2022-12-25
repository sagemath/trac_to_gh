# Issue 9755: Symmetric Function coercion issue

archive/issues_009755.json:
```json
{
    "body": "Assignee: @jbandlow\n\nCC:  sage-combinat\n\nKeywords: symmetric functions\n\nThe following was reported to me by Nicolas Thi\u00e9ry and Lenny Tevlin.\n\n\n```\nR.<q,t> = ZZ[]\nR = FractionField(R)\nP = MacdonaldPolynomialsP(R,q,t) \nQ = HallLittlewoodQ(R,t) # or Q or P (Qp = H)\nPh=HallLittlewoodP(R,t)\nSF = SymmetricFunctions(R)\nSF.inject_shorthands()\nQ(s.one())\n\nTraceback (click to the left of this block for traceback)\n...\nAttributeError: 'int' object has no attribute 'subs'\n```\n\nThe same error occurs with `Ph(s.one())`, although `P(s.one())` works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9755\n\n",
    "created_at": "2010-08-17T15:27:40Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Symmetric Function coercion issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9755",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @jbandlow

CC:  sage-combinat

Keywords: symmetric functions

The following was reported to me by Nicolas Thiéry and Lenny Tevlin.


```
R.<q,t> = ZZ[]
R = FractionField(R)
P = MacdonaldPolynomialsP(R,q,t) 
Q = HallLittlewoodQ(R,t) # or Q or P (Qp = H)
Ph=HallLittlewoodP(R,t)
SF = SymmetricFunctions(R)
SF.inject_shorthands()
Q(s.one())

Traceback (click to the left of this block for traceback)
...
AttributeError: 'int' object has no attribute 'subs'
```

The same error occurs with `Ph(s.one())`, although `P(s.one())` works.

Issue created by migration from https://trac.sagemath.org/ticket/9755





---

archive/issue_comments_095388.json:
```json
{
    "body": "Ready for review.",
    "created_at": "2010-08-19T19:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95388",
    "user": "https://github.com/jbandlow"
}
```

Ready for review.



---

archive/issue_comments_095389.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-19T19:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95389",
    "user": "https://github.com/jbandlow"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095390.json:
```json
{
    "body": "Note for combinat people: I've put this patch in the 'needs review' section of the queue.",
    "created_at": "2010-08-19T19:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95390",
    "user": "https://github.com/jbandlow"
}
```

Note for combinat people: I've put this patch in the 'needs review' section of the queue.



---

archive/issue_comments_095391.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T00:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95391",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095392.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-17T00:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95392",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_095393.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-18T07:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95393",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095394.json:
```json
{
    "body": "Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?",
    "created_at": "2010-09-18T07:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95394",
    "user": "https://github.com/qed777"
}
```

Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?



---

archive/issue_comments_095395.json:
```json
{
    "body": "Attachment [trac_9755_hall_littlewood_coercions-jb.patch](tarball://root/attachments/some-uuid/ticket9755/trac_9755_hall_littlewood_coercions-jb.patch) by @jbandlow created at 2010-09-18 14:28:04",
    "created_at": "2010-09-18T14:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95395",
    "user": "https://github.com/jbandlow"
}
```

Attachment [trac_9755_hall_littlewood_coercions-jb.patch](tarball://root/attachments/some-uuid/ticket9755/trac_9755_hall_littlewood_coercions-jb.patch) by @jbandlow created at 2010-09-18 14:28:04



---

archive/issue_comments_095396.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?\n\nOops, sorry about that.  Fixed.",
    "created_at": "2010-09-18T14:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95396",
    "user": "https://github.com/jbandlow"
}
```

Replying to [comment:4 mpatel]:
> Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?

Oops, sorry about that.  Fixed.



---

archive/issue_comments_095397.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-18T14:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95397",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095398.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-18T14:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95398",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095399.json:
```json
{
    "body": "Could you move `#9755: Fix...` to the first line of the commit string?  Otherwise, `hg log` gives, e.g.,\n\n```\nchangeset:   14948:0b3960059b6c\ntag:         qtip\ntag:         trac_9755_hall_littlewood_coercions-jb.patch\ntag:         tip\nuser:        Jason Bandlow <...>\ndate:        Thu Aug 19 15:08:26 2010 -0400\nsummary:     [mq]: trac_9755_hall_littlewood_coercions-jb.patch\n```\n",
    "created_at": "2010-09-18T20:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95399",
    "user": "https://github.com/qed777"
}
```

Could you move `#9755: Fix...` to the first line of the commit string?  Otherwise, `hg log` gives, e.g.,

```
changeset:   14948:0b3960059b6c
tag:         qtip
tag:         trac_9755_hall_littlewood_coercions-jb.patch
tag:         tip
user:        Jason Bandlow <...>
date:        Thu Aug 19 15:08:26 2010 -0400
summary:     [mq]: trac_9755_hall_littlewood_coercions-jb.patch
```




---

archive/issue_comments_095400.json:
```json
{
    "body": "Attachment [trac_9755_hall_littlewood_coercions-jb.2.patch](tarball://root/attachments/some-uuid/ticket9755/trac_9755_hall_littlewood_coercions-jb.2.patch) by @jbandlow created at 2010-09-18 21:52:28",
    "created_at": "2010-09-18T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95400",
    "user": "https://github.com/jbandlow"
}
```

Attachment [trac_9755_hall_littlewood_coercions-jb.2.patch](tarball://root/attachments/some-uuid/ticket9755/trac_9755_hall_littlewood_coercions-jb.2.patch) by @jbandlow created at 2010-09-18 21:52:28



---

archive/issue_comments_095401.json:
```json
{
    "body": "Sorry.  How's the new version (I forgot to overwrite the old one)?",
    "created_at": "2010-09-18T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95401",
    "user": "https://github.com/jbandlow"
}
```

Sorry.  How's the new version (I forgot to overwrite the old one)?



---

archive/issue_comments_095402.json:
```json
{
    "body": "Replying to [comment:8 jbandlow]:\n> Sorry.  How's the new version (I forgot to overwrite the old one)?\n\nNo worries.  V2 looks good.  Thanks!",
    "created_at": "2010-09-18T22:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95402",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:8 jbandlow]:
> Sorry.  How's the new version (I forgot to overwrite the old one)?

No worries.  V2 looks good.  Thanks!



---

archive/issue_events_009887.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T04:25:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9755#event-9887"
}
```



---

archive/issue_comments_095403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95403",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
