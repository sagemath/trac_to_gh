# Issue 7102: [with patch, positive review] R.py doctest fails for non-english locale

archive/issues_007102.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nTesting Sage-4.1.2-alpha4, I saw that the old failure from #6379 somehow was resurrected (probably by using some new version of the R package that has changed its internationalized warning messages). To reproduce the failure, do something (or nothing, see also #6379) like\n\n```\nexport LANG=de_DE.UTF-8\n```\nfrom a (sage -sh) shell and then you'll get:\n\n```\nsage -t -long \"devel/sage/sage/interfaces/r.py\"             \n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/interfaces/r.py\", line 549:\n    sage: r.library('foobar')\nExpected:\n    Traceback (most recent call last):\n    ...\n    ImportError: ...\nGot nothing\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/interfaces/r.py\", line 839:\n    sage: r.completions('tes')\nExpected:\n    ['testInheritedMethods', 'testPlatformEquivalence', 'testVirtual']\nGot:\n    ['testInheritedMethods', 'testInheritedMethods', 'testPlatformEquivalence', 'testPlatformEquivalence', 'testVirtual', 'testVirtual']\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_17\n   1 of   4 in __main__.example_34\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_r.py\n         [7.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage/sage/interfaces/r.py\"\n```\nFortunately, I fiddled around with this file and this bug more than once (see also #6594, #6646), so I knew where to look. Hopefully, this zombie is put down to rest ... \n\nIssue created by migration from https://trac.sagemath.org/ticket/7102\n\n",
    "closed_at": "2009-10-05T03:00:57Z",
    "created_at": "2009-10-03T19:14:40Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] R.py doctest fails for non-english locale",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7102",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: GeorgSWeber

Testing Sage-4.1.2-alpha4, I saw that the old failure from #6379 somehow was resurrected (probably by using some new version of the R package that has changed its internationalized warning messages). To reproduce the failure, do something (or nothing, see also #6379) like

```
export LANG=de_DE.UTF-8
```
from a (sage -sh) shell and then you'll get:

```
sage -t -long "devel/sage/sage/interfaces/r.py"             
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/interfaces/r.py", line 549:
    sage: r.library('foobar')
Expected:
    Traceback (most recent call last):
    ...
    ImportError: ...
Got nothing
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/interfaces/r.py", line 839:
    sage: r.completions('tes')
Expected:
    ['testInheritedMethods', 'testPlatformEquivalence', 'testVirtual']
Got:
    ['testInheritedMethods', 'testInheritedMethods', 'testPlatformEquivalence', 'testPlatformEquivalence', 'testVirtual', 'testVirtual']
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_17
   1 of   4 in __main__.example_34
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_r.py
         [7.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/interfaces/r.py"
```
Fortunately, I fiddled around with this file and this bug more than once (see also #6594, #6646), so I knew where to look. Hopefully, this zombie is put down to rest ... 

Issue created by migration from https://trac.sagemath.org/ticket/7102





---

archive/issue_comments_058669.json:
```json
{
    "body": "tested against 4.1.2.alpha4",
    "created_at": "2009-10-03T19:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7102#issuecomment-58669",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

tested against 4.1.2.alpha4



---

archive/issue_comments_058670.json:
```json
{
    "body": "Changing assignee from tbd to GeorgSWeber.",
    "created_at": "2009-10-03T19:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7102#issuecomment-58670",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing assignee from tbd to GeorgSWeber.



---

archive/issue_comments_058671.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-10-03T19:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7102#issuecomment-58671",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_058672.json:
```json
{
    "body": "Attachment [trac_7102_doctest.patch](tarball://root/attachments/some-uuid/ticket7102/trac_7102_doctest.patch) by GeorgSWeber created at 2009-10-03 19:19:29",
    "created_at": "2009-10-03T19:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7102#issuecomment-58672",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac_7102_doctest.patch](tarball://root/attachments/some-uuid/ticket7102/trac_7102_doctest.patch) by GeorgSWeber created at 2009-10-03 19:19:29



---

archive/issue_comments_058673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-05T03:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7102#issuecomment-58673",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_016796.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-05T03:00:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7102#event-16796"
}
```



---

archive/issue_comments_058674.json:
```json
{
    "body": "merged in sage-4.1.2.rc1...",
    "created_at": "2009-10-05T03:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7102#issuecomment-58674",
    "user": "https://github.com/williamstein"
}
```

merged in sage-4.1.2.rc1...
