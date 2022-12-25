# Issue 5205: [with patch, positive review] Set "# -*- coding: utf-8 -*-" encoding for sage/server/notebook/template.py

archive/issues_005205.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout @malb\n\nWhen building Sage 3.3.alpha6 every doctest passes. Move the tree, start Sage once so that all the pyc files are rewritten and then doctest and failures galore:\n\n```\nsage -t -long devel/sage/sage/server/notebook/cell.py # 136 doctests failed\nsage -t -long devel/sage/sage/server/notebook/worksheet.py # 379 doctests failed\nsage -t -long devel/sage/sage/server/notebook/twist.py # 39 doctests failed\nsage -t -long devel/sage/sage/server/notebook/notebook.py # 127 doctests failed\nsage -t -long devel/sage/sage/server/notebook/avatars.py # 13 doctests failed\nsage -t -long devel/sage/sage/server/notebook/template.py # 10 doctests failed\n```\nThis all boils down to\n\n```\nFile \"/scratch/mabshoff/sage-3.3.rc0/devel/sage-main/sage/server/notebook/worksheet.py\", line 347:\n    sage: nb = sage.server.notebook.notebook.Notebook(tmp_dir())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[2]>\", line 1, in <module>\n        nb = sage.server.notebook.notebook.Notebook(tmp_dir())###line 347:\n    sage: nb = sage.server.notebook.notebook.Notebook(tmp_dir())\n      File \"/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 94, in __init__\n        import sage.server.notebook.twist\n      File \"/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 44, in <module>\n        from sage.server.notebook.template import template\n      File \"/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/template.py\", line 64\n     SyntaxError: Non-ASCII character '\\xc3' in file /scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/template.py on line 65, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (template.py, line 64)\n```\nAs I pointed out in #5176 we must declare the encoding, but then I tested the cloning of the repo and could not get it to fail. I am clueless why, but the patch fixes the issue for me. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5205\n\n",
    "closed_at": "2009-02-08T07:42:03Z",
    "created_at": "2009-02-08T06:14:26Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] Set \"# -*- coding: utf-8 -*-\" encoding for sage/server/notebook/template.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jasongrout @malb

When building Sage 3.3.alpha6 every doctest passes. Move the tree, start Sage once so that all the pyc files are rewritten and then doctest and failures galore:

```
sage -t -long devel/sage/sage/server/notebook/cell.py # 136 doctests failed
sage -t -long devel/sage/sage/server/notebook/worksheet.py # 379 doctests failed
sage -t -long devel/sage/sage/server/notebook/twist.py # 39 doctests failed
sage -t -long devel/sage/sage/server/notebook/notebook.py # 127 doctests failed
sage -t -long devel/sage/sage/server/notebook/avatars.py # 13 doctests failed
sage -t -long devel/sage/sage/server/notebook/template.py # 10 doctests failed
```
This all boils down to

```
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage-main/sage/server/notebook/worksheet.py", line 347:
    sage: nb = sage.server.notebook.notebook.Notebook(tmp_dir())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        nb = sage.server.notebook.notebook.Notebook(tmp_dir())###line 347:
    sage: nb = sage.server.notebook.notebook.Notebook(tmp_dir())
      File "/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 94, in __init__
        import sage.server.notebook.twist
      File "/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 44, in <module>
        from sage.server.notebook.template import template
      File "/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/template.py", line 64
     SyntaxError: Non-ASCII character '\xc3' in file /scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/template.py on line 65, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (template.py, line 64)
```
As I pointed out in #5176 we must declare the encoding, but then I tested the cloning of the repo and could not get it to fail. I am clueless why, but the patch fixes the issue for me. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5205





---

archive/issue_comments_039807.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-08T06:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5205#issuecomment-39807",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039808.json:
```json
{
    "body": "Well, I am clueless when testing for this failure I could not get it to go boom. The fix itself is obvious.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T06:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5205#issuecomment-39808",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, I am clueless when testing for this failure I could not get it to go boom. The fix itself is obvious.

Cheers,

Michael



---

archive/issue_comments_039809.json:
```json
{
    "body": "Attachment [trac_5205_encoding.patch](tarball://root/attachments/some-uuid/ticket5205/trac_5205_encoding.patch) by mabshoff created at 2009-02-08 06:32:45",
    "created_at": "2009-02-08T06:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5205#issuecomment-39809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5205_encoding.patch](tarball://root/attachments/some-uuid/ticket5205/trac_5205_encoding.patch) by mabshoff created at 2009-02-08 06:32:45



---

archive/issue_comments_039810.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-02-08T06:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5205#issuecomment-39810",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_comments_039811.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T07:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5205#issuecomment-39811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_events_012052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-08T07:42:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5205#event-12052"
}
```



---

archive/issue_comments_039812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-08T07:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5205#issuecomment-39812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
