# Issue 6379: #2513 made R.py doctest fail for non-english locale

archive/issues_006379.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn ticket #276, the LANG environment variable was set in sage-env (to en_US.UTF-8) and in ticket #2513, this was undone. On my box, the following doctest failure was a consequence:\n\n```\nsage -t -long \"devel/sage/sage/interfaces/r.py\"             \n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.0.2/devel/sage/sage/interfaces/r.py\", line 554:\n    sage: r.library('foobar')\nExpected:\n    Traceback (most recent call last):\n    ...\n    ImportError: there is no package called 'foobar'\nGot nothing\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.0.2/devel/sage/sage/interfaces/r.py\", line 840:\n    sage: r.completions('tes')\nExpected:\n    ['testPlatformEquivalence', 'testVirtual']\nGot:\n    ['testPlatformEquivalence', 'testPlatformEquivalence', 'testVirtual', 'testVirtual']\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_17\n   1 of   3 in __main__.example_34\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/Shared/sage/sage-4.0.2/tmp/.doctest_r.py\n         [6.3 s]\n```\n\nI have *none* of the usual \"locale\" variables set (LANG, LC_ALL, ...) but nevertheless R is clever enough to detect that I might want read its messages in german. (It's using some Mac OS feature, I think.) But unfortunately the Sage code did parse for english key-words in the R messages. \nAnyway, the above doctest failure could be triggered by anyone by issuing e.g. \"export LANG=de_DE.UTF-8\" just before running the doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6379\n\n",
    "created_at": "2009-06-21T21:49:20Z",
    "labels": [
        "interfaces",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "#2513 made R.py doctest fail for non-english locale",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6379",
    "user": "GeorgSWeber"
}
```
Assignee: @williamstein

In ticket #276, the LANG environment variable was set in sage-env (to en_US.UTF-8) and in ticket #2513, this was undone. On my box, the following doctest failure was a consequence:

```
sage -t -long "devel/sage/sage/interfaces/r.py"             
**********************************************************************
File "/Users/Shared/sage/sage-4.0.2/devel/sage/sage/interfaces/r.py", line 554:
    sage: r.library('foobar')
Expected:
    Traceback (most recent call last):
    ...
    ImportError: there is no package called 'foobar'
Got nothing
**********************************************************************
File "/Users/Shared/sage/sage-4.0.2/devel/sage/sage/interfaces/r.py", line 840:
    sage: r.completions('tes')
Expected:
    ['testPlatformEquivalence', 'testVirtual']
Got:
    ['testPlatformEquivalence', 'testPlatformEquivalence', 'testVirtual', 'testVirtual']
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_17
   1 of   3 in __main__.example_34
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/Shared/sage/sage-4.0.2/tmp/.doctest_r.py
         [6.3 s]
```

I have *none* of the usual "locale" variables set (LANG, LC_ALL, ...) but nevertheless R is clever enough to detect that I might want read its messages in german. (It's using some Mac OS feature, I think.) But unfortunately the Sage code did parse for english key-words in the R messages. 
Anyway, the above doctest failure could be triggered by anyone by issuing e.g. "export LANG=de_DE.UTF-8" just before running the doctest.

Issue created by migration from https://trac.sagemath.org/ticket/6379





---

archive/issue_comments_051064.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-21T21:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51064",
    "user": "GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051065.json:
```json
{
    "body": "Changing assignee from @williamstein to GeorgSWeber.",
    "created_at": "2009-06-21T21:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51065",
    "user": "GeorgSWeber"
}
```

Changing assignee from @williamstein to GeorgSWeber.



---

archive/issue_comments_051066.json:
```json
{
    "body": "Attachment [trac_6379-Rdoctest.patch](tarball://root/attachments/some-uuid/ticket6379/trac_6379-Rdoctest.patch) by GeorgSWeber created at 2009-06-21 21:54:06\n\ntested against 4.0.2",
    "created_at": "2009-06-21T21:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51066",
    "user": "GeorgSWeber"
}
```

Attachment [trac_6379-Rdoctest.patch](tarball://root/attachments/some-uuid/ticket6379/trac_6379-Rdoctest.patch) by GeorgSWeber created at 2009-06-21 21:54:06

tested against 4.0.2



---

archive/issue_comments_051067.json:
```json
{
    "body": "All tests passed in Sage 4.1.",
    "created_at": "2009-07-13T22:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51067",
    "user": "mvngu"
}
```

All tests passed in Sage 4.1.



---

archive/issue_comments_051068.json:
```json
{
    "body": "While testing out this patch, I came across an incidental problem. It's reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/f8da7ca9d81b506b) thread. OK, so the patch fixes a locale problem. But then comes a problem with the R interface command `r.library()`. By the way, this has nothing to do with Georg's patch.",
    "created_at": "2009-07-14T10:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51068",
    "user": "mvngu"
}
```

While testing out this patch, I came across an incidental problem. It's reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/f8da7ca9d81b506b) thread. OK, so the patch fixes a locale problem. But then comes a problem with the R interface command `r.library()`. By the way, this has nothing to do with Georg's patch.



---

archive/issue_comments_051069.json:
```json
{
    "body": "Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T10:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51069",
    "user": "mvngu"
}
```

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_051070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6379#issuecomment-51070",
    "user": "mvngu"
}
```

Resolution: fixed
