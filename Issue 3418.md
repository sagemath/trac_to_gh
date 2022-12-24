# Issue 3418: added new combinatorial functions for tableaux and crystals

archive/issues_003418.json:
```json
{
    "body": "Assignee: Mike Hansen\n\nCC:  sage-combinat\n\nKeywords: promotion; reflection\n\nI added a two new functions \npromotion and promotion_inverse\nfor rectangular tableaux.\n\nI also added a reflection operator\nfor the crystal library.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3418\n\n",
    "created_at": "2008-06-13T18:30:06Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "added new combinatorial functions for tableaux and crystals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3418",
    "user": "@anneschilling"
}
```
Assignee: Mike Hansen

CC:  sage-combinat

Keywords: promotion; reflection

I added a two new functions 
promotion and promotion_inverse
for rectangular tableaux.

I also added a reflection operator
for the crystal library.

Issue created by migration from https://trac.sagemath.org/ticket/3418





---

archive/issue_comments_024060.json:
```json
{
    "body": "Attachment [promotion_reflection_for_trac.patch](tarball://root/attachments/some-uuid/ticket3418/promotion_reflection_for_trac.patch) by @anneschilling created at 2008-06-13 18:32:22",
    "created_at": "2008-06-13T18:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24060",
    "user": "@anneschilling"
}
```

Attachment [promotion_reflection_for_trac.patch](tarball://root/attachments/some-uuid/ticket3418/promotion_reflection_for_trac.patch) by @anneschilling created at 2008-06-13 18:32:22



---

archive/issue_comments_024061.json:
```json
{
    "body": "Hi Anne,\n\nThe one thing I would change is that instead of returning the string \"Tableaux is not rectangular\" is raising a ValueError with that message.  Also, could you add a line before \"EXAMPLES\" in \"def s(\"?\n\nOther than that, it looks good to go in.\n\n--Mike",
    "created_at": "2008-06-13T18:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24061",
    "user": "@mwhansen"
}
```

Hi Anne,

The one thing I would change is that instead of returning the string "Tableaux is not rectangular" is raising a ValueError with that message.  Also, could you add a line before "EXAMPLES" in "def s("?

Other than that, it looks good to go in.

--Mike



---

archive/issue_comments_024062.json:
```json
{
    "body": "Oh, the doctest for the ValueError would look something like this:\n\n\n```\nsage: t = Tableau([[1,2],[2]]) \nsage: t.promotion(3) \nTraceback (most recent call last):\n...\nValueError: Tableaux is not recutangular\n\n```\n",
    "created_at": "2008-06-13T18:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24062",
    "user": "@mwhansen"
}
```

Oh, the doctest for the ValueError would look something like this:


```
sage: t = Tableau([[1,2],[2]]) 
sage: t.promotion(3) 
Traceback (most recent call last):
...
ValueError: Tableaux is not recutangular

```




---

archive/issue_comments_024063.json:
```json
{
    "body": "fixed the issues that Mike raised",
    "created_at": "2008-06-13T19:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24063",
    "user": "@anneschilling"
}
```

fixed the issues that Mike raised



---

archive/issue_comments_024064.json:
```json
{
    "body": "Attachment [promotion_reflection-3418-submitted.patch](tarball://root/attachments/some-uuid/ticket3418/promotion_reflection-3418-submitted.patch) by @mwhansen created at 2008-06-13 22:37:32",
    "created_at": "2008-06-13T22:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24064",
    "user": "@mwhansen"
}
```

Attachment [promotion_reflection-3418-submitted.patch](tarball://root/attachments/some-uuid/ticket3418/promotion_reflection-3418-submitted.patch) by @mwhansen created at 2008-06-13 22:37:32



---

archive/issue_comments_024065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T22:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24065",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024066.json:
```json
{
    "body": "Merged promotion_reflection-3418-submitted.patch in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T22:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3418#issuecomment-24066",
    "user": "mabshoff"
}
```

Merged promotion_reflection-3418-submitted.patch in Sage 3.0.3.rc0
