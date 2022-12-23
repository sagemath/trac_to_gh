# Issue 9755: Symmetric Function coercion issue

archive/issues_009755.json:
```json
{
    "body": "Assignee: jbandlow\n\nCC:  sage-combinat\n\nKeywords: symmetric functions\n\nThe following was reported to me by Nicolas Thi\u00e9ry and Lenny Tevlin.\n\n\n```\nR.<q,t> = ZZ[]\nR = FractionField(R)\nP = MacdonaldPolynomialsP(R,q,t) \nQ = HallLittlewoodQ(R,t) # or Q or P (Qp = H)\nPh=HallLittlewoodP(R,t)\nSF = SymmetricFunctions(R)\nSF.inject_shorthands()\nQ(s.one())\n\nTraceback (click to the left of this block for traceback)\n...\nAttributeError: 'int' object has no attribute 'subs'\n```\n\nThe same error occurs with `Ph(s.one())`, although `P(s.one())` works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9755\n\n",
    "created_at": "2010-08-17T15:27:40Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Symmetric Function coercion issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9755",
    "user": "jbandlow"
}
```
Assignee: jbandlow

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

archive/issue_comments_095547.json:
```json
{
    "body": "Ready for review.",
    "created_at": "2010-08-19T19:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95547",
    "user": "jbandlow"
}
```

Ready for review.



---

archive/issue_comments_095548.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-19T19:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95548",
    "user": "jbandlow"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095549.json:
```json
{
    "body": "Note for combinat people: I've put this patch in the 'needs review' section of the queue.",
    "created_at": "2010-08-19T19:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95549",
    "user": "jbandlow"
}
```

Note for combinat people: I've put this patch in the 'needs review' section of the queue.



---

archive/issue_comments_095550.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T00:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95550",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095551.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-17T00:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95551",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_095552.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-18T07:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95552",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095553.json:
```json
{
    "body": "Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?",
    "created_at": "2010-09-18T07:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95553",
    "user": "mpatel"
}
```

Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?



---

archive/issue_comments_095554.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-18T14:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95554",
    "user": "jbandlow"
}
```

Attachment



---

archive/issue_comments_095555.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?\n\nOops, sorry about that.  Fixed.",
    "created_at": "2010-09-18T14:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95555",
    "user": "jbandlow"
}
```

Replying to [comment:4 mpatel]:
> Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?

Oops, sorry about that.  Fixed.



---

archive/issue_comments_095556.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-18T14:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95556",
    "user": "jbandlow"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095557.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-18T14:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95557",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095558.json:
```json
{
    "body": "Could you move `#9755: Fix...` to the first line of the commit string?  Otherwise, `hg log` gives, e.g.,\n\n```\nchangeset:   14948:0b3960059b6c\ntag:         qtip\ntag:         trac_9755_hall_littlewood_coercions-jb.patch\ntag:         tip\nuser:        Jason Bandlow <...>\ndate:        Thu Aug 19 15:08:26 2010 -0400\nsummary:     [mq]: trac_9755_hall_littlewood_coercions-jb.patch\n```\n",
    "created_at": "2010-09-18T20:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95558",
    "user": "mpatel"
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

archive/issue_comments_095559.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-18T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95559",
    "user": "jbandlow"
}
```

Attachment



---

archive/issue_comments_095560.json:
```json
{
    "body": "Sorry.  How's the new version (I forgot to overwrite the old one)?",
    "created_at": "2010-09-18T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95560",
    "user": "jbandlow"
}
```

Sorry.  How's the new version (I forgot to overwrite the old one)?



---

archive/issue_comments_095561.json:
```json
{
    "body": "Replying to [comment:8 jbandlow]:\n> Sorry.  How's the new version (I forgot to overwrite the old one)?\n\nNo worries.  V2 looks good.  Thanks!",
    "created_at": "2010-09-18T22:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95561",
    "user": "mpatel"
}
```

Replying to [comment:8 jbandlow]:
> Sorry.  How's the new version (I forgot to overwrite the old one)?

No worries.  V2 looks good.  Thanks!



---

archive/issue_comments_095562.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9755#issuecomment-95562",
    "user": "mpatel"
}
```

Resolution: fixed
