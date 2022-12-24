# Issue 5141: tinymce should be disabled on published worksheets

archive/issues_005141.json:
```json
{
    "body": "Assignee: boothby\n\nOtherwise bad things happen.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5141\n\n",
    "created_at": "2009-01-30T21:51:19Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "tinymce should be disabled on published worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5141",
    "user": "jason"
}
```
Assignee: boothby

Otherwise bad things happen.

Issue created by migration from https://trac.sagemath.org/ticket/5141





---

archive/issue_comments_039316.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T04:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39316",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_039317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T05:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39317",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039318.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T05:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39318",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039319.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-02T05:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39319",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039320.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-02T05:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39320",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_039321.json:
```json
{
    "body": "Ooops, this did break some doctests in cell.py:\n\n```\nsage -t -long \"devel/sage/sage/server/notebook/cell.py\"     \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py\", line 175:\n    sage: C.html()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[3]>\", line 1, in <module>\n        C.html()###line 175:\n    sage: C.html()\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 184, in html\n        if JEDITABLE_TINYMCE and not self.worksheet().is_published():\n    AttributeError: 'NoneType' object has no attribute 'is_published'\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py\", line 178:\n    sage: C.html(do_math_parse=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[5]>\", line 1, in <module>\n        C.html(do_math_parse=True)###line 178:\n    sage: C.html(do_math_parse=True)\n      File \"/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 184, in html\n        if JEDITABLE_TINYMCE and not self.worksheet().is_published():\n    AttributeError: 'NoneType' object has no attribute 'is_published'\n**********************************************************************\n```\n\n\nShame on me for giving this a positive review :p\n\nReopened. \n\nCheers,\n\nMichel",
    "created_at": "2009-02-02T05:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39321",
    "user": "mabshoff"
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

archive/issue_comments_039322.json:
```json
{
    "body": "Attachment [trac_5141-tinymce-published.patch](tarball://root/attachments/some-uuid/ticket5141/trac_5141-tinymce-published.patch) by jason created at 2009-02-02 20:19:36",
    "created_at": "2009-02-02T20:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39322",
    "user": "jason"
}
```

Attachment [trac_5141-tinymce-published.patch](tarball://root/attachments/some-uuid/ticket5141/trac_5141-tinymce-published.patch) by jason created at 2009-02-02 20:19:36



---

archive/issue_comments_039323.json:
```json
{
    "body": "patch updated to check for the existence of the .is_published() method.  It should work now.",
    "created_at": "2009-02-02T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39323",
    "user": "jason"
}
```

patch updated to check for the existence of the .is_published() method.  It should work now.



---

archive/issue_comments_039324.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-03T08:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39324",
    "user": "jason"
}
```

Changing priority from major to critical.



---

archive/issue_comments_039325.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2009-02-03T09:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39325",
    "user": "jason"
}
```

Changing status from reopened to new.



---

archive/issue_comments_039326.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2009-02-03T09:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39326",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_039327.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39327",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_039328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-04T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5141#issuecomment-39328",
    "user": "mabshoff"
}
```

Resolution: fixed
