# Issue 6327: optional doctest failure -- failure using pari C library

archive/issues_006327.json:
```json
{
    "body": "Assignee: tbd\n\nWhat's up with this?\n\n\n```\nsage -t -long --optional devel/sage/sage/libs/pari/gen.pyx\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/libs/pari/gen.pyx\", line 5801:\n    sage: e.ellpow([0,0], I+1) # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_177[4]>\", line 1, in <module>\n        e.ellpow([Integer(0),Integer(0)], I+Integer(1)) # optional###line 5801:\n    sage: e.ellpow([0,0], I+1) # optional\n      File \"gen.pyx\", line 9170, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44129)\n        raise PariError, errno\n    PariError: sorry, (15)\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_177\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wst\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6327\n\n",
    "created_at": "2009-06-16T15:04:26Z",
    "labels": [
        "optional packages",
        "major",
        "bug"
    ],
    "title": "optional doctest failure -- failure using pari C library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6327",
    "user": "was"
}
```
Assignee: tbd

What's up with this?


```
sage -t -long --optional devel/sage/sage/libs/pari/gen.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/libs/pari/gen.pyx", line 5801:
    sage: e.ellpow([0,0], I+1) # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_177[4]>", line 1, in <module>
        e.ellpow([Integer(0),Integer(0)], I+Integer(1)) # optional###line 5801:
    sage: e.ellpow([0,0], I+1) # optional
      File "gen.pyx", line 9170, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44129)
        raise PariError, errno
    PariError: sorry, (15)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_177
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wst
```


Issue created by migration from https://trac.sagemath.org/ticket/6327





---

archive/issue_comments_050503.json:
```json
{
    "body": "Changing component from optional packages to packages.",
    "created_at": "2010-08-01T16:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50503",
    "user": "jdemeyer"
}
```

Changing component from optional packages to packages.



---

archive/issue_comments_050504.json:
```json
{
    "body": "It means that complex multiplication for elliptic curves is not implemented in PARI/GP.  Like \"it would be nice if this would work, but it doesn't\".  Not sure what the correct keyword is for that :-)",
    "created_at": "2010-08-01T16:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50504",
    "user": "jdemeyer"
}
```

It means that complex multiplication for elliptic curves is not implemented in PARI/GP.  Like "it would be nice if this would work, but it doesn't".  Not sure what the correct keyword is for that :-)



---

archive/issue_comments_050505.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari cm curve ellpow\".",
    "created_at": "2010-09-16T21:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50505",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "pari cm curve ellpow".



---

archive/issue_comments_050506.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2010-09-16T21:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50506",
    "user": "jdemeyer"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_050507.json:
```json
{
    "body": "Changing assignee from tbd to mvngu.",
    "created_at": "2010-09-16T21:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50507",
    "user": "jdemeyer"
}
```

Changing assignee from tbd to mvngu.



---

archive/issue_comments_050508.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T07:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50508",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050509.json:
```json
{
    "body": "Changing keywords from \"pari cm curve ellpow\" to \"pari ellpow complex multiplication elliptic curve\".",
    "created_at": "2010-09-17T07:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50509",
    "user": "jdemeyer"
}
```

Changing keywords from "pari cm curve ellpow" to "pari ellpow complex multiplication elliptic curve".



---

archive/issue_comments_050510.json:
```json
{
    "body": "Attachment [6327_ellpow_cm.patch](tarball://root/attachments/some-uuid/ticket6327/6327_ellpow_cm.patch) by jdemeyer created at 2010-09-19 11:51:27",
    "created_at": "2010-09-19T11:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50510",
    "user": "jdemeyer"
}
```

Attachment [6327_ellpow_cm.patch](tarball://root/attachments/some-uuid/ticket6327/6327_ellpow_cm.patch) by jdemeyer created at 2010-09-19 11:51:27



---

archive/issue_comments_050511.json:
```json
{
    "body": "Changing component from doctest to elliptic curves.",
    "created_at": "2010-09-19T11:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50511",
    "user": "jdemeyer"
}
```

Changing component from doctest to elliptic curves.



---

archive/issue_comments_050512.json:
```json
{
    "body": "Looks good and all doctests pass. See #9977 for a follow-up ticket. (I wonder who will get to open the golden ticket #10000?)",
    "created_at": "2010-09-23T12:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50512",
    "user": "davidloeffler"
}
```

Looks good and all doctests pass. See #9977 for a follow-up ticket. (I wonder who will get to open the golden ticket #10000?)



---

archive/issue_comments_050513.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T12:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50513",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050514.json:
```json
{
    "body": "Replying to [comment:7 davidloeffler]:\n> Looks good and all doctests pass. See #9977 for a follow-up ticket. (I wonder who will get to open the golden ticket #10000?)\n\nThanks for the review and I completely agree with the follow-up ticket.",
    "created_at": "2010-09-23T14:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50514",
    "user": "jdemeyer"
}
```

Replying to [comment:7 davidloeffler]:
> Looks good and all doctests pass. See #9977 for a follow-up ticket. (I wonder who will get to open the golden ticket #10000?)

Thanks for the review and I completely agree with the follow-up ticket.



---

archive/issue_comments_050515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6327#issuecomment-50515",
    "user": "mpatel"
}
```

Resolution: fixed
