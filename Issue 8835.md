# Issue 8835: mark some latex doctests optional

archive/issues_008835.json:
```json
{
    "body": "Assignee: tbd\n\nOn t2 we have some failures due to assumptions in doctests about the latex install.  As latex is not a prereq for sage, not having it shouldn't result in latex errors.  These should thus be marked\n\n\n```\n    # optional - latex\n```\n\n\nThe failures:\n\n\n```\nsage -t  -long \"devel/sage/sage/misc/latex.py\"\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py\", line 1023:\n    sage: latex.has_file(\"article.cls\")\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py\", line 1050:\n    sage: latex.check_file(\"article.cls\")\nExpected nothing\nGot:\n    <BLANKLINE>\n    Warning: `article.cls` is not part of this computer's TeX installation.\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py\", line 1207:\n    sage: latex.extra_preamble()\nExpected:\n    '\\\\usepackage{xypic}\\n'\nGot:\n    ''\n**********************************************************************\n3 items had failures:\n   1 of   4 in __main__.example_28\n   1 of   6 in __main__.example_29\n   1 of   6 in __main__.example_35\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_latex.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8835\n\n",
    "created_at": "2010-05-01T06:18:36Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "mark some latex doctests optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8835",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

On t2 we have some failures due to assumptions in doctests about the latex install.  As latex is not a prereq for sage, not having it shouldn't result in latex errors.  These should thus be marked


```
    # optional - latex
```


The failures:


```
sage -t  -long "devel/sage/sage/misc/latex.py"
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py", line 1023:
    sage: latex.has_file("article.cls")
Expected:
    True
Got:
    False
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py", line 1050:
    sage: latex.check_file("article.cls")
Expected nothing
Got:
    <BLANKLINE>
    Warning: `article.cls` is not part of this computer's TeX installation.
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/misc/latex.py", line 1207:
    sage: latex.extra_preamble()
Expected:
    '\\usepackage{xypic}\n'
Got:
    ''
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_28
   1 of   6 in __main__.example_29
   1 of   6 in __main__.example_35
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_latex.py
```


Issue created by migration from https://trac.sagemath.org/ticket/8835





---

archive/issue_comments_081109.json:
```json
{
    "body": "Attachment [trac_8835.patch](tarball://root/attachments/some-uuid/ticket8835/trac_8835.patch) by @williamstein created at 2010-05-01 06:22:41",
    "created_at": "2010-05-01T06:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8835#issuecomment-81109",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8835.patch](tarball://root/attachments/some-uuid/ticket8835/trac_8835.patch) by @williamstein created at 2010-05-01 06:22:41



---

archive/issue_comments_081110.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-01T06:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8835#issuecomment-81110",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081111.json:
```json
{
    "body": "Yes, LaTeX is not a prerequisite. With the patch, the doctests under `sage/misc/latex.py` pass on t2.math.",
    "created_at": "2010-05-02T18:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8835#issuecomment-81111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Yes, LaTeX is not a prerequisite. With the patch, the doctests under `sage/misc/latex.py` pass on t2.math.



---

archive/issue_comments_081112.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-02T18:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8835#issuecomment-81112",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_021567.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-02T18:31:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8835",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8835#event-21567"
}
```
