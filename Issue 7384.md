# Issue 7384: SageNB -- Fix Sphinxify doctests

archive/issues_007384.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mpatel\n\n`sphinxify.py`'s doctests currently fail. Fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7384\n\n",
    "created_at": "2009-11-03T20:46:18Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "SageNB -- Fix Sphinxify doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7384",
    "user": "timdumol"
}
```
Assignee: boothby

CC:  mpatel

`sphinxify.py`'s doctests currently fail. Fix this.

Issue created by migration from https://trac.sagemath.org/ticket/7384





---

archive/issue_comments_062102.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-03T20:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62102",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062103.json:
```json
{
    "body": "Attachment\n\nFixed the doctests",
    "created_at": "2009-11-03T21:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62103",
    "user": "timdumol"
}
```

Attachment

Fixed the doctests



---

archive/issue_comments_062104.json:
```json
{
    "body": "I got two test failures:\n\n```\nsage -t  \"4.2/devel/sage-main/sage/sphinxify.py\"            \n**********************************************************************\nFile \"/home/apps/sage-4.2/devel/sage-main/sage/sphinxify.py\", line 51:\n    sage: sphinxify('A test')\nExpected:\n    '\\n<div class=\"docstring\">\\n    \\n  <p>A test</p>\\n\\n\\n</div>'\nGot:\n    '<div class=\"docstring\">\\n    \\n  <p>A test</p>\\n\\n\\n</div>'\n**********************************************************************\nFile \"/home/apps/sage-4.2/devel/sage-main/sage/sphinxify.py\", line 53:\n    sage: sphinxify('**Testing**\\n`monospace`')\nExpected:\n    '\\n<div class=\"docstring\"...<strong>Testing</strong>\\n<span class=\"math\"...</p>\\n\\n\\n</div>'\nGot:\n    '<div class=\"docstring\">\\n    \\n  <p><strong>Testing</strong>\\n<span class=\"math\">monospace</span></p>\\n\\n\\n</div>'\n**********************************************************************\n1 items had failures:\n   2 of   5 in __main__.example_2\n***Test Failed*** 2 failures.\n```\n\nBut it could be my setup.  If not, please see version 2 of the patch.",
    "created_at": "2009-11-04T05:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62104",
    "user": "mpatel"
}
```

I got two test failures:

```
sage -t  "4.2/devel/sage-main/sage/sphinxify.py"            
**********************************************************************
File "/home/apps/sage-4.2/devel/sage-main/sage/sphinxify.py", line 51:
    sage: sphinxify('A test')
Expected:
    '\n<div class="docstring">\n    \n  <p>A test</p>\n\n\n</div>'
Got:
    '<div class="docstring">\n    \n  <p>A test</p>\n\n\n</div>'
**********************************************************************
File "/home/apps/sage-4.2/devel/sage-main/sage/sphinxify.py", line 53:
    sage: sphinxify('**Testing**\n`monospace`')
Expected:
    '\n<div class="docstring"...<strong>Testing</strong>\n<span class="math"...</p>\n\n\n</div>'
Got:
    '<div class="docstring">\n    \n  <p><strong>Testing</strong>\n<span class="math">monospace</span></p>\n\n\n</div>'
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_2
***Test Failed*** 2 failures.
```

But it could be my setup.  If not, please see version 2 of the patch.



---

archive/issue_comments_062105.json:
```json
{
    "body": "Attachment\n\nUpdate doctest outputs.  Apply only this patch.",
    "created_at": "2009-11-04T05:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62105",
    "user": "mpatel"
}
```

Attachment

Update doctest outputs.  Apply only this patch.



---

archive/issue_comments_062106.json:
```json
{
    "body": "To the extent it counts, my review is positive.",
    "created_at": "2009-11-04T05:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62106",
    "user": "mpatel"
}
```

To the extent it counts, my review is positive.



---

archive/issue_comments_062107.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-12T02:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62107",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T02:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62108",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_062109.json:
```json
{
    "body": "merged into sagenb-0.4.3",
    "created_at": "2009-11-12T02:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7384#issuecomment-62109",
    "user": "was"
}
```

merged into sagenb-0.4.3
