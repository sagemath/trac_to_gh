# Issue 5524: attrcall missing __cmp__

archive/issues_005524.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat @jbandlow\n\nsage: f = attrcall(\"bla\")\nsage: dumps(f)\nsage: loads(dumps(f)) == f\nFalse\n\nThis is because AttrCallObject doesn't have a __cmp__ method:\n\nIssue created by migration from https://trac.sagemath.org/ticket/5524\n\n",
    "created_at": "2009-03-15T05:03:19Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "attrcall missing __cmp__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5524",
    "user": "@nthiery"
}
```
Assignee: cwitty

CC:  sage-combinat @jbandlow

sage: f = attrcall("bla")
sage: dumps(f)
sage: loads(dumps(f)) == f
False

This is because AttrCallObject doesn't have a __cmp__ method:

Issue created by migration from https://trac.sagemath.org/ticket/5524





---

archive/issue_comments_042976.json:
```json
{
    "body": "Changing keywords from \"\" to \"attrcall, pickling\".",
    "created_at": "2010-01-26T21:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42976",
    "user": "@nthiery"
}
```

Changing keywords from "" to "attrcall, pickling".



---

archive/issue_comments_042977.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T21:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42977",
    "user": "@nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042978.json:
```json
{
    "body": "Attachment [trac_5524_attrcall_eq.patch](tarball://root/attachments/some-uuid/ticket5524/trac_5524_attrcall_eq.patch) by @nthiery created at 2010-01-26 21:30:26",
    "created_at": "2010-01-26T21:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42978",
    "user": "@nthiery"
}
```

Attachment [trac_5524_attrcall_eq.patch](tarball://root/attachments/some-uuid/ticket5524/trac_5524_attrcall_eq.patch) by @nthiery created at 2010-01-26 21:30:26



---

archive/issue_comments_042979.json:
```json
{
    "body": "Changing assignee from cwitty to @nthiery.",
    "created_at": "2010-01-26T21:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42979",
    "user": "@nthiery"
}
```

Changing assignee from cwitty to @nthiery.



---

archive/issue_comments_042980.json:
```json
{
    "body": "I'm getting a failing doctest:\n\n```\nsage -t  \"devel/sage-trac/sage/misc/misc.py\"                \n**********************************************************************\nFile \"/usr/local/src/sage/devel/sage-trac/sage/misc/misc.py\", line 2103:\n    sage: TestSuite(f).run()\nException raised:\n...\nAttributeError: 'AttrCallObject' object has no attribute '_tester'\n```\n\n\nI'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?",
    "created_at": "2010-01-26T21:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42980",
    "user": "@jbandlow"
}
```

I'm getting a failing doctest:

```
sage -t  "devel/sage-trac/sage/misc/misc.py"                
**********************************************************************
File "/usr/local/src/sage/devel/sage-trac/sage/misc/misc.py", line 2103:
    sage: TestSuite(f).run()
Exception raised:
...
AttributeError: 'AttrCallObject' object has no attribute '_tester'
```


I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?



---

archive/issue_comments_042981.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T21:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42981",
    "user": "@jbandlow"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_042982.json:
```json
{
    "body": "Replying to [comment:4 jbandlow]:\n> I'm getting a failing doctest:\n> I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?\n\nI should have mentioned it depends on #8001.",
    "created_at": "2010-01-26T21:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42982",
    "user": "@nthiery"
}
```

Replying to [comment:4 jbandlow]:
> I'm getting a failing doctest:
> I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?

I should have mentioned it depends on #8001.



---

archive/issue_comments_042983.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T21:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42983",
    "user": "@nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042984.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-26T21:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42984",
    "user": "@jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042985.json:
```json
{
    "body": "Thanks.  That fixes it.  Passes tests and looks good to me.",
    "created_at": "2010-01-26T21:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42985",
    "user": "@jbandlow"
}
```

Thanks.  That fixes it.  Passes tests and looks good to me.



---

archive/issue_comments_042986.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42986",
    "user": "mvngu"
}
```

Resolution: fixed
