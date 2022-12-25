# Issue 5524: attrcall missing __cmp__

archive/issues_005524.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat @jbandlow\n\nsage: f = attrcall(\"bla\")\nsage: dumps(f)\nsage: loads(dumps(f)) == f\nFalse\n\nThis is because AttrCallObject doesn't have a __cmp__ method:\n\nIssue created by migration from https://trac.sagemath.org/ticket/5524\n\n",
    "created_at": "2009-03-15T05:03:19Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "attrcall missing __cmp__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5524",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_042892.json:
```json
{
    "body": "Changing keywords from \"\" to \"attrcall, pickling\".",
    "created_at": "2010-01-26T21:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42892",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "attrcall, pickling".



---

archive/issue_comments_042893.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T21:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42893",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042894.json:
```json
{
    "body": "Attachment [trac_5524_attrcall_eq.patch](tarball://root/attachments/some-uuid/ticket5524/trac_5524_attrcall_eq.patch) by @nthiery created at 2010-01-26 21:30:26",
    "created_at": "2010-01-26T21:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42894",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_5524_attrcall_eq.patch](tarball://root/attachments/some-uuid/ticket5524/trac_5524_attrcall_eq.patch) by @nthiery created at 2010-01-26 21:30:26



---

archive/issue_comments_042895.json:
```json
{
    "body": "Changing assignee from cwitty to @nthiery.",
    "created_at": "2010-01-26T21:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42895",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from cwitty to @nthiery.



---

archive/issue_comments_042896.json:
```json
{
    "body": "I'm getting a failing doctest:\n\n```\nsage -t  \"devel/sage-trac/sage/misc/misc.py\"                \n**********************************************************************\nFile \"/usr/local/src/sage/devel/sage-trac/sage/misc/misc.py\", line 2103:\n    sage: TestSuite(f).run()\nException raised:\n...\nAttributeError: 'AttrCallObject' object has no attribute '_tester'\n```\n\n\nI'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?",
    "created_at": "2010-01-26T21:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42896",
    "user": "https://github.com/jbandlow"
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

archive/issue_comments_042897.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T21:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42897",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_042898.json:
```json
{
    "body": "Replying to [comment:4 jbandlow]:\n> I'm getting a failing doctest:\n> I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?\n\nI should have mentioned it depends on #8001.",
    "created_at": "2010-01-26T21:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42898",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 jbandlow]:
> I'm getting a failing doctest:
> I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?

I should have mentioned it depends on #8001.



---

archive/issue_comments_042899.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T21:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42899",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042900.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-26T21:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42900",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042901.json:
```json
{
    "body": "Thanks.  That fixes it.  Passes tests and looks good to me.",
    "created_at": "2010-01-26T21:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42901",
    "user": "https://github.com/jbandlow"
}
```

Thanks.  That fixes it.  Passes tests and looks good to me.



---

archive/issue_comments_042902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5524#issuecomment-42902",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
