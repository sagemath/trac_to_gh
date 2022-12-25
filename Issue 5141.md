# Issue 5141: tinymce should be disabled on published worksheets

archive/issues_005141.json:
```json
{
    "body": "Assignee: boothby\n\nOtherwise bad things happen.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5141\n\n",
    "created_at": "2009-01-30T21:51:19Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "tinymce should be disabled on published worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5141",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

Otherwise bad things happen.

Issue created by migration from https://trac.sagemath.org/ticket/5141





---

archive/issue_comments_039240.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T04:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_events_005389.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-02T05:01:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5141#event-5389"
}
```



---

archive/issue_comments_039241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T05:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039242.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T05:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039243.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-02T05:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039244.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-02T05:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005390.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-02T05:25:12Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5141#event-5390"
}
```



---

archive/issue_comments_039245.json:
```json
{
    "body": "Ooops, this did break some doctests in cell.py:\n\n```\nsage -t -long \"devel/sage/sage/server/notebook/cell.py\"     \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py\", line 175:\n    sage: C.html()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[3]>\", line 1, in <module>\n        C.html()###line 175:\n    sage: C.html()\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 184, in html\n        if JEDITABLE_TINYMCE and not self.worksheet().is_published():\n    AttributeError: 'NoneType' object has no attribute 'is_published'\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py\", line 178:\n    sage: C.html(do_math_parse=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[5]>\", line 1, in <module>\n        C.html(do_math_parse=True)###line 178:\n    sage: C.html(do_math_parse=True)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 184, in html\n        if JEDITABLE_TINYMCE and not self.worksheet().is_published():\n    AttributeError: 'NoneType' object has no attribute 'is_published'\n**********************************************************************\n```\n\n\nShame on me for giving this a positive review :p\n\nReopened. \n\nCheers,\n\nMichel",
    "created_at": "2009-02-02T05:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, this did break some doctests in cell.py:

```
sage -t -long "devel/sage/sage/server/notebook/cell.py"     
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py", line 175:
    sage: C.html()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[3]>", line 1, in <module>
        C.html()###line 175:
    sage: C.html()
      File "/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 184, in html
        if JEDITABLE_TINYMCE and not self.worksheet().is_published():
    AttributeError: 'NoneType' object has no attribute 'is_published'
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py", line 178:
    sage: C.html(do_math_parse=True)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[5]>", line 1, in <module>
        C.html(do_math_parse=True)###line 178:
    sage: C.html(do_math_parse=True)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 184, in html
        if JEDITABLE_TINYMCE and not self.worksheet().is_published():
    AttributeError: 'NoneType' object has no attribute 'is_published'
**********************************************************************
```


Shame on me for giving this a positive review :p

Reopened. 

Cheers,

Michel



---

archive/issue_comments_039246.json:
```json
{
    "body": "Attachment [trac_5141-tinymce-published.patch](tarball://root/attachments/some-uuid/ticket5141/trac_5141-tinymce-published.patch) by @jasongrout created at 2009-02-02 20:19:36",
    "created_at": "2009-02-02T20:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39246",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5141-tinymce-published.patch](tarball://root/attachments/some-uuid/ticket5141/trac_5141-tinymce-published.patch) by @jasongrout created at 2009-02-02 20:19:36



---

archive/issue_comments_039247.json:
```json
{
    "body": "patch updated to check for the existence of the .is_published() method.  It should work now.",
    "created_at": "2009-02-02T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39247",
    "user": "https://github.com/jasongrout"
}
```

patch updated to check for the existence of the .is_published() method.  It should work now.



---

archive/issue_comments_039248.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-03T08:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39248",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to critical.



---

archive/issue_comments_039249.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2009-02-03T09:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39249",
    "user": "https://github.com/jasongrout"
}
```

Changing status from reopened to new.



---

archive/issue_comments_039250.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-02-03T09:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39250",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_039251.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_039252.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-04T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005391.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-04T01:16:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5141#event-5391"
}
```
