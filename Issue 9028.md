# Issue 9028: Basic Stats - Standard Deviation

archive/issues_009028.json:
```json
{
    "body": "Assignee: amhou\n\nFixes the calculation of standard deviation. \n\nPreviously, sample standard deviation had returned a denominator of n, this fix gives a denominator of n-1. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9028\n\n",
    "created_at": "2010-05-24T06:53:23Z",
    "labels": [
        "statistics",
        "minor",
        "bug"
    ],
    "title": "Basic Stats - Standard Deviation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9028",
    "user": "amhou"
}
```
Assignee: amhou

Fixes the calculation of standard deviation. 

Previously, sample standard deviation had returned a denominator of n, this fix gives a denominator of n-1. 

Issue created by migration from https://trac.sagemath.org/ticket/9028





---

archive/issue_comments_083550.json:
```json
{
    "body": "Attachment [trac_9028_stats.patch](tarball://root/attachments/some-uuid/ticket9028/trac_9028_stats.patch) by amhou created at 2010-05-24 06:53:54",
    "created_at": "2010-05-24T06:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83550",
    "user": "amhou"
}
```

Attachment [trac_9028_stats.patch](tarball://root/attachments/some-uuid/ticket9028/trac_9028_stats.patch) by amhou created at 2010-05-24 06:53:54



---

archive/issue_comments_083551.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T07:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83551",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083552.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-24T07:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83552",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083553.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-05-24T20:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83553",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083554.json:
```json
{
    "body": "Please add a new example to the docstring that illustrates that this bug has been fixed.",
    "created_at": "2010-05-24T20:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83554",
    "user": "was"
}
```

Please add a new example to the docstring that illustrates that this bug has been fixed.



---

archive/issue_comments_083555.json:
```json
{
    "body": "fix plus an example to test it",
    "created_at": "2010-11-18T22:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83555",
    "user": "benjaminfjones"
}
```

fix plus an example to test it



---

archive/issue_comments_083556.json:
```json
{
    "body": "Attachment [trac_9028_stats_fix+example.patch](tarball://root/attachments/some-uuid/ticket9028/trac_9028_stats_fix+example.patch) by benjaminfjones created at 2010-11-18 22:18:49\n\nI've attached a new patch witch includes the fix plus an example to test the affected block of code. I couldn't think of a better way to access the block than to define a toy class that has its own mean() function which returns a Python long. If the mean() function from basic_stats.py has to be called, the type of 'x' at line 289 won't ever be 'int' or 'long' so the code block in question is never reached.\n\nMaybe someone can suggest a better example?\n\nHere is a before / after log to show that the fix works and that the example tests it.\n\n\n```\n\nsage: R = SillyPythonList()\nsage: list(R)\n[2L, 4L]\nsage: len(R)\n2\nsage: mean(R)\n3L\nsage: variance(R)\n1\nsage: variance(R, bias=True)\n1\n\nsage: R = [2,4]\nsage: mean(R)\n3\nsage: variance(R)\n2\nsage: variance(R,bias=True)\n1\n\n### LOG (after patch)\nsage: R=SillyPythonList()\nsage: len(R)\n2\nsage: mean(R)\n3L\nsage: variance(R)\n2\nsage: variance(R, bias=True)\n1\nsage: R = [2,4]\nsage: variance(R)\n2\nsage: variance(R, bias=True)\n1\n```\n",
    "created_at": "2010-11-18T22:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83556",
    "user": "benjaminfjones"
}
```

Attachment [trac_9028_stats_fix+example.patch](tarball://root/attachments/some-uuid/ticket9028/trac_9028_stats_fix+example.patch) by benjaminfjones created at 2010-11-18 22:18:49

I've attached a new patch witch includes the fix plus an example to test the affected block of code. I couldn't think of a better way to access the block than to define a toy class that has its own mean() function which returns a Python long. If the mean() function from basic_stats.py has to be called, the type of 'x' at line 289 won't ever be 'int' or 'long' so the code block in question is never reached.

Maybe someone can suggest a better example?

Here is a before / after log to show that the fix works and that the example tests it.


```

sage: R = SillyPythonList()
sage: list(R)
[2L, 4L]
sage: len(R)
2
sage: mean(R)
3L
sage: variance(R)
1
sage: variance(R, bias=True)
1

sage: R = [2,4]
sage: mean(R)
3
sage: variance(R)
2
sage: variance(R,bias=True)
1

### LOG (after patch)
sage: R=SillyPythonList()
sage: len(R)
2
sage: mean(R)
3L
sage: variance(R)
2
sage: variance(R, bias=True)
1
sage: R = [2,4]
sage: variance(R)
2
sage: variance(R, bias=True)
1
```




---

archive/issue_comments_083557.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-18T22:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83557",
    "user": "benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083558.json:
```json
{
    "body": "Replying to [comment:5 benjaminfjones]:\n\n... and I made sure the doctest passes for the new example. I'm applying the patch to Sage Version 4.6.1.alpha1.",
    "created_at": "2010-11-18T22:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83558",
    "user": "benjaminfjones"
}
```

Replying to [comment:5 benjaminfjones]:

... and I made sure the doctest passes for the new example. I'm applying the patch to Sage Version 4.6.1.alpha1.



---

archive/issue_comments_083559.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-22T01:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83559",
    "user": "spice"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083560.json:
```json
{
    "body": "Changing keywords from \"\" to \"standard deviation\".",
    "created_at": "2011-03-22T01:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83560",
    "user": "spice"
}
```

Changing keywords from "" to "standard deviation".



---

archive/issue_comments_083561.json:
```json
{
    "body": "All good (reviewed trac_9028_stats_fix+example.patch; trac_9028_stats.patch is obsolete).",
    "created_at": "2011-03-22T01:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83561",
    "user": "spice"
}
```

All good (reviewed trac_9028_stats_fix+example.patch; trac_9028_stats.patch is obsolete).



---

archive/issue_comments_083562.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-13T07:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9028#issuecomment-83562",
    "user": "jdemeyer"
}
```

Resolution: fixed
